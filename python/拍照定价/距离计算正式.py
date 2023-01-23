import xlrd
import Distance

if __name__ == '__main__':
    S = []  # 存放会员个数
    # 打开附件一.xls
    data = xlrd.open_workbook('附件一.xls')
    # 获取第一个sheet
    table = data.sheets()[0]
    # 获取行数
    nrows = table.nrows
    # 获取列数
    ncols = table.ncols
    # 遍历行
    for i in range(nrows):
        A = []  # 动态列表
        s = 0  # 动态变量
        if i == 0:
            continue
        else:
            a1 = table.cell(i, 1).value  # 获取任务的纬度
            if type(a1) == str:
                print(a1)
                a1 = float(a1)
            a2 = table.cell(i, 2).value  # 获取任务的经度
            if type(a2) == str:
                a2 = float(a2)
            # 打开附件二.xls
            data1 = xlrd.open_workbook('附件二.xls')
            # 获取第一个sheet
            table1 = data1.sheets()[0]
            # 获取行数
            nrows1 = table1.nrows
            # 获取列数
            ncols1 = table1.ncols
            for j in range(nrows1):  # 循环行
                if j == 0:
                    continue
                else:
                    b = table1.cell(j, 1).value
                    s = b.find(' ')
                    a3 = float(table1.cell(j, 1).value[0:s])  # 获取会员的纬度
                    a4 = float(table1.cell(j, 1).value[s + 1:-1])  # 获取会员的经度
                    if Distance.Distance(a1, a2, a3, a4) < 5000:  # 判断是否在5000米范围内
                        A.append(table1.cell(j, 0).value)  # 将任务编号添加到A列表中
                        r=table1.cell(j, 2).value#获取任务的限额
                        s=s+r  # 加法运算
            S.append(len(A))  # 将数量添加到S列表中
        print(s)
    print('会员数量：', S)
