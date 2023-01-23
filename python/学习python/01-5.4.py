if __name__ == '__main__':
    from random import*
    lst_who=['小马','小羊','小鹿']
    lst_where=['草地上','电影院','家里']
    lst_what=['看电影','听故事','吃晚饭']
    a=randint(0,2)
    b=randint(0,2)
    c=randint(0,2)
    print('{}在{}{}'.format(lst_who[a],lst_where[b],lst_what[c]))
