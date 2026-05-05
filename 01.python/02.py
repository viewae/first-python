# # # s1 = "库萨克"
# # # s2 = '23'
# # # print(f"我是{s1}  {s2}")
# #
# #
# #
# # num1 = input("数字1: ")
# # num2 = input("数字2: ")
# # print(int(num1) + int(num2))
#
# x = int(input("输入:"))
# y = int(input("输入:"))
# # print(x//y)
# ok_user = "18888888"
# ok_password = "666888"
#
# user = input("输入账号:")
#
# password = input("输入密码:")
#
# if user == ok_user and password == ok_password :
#     print("成功登录")
# else:
#     print("失败")

# qian = int(input("输入金额:"))
# if qian >= 500:
#     print("购买打八折",qian*0.8)
# elif qian < 100:
#     print("无折扣",qian)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i * j}",end="\t")
#     print()

# import random
# a= random.randint(1,100)
# print(a)

# s = [1,2,3,4,5]
# s.sort()
# print(s)
s = []

# for i in range(10):
#    num = int(input("输入数字:"))
#    s.append(num)
# print(s)
#
# s.sort()
# print(s)


# # 练习1：判断字符串是否是回文
# def is_palindrome(s):
#     """
#     判断字符串是否是回文
#     :param s: 输入的字符串
#     :return: 布尔值，True表示是回文，False表示不是
#     """
#     # 去除字符串中的空格（避免空格影响判断，比如"上海自来水来自海上"有空格也能正确判断）
#     s_clean = s.replace(" ", "")
#     # 判断正序和逆序是否相等（s_clean[::-1] 是Python中快速反转字符串的写法）
#     return s_clean == s_clean[::-1]
#
# # 测试示例
# test_str1 = "黄山落叶叶落山黄"
# test_str2 = "上海自来水来自海上"
# test_str3 = "hello"
#
# # 输出测试结果
# print(f"'{test_str1}' 是否是回文：{is_palindrome(test_str1)}")
# print(f"'{test_str2}' 是否是回文：{is_palindrome(test_str2)}")
# print(f"'{test_str3}' 是否是回文：{is_palindrome(test_str3)}")
#
# # 也可以让用户手动输入字符串判断
# user_input = input("\n请输入一个字符串，判断是否是回文：")
# print(f"你输入的'{user_input}' 是否是回文：{is_palindrome(user_input)}")

#
# 初始化购物车字典，键为商品名称，值为包含价格和数量的字典
# shopping_cart = {}
#
#
# def show_menu():
#     """显示操作菜单"""
#     print("\n===== 购物车管理系统 =====")
#     print("1. 添加商品")
#     print("2. 修改商品")
#     print("3. 删除商品")
#     print("4. 查询购物车")
#     print("5. 退出系统")
#     print("==========================")
#
#
# def add_goods():
#     """添加商品到购物车"""
#     try:
#         # 获取用户输入
#         name = input("请输入商品名称：").strip()
#         price = float(input("请输入商品价格："))
#         quantity = int(input("请输入商品数量："))
#
#         # 验证价格和数量是否为正数
#         if price <= 0 or quantity <= 0:
#             print("错误：价格和数量必须大于0！")
#             return
#
#         # 保存商品信息（覆盖已存在的同名商品）
#         shopping_cart[name] = {"price": price, "quantity": quantity}
#         print(f"✅ 商品【{name}】添加成功！")
#     except ValueError:
#         print("❌ 输入错误：价格必须是数字，数量必须是整数！")
#
#
# def modify_goods():
#     """修改购物车中的商品信息"""
#     name = input("请输入要修改的商品名称：").strip()
#
#     # 检查商品是否存在
#     if name not in shopping_cart:
#         print(f"❌ 购物车中没有【{name}】这个商品！")
#         return
#
#     try:
#         # 获取新的价格和数量
#         new_price = float(input("请输入新的商品价格："))
#         new_quantity = int(input("请输入新的商品数量："))
#
#         # 验证输入合法性
#         if new_price <= 0 or new_quantity <= 0:
#             print("错误：价格和数量必须大于0！")
#             return
#
#         # 修改商品信息
#         shopping_cart[name]["price"] = new_price
#         shopping_cart[name]["quantity"] = new_quantity
#         print(f"✅ 商品【{name}】修改成功！")
#     except ValueError:
#         print("❌ 输入错误：价格必须是数字，数量必须是整数！")
#
#
# def delete_goods():
#     """删除购物车中的商品"""
#     name = input("请输入要删除的商品名称：").strip()
#
#     # 检查商品是否存在并删除
#     if name in shopping_cart:
#         del shopping_cart[name]
#         print(f"✅ 商品【{name}】删除成功！")
#     else:
#         print(f"❌ 购物车中没有【{name}】这个商品！")
#
#
# def query_cart():
#     """查询并展示购物车所有商品"""
#     if not shopping_cart:
#         print("📦 购物车为空！")
#         return
#
#     print("\n🛒 购物车商品信息：")
#     for name, info in shopping_cart.items():
#         print(f"商品名称：{name}，商品价格：{info['price']}，商品数量：{info['quantity']}")
#
#
# def main():
#     """系统主循环"""
#     while True:
#         show_menu()
#         try:
#             choice = int(input("请输入操作序号（1-5）："))
#             if choice == 1:
#                 add_goods()
#             elif choice == 2:
#                 modify_goods()
#             elif choice == 3:
#                 delete_goods()
#             elif choice == 4:
#                 query_cart()
#             elif choice == 5:
#                 print("👋 感谢使用购物车管理系统，再见！")
#                 break
#             else:
#                 print("❌ 输入错误：请输入1-5之间的数字！")
#         except ValueError:
#             print("❌ 输入错误：请输入有效的数字（1-5）！")
#
#
# # 启动系统
# if __name__ == "__main__":
#     main()

