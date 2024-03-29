"""AutoPlateTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#URL映射管理
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('polls/dictstudy',include('polls.urls')),
    path('polls/hello',include('polls.urls')),
    path('polls/upfile', include('polls.urls')),
    #bootstrap页
    path('polls/boothtml', include('polls.urls')),
    path('polls/uploadfile',include('polls.urls')),
    #path('polls/dictstudy',include('polls.dictstudy')),
    path('admin/', admin.site.urls),

]
