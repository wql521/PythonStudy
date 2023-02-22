if __name__ == '__main__':
    lst_student = ['001', '李梅', 19, '002', '刘祥', 20, '003', '张武', 18]
    lst_student.extend(['004', '刘宁', 20, '006', '梁峰', 19])
    lst_student.insert(12, '005')
    lst_student.insert(13, '林歌')
    lst_student.insert(14, 20)
    print(lst_student[6:9])
    print(lst_student[1], lst_student[4], lst_student[7], lst_student[10], lst_student[13], lst_student[16])
    for i in (2,5,8,11,14,17):
        if lst_student[i]>19:
            print(lst_student[i-2:i+1],end='')
