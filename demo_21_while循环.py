print("这是一个计算平均值的小代码1")
user_input = input("请输入想要计算的数值(q输入完成):") # 用户输入的数值

 # 变量👇
sum = 0 # 用户输入的和
number = 0 # 用户输入的个数

while user_input != "q": # 循环运行用户输入的数值 不等于 ”q"
    num = float(user_input) # num:变量

    sum += num # 用户输入的和=用户输入的和+用户输入的数 (用于计算每一次输入的和
    #sum = sum +num (同上👆 并覆盖变量 sum

    number += 1 # 用户输入的次数 = 用户输入的次数 + 1（用于计算用户输入的个数

    # 用于循环用户输入值 (👇
    user_input = input("请输入想要计算的数值(q输入完成):")

if number == 0: # 如果用户输入的次数是否为 0
    average = 0 # 返回True（对的结果：平均值为 0

else: # :其他的
    average = sum / number  # 返回fake的结果
  # 平均值 = 总数 / 个数（👆

    if user_input == "q": # 如果用户输入的信息（是否 为 "q"
        print("所输入的总和为: " + str(sum)) # 打印出用户输入的总和

print("所计算出的平均数为: " + str(average)) # 打印出用户需要计算的平均值


