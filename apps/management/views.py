from django.shortcuts import render
from django.views import View

from .utility import Menu_operator

# Create your views here.


# 登录
def login(request):
    return render(request, 'login.html')


def test123(request):
    return render(request, 'test123.html')


# 主界面与菜单
class Index(View):
    def get(self, request):
        list_menu = Menu_operator.toList()
        return render(request, 'index.html', {'menu': list_menu})

# 部门管理
class Department_list(View):
    def get(self, request):

        return render(request, 'management/department_list.html')
