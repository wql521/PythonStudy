if __name__ == '__main__':
    pi=3.14159
    def fun(r):
        global pi
        s=pi*r*r
        l=2*pi*r
        return '面积:{}'.format(s),'周长:{}'.format(l)
    print(fun(3))
    print(type(fun(3)))

if __name__ == '__main__':
    def fun(n):
        if n==1:
            return 1
        else:
            return n*fun(n-1)

    for i in range(1,9+1):
        print('{}!='.format(i),fun(i))


if __name__ == '__main__':
    def fun1(a,b,*c,**d):
        print(a,b,c,d)
#一个*获取元组，两个**获取字典
    print(fun1(10,99,[12,22,44],33,i=1,u=2))
