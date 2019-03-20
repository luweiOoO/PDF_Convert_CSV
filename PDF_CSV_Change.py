# -*- coding: utf-8 -*-
import tabula
import os
import csv
import pandas
def pcc():
    rootdir_pdf = input('请输入PDF文件文件夹所在路径：',)
    rootdir_pdf_csv = input('请输入PDF转换存放CSV文件的文件夹路径（需先自己创建：）：')
    #rootdir_pdf = 'F:\BaiduNetdiskDownload\qzsh_data\data_pdf'#pdf文件夹

    for namestr_pdf in os.listdir(rootdir_pdf):
         print('当前正在处理:',namestr_pdf)
         fileroad_pdf = os.path.join(rootdir_pdf, namestr_pdf)
         df = tabula.read_pdf(fileroad_pdf, encoding='GBK', pages='all')
         df.to_csv('%s\%s.csv'%(rootdir_pdf_csv,namestr_pdf))