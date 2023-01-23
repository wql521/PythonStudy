import wx


class MainFrame(wx.Frame):
    """从wx.Frame派生主窗口类"""

    def __init__(self, parent):
        """构造函数"""

        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE)

        self.SetTitle('栅格布局')
        self.SetSize((400, 440))  # 设置窗口大小

        self._init_ui()  # 初始化界面
        self.Center()  # 窗口在屏幕上居中

    def _init_ui(self):
        """初始化界面"""

        panel = wx.Panel(self, -1)  # 创建容器面板
        sizer = wx.GridBagSizer(10, 10)  # 每个控件之间横纵间隔10像素

        st = wx.StaticText(panel, -1, "用户名")
        sizer.Add(st, (0, 0), flag=wx.TOP | wx.ALIGN_RIGHT, border=20)  # 在第0行0列，距离上边缘20像素，右对齐

        userName = wx.TextCtrl(panel, -1)
        sizer.Add(userName, (0, 1), (1, 3), flag=wx.EXPAND | wx.TOP, border=20)  # 在第0行1列，跨3列，距离上边缘20像素

        st = wx.StaticText(panel, -1, "密码")
        sizer.Add(st, (1, 0), flag=wx.ALIGN_RIGHT)  # 在第1行0列，右对齐

        password = wx.TextCtrl(panel, -1, style=wx.TE_PASSWORD)
        sizer.Add(password, (1, 1), (1, 3), flag=wx.EXPAND)  # 在第1行1列，跨3列

        st = wx.StaticText(panel, -1, "学历")
        sizer.Add(st, (2, 0), flag=wx.ALIGN_RIGHT)  # 在第2行0列，右对齐

        level1 = wx.RadioButton(panel, -1, "专科")
        sizer.Add(level1, (2, 1))  # 在第2行1列

        level2 = wx.RadioButton(panel, -1, "本科")
        sizer.Add(level2, (2, 2))  # 在第2行1列

        level3 = wx.RadioButton(panel, -1, "研究生及以上")
        sizer.Add(level3, (2, 3))  # 在第2行1列

        st = wx.StaticText(panel, -1, "职业")
        sizer.Add(st, (3, 0), flag=wx.ALIGN_RIGHT)  # 在第3行0列，右对齐

        professional = wx.Choice(panel, -1, choices=["学生", "程序员", "软件工程师", "系统架构师"])
        professional.SetSelection(0)
        sizer.Add(professional, (3, 1), (1, 3), flag=wx.EXPAND)  # 在第3行1列，跨3列

        # 语言技能
        st = wx.StaticText(panel, -1, "语言技能")
        sizer.Add(st, (4, 0), flag=wx.ALIGN_RIGHT | wx.LEFT, border=20)  # 在第4行0列，距离左边缘20像素，右对齐

        choices = ["C", "C++", "Java", "Python", "Lua", "JavaScript", "TypeScript", "Go", "Rust"]
        language = wx.ListBox(panel, -1, choices=choices, style=wx.LB_EXTENDED)
        sizer.Add(language, (4, 1), (1, 3), flag=wx.EXPAND)  # 在第4行1列，跨3列

        isJoin = wx.CheckBox(panel, -1, "已加入QQ群", style=wx.ALIGN_RIGHT)
        sizer.Add(isJoin, (5, 0), (1, 4), flag=wx.ALIGN_CENTER)  # 在第5行0列，跨4列, 居中

        btn = wx.Button(panel, -1, "提交")
        sizer.Add(btn, (6, 0), (1, 4), flag=wx.ALIGN_CENTER | wx.BOTTOM, border=20)  # 在第6行0列，跨4列, 居中

        sizer.AddGrowableRow(4)  # 设置第4行可增长
        sizer.AddGrowableCol(3)  # 设置第3列可增长

        panel.SetSizer(sizer)
        panel.Layout()


if __name__ == '__main__':
    app = wx.App()  # 创建应用程序对象
    frame = MainFrame(None)  # 创建窗口对象
    frame.Show()  # 显示窗口
    app.MainLoop()  # 进入主事件循环
