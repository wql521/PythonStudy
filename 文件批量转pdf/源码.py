if __name__ == '__main__':
    import os
    # 获取当前路径
    path = os.getcwd()
    # 获取当前路径下的所有文件名
    file_list = os.listdir(path)
    list1= [] # 存放word文件名
    list2= [] # 存放ppt文件名
    list3= [] # 存放excel文件名
    list4= [] # 存放图片文件名
    list5= [] # 存放pdf件名
    for i in file_list:
        if i.endswith('.docx') or i.endswith('.doc'):
            list1.append(i)
        elif i.endswith('.pptx') or i.endswith('.ppt'):
            list2.append(i)
        elif i.endswith('.xlsx') or i.endswith('.xls'):
            list3.append(i)
        elif i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg'):
            list4.append(i)
        elif i.endswith('.pdf'):
            list5.append(i)
    print('word文件名:', list1)
    print('ppt文件名:', list2)
    print('excel文件名:', list3)
    print('图片文件名:', list4)
    print('pdf文件名:', list5)

    # 创建文件夹（存放转换后的文件）
    if not os.path.exists('转换后的文件'):
        os.mkdir('转换后的文件')
    # 创建子分类文件夹（存放word文件）
    if not os.path.exists('转换后的文件/word'):
        os.mkdir('转换后的文件/word')
    # 创建子分类文件夹（存放ppt文件）
    if not os.path.exists('转换后的文件/ppt'):
        os.mkdir('转换后的文件/ppt')
    # 创建子分类文件夹（存放excel文件）
    if not os.path.exists('转换后的文件/excel'):
        os.mkdir('转换后的文件/excel')
    # 创建子分类文件夹（存放图片文件）
    if not os.path.exists('转换后的文件/图片'):
        os.mkdir('转换后的文件/图片')

    # 将word文件转换为pdf文件
    # 将ppt文件转换为pdf文件
    # 将excel文件转换为pdf文件
    # 将图片文件转换为pdf文件






