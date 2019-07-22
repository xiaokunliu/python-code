#### django开发前期准备

> 安装django
```bash
pip install django
```

> 测试django版本
```python
import django
print django.VERSION
```


> 建立名称为website的django项目

```bash
django-admin startproject website
```

> 建立应用(项目模块)

```bash
python manage.py strtapp module_name
```

> 使用内置的服务器进行测试开发

```bash
python manager.py runserver 127.0.0.1:8080
```

#### django基础开发
> 视图开发
1. 在website/module_name/views.py 建立路由函数
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h3>xxxxx</h3>")

```

2. 在website/module_name下创建urls.py,管理所有app的url映射
```python
from django,conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index),
    url(r'user_input', views.user_input),
]
```

> 模型开发
1. 生成移植文件
```bash
# 生成数据移植文件，即将models.py定义的数据表转化为数据库生成脚本的过程
cd website/
python manage.py makemigraations module_name

# 执行之后会将所有的文件以及之后的migration文件都存在于目录website/app/migrations中
```
2. 移植到数据库中
```bash
cd website
python manage.py migrate
```
3. 模型的定义
```python
# models.py
from django.db import models, connection

class UserManager(models.Manager): 
    def auth_count(self,auth_string):
        return self.filter(user_auth=auth_string).count()
    
    def getUsersExceptSelf(self,auth_string):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT u.user_id FROM ss_user u WHERE u.user_auth!='%s' LIMIT 100
           """ % auth_string)
        
        _result = []
        
        for row in cursor.fetchall():
            _result.append(row[0])
        
        return _result
    
    def getId(self,auth_string):    
        cursor = connection.cursor()
        cursor.execute("""
        SELECT u.user_id FROM ss_user u WHERE u.user_auth!='%s'
           """ % auth_string)
        
        _id = 0
        try:
            _id = [0][0]
        except IndexError,e:
#             _log.error(e)
            print "UserManager-->token_expires-->",e
        finally:
            return _id
        
    
    def token_expires(self,auth_string):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT u.user_token_expires FROM ss_user u WHERE u.user_auth='%s'
           """ % auth_string)
        _token_expires = 0
        try:
            _token_expires = [0][0]
        except IndexError,e:
#             _log.error(e)
            print "UserManager-->token_expires-->",e
        finally:
            return _token_expires
        
        
    def userId_count(self,user_id):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT COUNT(0) FROM ss_user u WHERE u.user_id=%d
           """ % user_id)
        
        _nums = 0
        try:
            _nums = cursor.fetchall()[0][0]
        except IndexError,e:
#             _log.error(e)
            print "UserManager-->token_expires-->",e
        finally:
            return _nums  
         
    # for task 
    def getUserIdByLabelType(self,labelType,user_latitude,user_longitude):
        _label_list = labelType.split(",")
        
        if len(_label_list)==1:
            raise AppError("it must be use ',' to combinate label code ")
        
        toUserIds = []
        sql = """ SELECT u.user_id FROM ss_user u WHERE u.user_longitude=%d AND u.user_latitude=%d """ % (user_longitude,user_latitude)
        for label_code in _label_list:
            sql = sql + "u.user_label_type LIKE %"+label_code+"% ORDER BY u.user_type DESC LIMIT 1"
            print sql
            cursor = connection.cursor()
            cursor.execute(sql)
            toUserIds.append(cursor.fetchall()[0][0])
            
        return toUserIds 
     

class Users(models.Model):
    ## attention,this set blank = True but there is not applied at the db mysql
    user_id = models.PositiveIntegerField(auto_created=True,primary_key=True)
    user_email = models.EmailField(max_length=50,unique=True)
    user_phone = models.CharField(max_length=11,unique=True)
    user_pwd = models.CharField(max_length=32)
    user_really_name = models.CharField(max_length=50,blank=True,null=True)
    user_alias_name = models.CharField(max_length=50,blank=True,null=True)
    user_sex = models.SmallIntegerField(choices=((0, 'Male'), (1, 'Female')),default=1)
    user_auth = models.CharField(max_length=40,unique=True)
    user_token = models.CharField(max_length=40,unique=True)
    user_token_expires = models.FloatField()
    user_longitude =models.DecimalField(max_digits=10, decimal_places=6,blank=True,null=True)
    user_latitude =models.DecimalField(max_digits=10, decimal_places=6,blank=True,null=True)
    user_ip = models.PositiveIntegerField(blank=True,null=True)
    user_label_type = models.CharField(max_length=50,blank=True,null=True)
    user_type = models.SmallIntegerField(choices=((0, 'asker'), (1, 'helper')),default=0)
    
    def __unicode__(self):
        return u"%d %s %s %s" % (self.user_id,self.user_email,self.user_really_name,self.user_alias_name)
    
    auth_manager = UserManager()
    objects = models.Manager()
    
    class Meta:
        db_table = "ss_user"
```

> 表单开发
```python
# forms.py,定义表单类
from django.forms import ModelForm
from module_name.models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fileds = '__all__'      # 导入模型所有的数据
        # fields = ['user_email', 'user_really_name', ...]    # 导入部分数据
```

> 开发模版
```python
# 在website/templates/module_name/user_tpl.html
# 模版使用 {{ form_data.attr }}
```

> 开发视图
```python
from module_name.forms import UsersForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
import os

def user_input(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            users = form.save()
            users.save()
            return HttpResponseRedirect(reverse("module_name.views.index"))
    form = UsersForm()
    webroot = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(webroot, "templates/module_name", "user_tpl.html"), {"form": form})
```