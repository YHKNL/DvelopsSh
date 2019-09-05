# -*- coding:utf-8 -*-
import os
# 获取文件夹下的文件大小  https://www.jianshu.com/p/a5ec32322fd6
def Get_Dir_Size(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

# python 文件大小显示kb、mb或gb等  https://blog.csdn.net/mp624183768/article/details/84892999
def Covert_File_Size(size):
    kb = 1024;
    mb = kb * 1024;
    gb = mb * 1024;
    tb = gb * 1024;
    if size >= tb:
        return "%.1fTB" % float(size / tb)
    if size >= gb:
        return "%.1fGB" % float(size / gb)
    if size >= mb:
        return "%.1fMB" % float(size / mb)
    if size >= kb:
        return "%.1fKB" % float(size / kb)

os.chdir(r'/data/180neo4jbak') #更改当前工作目录

def Print_Size_Of_Current_Dir():
    file_size = dict()# 创建一个空的字典，用来存储我们的结果
    current_work_dir = os.curdir #指代当前目录，在windows系统下是'.'
    # current_work_dir = os.getcwd()#返回当前工作目录
    all_file = os.listdir(current_work_dir)#用列表列举当前目录中的文件名
    for each_file in all_file:#依次提取这个列表中的每一个元素（路径）
        if os.path.isdir(each_file) == True:#判断这个路径是否表示文件夹
            file_size.setdefault(each_file,Covert_File_Size(Get_Dir_Size(each_file)))
        else:# 如果不是文件夹，即是有后缀的那些文件
            file_size.setdefault(each_file, Covert_File_Size(os.path.getsize(each_file)))
    #下面我们来打印结果
    for type_file in file_size:
        print('【%s】:【%s】'%(type_file,file_size[type_file]))

if __name__ == '__main__':
    Print_Size_Of_Current_Dir()
    filesize = Get_Dir_Size('/data/180neo4jbak')
    print('There are %.3f' % (filesize / 1024 / 1024 /1024), 'Gb in /data/180neo4jbak')
#Print_Size_Of_Current_Dir()
