class Client():
    def __init__(self, full_name, balance):
        self._full_name=full_name
        self._balance=balance

    @property
    def full_name(self):
        return self._full_name
    @full_name.setter
    def full_name(self, name):
        check=True
        words=name.split(' ')
        if len(words)!=3:
            check=False
        for word in words:
            #print(word)
            if not word.istitle():
                check=False
        if check:
            self._full_name=name
        else:
            print('Name is not correct')

    @full_name.deleter
    def full_name(self):
        del self._full_name

client1=Client('Full Name Surname', 500)
client1.full_name=('Full Name Surname')
print(client1._full_name)