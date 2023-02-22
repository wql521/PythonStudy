def ocr():
    import pyautogui
    # 控制键盘
    pyautogui.keyDown('command')
    pyautogui.press('1')

    # 按住鼠标左键移动
    pyautogui.moveTo(x=380, y=660, duration=1)
    pyautogui.dragRel(934,90,duration=1,button='left')
    pyautogui.mouseUp()
