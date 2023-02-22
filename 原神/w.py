def w(t):
    import pyautogui
    import time

    # 长按w键
    pyautogui.keyDown('w')
    time.sleep(t)
    pyautogui.keyUp('w')

