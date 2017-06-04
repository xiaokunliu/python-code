#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" 
this urls is referenced on app client  
"""

from django.conf.urls import patterns, url

## update the password and check verify code,upload the photo/user_ip/user_opr_log have not done
## logout have not been completed

urlpatterns = patterns('',#must be required
                       url(r'^test/$', 'users.views.test'),
                       url(r'^login/$', 'users.views.login'),
                       url(r'^register/$', 'users.views.register'),
                       url(r'^detail/$', 'users.views.detail'),
                       url(r'^addPosition/$', 'users.views.addPosition'),
                       url(r'^editName/$', 'users.views.editName'),
                       url(r'^editLabel/$', 'users.views.editLabel'),
                       url(r'^queryUser/$', 'users.views.queryUser'),
                       url(r'^queryForDetail/$', 'users.views.queryForDetail'),
                       url(r'^offerHelp/$', 'users.views.offerHelp'),
                       url(r'^getVerifyCode/$', 'users.views.getVerifyCode'),
                       url(r'^updatePwd/$', 'users.views.updatePwd'),
                       #url(r'^logout/$', 'users.views.logout'),
                       )
