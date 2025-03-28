class Auto():
    def __init__(self, mark, model, distance, price):
        self.mark=mark
        self.model=model
        self.distance=distance
        self.__price=price
    @property
    def price(self):
        '''
        doc
        '''
        return self.__price
    @price.setter
    def price(self, new_price):
        self.__price=new_price
    @price.deleter
    def price(self):
        del self.__price

auto1=Auto('MARK', 'MODEL', 10000, 5000)
print(auto1.price)
auto1.price=1000
#del auto1.price
print(auto1.price)
print(Auto.price.__doc__)