if __name__ == '__main__':
    import pyautogui
    import ocr识别
    import xerox
    import time
    import reply

    # 移动鼠标
    pyautogui.moveTo(41, 580, duration=1)
    # 点击鼠标
    pyautogui.click()

    ocr识别.ocr()

    time.sleep(3)
    # 读取剪切版内容
    s = xerox.paste()
    # 回复
    a = reply.relpy(s)
    # 写入剪切版
    xerox.copy(a)

    # 移动鼠标
    pyautogui.moveTo(443, 843, duration=1)
    # 点击鼠标
    pyautogui.click()
    # 控制键盘
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')

    # 获取当前日期
    time_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    a = time_now[5:]

    # 创建excel文件
    import xlwt

    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet1')
    ws.write(0, 0, '时间')
    # 保存excel文件
    wb.save('聊天记录' + time_now[0:4] + '.xls')

    # 写入excel文件
    import xlrd
    import xlrd.sheet.cell

    # 读取excel文件
    rb = xlrd.open_workbook('聊天记录' + time_now[0:4] + '.xls')
    table = rb.sheets()[0]  # 打开第一张表
    # 获取表的列数
    ncols = table.ncols
    for i in range(ncols):
        if table.cell(0, i).value == a:
            continue
        if table.cell(0, i).value == '':
            table.write(0, i, a)
            rb.save('聊天记录' + time_now[0:4] + '.xls')
            break
