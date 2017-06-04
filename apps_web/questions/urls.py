#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" 
this urls is referenced on app client  
"""

from django.conf.urls import patterns, url


urlpatterns = patterns('',#must be required
                       url(r'^test/$', 'questions.views.test'),
                       url(r'^publish/$', 'questions.views.publishQuestion'),
                       url(r'^closeQt/$', 'questions.views.closeQt'),
                       url(r'^answer/$', 'questions.views.answer'),
                       url(r'^remark/$', 'questions.views.remark'),
                       url(r'^listAll/$', 'questions.views.listAll'),
                       url(r'^listRemark/$', 'questions.views.listRemark'),
                       )
