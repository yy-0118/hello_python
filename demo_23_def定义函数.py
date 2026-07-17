
 # def(定义函数):计算扇形(圆心角,半径):
def calculate_sector(central_angle,radius):
    # 接下来是一些定义函数的代码

    # 扇形的面积 = 圆心角/360 * Π * 半径的2次方 👇
    sector_area = central_angle / 360 * 3.14 * radius ** 2

    print(f"此扇形面积为: {sector_area}")
    # 在f-字符串中 花括号{}内的 内容会被直接求值👆

# calculate_sector()