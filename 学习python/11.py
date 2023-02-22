if __name__ == '__main__':
    from random import*
    RND1=randint(0,100)
    RND2=randint(0,100)
    for i in range(1,101):
        if RND1%i==0 and RND2%i==0:
            x=i #最大公约数
    r=RND2*RND1
    y=r/x #最小公倍数
    print('最大公约数{},最小公倍数{}'.format(x,int(y)))

