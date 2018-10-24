# from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View

from deviceManage.models import Device

from deviceManage.mjCommunity import WGPaketShort
from deviceManage.deviceSet import search_dev, set_ip, show_dev_info, open_door, get_auth, get_auth_no, get_device_time, get_door_option, get_no_readed, get_record, get_server_option, get_total_auth, set_device_time, set_door_option, set_no_readed, set_server_option


# Create your views here.
def hello(request):
    return render(request, 'hello.html')

def w1(request):
    return render(request, 'w1.html')

def dev_main(request):
    return render(request, 'dev_main.html')


def dev_list(request):
    devs = Device.objects.all()
    return render(request, 'dev_list.html', {'devs': devs})

def dev_add(request):
    qu = request.POST
    return render(request, 'dev_add.html', {'dev': qu})

def dev_search(request):
    devs = search_dev()
    return render(request, 'dev_search.html', {'devs': devs})


class DeviceSet(View):
    def get(self, request):
        return render(request, 'dev_list.html', {})

    def post(self, request):
        onedev = Device()
        tm = request.POST
        return HttpResponse("success")

        # if request.POST.get('search'):
        #     # 搜索控制器
        #     devs = search_dev()
        #
        #     return render(request, 'dev_search.html', {'devs': devs})
        #
        # elif 'add' in request.POST:
        #     onedev.sn = request.POST.get("dev_sn")
        #     onedev.name = request.POST.get("dev_name", onedev.sn)
        #
        #     onedev.ip = request.POST.get("dev_ip")
        #     onedev.netmask = request.POST.get("dev_netmask")
        #     onedev.netgate = request.POST.get("dev_netgate")
        #     onedev.mac = request.POST.get("dev_mac")
        #     onedev.ver = request.POST.get("dev_ver", '')
        #     onedev.save()
        #     all = Device.objects.all()
        #
        #     return redirect(request, 'dev_list.html')
        #
        # elif request.POST.get('open_door'):
        #     dev_ip = request.POST.get("dev_ip")
        #     dev_sn = int(request.POST.get("dev_sn"))
        #     door_no = int(request.POST.get('doorno'))
        #
        #     data = open_door(dev_ip, dev_sn, door_no)
        #     return render(request, 'dev_add.html', data)
        # else:
        #     return render(request, 'dev_list.html')





