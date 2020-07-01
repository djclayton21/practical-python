# practical python part 4, stock object


class Stock:
    __slots__ = ("name", "price", "_shares")

    def __init__(self, name, shares=0, price=0):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return (
            f"Stock(name='{self.name}', shares={self.shares}, price={self.price:.2f})"
        )

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("expected property shares to be of type int")
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        remaining_shares = self.shares - shares
        self.shares = remaining_shares
        return remaining_shares
