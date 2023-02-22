if __name__ == '__main__':
    import 智能聊天.botreply
    import 智能聊天.save
    import sizhibot

    msg = input("输入第一句聊天对话：")
    while True:
        tx_robot = 智能聊天.botreply.bot(msg)
        print("思知机器人:", tx_robot)

        msg = sizhibot.sizhi(tx_robot)
        print("零号机器人:", msg)
