# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic.base import View

from deviceManage.mjCommunity import WGPaketShort
from deviceManage.deviceSet import search_dev, set_ip, show_dev_info, open_door, get_auth, get_auth_no, get_device_time, get_door_option, get_no_readed, get_record, get_server_option, get_total_auth, set_device_time, set_door_option, set_no_readed, set_server_option


# Create your views here.
def home(request):
    return render(request, 't1.html')


def dev_test(request):
    return render(request, 'dev_manage.html')


class DeviceSet(View):
    def get(self, request):
        return render(request, 't1.html', {})

    def post(self, request):

        if request.POST.get('search_dev'):
            # 搜索控制器
            devs = search_dev()

            return render(request, 'dev_manage.html', devs)
        elif request.POST.get('update_dev'):
            dev_ip = request.POST.get("dev_ip")
            dev_sn = int(request.POST.get("dev_sn"))
            dev_netmask = request.POST.get('dev_netmask')
            dev_netgate = request.POST.get('dev_netgate')

            set_ip(dev_ip, dev_sn, dev_netmask, dev_netgate)

            return render(request, 'dev_manage.html', {})
        elif request.POST.get('show_devinfo'):
            dev_ip = request.POST.get("dev_ip")
            dev_sn = int(request.POST.get("dev_sn"))

            data = show_dev_info(dev_ip, dev_sn)
            return render(request, 'dev_manage.html', data)

        elif request.POST.get('open_door'):
            dev_ip = request.POST.get("dev_ip")
            dev_sn = int(request.POST.get("dev_sn"))
            door_no = int(request.POST.get('doorno'))

            data = open_door(dev_ip, dev_sn, door_no)
            return render(request, 'dev_manage.html', data)





