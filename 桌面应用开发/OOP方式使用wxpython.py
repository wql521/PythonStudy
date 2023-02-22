import wx


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.SetTitle('最简单的应用程序')  # 设置窗口标题
        self.SetBackgroundColour('white')  # 设置窗口背景色
        self.SetSize((200, 220))  # 设置窗口大小
        self.Center()  # 设置窗口居中

        # 创建一个静态文本
        st = wx.StaticText(self, -1, 'hello world', style=wx.ALIGN_CENTER)
        # 设置字体
        font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL, False, '宋体')
        st.SetFont(font)


if __name__ == '__main__':
    app = wx.App()  # 创建应用程序对象
    frame = MainFrame(None)  # 创建主窗口
    frame.Show()  # 显示窗口
    app.MainLoop()  # 进入主事件循环
