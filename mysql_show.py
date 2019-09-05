# -*- coding:utf-8 -*-import os
# 获取文件夹下的文件大小  https://www.jianshu.com/p/a5ec32322fd6
import os
import os.path
from decimal import Decimal

'''
path='/data/180mysqlbak'
def Get_Dir_Size(path):
    size = 0
    for root, dirs, files in os.walk(path):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    print('There are %.3f' % (size / 1024 / 1024 /1024), 'Gb in /data/180mysqlbak')

dict1 = {}
# 获取文件大小
def Get_File_Size(path):
    size=0
    fileList=os.listdir(path) #获取path目录下所以文件大小
    for filename in fileList:
        #获取组合后的路径
        pathTmp = os.path.join(path,filename)
        if os.path.isdir(pathTmp):
            get_size(pathTmp) #是目录就继续递归查找
        elif os.path.isfile(pathTmp):
            filesize1=os.path.getsize(pathTmp) #如果是文件，就获取相应的文件大小
        dict1[filename]=filesize1

#path= input("输入路径：").strip() #由用户指定文件路径
if __name__ == '__main__':
    Get_File_Size(path)
    for key,value in dict1.items():
        print('{key}: {value}bytes'.format(key = key, value = value)

#Print_Size_Of_Current_Dir()
'''
path = '/data/180mysqlbak'
dict1 = {}
def get_size(path):
    fileList = os.listdir(path) # 获取path目录下所有文件
    for filename in fileList:
        pathTmp = os.path.join(path,filename) # 获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   # 判断是否为目录
            get_size(pathTmp) # 是目录就继续递归查找
        elif os.path.isfile(pathTmp):  # 判断是否为文件
            filesize = os.path.getsize(pathTmp) # 如果是文件，则获取相应文件的大小
        dict1[filename]=filesize # 将文件的大小添加到字典
    #print(len(dict1))
    
#path= input("输入路径：").strip() #由用户指定文件路径
get_size(path)
for key,value in dict1.items():
    kk=value/1024/1024/1024
    print('{key}: {kk}Gb'.format(key = key, kk = kk)