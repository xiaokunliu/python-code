#!/usr/bin/env bash
apt-get update
apt-get upgrade
apt-get install -y build-essential
apt-get install -y libsqlite3-dev
apt-get install -y libreadline6-dev
apt-get install -y libgdbm-dev
apt-get install -y zliblg-dev
apt-get install -y libbz2-dev
apt-get install -y sqllite3
apt-get install -y tk-dev
apt-get install -y zip
apt-get install -y python-dev
wget http://python-distribute.org/distribute_setup.py
python3.5 distribute_setup.py
wget https://bootstrap.pypa.io/get-pip.py
python3.5 get-pip.py