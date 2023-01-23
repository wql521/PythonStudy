if __name__ == '__main__':
    def judge(password):
        all = 0
        flag = 0
        a = 0
        b = 0
        c = 0
        d = 0
        for i in password:
            all += 1
            if (i.isdigit() and a == 0):
                flag += 1
                a = 1
            if (i.islower() and b == 0):
                flag += 1
                b = 1
            if (i.isupper() and c == 0):
                flag += 1
                c = 1
            if (all >= 8 and d == 0):
                flag += 1
                d = 1
        return flag


    password = input("请输入测试密码:")
    print("{}的密码强度为{}".format(password, judge(password)))