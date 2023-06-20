"""
URL configuration for StudyDj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapps/',include("testapps.urls")),
    path('testapps/getinfo',include("testapps.urls")),
#引入url==============================================testapps
    path('testapps/index', include('testapps.urls')),
    path('testapps/dictstudy',include('testapps.urls')),
    path('testapps/hello',include('testapps.urls')),
    path('testapps/upfile', include('testapps.urls')),
    #requests模块使用
    path("testapps/req",include("testapps.urls")),
    #读取XMind文件返回
    path("testapps/xmd",include("testapps.urls")),
    #bootstrap页
    path('testapps/boothtml', include('testapps.urls')),
    path('testapps/uploadfile',include('testapps.urls')),
    #path('testapps/dictstudy',include('testapps.dictstudy')),
    #path("testapps/")
    path('testapps/tablehtml', include('testapps.urls')),
    path('testapps/tableinfo',include('testapps.urls')),
]
