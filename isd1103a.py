class CashRegister:

    #1 the beginning of the program, includes "itemCount" and "totalPrice"
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    #2 adding new item increases "itemCount" by 1 and adds "price" to "totalPrice"
    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalprice = self._totalPrice + price

    #3 returns "totalPrice"
    def getTotal(self):
        return self._totalPrice

    #4 returns "itemCount"
    def getCount (self):
        return self._itemCount

    #5 starts the program over when the cycle is completed
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
