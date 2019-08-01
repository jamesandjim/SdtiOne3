#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-10-15 11:17
# @Author  : James
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm

import xadmin

from .models import Device


class DeviceAdmin(object):
    list_display = ['name', 'sn', 'ip', 'netmask', 'netgate', 'mac', 'ver']
    search_fields = ['name', 'sn', 'ip', 'netmask', 'netgate', 'mac', 'ver']
    list_filter = ['name', 'sn', 'ip', 'netmask', 'netgate', 'mac', 'ver']


xadmin.site.register(Device, DeviceAdmin)