if __name__ == '__main__':
    import chat

    while True:
        x = chat.chat()  # 调用chat函数
        if x == 'exit':
            break  # 如果输入exit，则退出程序
        else:
            continue  # 如果输入其他，则继续循环
