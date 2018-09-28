#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-09-27 17:04
# @Author  : James
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include

from .views import DeviceSet
from .views import hello, home, dev_add, dev_list


urlpatterns = [
    url(r'^deviceset/', DeviceSet.as_view()),

    url(r'^hello/', hello),
    url(r'^list/', dev_list),
    url(r'^add/', dev_add)
]