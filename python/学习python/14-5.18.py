if __name__ == '__main__':
    import random
    count=1
    lst=[]
    for i in range(1,21):
        x=random.randint(10,99)
        lst.extend([x])
    print(lst)
    n=sorted(lst[0:10],reverse=False)
    m=sorted(lst[-1:-11:-1],reverse=True)
    print('升序：',n)
    print('降序:',m)
