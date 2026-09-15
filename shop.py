class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        self.points += int(0.15 * amount)

    def get_discount_rate(self):
        if self.grade == "vip":
            return 0.10
        else:
            return 0.03

    def summary(self):
        return f"[{self.grade}] {self.name} (포인트: {self.points:,})"

class Order:
    def __init__(self, order_id, customer, items=None):
        self.order_id = order_id
        self.customer = customer
        self.items = items if items is not None else []

    def total_price(self):
        total = sum(price for _, price in self.items)
        discount = self.customer.get_discount_rate()
        return int(total * (1 - discount))

    def add_item(self, name, price):
        self.items.append((name, price))

    def pay(self):
        total = self.total_price()
        self.customer.add_points(total)

if __name__ == "__main__":
    vip_customer = Customer("Alice", "vip")
    basic_customer = Customer("Bob", "basic")

    order1 = Order(1, vip_customer)
    order1.add_item("라떼", 5500)
    order1.add_item("아메리카노", 4500)

    order2 = Order(2, basic_customer)
    order2.add_item("카푸치노", 6000)

    order3 = Order(3, vip_customer)
    order3.add_item("에스프레소", 4000)

    print(order1.total_price())
    print(order2.total_price())
    print(order3.total_price())

    order1.pay()
    order2.pay()
    order3.pay()

    print(vip_customer.summary())
    print(basic_customer.summary())