class Product:
    """父类：商品基类"""
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def get_info(self):
        """获取商品信息（父类方法）"""
        print(f"商品名字: {self.name}, 价格: {self.price}, 数量: {self.num}")

    def sell(self):
        """销售商品（父类方法，子类可以重写）"""
        print(f"销售商品: {self.name}, 单价: {self.price}")


class New_product(Product):
    """子类1：新商品（继承自Product）"""
    def __init__(self, name, price, num, category):
        super().__init__(name, price, num)  # 调用父类构造函数
        self.category = category
    
    def get_info(self):
        """重写父类的get_info方法，添加类别信息"""
        print(f"【新商品】名称: {self.name}, 价格: {self.price}, 数量: {self.num}, 类别: {self.category}")

    def sell(self):
        """重写父类的sell方法，添加促销信息"""
        print(f"【新品促销】销售: {self.name}, 原价: {self.price}, 类别: {self.category}")


class Discount_product(Product):
    """子类2：打折商品（继承自Product）"""
    def __init__(self, name, price, num, discount):
        super().__init__(name, price, num)  # 调用父类构造函数
        self.discount = discount  # 折扣率，如0.8表示8折
    
    def get_info(self):
        """重写父类的get_info方法，添加折扣信息"""
        discounted_price = float(self.price) * self.discount
        print(f"【打折商品】名称: {self.name}, 原价: {self.price}, 折扣: {self.discount*10}折, 现价: {discounted_price:.2f}, 数量: {self.num}")

    def sell(self):
        """重写父类的sell方法，计算折后价"""
        discounted_price = float(self.price) * self.discount
        print(f"【打折销售】销售: {self.name}, 原价: {self.price}, 折后价: {discounted_price:.2f}")


def product_info(product):
    product.get_info()  # 多态：根据实际对象类型调用对应的方法


def sell_product(product):
    product.sell()  # 多态：根据实际对象类型调用对应的方法


if __name__ == '__main__':
    # 创建不同类型的商品实例
    normal_product = Product('普通可乐', '3', '5')
    new_product = New_product('新品雪碧', '4', '10', '饮料')
    discount_product = Discount_product('打折芬达', '5', '8', 0.8)

    print("\n多态示例1：使用多态函数查看商品信息\n")
    # 多态体现：同一个函数，传入不同的对象，执行不同的行为
    product_info(normal_product)      # 调用父类的get_info
    product_info(new_product)         # 调用New_product的get_info
    product_info(discount_product)    # 调用Discount_product的get_info

    print("\n多态示例2：使用多态函数销售商品\n")
    # 多态体现：同样的sell()调用，不同的子类有不同的销售逻辑
    sell_product(normal_product)      # 调用父类的sell
    sell_product(new_product)         # 调用New_product的sell
    sell_product(discount_product)    # 调用Discount_product的sell
