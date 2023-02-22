if __name__ == '__main__':
    mydict={'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
           'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._.', 'L': '._..',
           'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
           'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
           'Y': '_.__', 'Z': '__..'}
    you=input("请输入英文:")
    while not (you.isalpha() or ' '):
        print('并非全是英文')
        you=input("请重新输入英文:")
    you=you.upper()
    mylist=list(you)
    for i in mylist:
        if i==' ':
            continue
        print(mydict[i],end=' ')
