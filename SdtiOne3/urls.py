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
from django.views.generic import TemplateView
from django.contrib import admin
import xadmin


from deviceManage import views as dev_views

urlpatterns = [
    #后台管理
    url(r'^xadmin/', xadmin.site.urls),
    #进入前端系统首页
    url(r'^$', dev_views.hello),
    #首页的iframed页
    url(r'^w1/', dev_views.w1),
    #设备管理的导航
    url(r'^dev/', include('deviceManage.urls')),

    ]
