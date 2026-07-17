 # 赋予'hello' 为变量 s
s = "hello"
print(s.upper()) # 打印变量s upper；'HELLO'

# []是列表，方括号没东西就是空列表
shopping_list = []

 # append 用于添加物品至对象的末尾
 # ap；朝向 pend；悬挂
 # append； "追加" 或 "添加到末尾"。
shopping_list.append("键盘") # 添加 "键盘" 到购物清单末尾
shopping_list.append("键帽") # 添加 "键帽" 到购物清单末尾
print(shopping_list)

 # remove 用于移走对象中的物品
 # re；再次 move；移动
 # remove；再次移动-"移除"
shopping_list.remove("键帽")
print(shopping_list)

shopping_list.append("U盘")
shopping_list.append("鼠标")
shopping_list.append("音响")

 # 将对象第3个元素换成"xxx"
shopping_list[3] = "耳机"

print(shopping_list)

 # len函数；输出对象有多少个元素
print(len(shopping_list))
 # 打印出 索引对象第 1 位的元素
print(shopping_list[1])

 # price是价格
 # rice；大米   p批(发)大米-价格
price = [300, 200, 500, 50]

max_price = max(price) # 打印出最大的价格
min_price = min(price) # 打印出最小的价格
sorted_price = sorted(price) # 排序价格

print(max_price)
print(min_price)
print(sorted_price)




