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
    @staticmethod
    def adding(*args):
        if 0<len(args)<11:
            #print('result is:',sum(args))
            print(args, f'Sum is {sum(args)}')

Client.adding(1,2,3,4,5)