if __name__ == '__main__':
    count = 0
    def hanoi(n: int, start: str, end: str, mid: str):
        global count  # 将count改为本module的全局变量
        # 从最下面的那个圆盘开始编写移动
        if n == 1:
            # 打印第一个圆盘的移动位置
            print('{}:{}->{}'.format(1, start, end))
            # 记录本次移动
            count += 1
        # 然后 是除了最下面圆盘之外的圆盘
        else:
            # 递归最底层以上圆盘
            hanoi(n - 1, start, mid, end)
            # 打印最底层以上圆盘的位置
            print('{}:{}->{}'.format(n, start, end))
            count += 1
            # 再次递归本次函数　通过对参数位置的改变，从而实现递归关系的链接
            # 现在的开始柱子是上一次的中介柱子，现在的目标柱子是上一次的开始柱子，中介柱子是上一次的目标柱子
            hanoi(n - 1, mid, end, start)
    # 调用汉诺塔函数
    hanoi(12, 'a', 'c', 'b')
    print(count)

