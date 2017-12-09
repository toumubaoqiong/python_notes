# 去除leakCanary产生的重复日志文件
import os
import re
import shutil

CURRENT_PATH = os.path.dirname(os.getcwd())
LEAKCANARY_LOG_PATH = os.path.join(CURRENT_PATH, "leakCanary")
BLOCKCANARY_LOG_PATH = os.path.join(CURRENT_PATH, "blockCanary")
LEAKPATTERN = re.compile(r'(bfc-leakcanary:[\d\D]*\*\sleaks)')
BLOCKPATTERN = re.compile(r'((\r\n\r\n)([\d\D]*)(\r\n\r\n))')

# 去除dict里面value相同的item
tuple_r_dict = lambda _dict: dict(val[::-1] for val in _dict.items())


# 获取文件名和文件路径dict
def visitdir(path):
    iternal_filenamepathmap = {}
    for root, dirs, files in os.walk(path):
        for filepath in files:
            iternal_filenamepathmap[filepath] = os.path.join(root, filepath)
    return iternal_filenamepathmap


# leakCanary获取文件名和指定内容dict
def getfilecontentmap(iternal_filenamepathmap, pattern):
    iternal_filenamecontentmap = {}

    for key, value in iternal_filenamepathmap.items():
        file = open(value, 'rb')
        rbfilecontent = file.read()
        filecontent = rbfilecontent.decode('utf-8', 'ignore')
        iternal_filenamecontentmap[key] = re.findall(pattern, filecontent)[0]
        file.close()
    return iternal_filenamecontentmap


# blockCanary获取文件名和指定内容dict
def getfilecontentmapex(iternal_filenamepathmap):
    iternal_filenamecontentmap = {}

    for key, value in iternal_filenamepathmap.items():
        file = open(value, 'rb')
        rbfilecontent = file.read()
        filecontent = rbfilecontent.decode('utf-8', 'ignore')
        iternal_filenamecontentmap[key] = filecontent.split('\r\n\r\n')[2]
        file.close()
    return iternal_filenamecontentmap


# 拷贝去重之后文件到新文件目录下
def copyfiles(iternal_filenamepathmap, iternal_filenamecontentmap_noduplicate, path):
    newdir = os.path.join(path, "distinct")

    if not os.path.exists(newdir):
        os.makedirs(newdir)
    #     连续删除时,此处回报异常,原因待查
    else:
        # rmdirfile(newdir)
        shutil.rmtree(newdir)
        os.makedirs(newdir)

    for key in iternal_filenamecontentmap_noduplicate.keys():
        if key in iternal_filenamepathmap.keys():
            shutil.copy(iternal_filenamepathmap[key], newdir)


def rmdirfile(dirpath):
    filespath = {}

    for root, dirs, files in os.walk(dirpath):
        for filepath in files:
            filespath[filepath] = os.path.join(root, filepath)

    for filepath in filespath.values():
        os.remove(filepath)

# 一次性读取
def read():
    f = open("2017-11-30_19-27-49.943.log", "rb")
    content = f.read()
    filecontent = content.decode('utf-8', 'ignore')
    fps = filecontent.split('\r\n\r\n')
    print(fps[2])
    # for fp in fps:
    #     print(fp)

    print(len(fps))
    f.close()


if __name__ == '__main__':

    read()