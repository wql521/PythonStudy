if __name__ == '__main__':
    import pyautogui
    #获取鼠标位置
    print(pyautogui.position())

    #移动鼠标到指定位置
    pyautogui.moveTo(23,520, duration=2)
    #鼠标点击
    pyautogui.click()

    #键盘输入
    pyautogui.typewrite('ni')
    pyautogui.press('1')

    pyautogui.typewrite('hao')
    pyautogui.press('1')

    pyautogui.typewrite('wo')
    pyautogui.press('1')

    pyautogui.typewrite('shi')
    pyautogui.press('1')

    pyautogui.typewrite('python')

    pyautogui.typewrite('hengaoxing')
    pyautogui.press('1')

    pyautogui.typewrite('weinifuwu')
    pyautogui.press('1')

    pyautogui.press('enter')
    pyautogui.press('enter')



