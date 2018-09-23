# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic.base import View

from deviceManage.mjCommunity import WGPaketShort
from deviceManage.deviceSet import search_dev, set_ip, show_dev_info


# Create your views here.
class DeviceSet(View):
    def get(self, request):
        return render(request, 't1.html', {})

    def post(self, request):
        if request.POST.get('search_dev'):
            # 搜索控制器
            devs = search_dev()

            return render(request, 't1.html', devs)
        elif request.POST.get('update_dev'):
            dev_ip = request.POST.get("dev_ip")
            dev_sn = int(request.POST.get("dev_sn"))
            dev_netmask = request.POST.get('dev_netmask')
            dev_netgate = request.POST.get('dev_netgate')

            set_ip(dev_ip, dev_sn, dev_netmask, dev_netgate)

            return redirect('http://127.0.0.1:8000/test/')
        elif request.POST.get('show_devinfo'):
            dev_ip = request.POST.get("dev_ip")
            dev_sn = int(request.POST.get("dev_sn"))
            data = show_dev_info(dev_ip, dev_sn)
            return render(request, 't1.html', data)
        else:
            pass



# 开门功能
def open_door(request):
    dev = WGPaketShort(request.POST['dev_ip'], request.POST['dev_sn'], 0x40)
    # 定义门号
    dev.udp_data[8] = 1
    dev.send_data()
    ret = dev.rec_data
    if ret[8] == 1:
        result = '开门成功'
    else:
        result = '开门失败'

    return render(request, 't1.html', {'x': result})

