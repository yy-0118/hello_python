
 # contacts:"联系人“
 # dictionary数据结构 花括号{key:value}
 # 一个键(key)对应着一个值(value) 键为不可变
contacts = {"张三":"333","李四":"444"}

 # 字典可变 可添加 # 键存在会覆盖
contacts["王五"] = "555" # 添加["键"] = "值"

 # Add contact：添加联系人状态1
Add_contact_1 = input("查询通讯录联系人:")

 # 状态1/2
state_1 = "该联系人已存在该通讯录。" # state_1: 状态1
state_2 = "该联系人尚未添加通讯录。"

if Add_contact_1 in contacts: # 如果查询的联系人在通讯录中
                                                #  👇 通讯录中查询的联系人(键)的电话(值)
    print(state_1 + "\n该联系人号码为:" + (contacts[Add_contact_1]))
    ask_1 = input("是否更改此联系人的号码：")

    if ask_1 == "是": # 如果更改联系人的电话
        # 👆 将通讯录中查询的联系人(键)的电话(值)更改为:...

        ask_2 = input("此联系人的号码更改为：")
        contacts[Add_contact_1] = ask_2  # 覆盖原通讯录的号码

         # 成功更改(查询通讯录联系人:xx)的号码为：重新覆盖原通讯录的号码 👇
        print("成功更改" + Add_contact_1 + "的号码为：" + contacts[Add_contact_1])

else:
    print("该联系人尚未添加通讯录!") # 查询到联系人没有添加到字典
    Add_contact_2 = input("是否添加该联系人至通讯录:")
#             👆
    if Add_contact_2 == "是":
        Phone_number = input(Add_contact_1 + "的号码为:") # input输出为字符串
#       | 通讯录 |  添加该联系人  |的|     号码是      |
        contacts[Add_contact_1] = str(Phone_number)  # input输出为字符串 要用 str（内容）转印成正数
        print("添加成功")
        print("已添加" + Add_contact_1 + "至通讯录。\n" + Add_contact_1 + "的号码为" + contacts[Add_contact_1])
       #                                                   联系人                           联系人(键)的电话(值）
# print(Add_contact_1 + "号码为:" + (contacts[""]))