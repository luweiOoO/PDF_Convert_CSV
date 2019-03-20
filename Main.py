# -*- coding: utf-8 -*-
import Name_comparison
import Content_comparison
import PDF_CSV_Change
print('功能选项：')
print('nc:文件名称对比')
print('cc:文件内容对比（对比前需执行pcc）')
print('pcc:pdf文件格式转换')
print('-------------------------------')
def main_method():
    choice = input('请选择功能:',)
    if choice == 'nc':
         Name_comparison.nc()
    elif choice == 'pcc':
        PDF_CSV_Change.pcc()
    elif choice == 'cc':
        Content_comparison.cc()
    else:
        print('输入参数有误，请重新输入')
        main_method()

main_method()