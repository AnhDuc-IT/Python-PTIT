class Item:
    def __init__(self, id, name, quantity, price, discount):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
    def getCharge(self):
        return self.price * self.quantity - self.discount
    def __str__(self):
        return f'{self.id} {self.name} {self.quantity} {self.price} {self.discount} {self.getCharge()}'
if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        a = Item(input(), input(), int(input()), int(input()), int(input()))
        arr.append(a)
    arr.sort(key = lambda x : x.getCharge(), reverse = True)
    for x in arr:
        print(x)