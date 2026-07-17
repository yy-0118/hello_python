 # 创建"可爱猫咪“类 👇
class CuteCat:

    # __init__:初始化方法 可以定义对象有哪些属性 👇 self：这个cat的...
    def __init__(self,name,breed,age,gender): # 在括号内加入属性，属性之间用逗号隔开如 ：(属性1,属性2）
        self.name = name               # 👈 self.name：这个cat类的实例的name是: xxx
        self.breed = breed             # 👈 breed: 种类
        self.age = age                 # 👈 age: 年龄
        self.gender = gender           # 👈 gender： 性别
        if gender == "母":
            self.gender = '妹妹'
        if gender == '公':
            self.gender = '弟弟'

# 赋予cat1变量的 (CuteCat类的初始化信息) 👇
cat1 = CuteCat('歪歪','暹罗猫','七个月','公')
print(f"创建了一只猫猫{cat1.gender}：{cat1.name}({cat1.breed},{cat1.age}大)")

cat2 = CuteCat('海苔','三花猫','三个月','母')
print(f"创建了一只猫猫{cat2.gender}：{cat2.name}({cat2.breed},{cat2.age}大)")

cat3 = CuteCat('蜂蜂','大肥橘','一岁半','公')
print(f"创建了一只猫猫{cat3.gender}：{cat3.name}({cat3.breed},{cat3.age}大)")

cat4 = CuteCat('脆皮','三花猫','九十八岁','公')
print(f"创建了一只猫猫{cat4.gender}：{cat4.name}({cat4.breed},{cat4.age}大)")
