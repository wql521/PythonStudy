if __name__ == '__main__':
    from random import*
    T=randint(0,9)
    you=eval(input('请输入0-9的整数:'))
    N=1
    while you!=T:
        if you>T:
            print('遗憾，太大了！')
        elif you<T:
            print('遗憾，太小了！')
        you=eval(input('请再次输入0-9的整数:'))
        N+=1
    print('预测{}次，你猜中了！'.format(N))


