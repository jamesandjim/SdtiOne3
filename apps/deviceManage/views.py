#from __future__ import unicode_literals
from django.shortcuts import render

from deviceManage.mjCommunity import WGPaketShort


# Create your views here.
#开门功能
def open_door(request):
    dev = WGPaketShort('192.168.0.99', 123300755, 0x40)
    # 定义门号
    dev.udp_data[8] = 1
    ret = dev.send_data()

    return render(request, 't1.html', {'x': ret})

#
def show_devinfo(request):
    dev = WGPaketShort('192.168.0.99', 123300755, 0x20)
    ret = dev.send_data()

    return render(request, 't1.html', {'x': ret})