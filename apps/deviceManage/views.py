# from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View

from deviceManage.models import Device

from deviceManage.mjCommunity import WGPaketShort
from deviceManage.deviceSet import search_dev, set_ip, show_dev_info, open_door, get_auth, get_auth_no, get_device_time, get_door_option, get_no_readed, get_record, get_server_option, get_total_auth, set_device_time, set_door_option, set_no_readed, set_server_option


# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):

    return render(request, 'index.html')

def acc_list(request):
    return render(request, 'acc-list.html')

def acc_add(request):
    return render(request, 'acc-add.html')

def acc_search(request):
    devs = search_dev()

    return render(request, 'acc-search.html', {'devs': devs})




