import wx


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE)  # 设置窗口风格
        self.SetTitle('组件集合')
        self.SetBackgroundColour('white')
        self.SetSize((860, 450))
        self.Center()

        # 创建一个面板放组件
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, '静态文本', pos=(20, 20))

        wx.TextCtrl(panel, -1, value='文本输入框', pos=(20, 50), size=(260, -1))

        wx.TextCtrl(panel, -1, value='密码输入框', pos=(20, 90), style=wx.TE_PASSWORD)

        wx.RadioButton(panel, -1, '单选按钮1', pos=(20, 130), style=wx.RB_GROUP)
        wx.RadioButton(panel, -1, '单选按钮2', pos=(100, 130))
        wx.RadioButton(panel, -1, '单选按钮3', pos=(180, 130))

        wx.CheckBox(panel, -1, '复选框', pos=(20, 160))
        wx.CheckBox(panel, -1, '文字在左侧的复选框', pos=(100, 160), style=wx.ALIGN_RIGHT)

        ch = wx.Choice(panel, -1, pos=(20, 190), choices=['选项1', '选项2', '选项3'])  # 选择框
        ch.SetSelection(0)  # 设置默认选中项

        wx.Button(panel, -1, '按钮', pos=(150, 190))

        wx.TextCtrl(panel, -1, value='只读文本框', pos=(20, 230), size=(260, 150),
                    style=wx.TE_MULTILINE | wx.TE_READONLY)


if __name__ == '__main__':
    app = wx.App()  # 创建应用程序对象
    frame = MainFrame(None) # 创建主窗口
    frame.Show()    # 显示窗口
    app.MainLoop()  # 进入主事件循环
