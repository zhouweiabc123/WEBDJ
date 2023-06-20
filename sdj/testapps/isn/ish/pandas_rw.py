import pandas as pd
from pandas import Timestamp
def read_excelq(filepaths:list):
    data=pd.read_excel(filepaths,encoding="utf-8")
    data = data.to_dict()
    df = pd.DataFrame(filepaths[0])
    df.to_html("abc")
    pd.read_html()

def read_excel(file,**kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file,engine="openpyxl",parse_dates=True,**kwargs)
        data_dict = data.to_dict("records")
        print("这是data_dict生成的df")
        print(pd.DataFrame(data_dict))
    except Exception as e:
        print(e)
    finally:
        print(data_dict)
        return data
def excel_tohtml(filename="testxls_html.xlsx",nowpath="./"):
    excel_df=read_excel(nowpath+filename)
    try:
        excel_df.to_html(nowpath+"testxls.html",index=False)
    except Exception as e:
        print("出错了")
        print(e)
    else:
        print(filename+"文件写入变成html成功")

def new_excel_tohtml(filename="testxls_html.xlsx",nowpath="./",htmldirpath="./"):
    excel_df = read_excel(nowpath + filename)
    print("读取成功!下面是数据")
    print(excel_df)
    try:
        xls_htmlname = filename.replace(".xlsx", ".html")
        htmlpathname = htmldirpath + xls_htmlname
        print("最终文件写入的路径：" + htmlpathname)
        excel_df.to_html(htmlpathname, index=False)
    except Exception as e:
        print("出错了")
        print(e)
    else:
        print(filename + "文件写入变成html成功")
def xls_tohtml(filepaths=["pandas_rw.py"],nowpath="./",htmldirpath="./xlshtmls/"):
    # filepaths：仅当前目录下的excel文件，暂不包括子集里的
    pathlist = []
    for fp in filepaths:
        filepath = fp
        pathlist.append(filepath)
    # 打开当前目录下的python文件

    # with open(nowpath + filepath, "r", encoding="utf-8") as f:
    #     # print(f.readlines())
    #     flines = f.readlines()
    #     for i in flines:
    #         # i.write("./new_rdcontrol.html")
    #         print(i)
    # 判断htmls是否存在，不存在则创建
    try:
        print(os.listdir().index("xlshtmls"))
    except Exception as e:
        print(e)
        print("这是一个简单的错误，当前文件夹里没有xlshtmls")
        os.mkdir("./xlshtmls")
        print("创建成功")
    else:
        pass
    finally:
        print("必须执行的一步")
    # print(os.listdir().index("htmls"))

    # 有多少excel文件就写多少HTML文件,调用 excel_tohtml()
    for flp in pathlist:
        # 先读取每一个excel文件
        if ".xlsx" in flp:
            new_excel_tohtml(filename=flp, nowpath="./", htmldirpath=htmldirpath)
            print(flp)

            # 根据当前文件名，替换.xlsx后缀为html
            # flp=flp.replace(".xlsx",".html")
            # 排除掉非Python文件，方便创建html文件，放到当前目录的html文件夹下
            # htmlfilepath = htmlfilepath+ flp
        else:
            print(flp + "：不是excel文件")
        # 执行创建html文件，放到当前目录的html文件夹下

def read_htmlxls(filename="testxls_html1.html",nowpath="./",xlspath="./"):
    '''
    用于把读取HTML的网页数据，写入Excel里
    filename：文件名
    nowpath：文件所处路径
    '''
    #预先获取应该生成的Excel文件名
    html_xlsname = xlspath+filename.replace(".html", ".xlsx")

    #读取单个HTML的table数据,返回DataFrame
    try:
        html_df = pd.read_html(nowpath + filename, encoding="utf-8")
        #写入创建Excel
        for hdf in html_df:
            print("写入中")
            hdf.to_excel(html_xlsname,index=False)

    except Exception as e:
        print(e)
    else:
        print("成功")
    return html_df

def new_read_htmlxls(xls_files=["testxls_html1.html","testxls_html2.html","a","b"],nowpath="./",xlspath="./xlspathfiles/"):
    '''
    用于把读取HTML的网页数据，写入Excel里
    filename：文件名
    nowpath：文件所处路径
    '''
    # 判断xlspathfiles是否存在，不存在则创建
    try:
        print(os.listdir().index("xlspathfiles"))
    except Exception as e:
        print(e)
        print("这是一个简单的错误，当前文件夹里没有xlspathfiles")
        os.mkdir("./xlspathfiles")
        print("创建成功")
    else:
        pass
    finally:
        print("必须执行的一步")
    #预先获取应该生成的Excel文件名
    xlsnames=[]
    df_xlslist=[]
    for xlsfile in xls_files:
        if ".html" in  xlsfile:
            html_xlsname = xlspath+xlsfile.replace(".html", ".xlsx")
            xlsnames.append(html_xlsname)
        else:
            print(xlsfile+"：不是HTML文件")

    #读取单个HTML的table数据,返回DataFrame,添加到dflist里面
        try:
            html_df = pd.read_html(nowpath + xlsfile, encoding="utf-8")
            #写入创建Excel
            for hdf in html_df:
                print("写入中......")
                hdf.to_excel(html_xlsname,index=False)

        except Exception as e:
            print(e)
        else:
            print("成功")


if __name__ == '__main__':
    #data=read_excel(file=r"C:\Users\zhouwei\Desktop\atest.xlsx")
    #data.to_html("./testxls_html.html",encoding="utf-8")
    #htmldata=read_htmlxls()
    #dfhtml=pd.DataFrame(htmldata)
    # data = pd.read_excel(r"C:\Users\zhouwei\Desktop\atest.xlsx")
    print("下面是从html读取的数据")
    #print(htmldata)
    # for i in htmldata:
    #     #astr=str(i)
    #     print(type(i))
    #     i=i.to_dict("list")
    #i=htmldata[0].to_dict("records")
    #print(i)
    #写入Excel
    print("开始写入")
    # try:
    #     htmldata[0].to_excel()
    # except Exception as e:
    #     print("出现错误了")
    #     print(e)
    import os
    listdirs=os.listdir()
    xlspath_list=[]
    print(listdirs)
    for l in listdirs:
        if ".html" in l:
            xlspath_list.append(l)
            print("文件："+l+"写入成功")
    #print(type(data))
    #excel_tohtml()
    #xls_tohtml(nowpath="./", filepaths=["testxls_html2.xlsx", "testxls_html3.xlsx", "a", "b"])
    print("操作成功")


    new_read_htmlxls(xls_files=xlspath_list)

