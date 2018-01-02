#### python 微服务开发

> python版本

`2.7`

> 使用到的python均存放在requirements.txt,可以使用以下的命令安装相应的python库

```bash
# 每个项目有对应的python库，即都有相应的requirements.txt
# 可以在相应的目录下执行获取python的库以及对应的版本
pip install -r requirements.txt
```

> 安装python库之后创建nameko的python微服务

```bash
# 这里的微服务项目名称为demo，在unix或者linux下执行以下的命令
nameko-admin createproject demo

# 隐去相应的域名，需自行设置
```

> nameko本身依赖的第三方插件

```text
urllib3, idna, chardet, certifi, requests, six, greenlet, enum34, enum-compat, eventlet, wrapt, funcsigs, pbr, mock, werkzeug, pyyaml, path.py, anyjson, amqp, kombu, nameko
```

