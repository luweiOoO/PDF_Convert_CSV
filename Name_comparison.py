# -*- coding: utf-8 -*-
#判断两个文件夹下的文件名称是否一致
import os
import os.path
def nc():
    list1 = []#保存遍历csv后的文件名称列表
    list2 = []#保存遍历pdf后的文件名称列表
    #rootdir1 = "F:\BaiduNetdiskDownload\qzsh_data\data_csv"
    rootdir_csv =input('请输入csv文件所在文件夹路径：',)
    rootdir_pdf = input('请输入PDF文件文件夹所在路径：',)
    file_object = open('train_list.txt','w')
    for parent,dirnames,filenames1 in os.walk(rootdir_csv):
        for filename1 in filenames1:
            filename1 = filename1[:-4]
            file_object.write(filename1+ '\n')
            list1.append(filename1)#将文件名存入列表
            #print(filename1)
    #rootdir2 = "F:\BaiduNetdiskDownload\qzsh_data\data_pdf"

    #file_object = open('train_list.txt','w')
    for parent,dirnames,filenames2 in os.walk(rootdir_pdf):
        for filename2 in filenames2:
            filename2 = filename2 [:-4]
            file_object.write(filename2+ '\n')
            list2.append(filename2)#将文件名存入列表
            #print(filename2)
    #print(filenames2)
    count = 0
    for i in range(len(list2)):
        if list1[i] == list2[i]:
            print('正确')
        else:
            print('错误',list1[i],list2[i])
            count += 1
    print(count)
    file_object.close()