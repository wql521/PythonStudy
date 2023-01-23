if __name__ == '__main__':
    import search
    import sizhibot1
    import save
    import botreply

    me = input('请输入：')
    while True:
        print('-----------------------------')
        print('零号：' + me)
        you = search.search(me)
        if you == '没有找到相关内容':
            f = sizhibot1.sizhi(me)  # 调用思知机器人进行回答
            print('小思：' + f)  # 输出回答
            if '小思' in f or '小思' in me:
                continue
            else:
                save.save(me, f, 2, -1)  # 保存回答
            print('-----------------------------')  # 输出分割线
            me = botreply.bot(f)  # 调用零号机器人进行回答
        else:
            f0 = you[0]  # 获取思知回答
            print('小思：' + you[0])
            f1 = sizhibot1.sizhi(me)
            if '小思' in f1 or '小思' in me:
                continue
            else:
                k = you[1]
                r = you[2]
                save.save(me, f1, r + 1, k)
            print('-----------------------------')
            me = botreply.bot(f0)
