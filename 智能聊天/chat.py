def chat():
    import search
    import save
    me = input('请输入：')
    if me == 'exit':
        return 'exit'
    print('-----------------------------')
    print('我：' + me)
    you = search.search(me)
    if you == '没有找到相关内容':
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        f = input('请输入你想要的回答:')
        save.save(me, f, 2, -1)
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    else:
        print('你：' + you[0])
        print('-----------------------------')
        print('是否增添？')
        u = input('1:增添\n2:不增添\n：')
        if u == '1':
            print('****************************')
            f1 = input('你想要的回答是:')
            k = you[1]
            r = you[2]
            save.save(me, f1, r+1, k)
            print('****************************')


