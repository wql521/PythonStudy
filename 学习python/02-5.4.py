if __name__ == '__main__':
    x=['31','28','31','30','31','30','31','31','30','31','30','31']
    a=int(input('请输入所查询的月份:'))
    while a!=0:
        print('{}月的天数:{}'.format(a,x[a-1]))
        a = int(input('请输入所查询的月份:'))
    else:
        print('结束！')

