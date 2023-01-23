if __name__ == '__main__':
    # 导入模块
    import wx
    # 创建应用程序对象
    app = wx.App()
    # 创建主窗口
    frame = wx.Frame(None,title="hello world")
    # 在窗口上实现业务逻辑
    st=wx.StaticText(frame,-1,'hello world')
    # 显示窗口
    frame.Show()
    # 进入主事件循环
    app.MainLoop()

