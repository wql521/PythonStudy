if __name__ == '__main__':
    s = 'When in the course of human events.it becomes necessary for one people to dissolve the political bands which have connected them with another,and to assume among the powers of the earth,the separate and equal station to which the Laws of Nature and of Nature"s God entitle them,a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.'
    s2=''
    cishu=[]
    for i in s:
        if i.isalpha():
            s2=s2+i
        s1=set(s2)  #s1一个集合，存放了不相同的字母
    for x in s1:
        cont=0
        for y in s2:
            if y==x:
                cont=cont+1   #次数存放了s1集合对应字母的次数，是一个列表
        cishu=cishu+[cont]
    cishu1=sorted(cishu,reverse=True)
    mydict=dict(zip(s1,cishu))
    print(mydict)
    good=[]
    for l in range(5):
        for n,m in mydict.items():
            if m==cishu1[l]:
                good=good+[n]
    good1='、'.join(good)
    print("出现次数排在前五的单词依次是:",good1)






