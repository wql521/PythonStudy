if __name__ == '__main__':
    s="语文：80，数学：82，英语：90，物理：85，化学：88，美术：80"
    x,y=3,5
    lst=[]
    while y<=(len(s)):
       lst.extend([eval(s[x:y])])
       x=x+6
       y=y+6
    print(lst)
    a=len(lst)
    b=sum(lst)
    print('{}门课程总分:{},{}门课程平均分{:.2f}'.format(a,b,a,b/a))
