import random
from encodings.utf_8 import decode

import django.http.response
import requests
from django.shortcuts import render,HttpResponse
#引入
import json

from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect,JsonResponse
#from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

import pandas as pd

from testapps.ReadXmind import xmd

NaN=""

# Create your views here.
import pandas
def getinfo(request):
    print("访问一遍")
    user=range(0,20)
    for userid in user:
        print(userid)
    nums=[1,2,3,4,5]
    s=str(nums)
    print(s)
    return HttpResponse('{"nums":222,"user":"zhouwei","password":"密码123","userids":[1,2,3,4]}')
def get_tabledict(request):
    pass
#=========================================================================引入的view

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
    # if request.method == 'get':
    #     print("1")
    #     return HttpResponse("你好")
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
    return HttpResponse(ll)#r[0]["yqreponse"]ll.encode('utf-8').decode('unicode_escape')
def hello(request):
    return render(request,'templates/demo.html')
def upfile(request):
    return render(request,'templates/upload.html')
#bootstrap页面
def boothtml(request):
    return render(request,'templates/btStrapStudy.html')
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
    print(random.randint(0, 1000))
    print("请随意输入：",)
    a=input()
    print("这是文件下载方法",a)
    pass
#requests请求测试demo
def send_reqget(request):
    #发送
    print("开始请求发送request")
    try:
        result=requests.request(method="get",
            url="https://www.runoob.com/wp-content/themes/runoob/option/alisearch/v330/hot_hint.php?type=hint&user_id=52e90fcc-4eff-4918-a44f-8f494da97561",
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105"})
        print(result.status_code)
        print(result.text)
        return HttpResponse(result.content.decode(encoding="utf-8"))
    except Exception as e:
        print("发送request请求出现错误了")
        print(e)
    else:
        return HttpResponse("访问失败")

#读取XMind请求demo
def rxmd(request):
    #读取
    print("请求读取XMind")
    xd=xmd()
    xd=json.dumps(xd,ensure_ascii=False)
    print("读取成功！")
    return HttpResponse(xd)
#带table列表参数传参
def table_info(request):
    print("WEB端发送了请求")
    print("开始获取参数")
    tabledata=request.GET
    webdata1=tabledata.get("da")
    webdata2=tabledata.get("db")
    print(tabledata.get("da"))
    print(webdata2)
    tt={"t":tabledata}
    print(tabledata)
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105"}
    #requests.request(method="post",json=webdata,url="https://www.baidu.com",headers=header)
    return HttpResponse(webdata1+webdata2)

def all_tbinfo(request):
    print("一键执行前端列表所有接口请求")
    return "错误的返回"


#请求进入接口参数列表页
def table_html(request):
    #return redirect()
    return render(request=request,template_name="./templates/tb_datahtml.html")


if __name__ == '__main__':
    download_file()