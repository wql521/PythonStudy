if __name__ == '__main__':
    import os

    path = os.getcwd()  # 获取当前路径
    files = os.listdir(path)  # 获取指定路径下的所有文件的文件名称
    lists = []  # 创建一个空的列表，用于存储提取的工作簿名
    for file in files:  # 遍历已获取的文件路径
        if file.split('.')[-1] in ['xls', 'xlsx']:
            for x in file:
                if x == '.':
                    lists.append(file[:file.index(x)])
    print(lists)  # 打印出已提取的文件名列表

    # 创建一个新的excel文件
    import xlwt

    wb = xlwt.Workbook()  # 创建一个新的excel文件
    sheet1 = wb.add_sheet('单周')
    sheet2 = wb.add_sheet('双周')
    wb.save('汇总空课表.xls')

    p = ['一', '二', '三', '四', '五']
    for h in range(len(p)):
        sheet1.write(0, h + 1, '星期{}'.format(p[h]))
        sheet2.write(0, h + 1, '星期{}'.format(p[h]))
        wb.save('汇总空课表.xls')

    q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(q)):
        sheet1.write(i + 1, 0, '第{}节'.format(q[i]))
        sheet2.write(i + 1, 0, '第{}节'.format(q[i]))
        wb.save('汇总空课表.xls')

    # 读取所有工作簿的数据
    import xlrd

    a1 = []
    a11 = []
    a2 = []
    a22 = []
    a3 = []
    a33 = []
    a4 = []
    a44 = []
    a5 = []
    a55 = []
    a6 = []
    a66 = []
    a7 = []
    a77 = []
    a8 = []
    a88 = []
    a9 = []
    a99 = []

    # 打开所有工作簿
    for i in range(len(lists)):
        wb = xlrd.open_workbook('{}.xls'.format(lists[i]), formatting_info=True)
        sheet = wb.sheet_by_index(0)  # 获取第一个工作表
        rows = sheet.nrows  # 获取第一个工作表的行数
        cols = sheet.ncols  # 获取第一个工作表的列数
        print(rows, cols)

        for j in range(1, rows):
            for k in range(1, cols):
                a = sheet.cell_value(j, k)  # 获取单元格的值
                print('单周',a)
                if j == 1:
                    a1.append(a)
                elif j == 2:
                    a2.append(a)
                elif j == 3:
                    a3.append(a)
                elif j==4:
                    a4.append(a)
                elif j==5:
                    a5.append(a)
                elif j==6:
                    a6.append(a)
                elif j==7:
                    a7.append(a)
                elif j==8:
                    a8.append(a)
                elif j==9:
                    a9.append(a)

        wb1 = xlrd.open_workbook('{}.xls'.format(lists[i]), formatting_info=True)
        sheet1 = wb1.sheet_by_index(1)  # 获取第二个工作表
        rows = sheet1.nrows  # 获取第二个工作表的行数
        cols = sheet1.ncols  # 获取第二个工作表的列数
        print(rows, cols)

        for j in range(1, rows):
            for k in range(1, cols):
                v = sheet.cell_value(j, k)  # 获取单元格的值
                print('双周', v)
                if j == 1:
                    a11.append(v)
                elif j == 2:
                    a22.append(v)
                elif j == 3:
                    a33.append(v)
                elif j==4:
                    a44.append(v)
                elif j==5:
                    a55.append(v)
                elif j==6:
                    a66.append(v)
                elif j==7:
                    a77.append(v)
                elif j==8:
                    a88.append(v)
                elif j==9:
                    a99.append(v)


    # 打开汇总表
    import xlutils.copy
    rb = xlrd.open_workbook('汇总空课表.xls', formatting_info=True)
    wb = xlutils.copy.copy(rb)
    sheet1 = wb.get_sheet(0)
    rows = rb.sheet_by_index(0).nrows
    cols = rb.sheet_by_index(0).ncols
    print(rows, cols)

    # 写入数据
    for i in range(1, rows):
        for j in range(1, cols):
            if i == 1:
                sheet1.write(i, j, a1[j - 1]+a1[j+4]+a1[j+9]+a1[j+14]+a1[j+19]+a1[j+24]+a1[j+29])
            elif i == 2:
                sheet1.write(i, j, a2[j - 1]+a2[j+4]+a2[j+9]+a2[j+14]+a2[j+19]+a2[j+24]+a2[j+29])
            elif i == 3:
                sheet1.write(i, j, a3[j - 1]+a3[j+4]+a3[j+9]+a3[j+14]+a3[j+19]+a3[j+24]+a3[j+29])
            elif i==4:
                sheet1.write(i, j, a4[j - 1]+a4[j+4]+a4[j+9]+a4[j+14]+a4[j+19]+a4[j+24]+a4[j+29])
            elif i==5:
                sheet1.write(i, j, a5[j - 1]+a5[j+4]+a5[j+9]+a5[j+14]+a5[j+19]+a5[j+24]+a5[j+29])
            elif i==6:
                sheet1.write(i, j, a6[j - 1]+a6[j+4]+a6[j+9]+a6[j+14]+a6[j+19]+a6[j+24]+a6[j+29])
            elif i==7:
                sheet1.write(i, j, a7[j - 1]+a7[j+4]+a7[j+9]+a7[j+14]+a7[j+19]+a7[j+24]+a7[j+29])
            elif i==8:
                sheet1.write(i, j, a8[j - 1]+a8[j+4]+a8[j+9]+a8[j+14]+a8[j+19]+a8[j+24]+a8[j+29])
            elif i==9:
                sheet1.write(i, j, a9[j - 1]+a9[j+4]+a9[j+9]+a9[j+14]+a9[j+19]+a9[j+24]+a9[j+29])

    sheet2 = wb.get_sheet(1)
    rows1 = rb.sheet_by_index(1).nrows
    cols1 = rb.sheet_by_index(1).ncols
    for x in range(1, rows1):
        for y in range(1, cols1):
            if x == 1:
                sheet2.write(x, y, a11[y - 1]+a11[y+4]+a11[y+9]+a11[y+14]+a11[y+19]+a11[y+24]+a11[y+29])
            elif x == 2:
                sheet2.write(x, y, a22[y - 1]+a22[y+4]+a22[y+9]+a22[y+14]+a22[y+19]+a22[y+24]+a22[y+29])
            elif x == 3:
                sheet2.write(x, y, a33[y - 1]+a33[y+4]+a33[y+9]+a33[y+14]+a33[y+19]+a33[y+24]+a33[y+29])
            elif x==4:
                sheet2.write(x, y, a44[y - 1]+a44[y+4]+a44[y+9]+a44[y+14]+a44[y+19]+a44[y+24]+a44[y+29])
            elif x==5:
                sheet2.write(x, y, a55[y - 1]+a55[y+4]+a55[y+9]+a55[y+14]+a55[y+19]+a55[y+24]+a55[y+29])
            elif x==6:
                sheet2.write(x, y, a66[y - 1]+a66[y+4]+a66[y+9]+a66[y+14]+a66[y+19]+a66[y+24]+a66[y+29])
            elif x==7:
                sheet2.write(x, y, a77[y - 1]+a77[y+4]+a77[y+9]+a77[y+14]+a77[y+19]+a77[y+24]+a77[y+29])
            elif x==8:
                sheet2.write(x, y, a88[y - 1]+a88[y+4]+a88[y+9]+a88[y+14]+a88[y+19]+a88[y+24]+a88[y+29])
            elif x==9:
                sheet2.write(x, y, a99[y - 1]+a99[y+4]+a99[y+9]+a99[y+14]+a99[y+19]+a99[y+24]+a99[y+29])
    # 保存
    wb.save('汇总空课表.xls')


