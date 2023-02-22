if __name__ == '__main__':
    i1=[] #原码
    i2=[] #密文
    y=input("请输入明文:")
    for i in range(26):
        i1=i1+[chr(ord('a')+i)]
    x=eval(input("请输入偏移数目:"))
    for n in range(ord('a'),ord('z')+1):
        ch=n+x
        if ch<=122:
            mi=ch
        elif ch>122:
            mi=ch-122+96
        i2=i2+[chr(mi)]
    mydic=dict(zip(i1,i2))
    print('字典:',mydic)
    y=list(y)
    for u in range(len(y)):
        if y[u].islower():
            y[u]=mydic[y[u]]
        elif y[u].isupper():
            y[u]=mydic[chr(ord(y[u])+32)]
    y=''.join(y)
    print("密文:",y)

