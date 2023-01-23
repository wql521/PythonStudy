if __name__ == '__main__':
    from random import*
    n=randint(101,9999999)
    print("n=",n)
    count1=0
    count2=0
    for i in range(n):
        x=randint(0,1)
        if x==0:
            count1+=1
        else:
            count2+=1
    print('count1=',count1)
    print('count2=',count2)
    if count1==count2:
        print('0和1出现次数相同')
    else:
        print('0和1出现次数不同')

