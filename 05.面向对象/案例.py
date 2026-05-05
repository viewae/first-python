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


def display_menu():
    """显示主菜单"""
    print("\n" + "="*50)
    print("       图书馆管理系统")
    print("="*50)
    print("1. 注册新会员")
    print("2. 会员登录")
    print("3. 查看所有图书")
    print("4. 查找图书")
    print("5. 退出系统")
    print("="*50)


def member_menu():
    """显示会员操作菜单"""
    print("\n" + "-"*50)
    print("       会员操作菜单")
    print("-"*50)
    print("1. 查看个人信息")
    print("2. 查看所有图书")
    print("3. 查找图书")
    print("4. 借书")
    print("5. 还书")
    print("6. 查看已借书籍")
    print("7. 退出登录")
    print("-"*50)


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

    current_user = None

    while True:
        if current_user is None:
            # 未登录状态，显示主菜单
            display_menu()
            choice = input("\n请选择操作 (1-5): ").strip()

            if choice == '1':
                # 注册新会员
                print("\n--- 注册新会员 ---")
                name = input("请输入姓名: ").strip()
                account = input("请输入账号: ").strip()
                password = input("请输入密码: ").strip()
                
                # 选择会员类型
                member_type = input("请选择会员类型 (1-普通会员 2-VIP会员): ").strip()
                if member_type == '2':
                    level = int(input("请输入VIP等级 (1-5): ").strip())
                    new_member = vip(name, account, password, level)
                else:
                    new_member = normal_member(name, account, password)
                
                lib.register_member(new_member)

            elif choice == '2':
                # 会员登录
                print("\n--- 会员登录 ---")
                account = input("请输入账号: ").strip()
                password = input("请输入密码: ").strip()
                current_user = lib.login(account, password)

            elif choice == '3':
                # 查看所有图书
                print("\n所有图书:")
                all_books = lib.get_all_books()
                if all_books:
                    for i, b in enumerate(all_books, 1):
                        print(f"  {i}. {b}")
                else:
                    print("  暂无图书")

            elif choice == '4':
                # 查找图书
                keyword = input("\n请输入搜索关键词（书名或作者）: ").strip()
                results = lib.find_book(keyword)
                if results:
                    print(f"\n找到 {len(results)} 本相关图书:")
                    for b in results:
                        print(f"  {b}")
                else:
                    print("未找到相关图书")

            elif choice == '5':
                # 退出系统
                print("\n感谢使用图书馆管理系统，再见！")
                break

            else:
                print("无效选择，请重新输入")

        else:
            # 已登录状态，显示会员菜单
            member_menu()
            choice = input("\n请选择操作 (1-7): ").strip()

            if choice == '1':
                # 查看个人信息
                print(f"\n{current_user}")

            elif choice == '2':
                # 查看所有图书
                print("\n所有图书:")
                all_books = lib.get_all_books()
                if all_books:
                    for i, b in enumerate(all_books, 1):
                        print(f"  {i}. {b}")
                else:
                    print("  暂无图书")

            elif choice == '3':
                # 查找图书
                keyword = input("\n请输入搜索关键词（书名或作者）: ").strip()
                results = lib.find_book(keyword)
                if results:
                    print(f"\n找到 {len(results)} 本相关图书:")
                    for i, b in enumerate(results, 1):
                        print(f"  {i}. {b}")
                else:
                    print("未找到相关图书")

            elif choice == '4':
                # 借书
                print("\n可借图书:")
                available_books = [b for b in lib.get_all_books() if b.available_num > 0]
                if available_books:
                    for i, b in enumerate(available_books, 1):
                        print(f"  {i}. {b}")
                    
                    try:
                        book_idx = int(input("\n请选择要借的图书编号: ").strip()) - 1
                        if 0 <= book_idx < len(available_books):
                            current_user.borrow_book(available_books[book_idx])
                        else:
                            print("无效的图书编号")
                    except ValueError:
                        print("请输入有效的数字")
                else:
                    print("当前没有可借的图书")

            elif choice == '5':
                # 还书
                borrowed = current_user.get_borrowed_books()
                if borrowed:
                    print("\n已借图书:")
                    for i, b in enumerate(borrowed, 1):
                        print(f"  {i}. {b}")
                    
                    try:
                        book_idx = int(input("\n请选择要还的图书编号: ").strip()) - 1
                        if 0 <= book_idx < len(borrowed):
                            current_user.return_book(borrowed[book_idx])
                        else:
                            print("无效的图书编号")
                    except ValueError:
                        print("请输入有效的数字")
                else:
                    print("您当前没有借阅任何图书")

            elif choice == '6':
                # 查看已借书籍
                borrowed = current_user.get_borrowed_books()
                if borrowed:
                    print(f"\n{current_user.name}的已借书籍:")
                    for i, b in enumerate(borrowed, 1):
                        print(f"  {i}. 《{b.name}》 by {b.author}")
                else:
                    print("您当前没有借阅任何图书")

            elif choice == '7':
                # 退出登录
                print(f"\n{current_user.name}，您已退出登录")
                current_user = None

            else:
                print("无效选择，请重新输入")


if __name__ == "__main__":
    main()
