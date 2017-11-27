#### python 环境搭建
> apt软件包
```bash
### 基于ubuntu系统下的开发环境
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y build-essential
sudo apt-get install -y libsqlite3-dev
sudo apt-get install -y libreadline6-dev
sudo apt-get install -y libgdbm-dev
sudo apt-get install -y zliblg-dev
sudo apt-get install -y libbz2-dev
sudo apt-get install -y sqllite3
sudo apt-get install -y tk-dev
sudo apt-get install -y zip
```
> python相关包的安装
```bash
### 安装python-dev包
sudo apt-get install -y python-dev
### 安装distribute包
sudo chmod -R 0755 /usr/local   ### 修改本地/usr/local权限
sudo chgrp -R gname /usr/lcoal  ### 更改文件所属用户组
wget http://python-distribute.org/distribute_setup.py
sudo python distribute_setup.py
```
> pip安装
```bash
#### 参考url:https://pip.pypa.io/en/stable/installing/
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
```
> virtualenvwrapper
```bash
### 相比virtualenv更简单的工具
pip install virtualenvwrapper
### 配置.bashrc or .bash_profile or .zshrc
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
  export WORKON_HOME=~/workdir/python/pyenv
  export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
  export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
  export PROJECT_HOME=/Users/wind/projects/python/
  source /usr/local/bin/virtualenvwrapper.sh
fi
### 配置生效
source ~/.bash_profile(.bashrc/.zshrc)
### help帮助命令
mkvirtualenv --help
### 创建python开发目录并指定python版本
mkvirtualenv --python=/usr/bin/python2.7 pyen2.7 
OR
mkvirtualenv --python=/usr/bin/python3.5 pyen3.5
### 官网参考
https://virtualenvwrapper.readthedocs.io/en/latest/
```
> virtualenv-burrito
```bash
### virtualenv-burrito 是一个安装、配置virtualenv和virtualenvwrapper以及其依赖的傻瓜式工具
curl -sL https://github.com/brainsik/virtualenv-burrito/blob/master/virtualenv-burrito.sh | $SHELL
### 自动把初始化脚本放在/home/username/.zprofile 里面
source /home/username/.vennburrito/startup.sh
### 更新virtualenv和virtualenvwrapper
virtualenv-burrito upgrade
```
> autoenv
```bash
sudo pip install autoenv
source /usr/local/bin/activate.sh
### 在virtualenv切换的目录下新建.env文件
touch .env
echo "source /home/usernmae/.virtualenvs/venv/bin/activate" > .env
```
> mercurial 搭建
```bash
sudo pip install mercurial
#### 参考官网
https://www.mercurial-scm.org/guide
```
> 检查代码风格工具
```bash
pip install pep8
```
> 语法检查工具
```bash
pip install pyflakes
```
> 命令自动补全
```bash
### 1 way
pip completion --zsh >> .zprofile
source ~/.zprofile

### 2 way,在~/.zshrc里面一行
eval "pip completion --zsh"

### 3.使用bash
pip completion --bash >> ~/.profile
```
