try: #👈 捕捉缩进可能会报错的代码
    # 男/女 👨🏻‍🤝‍👨🏻👇
    user_gender = input('你的性别：')


                  # 👇 函数：float(转变为浮点数)
    user_height = float(input('你的身高(单位：m)：'))
    user_weight = float(input('你的体重(单位：kg)：'))

    # 👇 BMI计算公式 = 体重kg / (身高m ** 2)
    user_BMI = user_weight / user_height ** 2 # 用户的BMI
except: # except后面要更错误类型 空白就是所有错误类型
    print("你输入的数据不合理，重新运行程序并输入正确的数据！😡😡😡")
    # 如果发生指定类型的异常，执行这里的处理代码

 # 偏瘦：user_BMI <= 18.5
 # 正常：18.5 < user_BMI <= 25
 # 偏胖：25 < user_BMI <= 30
 # 肥胖：user_BMI > 30

if user_BMI <= 18.5:
    bmi_category = '偏瘦'
elif 18.5 < user_BMI <= 25:
    bmi_category = '正常'
elif 25 < user_BMI <= 30:
    bmi_category = '偏胖'
else:
    bmi_category = '肥胖'

# if函数赋予 user_gender 为新的变量：title
if user_gender == '男':
    title = '先生'
elif user_gender == '女':
    title = '女士'


 # python （user_BMI）计算结果为整数 所以要使用str函数进行转化为字符串
print('你好' + title +  '！你的BMI为:' + str(user_BMI) +'\n经计算你的BMI类型为:' + bmi_category)

# print(f'你好{title}！你的BMI为:{user_BMI}\n经计算你的BMI类型为:{bmi_category}')
# f字符串 花括号内容直接求值




