if __name__ == '__main__':
    from random import *
    a=randint(1,9)
    n=int(input('请输入正整数:'))
    x=a
    s=a
    for i in range(n-1):
        x=x*10+a
        s=s+x
    print(s)

