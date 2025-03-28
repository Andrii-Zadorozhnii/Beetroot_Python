class Node:
    def __init__(self, data: int):
        """
        Инициализация узла бинарного дерева.
        :param data: Значение данных для узла.
        """
        self.data = data
        self.left = None
        self.right = None

    def add_main(self, head_value: int) -> None:
        """
        Добавление основного значения в дерево, если оно пустое.
        :param head_value: Значение, которое будет установлено, если узел пуст.
        """
        if self.data is None:
            self.data = head_value

    def add_left(self, value: int) -> None:
        """
        Добавление значения в левое поддерево.
        Если левый узел уже существует, рекурсивно добавляется в него.
        :param value: Значение для левого узла.
        """
        if self.left is None:
            self.left = Node(value)
        else:
            self.left.add_left(value)

    def add_right(self, value: int) -> None:
        """
        Добавление значения в правое поддерево.
        Если правый узел уже существует, рекурсивно добавляется в него.
        :param value: Значение для правого узла.
        """
        if self.right is None:
            self.right = Node(value)
        else:
            self.right.add_right(value)

    def preorder(self) -> None:
        """
        Обход дерева в префиксном порядке (сначала корень, затем левое поддерево, потом правое).
        """
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self) -> None:
        """
        Обход дерева в инфиксном порядке (сначала левое поддерево, затем корень, потом правое).
        """
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def postorder(self) -> None:
        """
        Обход дерева в постфиксном порядке (сначала левое поддерево, потом правое, затем корень).
        """
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)


# Создание дерева в глобальной области видимости
root = Node(5)
root.add_left(3)
root.add_left(4)
root.add_left(2)
root.add_left(1)
root.add_right(6)
root.add_right(7)
root.add_right(8)

# Пример обходов
print("Preorder:")
root.preorder()

print("\nInorder:")
root.inorder()

print("\nPostorder:")
root.postorder()
