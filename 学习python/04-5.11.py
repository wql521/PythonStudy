if __name__ == '__main__':
    lst_busstop=['龙江新城市','阳光广场','汉江路','嫩江路','清凉山公路','拉萨路','五台山','莫愁路']
    a=input('请输入起点站:')
    b=input('请输入终点站:')
    n=a in lst_busstop
    m=b in lst_busstop
    while n!=True or m!=True:
        print('您所查询的不再本线路上哈')
        print('你想继续查询本线路吗？yes/no')
        you=input('yes/no：')
        if you == 'yes':
            a = input('请再次输入起点站:')
            b = input('请再次输入终点站:')
            n = a in lst_busstop
            m = b in lst_busstop
        else:
            break
    x=lst_busstop.index(a)
    y=lst_busstop.index(b)
    if x>y:
        print('您需要乘坐反方向线路')
    elif x<y:
        print('从{}站前往{}站需要{}站路'.format(a,b,(y-x)))
    elif x==y:
        print('您已经在终点站了哦')


