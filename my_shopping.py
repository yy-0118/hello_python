
# shopping_list = {"每日酸奶": 26, "百事可乐": 3, "奶奶的玉米": 5} # 👈定义购物清单属性

# 👇定义一个叫:购物清单_的类
class ShoppingList:

    def __init__(self,shopping_list): # 👈初始化购物清单的内容

        self.shopping_list = shopping_list # 👈购物清单属性 被赋值为 变量的值

    def get_total_price(self): # 👈创建一个计算商品总价的方法
        total_price = 0 # 👈初始化总价为0
        for unit_price in self.shopping_list.values(): # 👈用单价遍历购物清单的values（值）
            total_price += unit_price # 👈总价 = 总价 + 单价
        # print(total_price)
        return total_price # 返回计算得到的总价格



# my_cart = ShoppingList() # 👈创建一个变量为ShoppingList类新的实例对象
# total_price = my_cart.get_total_price() # 👈创建价格变量 他是my_cart实例对象使用 计算商品总价方法得出来的结果
# print(f"总价格为:{total_price}") # 👈打印总价


