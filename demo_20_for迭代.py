temperature_dict = {"111":36.4, "112":38.5, "113":36.2}
 # ("113", 36.2)  # 这行是注释或示例，不是可执行代码

 # for(迭代) 变量名1 in 可迭代的对象(列表，字典，字符串） loop
 # for就是点名同学 变量名1:班上的每一位同学 可迭代的对象:班上所有的同学
for staff_id in temperature_dict.keys(): # .key() 因为迭代的对象为字典 代表 键
    print(staff_id)
for temperature in temperature_dict.values(): # .values() 因为迭代的对象为字典 代表 值
    print(temperature)

 # range:整数数列 (起始值,结束值,步长默认1 )
zero = 0
for integer in range(1,101,1):
    zero = zero + integer # zero = 1+0 + 2+0...
print(zero)

list1 = ["你", "好", "吗", "兄", "弟"]
for item in range(0,len(list1)):
    print(list1[item])