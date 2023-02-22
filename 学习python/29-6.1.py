if __name__ == '__main__':
    dic_city={'张三风':['北京','成都'],'李茉绸':['上海','广州','兰州'],'慕容福':['太原','西安','济南','上海']}
    cont=0
    name=[]
    for x,y in dic_city.items():
        z=len(y)
        print('{}去过{}个城市'.format(x,z))
        for i in y:
            if i=='上海':
                cont+=1
                name=name+[x]
    t='、'.join(name)
    print('去过上海的有{}人,他们分别是{}'.format(cont,t))
