if __name__ == '__main__':
    def fun3(x):
        number=[]
        for i in range(3,8):
            x1=x*i
            x1 = str(x1)
            lst = list(map(int, x1))
            sum1 = sum(lst)
            number=number+[sum1]
        if (number[0]==number[1]) and (number[0]==number[2]) and (number[0]==number[3]) and (number[0]==number[4]):
            return x,number





    for x in range(100,1000):
        if fun3(x)!=None:
            print('x={}:x*3={},x*4={},x*5={},x*6={},x*7={}'.format(int(fun3(x)),3*int(fun3(x)),4*int(fun3(x)),5*int(fun3(x)),6*int(fun3(x)),7*int(fun3(x))))






