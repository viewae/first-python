class Product:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def get(self): #获取商品信息
        print(f"商品名字{self.name}")

    def sell(self): #销售商品
        print(f"销售商品{self.name}")

    def get_number(self): #获取商品数量
        print(f"商品数量{self.num}")

if __name__ == '__main__':
    product = Product('colo','3','5')


class New_product(Product):
    def __init__(self, name, price, num, category):
        super().__init__(name, price, num)  # 调用父类构造函数
        self.category = category
    
    def show_info(self):
        print(f"商品名称: {self.name}, 价格: {self.price}, 数量: {self.num}, 类别: {self.category}")


# 测试新类
new_product = New_product('cola', '4', '10', '饮料')
new_product.get()
new_product.show_info()#实例调用

New_product.show_info(new_product)#类名调用，传递实参