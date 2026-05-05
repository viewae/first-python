class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def buy(self):
        print(f"商品名字{self.name}")



if __name__ == '__main__':
    a1 = Product('colo','3')
    print(a1.name)
    print(a1.price)
    a1.buy()
