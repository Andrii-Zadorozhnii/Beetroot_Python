class Client():
    def __init__(self, full_name, balance):
        self.full_name=full_name
        self._balance=balance
    def balance_getter(self):
        return self._balance
    def balance_setter(self, new_balance):
        self._balance=new_balance
    def balance_deleter(self):
        del self._balance

client1=Client('Full Name', 500)
print(client1.balance_getter())
client1.balance_setter(1000)
print(client1.balance_getter())
client1.balance_deleter()
print(client1.balance_getter())