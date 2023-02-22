if __name__ == '__main__':
    from random import*
    r=0
    for m in range(102,10000):
        n=randint(101,m)
        #print("n=",n)
        count1=0
        count2=0
        for i in range(n):
            x=randint(0,1)
            if x==0:
                count1+=1
            else:
                count2+=1
        #print('count1=',count1)
        #print('count2',count2)
        #if count1==count2:
            #print('0和1出现次数相同')
        #else:
            #print('0和1出现次数不同')
        count=count2-count1
        if count>0:
            c=count
        if count<0:
            c=-count
        print(c,end=' ')
        r+=1
        if count==0:
            print()
            print('出现0!',r)

