import os


def menu():
    print('====================学生信息管理系统====================')
    print('-----------------------功能菜单-----------------------')
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出')
    print('-----------------------------------------------------')


def main():
    while True:
        menu()
        choice = int( input('请选择：') )
        if choice in [0, 1, 2 ,3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要推出系统吗？（y/n）\t')
                if answer == 'y' or answer == 'Y':
                    print('感谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


filename = 'student.txt'

def save(lst):
    print( str(lst) + '\n' )
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')

    for item in lst:
        stu_txt.write( str(item) + '\n' )

    stu_txt.close()     # 将文件流关闭


def insert():
    student_list = []       # 创建 学生列表，用以存储每个学生信息
    while True:
        id = input('请输入ID（如1001）：')
        if not id:      # id 为 null，跳出循环
            break

        name = input('请输入名字：')
        if not name:    # name 为 null，跳出循环
            break

        try:
            english = int( input('请输入英语成绩：') )
            python = int( input('请输入Python成绩：') )
            java = int( input('请输入Java成绩：') )
        except:
            print('输入无效，不是整数类型，请重新输入：')
            continue

        student = { 'id':id, 'name':name, 'english':english, 'python':python, 'java':java }         # 将录入的学生信息保存到【字典】中
        student_list.append(student)        # 将学生信息存到【列表】中

        answer = input('是否继续添加？（y/n）\t')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    save(student_list)  # 保存到文件中
    print('学生信息录入成功！')


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input("按 ID 查找请输入 1，按姓名查找请输入 2： ")
            if mode == '1':
                id == input('请输入学生 ID：')
            elif mode == '2':
                name == input('请输入学生 姓名：')
            else:
                print('您的输入有误，请重新输入！！！')
                search()
            with open(filename, 'r', encoding='utf-8' ) as rfile:
                student = rfile.readlines()     # 读出来的是 列表
                for item in student:            # 遍历 列表，得到 String
                    d = dict( eval(item) )      # 将 Strng 转成 字典
                    if d !='':
                        if d[ 'id' ] == id:
                            student_query.append(d)
                    elif name != '':
                        if d[ 'name' ] == name:
                            student_query.append(d)

            show_student(student_query)
            answer = input('是否要继续查询？（y/n）\t')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break

def show_student(lst):
    if len(lst):
        print('没有查询到学生信息，无数据显示！！！')
        return

    format_title = '{: ^6}\t{: ^12}\t{: ^8}\t{: ^10}\t{: ^10}\t{: ^8}'
    print( format_title.format( 'ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩' ) )

    format_date = '{: ^6}\t{: ^12}\t{: ^8}\t{: ^8}\t{: ^8}\t{: ^8}'
    for item in lst:
        print( format_date.format( item.get('id'),
                                   item.get('name'),
                                   item.get('english'),
                                   item.get('python'),
                                   item.get('java'),
                                   item.get('english') + item.get('python') + item.get('java')
                                   ) )


def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if student_id != '':
            if os.path.exists( filename ):
                with open( filename, 'r', encoding='utf-8' ) as file:
                    student_old = file.readlines()
            else:
                student_old = []

            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict( eval(item) )      # 将字符串转成字典
                        if d[ 'id' ] != student_id:
                            wfile.write( str(d) + '\n' )
                        else:
                            flag = True

                    if flag:
                        print( f'id为 {student_id} 的学生信息已被删除' )
                    else:
                        print( f'没有找到ID为 {student_id} 的学生信息' )
            else:
                print( '无学生信息' )
                break
            show()
            answer = input( '是否继续删除？（y/n）\t' )
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open( filename, 'r', encoding='utf-8' ) as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("请输入要修改的学院的ID： ")
    with open( filename, 'w', encoding='utf-8' ) as wfile:
        for item in student_old:
            d = dict( eval(item) )
            if d['id'] ==student_id:
                print('找到学生信息，可以修改他的相关信息')
                while True:
                    try:
                        d[ 'name' ] = input('请输入姓名： ')
                        d[ 'english' ] = input('请输入英语成绩： ')
                        d[ 'python' ] = input('请输入python成绩： ')
                        d[ 'java' ] = input('请输入java成绩： ')
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write( str(d) + '\n' )
                print('修改成功')
            else:
                wfile.write( str(d) + '\n' )
        answer = input('是否继续修改其他学生信息？（y/n）\n')
        if answer == 'y' or answer == 'Y':
            modify()
        else:
            return

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict( eval(item) )
            student_new.append(d)
    else:
        return
    asc_or_desc = input('请选择（0.升序   1.降序）')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()

    mode = input('请选择排序方式（1.按英语成绩排序\t2.按Python成绩排序\t3.按Java成绩排序\t0.按总成绩排序）')
    if mode == 1:
        student_new.sort(key = lambda x : int(x['english']), reverse = asc_or_desc_bool)
    elif mode == 2:
        student_new.sort(key = lambda x: int(x['python']), reverse = asc_or_desc_bool)
    elif mode == 3:
        student_new.sort(key = lambda x: int(x['java']), reverse = asc_or_desc_bool)
    elif mode == 0:
        student_new.sort(key = lambda x: int(x['english']) + int(student_new['python']) + int(student_new['java']), reverse = asc_or_desc_bool)

    else:
        print('您的输入有误，请重新输入')
        sort()

    show_student(student_list)




def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                print( f'一共有 {len(student)} 名学生 ')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息')

def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        for item in students:
            student_list.append( eval(item) )
        if student_list:
            show_student(student_list)
    else:
        print('暂未保存数据信息！！！')



if __name__ == '__main__':
    main()







