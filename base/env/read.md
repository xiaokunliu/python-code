#### 基于python开发环境的Dockerfile
> 在本地创建一个管理Docker的目录
```code
## MacOSX 系统下的
mkdir -p ~/mywork/docker/python

## 其他操作系统平台自定义管理目录，这里省略
```

> python开发环境的Dockerfile
```code
FROM ubuntu  ## 不指定版本默认使用最新版本
MAINTAINER keithl <define_yourselves email>

## 更改配置源
RUN mv /etc/apt/sources.list /etc/apt/sources-bak.list
ADD $PWD/sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root123' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN apt-get install -y vim

# install zsh
RUN apt-get install -y zsh && apt-get install -y wget
RUN apt-get install -y git
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh

RUN mkdir -p ~/work/python/projects
RUN chmod 775 -R ~/work/python/

ADD $PWD/install.sh ~/work/python/
ADD $PWD/code.sh ~/work/python/

## 安装python的apt软件包
RUN chmod a+x ~/work/python/install.sh && ~/work/python/install.sh

## 安装python的工具
RUN chmod a+x ~/work/python/code.sh && ~/work/python/code.sh

## 自定义配置python环境并使之生效
ADD $PWD/.zshrc ~/.zshrc
RUN source ~/.zshrc

## 搭建python2.7 以及 python3.x的开发环境
RUN mkvirtualenv --python=/usr/bin/python2.7 env2.7 && mkvirtualenv --python=/usr/bin/python3.5 env3.5

## 暴露docker容器的端口
EXPOSE 3306 80 22
CMD ["/usr/sbin/sshd", "-D"]
```

> 构建python环境下的Docker 镜像
```code
docker build -t docker-ssh:v1 $PWD
```

> 构建容器并挂载本地持久化文件目录到docker容器中，并指定docker映射端口
```code
docker run -d -P 22:32770 80:32769 3306:32768 --name pydev -v $PWD/data:/opt/data docker-ssh:v1
```

> 参见github
```
https://github.com/xiaokunliu/python-code/tree/master/base/env
```