# def num(*numbers):
#     b=min(numbers)
#     a=max(numbers)
#     return a,b
# print(num(1,2,3,4))

# def jc(n):
#     if n==1:
#         return 1
#     else:
#         return n*jc(n-1)
# print(jc(5))
#
# def good():
#     good_name = input("商品名:")
#     good_price = input("价格:")
#     good_num = input("数量:")
#     return good_name, good_price, good_num
# print(good())
#
# a2: int = 112

# class Student(object):
#     def __init__(self, name, chinese_course,math_course,english_course):
#         self.name = name
#         self.chinese_course = chinese_course
#         self.math_course = math_course
#         self.english_course = english_course
#
#     def __str__(self):
#         return self.name
#
#     def up(self,chinese_course,math_course,english_course):
#         if chinese_course is None or math_course is None or english_course is None:
#             return False
#         else
#             self.chinese_course = chinese_course
#             self.math_course = math_course
#             self.english_course = english_course
#             return True
#
#     def

# 商品类：存储单个商品的信息
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# 购物车类：管理多个商品的增删改查
class ShoppingCart:
    def __init__(self):
        self.items = []  # 存储所有商品对象

    # 1. 添加商品
    def add_product(self, name, price, quantity):
        # 检查商品是否已存在
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                print(f"商品 {name} 已存在，数量增加为 {item.quantity}")
                return
        # 不存在则新建商品
        new_product = Product(name, price, quantity)
        self.items.append(new_product)
        print(f"商品 {name} 已成功添加到购物车")

    # 2. 修改商品
    def modify_product(self, name, new_price, new_quantity):
        for item in self.items:
            if item.name == name:
                item.price = new_price
                item.quantity = new_quantity
                print(f"商品 {name} 已修改完成")
                return
        print(f"未找到商品 {name}，无法修改")

    # 3. 删除商品
    def delete_product(self, name):
        for i, item in enumerate(self.items):
            if item.name == name:
                del self.items[i]
                print(f"商品 {name} 已从购物车中删除")
                return
        print(f"未找到商品 {name}，无法删除")

    # 4. 查询所有商品
    def query_all(self):
        if not self.items:
            print("购物车为空")
            return
        print("\n=== 购物车商品列表 ===")
        for item in self.items:
            print(f"商品名称：{item.name}，商品价格：{item.price}，商品数量：{item.quantity}")
        print("======================\n")

# 主程序：控制台菜单交互
def main():
    cart = ShoppingCart()
    while True:
        print("\n===== 购物车管理系统 =====")
        print("1. 添加购物车")
        print("2. 修改购物车")
        print("3. 删除购物车")
        print("4. 查询购物车")
        print("5. 退出购物车")
        choice = input("请输入功能编号：")

        if choice == "1":
            name = input("请输入商品名称：")
            price = float(input("请输入商品价格："))
            quantity = int(input("请输入商品数量："))
            cart.add_product(name, price, quantity)

        elif choice == "2":
            name = input("请输入要修改的商品名称：")
            new_price = float(input("请输入新的商品价格："))
            new_quantity = int(input("请输入新的商品数量："))
            cart.modify_product(name, new_price, new_quantity)

        elif choice == "3":
            name = input("请输入要删除的商品名称：")
            cart.delete_product(name)

        elif choice == "4":
            cart.query_all()

        elif choice == "5":
            print("退出购物车管理系统，再见！")
            break

        else:
            print("输入无效，请重新输入")

if __name__ == "__main__":
    main()


