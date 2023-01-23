import xlrd

if __name__ == '__main__':
    A=[]    #完成任务编号
    B=[]    #未完成任务编号

    #打开附件一.xlx
    data = xlrd.open_workbook('附件一.xls')
    #获取第一个sheet
    table = data.sheets()[0]
    #获取行数
    nrows = table.nrows
    #获取列数
    ncols = table.ncols
    for i in range(nrows):  # 循环行
        if i == 0:
            continue
        else:
            if table.cell(i, 4).value == 1:   #判断是否完成
                A.append(table.cell(i, 0).value)    #将完成任务编号添加到A列表中
            else:
                B.append(table.cell(i, 0).value)    #将未完成任务编号添加到B列表中

    print('完成任务编号：',A)
    print('未完成任务编号：',B)
    print('完成任务编号数量：',len(A))
    print('未完成任务编号数量：',len(B))
    print('完成任务占比：',len(A)/(len(A)+len(B)))
    print('未完成任务占比：',len(B)/(len(A)+len(B)))