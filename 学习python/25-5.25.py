if __name__ == '__main__':
    mydict={'方糖':99,'X1':499,"魔盒":399,'曲奇':299}
    sum1=0
    m=0
    x=0
    for i in mydict:
        print("{}******{}元".format(i,mydict[i]))
        sum1 = mydict[i] + sum1
        if m < mydict[i]:
            m=mydict[i]
            x=i
    print('平均价格:',sum1/len(mydict))
    print('最高价格产品:',x)
