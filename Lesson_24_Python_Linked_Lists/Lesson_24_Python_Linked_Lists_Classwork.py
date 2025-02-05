# Для простого списку:
# допрацювати пошук, щоб за шуканим значенням повертався список id для випадку, якщо якесь значення зустрічається кілька раз
# реалізувати видалення елементу (підказка: збиральник мусора сам видаляе об“єкти, на які ніхто не посилається)
# реалізувати методи добавляння нового елементу як в голову списку, так і в хвіст


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def append_list_item(self, item):

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
        self.counter += 1

    def add_first_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = self.tail = item
        else:
            item.next = self.head
            self.head = item
            self.counter += 1

    def delete_item(self, item):
        current = self.head
        prev = None

        while current:
            if current.data == item:
                if prev:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                else:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None

                self.counter -= 1
                return 'Deleting is completed'
            prev = current
            current = current.next

        return 'Deleting un-completed, no current item'

    def display_most_popular_id(self, value):
        current = self.head
        while current:
            if current.data == value:
                print(current.data)
            current = current.next


list_1 = SingleList()
list_1.append_list_item(1)
list_1.append_list_item(3)
list_1.append_list_item(3)
list_1.add_first_list_item(2)
list_1.add_first_list_item(1)
list_1.display_most_popular_id(2)
