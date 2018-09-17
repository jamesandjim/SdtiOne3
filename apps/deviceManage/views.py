#from __future__ import unicode_literals
from django.shortcuts import render

from deviceManage.mjCommunity import WGPaketShort


# Create your views here.
#开门功能
def open_door(request):
    dev = WGPaketShort('192.168.0.99', 123300755, 0x40)
    # 定义门号
    dev.udp_data[8] = 1
    dev.send_data()
    ret = dev.rec_data
    if ret[8] == 1:
        result = '开门成功'
    else:
        result = '开门失败'

    return render(request, 't1.html', {'x': result})

#
def show_devinfo(request):
    dev = WGPaketShort('192.168.0.99', 123300755, 0x20)
    dev.send_data()
    ret = dev.rec_data
    

    return render(request, 't1.html', {'x': ret})