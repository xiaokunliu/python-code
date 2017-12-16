#!/bin/sh
# vim: et ts=4 sw=4

# http://stackoverflow.com/a/1482133/4740627
base_dir=$(dirname "$(dirname "$(readlink -f "$0")")")
cd $base_dir

service=$(basename $base_dir)
module=${NAMEKO_MODULE-service}
config=${NAMEKO_CONFIG-$base_dir/conf/config.yaml}
config_debug=${NAMEKO_CONFIG_DEBUG-$base_dir/conf/config.debug.yaml}
log_dir=${NAMEKO_LOGDIR-$base_dir/logs}
log_file=${NAMEKO_LOGFILE-$log_dir/console.log}
pid_file=$log_dir/${service}.pid
env=${ENV-py27}
log_level=${LOG_LEVEL-DEBUG}
port=$(python -c "print (hash('$service$(whoami)') % 10000 + 10000)")
default_addr="0.0.0.0:$port"
web_addr=${WEB_ADDRESS-$default_addr}
setup_marker=.tox/.setup-marker
requirements_md5=.tox/.requirements_md5

if [ -f "$config_debug" ]; then
    config=$config_debug
fi

usage() {
    echo "\
Usage: ./run.sh [start|stop|restart|shell|install|uninstall|test|pre-commit|setup-dev] [-D] [...]

Options:
    -D    none daemon mode, default is deamon mode

Environment variables:
    NAMEKO_MODULE=service
    NAMEKO_CONFIG={base_dir}/conf/config.yaml
    NAMEKO_LOGDIR={base_dir}/logs/
    NAMEKO_LOGFILE={base_dir}/logs/{basename}.log
    ENV=py27
    LOG_LEVEL=DEBUG
    WEB_ADDRESS=$default_addr
"
}

log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") $@"
}

log "Use config: $config"

start() {
    if [ -f $pid_file ] && ps -p $(<$pid_file) >/dev/null 2>&1; then
        log "Service already running $(<$pid_file)" >&2
        return
    fi

    # export envs
    export LOG_LEVEL=$log_level WEB_ADDRESS=$web_addr

    # start service
    if [ "$1" != "-D" ]; then
        nohup .tox/$env/bin/nameko run --config "$config" $module >> $log_file 2>&1 &
        pid=$!
        echo $pid > $pid_file
        log "Start $service in background with pid $pid"
        since=$(date +%s)
        while true; do
            listen_line=$(lsof -nlp "$pid" 2>&1 | grep LISTEN)
            if ! ps -p $pid >/dev/null; then
                log "Service stopped unexpectedly $pid, see $log_file"
                return
            elif [ -z "$listen_line" ]; then
                elapsed=$(expr $(date +%s) - $since)
                if [ "$elapsed" -gt 10 ]; then
                    log "Wait too long to get listen address, see $log_file"
                    break
                fi
                sleep 0.3
                continue
            fi

            listen_host=$(echo $listen_line | awk -F'TCP |:' '{print $2}')
            if [ "$listen_host" == "*" ]; then
                listen_host="0.0.0.0"
            fi
            listen_port=$(echo $listen_line | awk -F':| \(' '{print $2}')
            log "Service listen on: http://$listen_host:$listen_port"
            break
        done
    else
        # Force unbuffering of stdout
        # http://stackoverflow.com/a/11337109
        log "Start $service in foreground"
        stdbuf -o0 .tox/$env/bin/nameko run --config "$config" $module 2>&1 | tee -a $log_file
    fi
}

stop() {
    if [ -f "$pid_file" ]; then
        pid=$(<$pid_file)
        log "Stop $service (pid $pid)"
        kill "$pid" >/dev/null 2>&1
        i=0
        while ps -p "$pid" >/dev/null 2>&1; do
            if ((i >= 10)); then
                log "Waiting $service (pid $pid) to stop"
                sleep 1
            else
                sleep 0.2
            fi
            i=$((i + 1))
        done
        rm -f $pid_file
    fi
}

