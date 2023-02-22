if __name__ == '__main__':
    lst_fib=[1,1]
    for i in range(1,29):
        lst_fib.append(lst_fib[-2]+lst_fib[-1])
    print(lst_fib)
