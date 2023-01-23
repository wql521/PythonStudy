import time

if __name__ == '__main__':
    # 获取当前日期
    time_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    a = time_now[5:]

    # 创建excel文件
    import xlwt
    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet1')
    ws.write(0, 0, '时间')
    ws.write(0, 1, '0')
    wb.save('聊天记录' + time_now[0:4] + '.xls')

    # 读取写入excel文件
    import xlutils.copy
    import xlrd

    data = xlrd.open_workbook('聊天记录' + time_now[0:4] + '.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    a1 = table.ncols  # 获取表的列数
    for i in range(a1):
        rb=xlutils.copy.copy(data)
        ws=rb.get_sheet(0)
        if table.cell(0, i).value == a:
            continue
        if table.cell(0, i).value == '':
            ws.write(0, i, a)
            rb.save('聊天记录' + time_now[0:4] + '.xls')
            break

