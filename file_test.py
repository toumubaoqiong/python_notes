'''
des:文件相关操作
author: zhua
'''
import os
import shutil
import glob
import re


# 文件创建和写入
def create_write():
    context = "hello world"
    file = open("hello.txt", "w")
    file.write(context)
    file.close()


# 文件的单行读取
def readline():
    file = open("hello.txt", "r")

    while True:
        # line = file.readline(2)
        line = file.readline()
        if line:
            print(line)
        else:
            break
    file.close()


# 多行读取
def readlines():
    f = open("hello.txt", "r")
    lines = f.readlines()

    for line in lines:
        print(line)
    f.close()


# 一次性读取
def read():
    f = open("hello.txt", "r")
    # content = f.read()
    content = f.read(5)
    print(content)
    print(f.tell())
    content = f.read(5)
    print(content)
    print(f.tell())
    f.close()


# 文件的写入
def writelines():
    f = open("hello.txt", "a")
    li = ["hello world\n", "hello China\n"]
    f.writelines(li)
    f.write("hello zhua")
    f.close()


# 文件的删除
def rm():
    if os.path.exists("hello.txt"):
        os.remove("hello.txt")


# 通过读取方式复制文件
def cp():
    src = open("hello.txt", "r")
    dst = open("hello1.txt", "w")
    dst.write(src.read())
    src.close()
    dst.close()


# 通过shutil拷贝
def cpwithshutil():
    shutil.copyfile("hello.txt", "hello2.txt")
    shutil.move("hello.txt", "../")
    shutil.move("hello2.txt", "hello3.txt")


# 文件重命名
def rename():
    li = os.listdir(".")
    print(li)

    if "hello1.txt" in li:
        os.rename("hello1.txt", "hi.txt")
    elif "hello3.txt" in li:
        os.rename("hello3.txt", "hello.txt")


# 修改后缀名
def renamesuffix():
    files = os.listdir(".")

    for filename in files:
        # pos = filename.find(".")
        # if filename[pos+1:] == "html":
        #     newname = filename[:pos+1] + "htm"
        #     os.rename(filename, newname)
        li = os.path.splitext(filename)
        if li[1] == ".htm":
            newname = li[0] + ".html"
            os.rename(filename, newname)


# glob路径匹配
def match():
    print(glob.glob("*.html"))


# 统计
def statistics():
    file = open("hello.txt")
    count = 0
    for line in file.readlines():
        li = re.findall("hello", line)
        if len(li) > 0:
            # li.count()统计hello出现的次数
            count = count + li.count("hello")

    print("查找到" + str(count) + "个hello")
    file.close()


# 内容替换
def exchange():
    f1 = open("hello.txt", "r")
    f2 = open("hello2.txt", "w")

    for line in f1.readlines():
        f2.write(line.replace("hello", "hi"))
    f1.close()
    f2.close()

if __name__ == '__main__':
    # create_write()
    # readline()
    # readlines()
    # read()

    writelines()
    # rm()
    # cp()
    # cpwithshutil()
    # rename()
    # renamesuffix()
    # match()
    # statistics()
    # exchange()

