from random import *
a1=int(input("请输入范围起点："))  
a2=int(input("请输入范围终点："))
a=randint(a1,a2)
name=eval(input("请输入数字:"))
while name>a2 or name<a1:
    print("所输入数字超出目标范围，请输入正确的数字：")
    name=eval(input("请输入数字:"))
name1=a1
name2=a2
while name!=a:
    if name>a:
        name2=name
        print("大了({},{})".format(name1,name2))       
    else:
        name1=name
        print("小了({},{})".format(name1,name2))   
    name=eval(input("数字:"))
    while name>name2 or name<name1:
        print("输入错误，请重新输入：")
        name=eval(input("数字:"))
else:
    print("砰！砰！砰！")
    print("答案是：",a) 
    x1=input("请输入第一个惩罚:") 
    x2=input("请输入第二个惩罚:")
    x3=input("请输入第三个惩罚:")
    x4=input("请输入第四个惩罚:")
    x5=input("请输入第五个惩罚:")
    x6=input("请输入第六个惩罚:")
    ls=[x1,x2,x3,x4,x5,x6]
    r=sample(ls,1)
    print(r)
    i=input("是否接受惩罚？")
    while i=="是":
        print("惩罚：",r)
        print("惩罚已经接受！")
        print("游戏结束！")
        break
    else:
        print("拒绝惩罚！")
        t=input("是否再次抽取惩罚？")
        while t=="是":
            r=sample(ls,1)
            print(r)
            print("惩罚：",r)
            print("请开始惩罚！")
            break
        else:
            print("强制再次抽取惩罚！")
            r=sample(ls,1)
            print(r)
            print("惩罚：",r)
            print("请开始惩罚！")
            

    






