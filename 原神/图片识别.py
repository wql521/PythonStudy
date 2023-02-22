if __name__ == '__main__':
    import pyscreenshot
    import pyautogui

    # 全屏截图
    im1 = pyscreenshot.grab()
    # 保存图片
    im1.save('screen.png')

    # 区域截图
    im2 = pyscreenshot.grab(bbox=(0, 0, 100, 100))
    # 保存图片
    im2.save('search.png')

    # 查找图片
    im3 = pyscreenshot.locateOnScreen('search.png')
    print(im3)

    # 查找图片，返回坐标
    im4 = pyscreenshot.locateAllOnScreen('search.png')
    print(im4)
    


    # 获取屏幕截图中像素的RGB颜色：
    img = pyautogui.screenshot()
    img.getpixel((100, 200))

    # 验证单个像素是否与给定的像素匹配
    pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))  # True


