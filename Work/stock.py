# practical python part 4, stock object


class Stock:
    def __init__(self, name, shares=0, price=0):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        cost = self.shares * self.price
        return cost

    def sell(self, shares):
        remaining_shares = self.shares - shares
        self.shares = remaining_shares
        return remaining_shares
