class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        self.points += int(0.05 * amount)

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