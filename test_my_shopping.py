import unittest # 导入函数库unittest
from my_shopping import ShoppingList # 从 my_shopping实现代码 导入 ShoppingList类

class TestShopping(unittest.TestCase): # 创建'测试购物'类,继承unittest库的子类TestCase
    # def setUp(self):
    #     self.shopping_list

    def test_get_total_price(self): # 创建一个测试获得总价的方法
        shopping_list = ShoppingList({"每日酸奶": 26, "百事可乐": 3, "奶奶的玉米": 5})
        # 👆一个变量 被赋予为 新创建一个测试的购物清单(实例对象）
        self.assertEqual(shopping_list.get_total_price(),34)
        # 👆测试的购物清单.使用断言方法（使用.get_total_price()方法获得总价，second:期望的值）

# python -m unittest test_my_shopping.py



























# import unittest
# from my_calculator import adder
#
# class TestAdder(unittest.TestCase):
#     def test_positive_add_positive(self):
#         self.assertEqual(adder(1, 2), 3)
#     def test_negative_add_positive(self):
#         self.assertEqual(adder(-1, 2), 1)