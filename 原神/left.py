def left(t):
    import pyautogui
    import time

    # 长按a键
    pyautogui.keyDown('a')
    time.sleep(t)
    pyautogui.keyUp('a')