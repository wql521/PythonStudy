if __name__ == '__main__':
    from pathlib import Path

    folder_path = Path('/Users/wangqianlong/Desktop/Pycharm/python/空课表制作')
    file_list = folder_path.glob('*.xls*')  # 获取文件夹下所有工作簿的文件路径
    lists = []  # 创建一个空的列表，用于存储提取的工作簿名
    for i in file_list:  # 遍历已获取的文件路径
        file_name = i.name  # 提取工作簿的文件名
        for x in file_name:
            if x == '.':
                lists.append(file_name[:file_name.index(x)])
    print(lists)  # 打印出已提取的文件名列表

    # 青协部门
    list1 = ['汉语']

    # 创建一个新的excel文件
    import xlwt

    for x in list1:
        wb = xlwt.Workbook()
        sheet1 = wb.add_sheet('单周')
        sheet2 = wb.add_sheet('双周')
        a = list1.index(x)
        wb.save('{}空课表.xls'.format(list1[a]))

        p = ['一', '二', '三', '四', '五']
        for h in range(len(p)):
            sheet1.write(0, h+1, '星期{}'.format(p[h]))
            sheet2.write(0, h+1, '星期{}'.format(p[h]))
            wb.save('{}空课表.xls'.format(list1[a]))

        q=[1,2,3,4,5,6,7,8,9]
        for i in range(len(q)):
            sheet1.write(i+1, 0, '第{}节'.format(q[i]))
            sheet2.write(i+1, 0, '第{}节'.format(q[i]))
            wb.save('{}空课表.xls'.format(list1[a]))

    # 读取写入excel数据
    import xlrd
    import xlutils.copy

    f = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9,0]

    for q in lists:
        data = xlrd.open_workbook('{}.xls'.format(q))  # 打开xls文件
        table = data.sheets()[0]  # 打开第一张表
        s1 = table.nrows  # 获取表的行数
        for i in range(s1):
            if i == 0:
                continue
            if i % 2 == 0:
                continue
            if i == 19:
                break
            a = table.row_values(i)[3:8]
            b = table.row_values(19)[3]
            rb = xlrd.open_workbook('{}空课表.xls'.format(b))  # 打开xls文件
            wb = xlutils.copy.copy(rb)  # 复制一个xls文件
            sheet11 = wb.get_sheet(0)  # 获取第一个sheet 单
            sheet22 = wb.get_sheet(1)  # 获取第二个sheet 双
            for x in range(len(a)):
                if a[x] == '':
                    data1 = xlrd.open_workbook('{}空课表.xls'.format(b))  # 打开xls文件
                    table1 = data1.sheets()[0]  # 打开第一张表
                    table2 = data1.sheets()[1]  # 打开第二张表
                    s2 = table1.nrows  # 获取表的行数
                    for j in range(10):
                        if j == f[i]:
                            e = table1.row_values(j)[x+1]
                            e3 = table2.row_values(j)[x+1]
                            if e == '' and e3 == '':
                                e = q
                                e3 = q
                                sheet11.write(f[i], x + 1, e)
                                sheet22.write(f[i], x + 1, e3)
                                wb.save('{}空课表.xls'.format(b))
                            else:
                                if q in e:
                                    continue
                                else:
                                    e = e + ',' + q
                                    sheet11.write(f[i], x+1, e)
                                    wb.save('{}空课表.xls'.format(b))
                                if q in e3:
                                    continue
                                else:
                                    e3 = e3 + ',' + q
                                    sheet22.write(f[i], x+1, e3)
                                    wb.save('{}空课表.xls'.format(b))
                if '单' in a[x] and '双' not in a[x]:
                    data1 = xlrd.open_workbook('{}空课表.xls'.format(b))  # 打开xls文件
                    table1 = data1.sheets()[1]  # 打开第二张表
                    s2 = table1.nrows  # 获取表的行数
                    for j in range(s2):
                        if j == f[i]:
                            e1 = table1.row_values(j)[x+1]
                            if e1 == '':
                                e1 = q
                                sheet22.write(f[i], x + 1, e1)
                                wb.save('{}空课表.xls'.format(b))
                            else:
                                if q in e1:
                                    continue
                                else:
                                    e1 = e1 + ',' + q
                                    sheet22.write(f[i], x+1, e1)
                                    wb.save('{}空课表.xls'.format(b))
                if '双' in a[x] and '单' not in a[x] and '双语' not in a[x]:
                    data1 = xlrd.open_workbook('{}空课表.xls'.format(b))  # 打开xls文件
                    table1 = data1.sheets()[0]  # 打开第一张表
                    s2 = table1.nrows  # 获取表的行数
                    for j in range(s2):
                        if j == f[i]:
                            e2 = table1.row_values(j)[x+1]
                            if e2 == '':
                                e2 = q
                                sheet11.write(f[i], x + 1, e2)
                                wb.save('{}空课表.xls'.format(b))
                            else:
                                if q in e2:
                                    continue
                                else:
                                    e2 = e2 + ',' + q
                                    sheet11.write(f[i], x+1, e2)
                                    wb.save('{}空课表.xls'.format(b))


