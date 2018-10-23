#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-09-27 17:04
# @Author  : James
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from .views import DeviceSet
from .views import dev_add, dev_list, dev_search


urlpatterns = [
    url(r'^deviceset/', csrf_exempt(DeviceSet.as_view())),

    url(r'^list/', dev_list),
    url(r'^add/', dev_add),
    url(r'^search/', dev_search),

]