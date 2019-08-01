"""SdtiOne3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
import xadmin

from management import views as management_views
from deviceManage import views as dev_views

urlpatterns = [
    #后台管理
    path('xadmin/', xadmin.site.urls),

    #系统登录
    path('', management_views.login, name='login'),

    #进入前端系统首页
    path('index/', management_views.Index.as_view(), name='index'),

    #管理中心的导航
    path('management/', include('management.urls')),

    #门禁系统的导航
    path('access/', include('access.urls')),

    #访客系统的导航
    path('vistor/', include('vistor.urls')),

    #消费系统的导航
    path('xf/', include('xf.urls')),


]
