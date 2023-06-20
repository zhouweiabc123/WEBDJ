import os
def red(filepath="pandas_rw.py",nowpath="./",totype="html",new_pypath="./"):
    '''
    :param filepath: 读取的文件名
    :param nowpath: 当前路径，或其他路径
    :param totype: python文件转html  "html"，或html转python  "python"，用os模块改变名字
    :return:
    '''
    flines=""
    #filepath=nowpath+filepath
    #如果是转成python文件
    if totype=="python":
        try:
            print(os.listdir().index("htmltopys"))
        except Exception as e:
            print(e)
            print("这是一个简单的错误，当前文件夹里没有htmltopys")
            os.mkdir("./htmltopys")
            print("创建成功")
        else:
            pass
        finally:
            print("必须执行的一步")

        try:
            # 打开html文件并读取
            with open(nowpath + filepath, "r", encoding="utf-8") as f:
                flines = f.readlines()
                for i in flines:
                    print(i)
            # 赋予新py文件名字
            filepath = filepath.replace(".html", ".py")
            # py文件存放地址，默认当前
            pythonfilepath = new_pypath + filepath
            with open(pythonfilepath, "w", encoding="utf-8") as rf:
                for i in flines:
                    rf.write(i)
                print("html转python成功")
            return "success"
        except Exception as  e:
            print("出现意外错误")
            print(e)
        #打开html文件并读取
        with open(nowpath+filepath,"r",encoding="utf-8") as f:
            flines=f.readlines()
            for i in flines:
                print(i)
        #赋予新py文件名字
        filepath=filepath.replace(".html",".py")
        #py文件存放地址，默认当前
        pythonfilepath=new_pypath+filepath
        with open(pythonfilepath,"w",encoding="utf-8") as rf:
            for i in flines:
                rf.write(i)
            print("html转python成功")
        return "success"
    else:
        #打开当前目录下的python文件
        with open(nowpath+filepath, "r", encoding="utf-8") as f:
            #print(f.readlines())
            flines = f.readlines()
            for i in flines:
                #i.write("./new_rdcontrol.html")
                print(i)
        #根据当前文件名，替换.py后缀为html
        filepath=filepath.replace(".py",".html")
        #判断htmls是否存在，不存在则创建
        try:
            print(os.listdir().index("htmls"))
        except Exception as e:
            print(e)
            print("这是一个简单的错误，当前文件夹里没有htmls")
            os.mkdir("./htmls")
            print("创建成功")
        else:
            print("htmls存在当前文件夹")
        finally:
            print("必须执行的一步")
        # print(os.listdir().index("htmls"))
        #创建html文件，放到当前目录的html文件夹下
        htmlfilepath=nowpath+"htmls/"+filepath
        print(filepath)
        with open(htmlfilepath,"w",encoding="utf-8") as rf:
            for i in flines:
                rf.write(i)
                print(i)
            print("写入到HTML成功！")
def pys_tohtml(filepaths=["pandas_rw.py"],nowpath="./"):
    #filepaths：仅当前目录下的py文件，暂不包括子集里的
    pathlist=[]
    for fp in filepaths:
        filepath = nowpath+fp
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
        print(os.listdir().index("htmls"))
    except Exception as e:
        print(e)
        print("这是一个简单的错误，当前文件夹里没有htmls")
        os.mkdir("./htmls")
        print("创建成功")
    else:
        pass
    finally:
        print("必须执行的一步")
    # print(os.listdir().index("htmls"))

    #有多少py文件就写多少HTML文件
    for flp in pathlist:
        #flines=[]
        #先读取每一个py文件
        if ".py" in flp:
            with open(flp,"r",encoding="utf-8") as pyf:
                flines=pyf.readlines()
                # for l in lines:
                #     flines.append(l)
            # 根据当前文件名，替换.py后缀为html
                flp=flp.replace(".py",".html")
                # 排除掉非Python文件，方便创建html文件，放到当前目录的html文件夹下
                htmlfilepath = nowpath + "htmls/" + flp
        else:
            print(flp+"：不是py文件")
        # 执行创建html文件，放到当前目录的html文件夹下
        with open(htmlfilepath, "w", encoding="utf-8") as rf:
            for i in flines:
                rf.write(i)
                print(i)
            print("写入到HTML成功！")
    # filepath = filepath.replace(".py", ".html")
    # # 创建html文件，放到当前目录的html文件夹下
    # htmlfilepath = nowpath + "htmls/" + filepath
    # print(filepath)
    # with open(htmlfilepath, "w", encoding="utf-8") as rf:
    #     for i in flines:
    #         rf.write(i)
    #         print(i)
    #     print("写入到HTML成功！")
    #pass
# red()
# class ReControl(RedisControl):
#     def r(self):
#         print(1234)

def htmls_topy(htmlpaths_name=["testxls_html1.html"],new_pypathn="./"):
    #直接循环调用转py的方法，将html转成Python文件
    for hname in htmlpaths_name:
        if ".html" in hname:
            red(filepath=hname,nowpath="./",totype="python",new_pypath=new_pypathn)
        else:
            print(hname+"：不是HTML文件")
    # with open(nowpath + htmlpaths_name, "r", encoding="utf-8") as f:
    #     flines = f.readlines()
    #     for i in flines:
    #         print(i)
    # filepath = htmlpaths_name.replace(".html", ".py")
    # pythonfilepath = nowpath+filepath
    # with open(pythonfilepath, "w", encoding="utf-8") as rf:
    #     for i in flines:
    #         rf.write(i)
    #     print("html转python成功")
    # return "success"
    # pass
if __name__ == '__main__':
    #red(filepath="study_gameui.py")
    import os
    #os.renames("./htmls/ARedisControl.py","./htmls/RedisControl.html")
    # rct = ReControl()
    #red(filepath="pandas_rw.py")
    listpys=os.listdir()
    lpys=[]
    for pyname in listpys:
        if ".py" not in pyname:
            print(pyname)
            listpys.remove(pyname)
        # if pyname=="__init__.py":
        #     listpys.remove(pyname)
    listpys.remove("__init__.py")
    print(listpys)
    # pys_tohtml(filepaths=["cpaaa.py","cpbbb.py","nopy"],nowpath="./")
    # print(os.listdir())
    print(listpys)
    for i in os.listdir():
        if ".html" in i:
            lpys.append(i)
            print(i)
        else:
            print(i+"：不是HTML文件类型")
    htmls_topy(htmlpaths_name=lpys,new_pypathn="./htmltopys/")
    #htmls_topy(htmlpaths_name=["testxls_html1.html","testxls_html2.html","a","b"],new_pypathn="./htmltopys/")