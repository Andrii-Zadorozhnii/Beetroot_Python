class Client():
    number=0
    def __init__(self, full_name, balance):
        self.full_name=full_name
        self._balance=balance
        Client.number+=1
    def balance_getter(self):
        return self._balance
    def balance_setter(self, new_balance):
        self._balance=new_balance
    def balance_deleter(self):
        del self._balance
    @staticmethod
    def print_total():
        print(Client.number)

client1=Client('Full Name1', 500)
client2=Client('Full Name2', 500)
Client.print_total()