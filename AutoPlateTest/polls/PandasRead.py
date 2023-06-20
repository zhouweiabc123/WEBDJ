import pandas as pd

#pandas读取Excel文件
def read_excel(file,**kwargs):
    data_dict = [1]
    data_json = "{'a':'1'}"
    try:
        data = pd.read_excel(file,**kwargs)
    except Exception as e:
        print(e)
    finally:
        #print(data)
        print(type(data))
        #转换成字典，即[{},{}]
        data_dict = data.to_dict('records')
        #转换成json
        #data_json = data.to_json('table')
        #print(data_dict)
        print(data_json)
        return data_dict

if __name__ == '__main__':
    #a = read_excel(file="E:\A_test\AutoPlateTest\polls\Excels\按行写入.xlsx")
    a = read_excel(file=r"D:\A_Python\GitProjects\DjProject\WEBDJ\AutoPlateTest\polls\Excels\模板.xlsx")
    for i in a:
        print(i)
    print(a)

