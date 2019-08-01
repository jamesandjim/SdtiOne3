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
    path('device_list', views.Device_list.as_view(), name='access_device_list'),
    path('device_list1', views.Device_list1.as_view(), name='access_device_list1'),
    path('device_add_one', views.Device_add_one.as_view(), name='access_device_add_one'),
    path('device_search', views.Device_search.as_view(), name='access_device_search'),
    path('device_search1', views.Device_search1.as_view(), name='access_device_search1'),
    path('device_del_one', views.Device_del_one.as_view(), name='access_device_del_one'),
    path('device_edit1', views.Device_edit1.as_view(), name='access_device_edit1'),

    ]