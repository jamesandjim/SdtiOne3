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
    path('register_list', views.Register_list.as_view(), name='vistor_register_list'),

]