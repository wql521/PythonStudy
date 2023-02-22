def right(t):
    import pyautogui
    import time

    # 长按d键
    pyautogui.keyDown('d')
    time.sleep(t)
    pyautogui.keyUp('d')
