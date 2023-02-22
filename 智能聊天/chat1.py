def chat1():
    import search
    import save
    import botreply
    me = input('请输入：')
    if me == 'exit':
        return 'exit'
    print('-----------------------------')
    print('我：' + me)
    you = search.search(me)
    if you == '没有找到相关内容':
        f = botreply.bot(me)
        print('你：' + f)
        save.save(me, f, 2, -1)
        print('-----------------------------')
    else:
        print('你：' + you[0])
        f1 = botreply.bot(me)
        k = you[1]
        r = you[2]
        save.save(me, f1, r + 1, k)
        print('-----------------------------')
