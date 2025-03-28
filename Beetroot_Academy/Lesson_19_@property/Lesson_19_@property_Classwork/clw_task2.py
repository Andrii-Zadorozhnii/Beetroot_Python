class Auto():
    def __init__(self, mark, model, distance, price):
        self.mark=mark
        self.model=model
        self.distance=distance
        self.__price=price
    def price_getter(self):
        return self.__price
    def price_setter(self, new_price):
        self.__price=new_price
    def price_deleter(self):
        del self.__price
    my_property=property(price_getter, price_setter, price_deleter, 'doc')

auto1=Auto('MARK', 'MODEL', 10000, 5000)
print(auto1.my_property)
auto1.my_property=1000
#del auto1.my_property
print(auto1.my_property)
print(Auto.my_property.__doc__)