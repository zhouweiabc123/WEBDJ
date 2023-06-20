import os
import pandas as pd

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
def excel_tohtml(filename="testxls_html.xlsx",nowpath="./",htmldirpath="./"):
    excel_df=read_excel(nowpath+filename)
    print("读取成功!下面是数据")
    print(excel_df)
    try:
        xls_htmlname=filename.replace(".xlsx",".html")
        htmlpathname=htmldirpath+xls_htmlname
        print("最终文件写入的路径："+htmlpathname)
        excel_df.to_html(htmlpathname,index=False)
    except Exception as e:
        print("出错了")
        print(e)
    else:
        print(filename+"文件写入变成html成功")
def xls_tohtml(filepaths=["testxls_html.xlsx"],nowpath="./",htmldirpath="./xlshtmls/"):
    #filepaths：仅当前目录下的excel文件，暂不包括子集里的
    pathlist=[]
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

    #有多少excel文件就写多少HTML文件,调用 excel_tohtml()
    for flp in pathlist:
        #先读取每一个excel文件
        if ".xlsx" in flp:
            excel_tohtml(filename=flp,nowpath="./",htmldirpath=htmldirpath)
            print(flp)

            # 根据当前文件名，替换.xlsx后缀为html
            #flp=flp.replace(".xlsx",".html")
            # 排除掉非Python文件，方便创建html文件，放到当前目录的html文件夹下
            #htmlfilepath = htmlfilepath+ flp
        else:
            print(flp+"：不是excel文件")
        # 执行创建html文件，放到当前目录的html文件夹下

if __name__ == '__main__':
    listpys = os.listdir()
    lpys = []
    for pyname in listpys:
        if ".xlsx" in pyname:
            print(pyname)
            lpys.append(pyname)
            print("添加成功！")
        # if pyname=="__init__.py":
        #     listpys.remove(pyname)
    #listpys.remove("__init__.py")
    print(lpys)
    xls_tohtml(filepaths=lpys, nowpath="./")
    # print(os.listdir())
    # print(listpys)
    #excel_tohtml()
    #xls_tohtml(nowpath="./",filepaths=["testxls_html2.xlsx","testxls_html3.xlsx","a","b"])
