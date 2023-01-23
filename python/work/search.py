if __name__ == '__main__':
    A=["秦俊贤","汤芷涵","许亮","余心悦","于馨琦","廖鸿伟","张鸿伟","谭秀娟","左乔升","杨佳宁","董咨含","王钱龙","赵怡豪","李苗苗","李维洁","刘乾","张郡铄","王世琳","冯雨晴","朱思勤","洪宇萌","魏薇","童杨凯"]  #武进青协人员名单
    B=[] # 还未获取人员
    from pathlib import Path
    folder_path =Path('/Users/wangqianlong/Downloads')
    file_list = folder_path.glob('*.xls*')  # 获取文件夹下所有工作簿的文件路径
    lists = []  # 创建一个空的列表，用于存储提取的工作簿名
    for file in file_list:  # 遍历已获取的文件路径
        if file.suffix in ['.xls','.xlsx']: # 判断文件后缀是否为xls或xlsx
            lists.append(file.stem) # 提取文件名，不包含后缀
    print("已经获取名单：",lists)
    print("共获取：",len(lists))
    for i in A:
        if i in lists:
            continue
        else:
            B.append(i)

    print("还未获取名单：",B)
    print("共未获取：",len(B))

    