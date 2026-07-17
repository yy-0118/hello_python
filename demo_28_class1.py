class Student: # 创建类 名字必须大写开头
    def __init__(self,name,student_id): # 初始化方法，设置名字和学号
        self.name = name
        self.student_id = student_id
        self.grades = {'语文':0 , '数学':0 , '英语':0} # 成绩字典初始化

    def set_grade(self,course,grade):       # 设置成绩的方法(course,grade) 分别对应(键，值)
        if course in self.grades:           # 如果科目存在成绩字典中
            # 输出‘对’的内容
            self.grades[course] = grade     # 修改对应科目的成绩
            # print(f"已将{self.name}的{course}成绩设置为{grade}😃")

        else:                               # 如果科目存在成绩字典中
            # 输出‘错’的内容
            print(f"该科目{course}不存在😡")

    def print_grades(self):
        print(f"姓名:{self.name},学号:{self.student_id},全部成绩为:")

        for course in self.grades: # 用‘course’遍历成绩字典的key
                     # 👇 依次提取出每个科目(key)
            print(f"{course}:{self.grades[course]}分",end ='|')
                                     # 👆 成绩字典对应科目(键key)的分数(值value)



# chen = Student('小陈',26042901)
# chen.set_grade('语文',87)
# chen.set_grade('数学',100)
# chen.set_grade('英语',57)
# chen.print_grades()