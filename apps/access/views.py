# from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

from django.http import JsonResponse
from django.views import View
from access.hid import *

import json

from .models import Device

from deviceManage.mjCommunity import WGPaketShort
from . import deviceSet


# Create your views here.
class Device_list(View):
    def get(self, request):
        device = Device.objects.all()
        return render(request, 'device_list.html')


class Device_list1(View):
    def post(self, request):
        device = Device.objects.all()
        total = device.count()
        result = {}
        dev_list =[]
        for d in device:
            dic = {}
            dic['mjtype'] = d.mjtype
            dic['name'] = d.name
            dic['sn'] = d.sn
            dic['ip'] = d.ip
            dic['netmask'] = d.netmask
            dic['netgate'] = d.netgate
            dic['ver'] = d.ver
            dic['mac'] = d.mac
            dev_list.append(dic)

        result['code'] = 0
        result['msg'] = ""
        result['count'] = total
        result['data'] = dev_list
        return JsonResponse(result, safe=True)


class Device_add_one(View):
    def post(self, request):
        result = {}
        sn = request.POST.get('sn', '')
        ip = request.POST.get('ip', '')
        name = '控制器'+sn
        netmask = request.POST.get('netmask', '')
        netgate = request.POST.get('netgate', '')
        mac = request.POST.get('mac', '')
        ver = request.POST.get('ver', '')

        if not Device.objects.filter(sn=sn):

            device = Device.objects.create(sn=sn, ip=ip, name=name, netmask=netmask, netgate=netgate, mac=mac, ver=ver,
                                           mjtype='KW')
            result['msg'] = '门禁 sn:{} 成功增加到系统！'.format(sn)
        else:
            result['msg'] = '门禁 sn:{} 已存在系统中，请确认！'.format(sn)

        result['code'] = 0

        return JsonResponse(result, safe=True)


#导航到搜索控制器界面
class Device_search(View):
    def get(self, request):
        return render(request, 'device_search1.html')


#搜索控制器，并产生数据
class Device_search1(View):
    def post(self, request):
        devs = deviceSet.search_dev()
        total = devs.count(Device)
        result = {}
        result['code'] = 0
        result['msg'] = ""
        result['count'] = total
        result['data'] = devs
        return JsonResponse(result, safe=True)


class Device_del_one(View):
    def post(self, request):
        sn = request.POST.get('sn', '')
        Device.objects.filter(sn=sn).delete()
        result = {}
        result['code'] = 0
        return JsonResponse(result, safe=True)



class Device_edit(View):
    def get(self, request):
        dic = {}
        sn = request.GET.get('sn', '')
        try:
            dev = Device.objects.get(sn=sn)
            dic['mjtype'] = dev.mjtype
            dic['name'] = dev.name
            dic['sn'] = dev.sn
            dic['ip'] = dev.ip
            dic['netmask'] = dev.netmask
            dic['netgate'] = dev.netgate
            dic['ver'] = dev.ver
            dic['mac'] = dev.mac
        except Device.DoesNotExist:
            pass

        return JsonResponse(dic, safe=True)


class Device_edit1(View):
    def post(self, request):
        result ={}
        sn = request.POST.get('sn', '')
        name = request.POST.get('name', '')
        Device.objects.filter(sn=sn).update(name=name)
        result['msg']= 0

        return JsonResponse(result, safe=True)


