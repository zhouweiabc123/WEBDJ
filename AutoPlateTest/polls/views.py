import json

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

import pandas as pd
NaN=""
#pandas读取Excel文件
def read_excel(file,**kwargs):
    data_dict = [1]
    data_json = "{'a':'1'}"
    try:
        data = pd.read_excel(file,**kwargs)
    except Exception as e:
        print(e)
    finally:
        print(data)
        print(type(data))
        #转换成字典，即[{},{}]
        data_dict = data.to_dict('records')
        #转换成json
        #data_json = data.to_json('records')
        #print(data_dict)
        print(data_json)
        return data_dict

import os
BASC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
def index(request):
    #return HttpResponse("Hello,woeld,You're at the polls indxe.")
    msg = "{'a':'a','b':'b','c':'c'}"
    if request.method =='post':
        return HttpResponse("abc")
    #js = json.dumps(msg)
    #js = json.loads(msg)
    return HttpResponse(msg)
def dictstudy(request):
    #return HttpResponse([1,2,3,4,5,6])
    r = read_excel(file=r"D:\A_Python\GitProjects\DjProject\WEBDJ\AutoPlateTest\polls\Excels\按行写入.xlsx")
    #print(r)
    #print(request.getReponse('data'))
    if request.method == 'get':
        print("1")
        return HttpResponse("你好")
    #print(r[0])
    #r = json.dumps(r[0])
    # for rdt in r:
    #     print(type(rdt))
    #     print(rdt)

    #print(type(eval(r)))
    # bb=r
    # b_dict={}
    # b_dict["data"]=bb
    # b_dict=b_dict
    # print(b_dict)
    #获取传入的参数
    redata = request.GET
    print("这个是传入的参数",redata.get('inputtext'))
    print(type(redata.get('inputtext')))
    #return HttpResponse(r[1]['yqreponse'])
    #return HttpResponse('{"yp":{"yqreponse":{"code": 1, "msg": null,"data": {"userName": "test", "userId": 104,"token": "token"}}}}')
    #return HttpResponse(r[1]["parm"])
    print(r[1]["parm"])
    print(type(r[1]["parm"]))
    #print(json.dumps(r[1]["parm"]))
    # r[0] = json.dumps(r[0],ensure_ascii=False)
    # r[1] =json.dumps(r[1],ensure_ascii=False)
    #把excle里的json数据 将某些value转成字典，最后转成合在一起转json，返回给前端所需要的数据
    for rdit in r:
        rdit["parm"] = json.loads(rdit["parm"])
        # sj = json.loads(rdit["sjreponse"])
        rdit["yqreponse"] = json.loads(rdit["yqreponse"])
        # print(pa)
        #print(type(json.loads(rdit["parm"])))
    list_r=[r[0],r[1]]
    ll = {}
    ll["l"] = list_r
    ll = json.dumps(ll,ensure_ascii=False)
    #{'userName':'test','password':'27f24543d35a34054d1517a5f7cd8b07'}  '{"userName":"test","password":"27f24543d35a34054d1517a5f7cd8b07"}'
    print(ll)
    return (ll)#r[0]["yqreponse"]ll.encode('utf-8').decode('unicode_escape')
def hello(request):
    return render(request,'polls/templates/demo.html')
def upfile(request):
    return render(request,'polls/templates/upload.html')
#bootstrap页面
def boothtml(request):
    return render(request,'polls/templates/btStrapStudy.html')
def uploadfile(request):
    '''
    :param request:
    :return:
    '''
    #文件上传
    print("这是文件上传方法")
    if request.method == "POST":
        newfile = request.FILES.get('newfile',None)
        if not newfile:
            return HttpResponse("提交无效，没有文件上传！")
        try:
            print("开始上传文件")
        except Exception as e:
            print("出现错误了")
            raise e
        finally:
            print("正在跳转文件下载页")
        to_path = open(os.path.join(BASC_DIR,'uploadfile',newfile.name),'wb')
        for chunk in newfile.chunks():
            to_path.write(chunk)
        to_path.close()
        return HttpResponse('文件上传成功！')
    else:
        return HttpResponse('非表单提交访问')
    #pass
def download_file():
    #文件下载
    print("这是文件下载方法")
    pass