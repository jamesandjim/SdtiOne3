from django.shortcuts import render
from django.views import View

# Create your views here.


class Device_list(View):
    def get(self, request):
        return render(request, 'device_list.html')
