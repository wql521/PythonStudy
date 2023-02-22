if __name__ == '__main__':
    lst=['甲','乙','丙','丁']
    for i in lst:
        if (i!='甲')+(i=='丙')+(i=='丁')+(i!='丁')==3:
            print('好人:',i)