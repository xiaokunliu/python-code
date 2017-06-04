#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" 
this urls is referenced on app client  
"""

from django.conf.urls import patterns, url

## update the password and check verify code,upload the photo/user_ip/user_opr_log have not done
## logout have not been completed

urlpatterns = patterns('',#must be required
                       url(r'^getLabelTypes/$', 'dictionary.views.getLabelTypes'),
                       )
