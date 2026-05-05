from abc import ABC, abstractmethod

class normal(ABC):
    """普通会员"""
    def __init__(self, name,account,password):
        self.account = account
        self.password = password
        self.name = name
        self.__borrow_book = []

    def borrow_book(self,book):
        """借书"""
        if len(self.__borrow_book) >= self.get_max_book():
            print("借书失败,借书已达上限")
            return False

        if book in self.__borrow_book:
            print("借书失败,已借过此书")
            return False

        if book.borrow():
            self.__borrow_book.append(book)
            print(f"{self.name}借书成功{book.name}")
            return True
        else:
            print("借书失败")
            return False

    def return_book(self,book):
        """还书"""
        if book in self.__borrow_book:
            self.__borrow_book.remove(book)
            book.return_book()
            print(f"{self.name}还书成功{book.name}")
        else:
            print("还书失败,未借过此书")

    def get_borrowed_books(self):
        """获取已借书籍列表"""
        return self.__borrow_book.copy()

    def __str__(self):
        """显示会员信息"""
        return f"会员:{self.name} | 账号:{self.account} | 已借:{len(self.__borrow_book)}/{self.get_max_book()}本"

    @abstractmethod
    def get_max_book(self) -> int:
        pass

class normal_member(normal):
    """普通会员"""
    def get_max_book(self) -> int:
        return 3


class vip(normal):
    """VIP会员"""
    def __init__(self, name,account,password,level):
        super().__init__(name,account,password)
        self.level = level

    def get_max_book(self) -> int:
        """获取最大借书数量"""
        return 6 + self.level

    def __str__(self):
        """显示VIP会员信息"""
        borrowed = len(self.get_borrowed_books())
        max_books = self.get_max_book()
        return f"VIP会员:{self.name} | 账号:{self.account} | 等级:{self.level} | 已借:{borrowed}/{max_books}本"


class book:
    """图书类"""
    def __init__(self,book_id,name,author,total_num):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.total_num = total_num
        self.available_num = total_num

    def borrow(self):
        """借书"""
        if self.available_num > 0:
            self.available_num -= 1
            return True
        else:
            print("借书失败，图书已借完")
            return False

    def return_book(self):
        """还书"""
        self.available_num += 1
        print("还书成功")

    def __str__(self):
        """显示图书信息"""
        status = "可借" if self.available_num > 0 else "已借完"
        return f"《{self.name}》 by {self.author} | 总数:{self.total_num} 剩余:{self.available_num} [{status}]"


class library:
    """图书馆类"""
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        """添加图书"""
        self.books.append(book)
        print(f"添加图书成功: {book.name}")

    def remove_book(self, book_id):
        """删除图书"""
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"删除图书成功: {book.name}")
                return True
        print("图书不存在")
        return False

    def find_book(self, keyword):
        """查找图书（支持书名或作者）"""
        results = []
        for book in self.books:
            if keyword in book.name or keyword in book.author:
                results.append(book)
        return results

    def get_all_books(self):
        """获取所有图书"""
        return self.books.copy()

    def register_member(self, member):
        """注册会员"""
        # 检查账号是否已存在
        for m in self.members:
            if m.account == member.account:
                print("注册失败，账号已存在")
                return False
        self.members.append(member)
        print(f"注册成功: {member.name}")
        return True

    def login(self, account, password):
        """登录"""
        for member in self.members:
            if member.account == account and member.password == password:
                print(f"登录成功: {member.name}")
                return member
        print("登录失败，账号或密码错误")
        return None

    def __str__(self):
        """显示图书馆信息"""
        return f"图书馆: {len(self.books)}本图书, {len(self.members)}个会员"


def main():
    """主程序入口"""
    # 创建图书馆实例
    lib = library()

    # 添加一些示例图书
    books_data = [
        (1, "Python编程从入门到实践", "Eric Matthes", 5),
        (2, "Java核心技术", "Cay S. Horstmann", 3),
        (3, "数据结构与算法分析", "Mark Allen Weiss", 4),
        (4, "深度学习", "Ian Goodfellow", 2),
        (5, "人工智能:现代方法", "Stuart Russell", 3),
    ]

    for book_id, name, author, total_num in books_data:
        lib.add_book(book(book_id, name, author, total_num))

    print("\n" + "="*50)
    print("欢迎使用图书馆管理系统")
    print("="*50)

    # 注册示例会员
    member1 = normal_member("张三", "user001", "123456")
    member2 = vip("李四", "vip001", "123456", level=2)
    
    lib.register_member(member1)
    lib.register_member(member2)

    # 模拟登录和操作
    print("\n--- 测试普通会员功能 ---")
    current_user = lib.login("user001", "123456")
    if current_user:
        print(current_user)
        
        # 显示所有图书
        print("\n所有图书:")
        for b in lib.get_all_books():
            print(f"  {b}")
        
        # 借书
        print("\n尝试借书:")
        python_book = lib.find_book("Python")[0]
        java_book = lib.find_book("Java")[0]
        ai_book = lib.find_book("人工智能")[0]
        
        current_user.borrow_book(python_book)
        current_user.borrow_book(java_book)
        current_user.borrow_book(ai_book)
        
        # 查看已借书籍
        print(f"\n{current_user.name}的已借书籍:")
        for borrowed in current_user.get_borrowed_books():
            print(f"  《{borrowed.name}》")
        
        # 还书
        print("\n尝试还书:")
        current_user.return_book(python_book)
        
        print(f"\n{current_user}")

    print("\n--- 测试VIP会员功能 ---")
    current_user = lib.login("vip001", "123456")
    if current_user:
        print(current_user)
        
        # VIP可以借更多书
        print("\nVIP会员借书测试:")
        all_books = lib.get_all_books()
        for b in all_books[:5]:  # 尝试借5本书
            current_user.borrow_book(b)
        
        print(f"\n{current_user}")

    print("\n" + "="*50)
    print("感谢使用图书馆管理系统！")
    print("="*50)


if __name__ == "__main__":
    main()
