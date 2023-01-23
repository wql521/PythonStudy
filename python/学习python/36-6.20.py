if __name__ == '__main__':
    #https://blog.csdn.net/qq_41404557/article/details/122406114?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-13-122406114-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-13-122406114-null-null.nonecase
    def menum():  # 菜单
        print('==========雨伞信息管理系统==========')
        print('   ----------功能菜单----------')
        print('\t1.录入借伞人信息')
        print('\t2.查找借伞人信息')
        print('\t3.删除借伞人信息')
        print('\t4.修改借伞人信息')
        print('\t5.显示逾期未还雨伞')
        print('\t6.显示丢失雨伞信息')
        print('\t0.退出系统')
        print('----------------------------------')


    def main():  # 主函数
        while True:
            menum()
            choice = int(input('请选择:'))
            if choice in [0, 1, 2, 3, 4, 5, 6]:
                if choice == 0:
                    answer = input('您是否要退出系统(是/否)')
                    if answer == '是':
                        print('感谢使用')
                        break
                    else:
                        continue
                if choice == 1:
                    insert()
                if choice == 2:
                    search()
                if choice == 3:
                    delt()
                if choice == 4:
                    change()
                if choice == 5:
                    yuqi()
                if choice == 6:
                    diushi()

            else:
                print('您输入有误，请重新输入！')
                main()


    def insert():  # 录入借伞人信息
        person_list = []  # 存放借伞人的个人形式
        while True:
            name = input("请输入借伞人姓名:")
            if not name:
                break
            try:
                Number = input('请输入手机号码:')
                cls = input('请输入班级:')
                san = input('请输入借伞编号:')
                riqi = input('请输入借伞日期:')
            except:
                print('您输入有误!请重新输入')
                continue

    # def search():#查找借伞人信息

    # def delt():#删除借伞人信息

    # def change():#修改借伞人信息

    # def yuqi():#显示逾期未还雨伞

    # def diushi():#显示丢失雨伞信息
