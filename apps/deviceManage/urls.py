#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-09-27 17:04
# @Author  : James
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include

from .views import DeviceSet
from .views import hello, home,dev_test,dev_xx


urlpatterns = [
    url(r'^deviceset/', DeviceSet.as_view()),

    url(r'^hello/', hello),
    url(r'^test/', dev_test),
    url(r'^xx/', dev_xx)
]