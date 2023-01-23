if __name__ == '__main__':
    lst_staff=['李梅','张富','付妍','赵诺','刘江']
    award=[x for x in range(len(lst_staff))]
    dict_award=dict(zip(lst_staff,award))
    for i in dict_award.keys():
        if i=='张富':
            dict_award[i]=10000
        elif i=='赵诺':
            dict_award[i]=15000
        else:
            dict_award[i]=5000
    print(dict_award)