restart() {
    stop $@
    start $@
}

shell() {
    .tox/$env/bin/nameko shell --config "$config" $@
}

install() {
    for env in $(tox --listenvs); do
        log "+ .tox/$env/bin/pip install $@"
        .tox/$env/bin/pip install  --disable-pip-version-check --no-binary greenlet $@
    done
}

uninstall() {
    for env in $(tox --listenvs); do
        log "+ .tox/$env/bin/pip uninstall $@"
        .tox/$env/bin/pip uninstall --disable-pip-version-check -y $@
    done
}

simple_test() {
    log "+ .tox/$env/bin/py.test service test"
    .tox/$env/bin/py.test --doctest-modules --capture=no --exitfirst --log-level=$log_level $@ service test
    log "+ .tox/$env/bin/flake8 service test"
    .tox/$env/bin/flake8 service test
}

pre_commit() {
    # .tox/$env/bin/pre-commit run --files xxx.py
    # .tox/$env/bin/pre-commit run --all-files
    # .tox/$env/bin/pre-commit install
    log "+ .tox/$env/bin/pre-commit $@"
    .tox/$env/bin/pre-commit $@
}

update_requirements() {
    set -e
    md5="$(echo -n $(md5sum requirements*))"
    old_md5="$(echo -n $(cat $requirements_md5 2>&1))"
    if [ "$md5" != "$old_md5" ]; then
        log "requirements file changed, update requirements"
        for req in $(ls requirements*); do
            log "+ .tox/$env/bin/pip install -r $req"
            .tox/$env/bin/pip install -r $req
        done
        echo $md5 > $requirements_md5
    fi
    set +e
}

setup_dev() {
    set -e
    log "Setup development envrioment..."
    host=xxx.xxx.xxx.xxx
    pydistconf=~/.pydistutils.cfg
    pipconf=~/.cache/pip/pip.conf

    if [ -z "$(grep $host $pydistconf 2>/dev/null)" ]; then
        log "setup $pydistconf"
        mkdir -p $(dirname $pydistconf)
        echo >> $pydistconf "\
[easy_install]
index_url = https://$host
"
    fi

    if [ -z "$(grep $host $pipconf 2>/dev/null)" ]; then
        log "setup $pipconf"
        mkdir -p $(dirname $pipconf)
        echo >> $pipconf "\
[global]
index-url = https://$host

[install]
trusted-host = $host
"
    fi

    if ! which tox >/dev/null 2>&1; then
        log "install tox"
        sudo pip install "tox>=2.5.0"
    fi

    log "init tox virtual envs"
    tox -vv --notest

    log "init pre-commit"
    .tox/py27/bin/pre-commit install

    # mark setup successful
    touch $setup_marker

    deps="python-dev libmysqlclient-dev libffi-dev libssl-dev libmemcached-dev"
    if command -v dpkg >/dev/null 2>&1 && ! dpkg -s $deps >/dev/null 2>&1; then
        log "install system dependencies $deps"
        sudo apt-get update
        sudo apt-get install -y $deps
    fi
    set +e
}

if [ "$#" -eq 1 -a "$1" == "-D" ]; then
    op=start
else
    op=$1
    shift
fi

if [ ! -f $setup_marker ]; then
    if [ "$op" != "setup-dev" ]; then
        read -p "Do you wish to setup development environment now? Y/n " yn
        case $yn in
            [Yy]* ) true;;
            * ) exit;;
        esac
    fi
    setup_dev $@
fi

update_requirements

case "$op" in
    "")
        start $@
        ;;
    start)
        start $@
        ;;
    stop)
        stop
        ;;
    restart)
        restart $@
        ;;
    shell)
        shell $@
        ;;
    install)
        install $@
        ;;
    uninstall)
        uninstall $@
        ;;
    test)
        simple_test $@
        ;;
    pre-commit)
        pre_commit $@
        ;;
    setup-dev)
        true
        ;;
    *)
        usage
        exit 1
        ;;
esac
