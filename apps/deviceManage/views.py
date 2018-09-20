#from __future__ import unicode_literals
from django.shortcuts import render

from deviceManage.mjCommunity import WGPaketShort


# Create your views here.

#搜索控制器
def search_devs(request):
    dev = WGPaketShort('255.255.255.255', 0, 0x94)
    dev.send_data()
    if dev.rec_data[0] == 0x17 and dev.rec_data[1] == 0x94:
        dev_sn = dev.rec_data[4:8]
        tm_ip = dev.rec_data[8:12]

        list_ip = [str(tm_ip[i]) for i in range(4)]

        dev_ip = '.'.join(list_ip)
        print(dev_ip)

        dev_netmask = dev.rec_data[12:16]
        dev_netgate = dev.rec_data[16:20]
        dev_mac = dev.rec_data[20:26]
        dev_ver = dev.rec_data[26:28]
        dev_d = dev.rec_data[28:32]

        result = int.from_bytes(dev_sn, byteorder='little')

    return render(request, 't1.html', {'x': result,'y':dev_ip, 'z':dev_ver})

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