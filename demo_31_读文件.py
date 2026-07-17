import os
print(os.path.abspath(__file__))

    # 返回两级 进回data文件夹 进回选中静夜思.txt            👇 as赋予打开文件对象的变量命名=file(文件)
with open("..\\data\\静夜思.txt","r",encoding="utf-8") as file: # with自动管理资源 自动关闭资源
                 # r表示读 w表示写 👆        👆 用来指定文本文件的编码格式
    # 所有和读文件相关的操作都要 缩进字符
    content = file.readlines() # 命名变量=(读文件).打印每行内容转化为列表
    print(content) # 打印读文件