#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" 
this urls is referenced on app client  
"""

from django.conf.urls import patterns, url


urlpatterns = patterns('',#must be required
                       url(r'^test/$', 'task.views.test'),
                       url(r'^addTask/$', 'task.views.addTask'),
                       url(r'^redeploy/$', 'task.views.redeploy'),
                       url(r'^receiveTask/$', 'task.views.receiveTask'),
                       url(r'^cooperate/$', 'task.views.cooperate'),
                       url(r'^queryTaskByPublisher/$', 'task.views.queryTaskByPublisher'),
                       )
