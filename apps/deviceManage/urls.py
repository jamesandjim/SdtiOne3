#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-09-27 17:04
# @Author  : James
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


from . import views


urlpatterns = [
    path('acc_list', views.acc_list, name='acc_list'),
    path('acc_add', views.acc_add, name='acc_add'),
    path('acc_search', views.acc_search, name='acc_search'),
]