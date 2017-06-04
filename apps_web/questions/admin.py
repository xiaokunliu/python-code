#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" 
this is for module to registered at the admin manager gui  
"""

from django.contrib import admin
from questions.models import Question

# Register your models here.
admin.site.register(Question)