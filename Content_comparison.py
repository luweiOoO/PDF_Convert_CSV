# -*- coding: utf-8 -*-
import csv
import os
import os.path

def cc():
    rootdir_pdf_csv = input('请输入PDF转换csv存放文件夹路径：',)#'F:/ceshizhuanhuan/covert_csv'#PDF转换后的csv文件所在文件夹
    rootdir_csv =input('请输入csv文件所在文件夹路径：',)# 'F:\qzsh_data\data_csv'#原来的csv文件所在文件夹
    list1 = os.listdir(rootdir_csv)#csv文件夹内所有csv文件名列表
    list3 = os.listdir(rootdir_pdf_csv)#pdf-csv文件夹内所有csv文件名列表
    count = 0
    for o in range(0,len(list3)):
        list4 = []#存放初始pdf-csv遍历文件内容
        list5 = []#存放去除无效数据之后的pdf-csv文件内容
        list2 = []
        fileroad2 = os.path.join(rootdir_pdf_csv, list3[o])#获取对应pdf-csv文件地址
        csv_reader2 = csv.reader(open(fileroad2))#获取对应pdf-csv文件内容
        #读取pdf-csv文件内容并存放在list4列表
        for row in csv_reader2:
                     list4.append(row)
        #去除list4列表中每页pdf首行无用数据,并存放在list5中
        for i in range(0,len(list4)):
            if i % 53 == 0:
                pass
            else:
                list5.append(list4[i])
        #去除pdf-csv文件中首列无用数据，并将901.0转换成901
        for m in range(0,len(list5)):
            del list5[m][0]
            if list5[m][1] == '901.0':
                list5[m][1] = '901'
        fileroad1 = os.path.join(rootdir_csv, list1[o])#获取对应csv文件地址
        csv_reader1 = csv.reader(open(fileroad1))#获取对应csv文件内容
        #读取csv文件内容并放在列表list2中
        for row in csv_reader1:
            list2.append(row)
        del list2[0]#删除csv文件首行无效内容
        #对比pdf-csv和csv文件
        for k in range(0,len(list2)):
            pdf_csv_str = ''#提取pdf-csv表格中每行数据并放入字符串中
            csv_str = ''#提取csv表格中每行数据并放入字符串中
            #循环遍历存放pdf-csv每行内容
            for kk1 in list5[k]:
                if kk1 != ' ':
                    pdf_csv_str = pdf_csv_str + ' ' + kk1
            #循环遍历存放csv每行内容
            for kk2 in list2[k]:
                csv_str = csv_str + ' ' + kk2
            pdf_csv_str = pdf_csv_str[0:len(csv_str)]#删除pdf-csv存放内容字符串的多余空格
            if csv_str == pdf_csv_str:
                pass
                #print('true')
            else:
                print('false')
                print('文件名：',list1[o])
                print('对应行数：',k+2)
                #print('对应行内容：',list5[k],list2[k])
                print(csv_str)
                #print(len(csv_str))
                print(pdf_csv_str)
                #print(len(pdf_csv_str))
                print('------------')
                #print(list5[k+1])
                #print(list2[k+1])
                count += 1
        del list5,list2,list4
    print('-------------')
    print('不一致内容个数：',count)