import os
def pys_tohtml(filepaths=["cpttt.py"],nowpath="./"):
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
        print(os.listdir().index("html"))
    except Exception as e:
        print(e)
        print("这是一个简单的错误，当前文件夹里没有html")
        os.mkdir("./html")
        print("创建成功")
    else:
        pass
    finally:
        print("必须执行的一步")
    # print(os.listdir().index("htmls"))

    #有多少py文件就写多少HTML文件
    for flp in pathlist:
        #先读取每一个py文件
        if ".py" in flp:
            with open(flp,"r",encoding="utf-8") as pyf:
                flines=pyf.readlines()

            # 根据当前文件名，替换.py后缀为html
                flp=flp.replace(".py",".html")
                # 排除掉非Python文件，方便创建html文件，放到当前目录的html文件夹下
                htmlfilepath = nowpath + "html/" + flp
        else:
            print(flp+"：不是py文件")
        # 执行创建html文件，放到当前目录的html文件夹下
        with open(htmlfilepath, "w", encoding="utf-8") as rf:
            for i in flines:
                rf.write(i)
                print(i)
            print("写入到HTML成功！")
if __name__ == '__main__':
    listpys = os.listdir()
    lpys = []
    for pyname in listpys:
        if ".py" not in pyname:
            print(pyname)
            listpys.remove(pyname)
        # if pyname=="__init__.py":
        #     listpys.remove(pyname)
    listpys.remove("__init__.py")
    print(listpys)
    pys_tohtml(filepaths=listpys, nowpath="./")
    print(os.listdir())
    print(listpys)