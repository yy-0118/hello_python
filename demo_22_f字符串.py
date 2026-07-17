users_inf = {"张三":23,"李四":24,"王五":25}

 # item是项目的意思 s复数_items:多个项目(键，值）
for name,age in users_inf.items():  # .items(): 键值对
    # f"{name}的年龄为:{age}"
    output = f"{name}的年龄为:{age}" # 在f-字符串中 花括号{}内的 内容会被直接求值
    print(output)

print(type(name))

