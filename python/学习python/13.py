if __name__ == '__main__':
    x=1*1.01
    for i in range(1,53):
        x = x * 1.01
        x = x * 1.01
        x = x * 1.01
        x = x * 1.01
        x = x * 1.01
        x = x * 0.99
        x = x * 0.99
    print('{:.2f}'.format(x))




