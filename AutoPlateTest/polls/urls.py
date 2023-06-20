from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name = 'index'),
    path('dictstudy',views.dictstudy,name='dictstudy'),
    path('hello',views.hello,name='hello'),
    path('upfile',views.upfile,name='upfile'),
    #boothtml
    path('boothtml', views.boothtml, name='boothtml'),
    path('uploadfile',views.uploadfile,name='uploadfile')

]