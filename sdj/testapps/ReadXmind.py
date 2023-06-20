#xmind文件读取
import pandas as pd
import xmindparser
import zipimport

#xmindzip = 1
def xmd():
    print("读取xmind中......")
    x = xmindparser.xmind_to_dict(r"C:\Users\zhouwei\Documents\主题readtest.xmind")
    print(type(x))
    print(x)
    try:
        x_df = pd.DataFrame(x)
    except Exception as e:
        print("出现错了，下面是错误信息")
        print(e)
    print(x_df)
    return x[0]
if __name__ == '__main__':
   print("读取xmind成功")
   print("看下面")
   xmd()