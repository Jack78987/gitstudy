# #待改进
# 无法搜索磁盘根目录会报错
# 使用正则匹配
import os,re

def getdir(path):
    filelist = os.listdir(path)
    for file in filelist:
        if file == '$RECYCLE.BIN' or file == 'System Volume Information' or file == 'Config.Msi':
            continue
        fpath = path + '\\' + file
        if os.path.isfile(fpath) and filename in file and file.endswith('.'+filetype):
            print(fpath)
        if os.path.isdir(fpath):
            getdir(fpath)


if __name__ == '__main__':
    path = input("输入查找路径：")
    filename = input("输入文件名：")
    filetype = input("文件后缀：")
    getdir(path)

