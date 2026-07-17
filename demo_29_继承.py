
class Employee:     # 👈创建(全部)员工类
    def __init__(self,name,id):  # 👈构造函数 （定义员工的属性
        self.name = name
        self.id = id

    def print_info(self):  # 👈定义打印函数
        print(f'姓名:{self.name} 工号:{self.id}')

class full(Employee): # 👈创建全职员工类（继承全部员工类
    def __init__(self,name,id,mon_salary): #  👈构造函数 定义全职员工的属性函数
        super().__init__(name,id) # 调用父类函数
        self.mon_salary = mon_salary # 定义月薪属性

    def calculate_monthly_pay(self): #👈构造函数 定义计算全职员工月薪的函数
        return self.mon_salary # 返回函数计算的结果（让函数计算结果不为：无


class part(Employee): # 👈创建兼职员工类（继承全部员工类
    def __init__(self,name, id,work_days,day_salary): # 👈姓名，工号，工作天数，日薪）
        # 定义全职员工的属性函数👆
        super().__init__(name, id) # 调用父类函数
        self.work_days = work_days # 定义工作天数属性
        self.day_salary = day_salary #定义日薪属性

    def calculate_monthly_pay(self): # 定义计算兼职员工月薪的函数
        return self.work_days * self.day_salary # 工作天数 * 日薪
        # 兼职员工的工作天数 * 日薪


one = full("一一","001",6000) # 调用函数full
two = part('二二','002',12,180) # 调用函数oart

one.print_info() # one变量调用打印函数
two.print_info()

print(one.calculate_monthly_pay()) # 打印出：计算月薪 再打印结果
print(two.calculate_monthly_pay())