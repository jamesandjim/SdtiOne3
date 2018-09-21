#from __future__ import unicode_literals
from django.shortcuts import render

from deviceManage.mjCommunity import WGPaketShort


# Create your views here.

#搜索控制器
def search_devs(request):
    dev = WGPaketShort('255.255.255.255', 0, 0x94)
    dev.send_data()
    if dev.rec_data[0] == 0x17 and dev.rec_data[1] == 0x94:
        #从返回值取得设备的SN,并以低位在前的方式，将字节码转为int
        dev_sn = dev.rec_data[4:8]
        rt_dev_sn = int.from_bytes(dev_sn, byteorder='little')

        #从返回的字节中分别取出IP的四个段并生成列表.进行组合，形成IP字符串
        tm_ip = dev.rec_data[8:12]
        list_ip = [str(tm_ip[i]) for i in range(4)]
        rt_dev_ip = '.'.join(list_ip)

        #从返回的字节中分别取出掩码的四个段并生成列表.进行组合，形成掩码字符串
        dev_netmask = dev.rec_data[12:16]
        list_netmask = [str(dev_netmask[i]) for i in range(4)]
        rt_dev_netmask = '.'.join(list_netmask)

        #从返回的字节中分别取出网关的四个段并生成列表.进行组合，形成网关字符串
        dev_netgate = dev.rec_data[16:20]
        list_netgate= [str(dev_netgate[i]) for i in range(4)]
        rt_dev_netgate = '.'.join(list_netgate)

        # 从返回的字节中分别取出MAC的6个段并生成列表.进行组合，形成MAC字符串
        dev_mac = dev.rec_data[20:26]
        list_mac = [str(hex(dev_mac[i])) for i in range(6)]
        rt_dev_mac = ':'.join(list_mac)

        dev_ver = dev.rec_data[26:28]
        list_ver = [str(dev_ver[i]) for i in range(2)]
        rt_dev_ver = '.'.join(list_ver)

        #rt_dev_ver = dev_ver-(dev_ver/16)*6
        # 从返回的字节中分别取出时间的四个段并生成列表.进行组合，形成时间字符串
        dev_date = dev.rec_data[28:32]
        list_date = [str(dev_date[i]) for i in range(4)]
        rt_dev_date = '-'.join(list_date)

    return render(request, 't1.html', locals())

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