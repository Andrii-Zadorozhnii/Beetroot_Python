class Node:
    """
    Клас для представлення вузла дерева.

    Атрибути:
        value (str): Значення вузла.
        children (list[Node]): Список дочірніх вузлів.
    """

    def __init__(self, value: str) -> None:
        self.value: str = value
        self.children: list[Node] = []

    def add_child(self, child: "Node") -> None:
        """
        Додає дочірній вузол до поточного вузла.

        Параметри:
            child (Node): Вузол, який додається як дочірній.
        """
        self.children.append(child)

    def find_node(self, value: str) -> "TreeNode | None":
        """
        Шукає вузол у дереві за значенням.

        Параметри:
            value (str): Значення вузла, який шукається.

        Повертає:
            TreeNode | None: Вузол, якщо знайдено, або None, якщо вузол відсутній.
        """
        if self.value == value:
            return self
        for child in self.children:
            found = child.find_node(value)
            if found:
                return found
        return None

    def insert_subtree(self, parent_value: str, subtree: "Node") -> bool:
        """
        Вставляє піддерево у вказаний вузол.

        Параметри:
            parent_value (str): Значення вузла, до якого додається піддерево.
            subtree (TreeNode): Піддерево для вставки.

        Повертає:
            bool: True, якщо вставка успішна, інакше False.
        """
        parent_node = self.find_node(parent_value)
        if parent_node:
            parent_node.add_child(subtree)
            return True
        return False

    def remove_subtree(self, value: str) -> bool:
        """
        Видаляє піддерево, починаючи з вказаного вузла.

        Параметри:
            value (str): Значення вузла, з якого починається видалення.

        Повертає:
            bool: True, якщо видалення успішне, інакше False.
        """
        for i, child in enumerate(self.children):
            if child.value == value:
                del self.children[i]
                return True
            if child.remove_subtree(value):
                return True
        return False

    def print_tree(self, level: int = 0) -> None:
        """
        Виводить дерево у консоль у вигляді ієрархії.

        Параметри:
            level (int): Поточний рівень відступу (використовується для рекурсії).
        """
        print(" " * (level * 2) + self.value)
        for child in self.children:
            child.print_tree(level + 1)


# Приклад використання
root = Node("Root")
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

root.add_child(node_a)
root.add_child(node_b)
node_a.add_child(node_c)

# Вставка піддерева
subtree = Node("Subtree")
subtree.add_child(Node("Sub1"))
subtree.add_child(Node("Sub2"))
root.insert_subtree("B", subtree)

# Виведення дерева перед видаленням
print("Дерево перед видаленням:")
root.print_tree()

# Видалення піддерева
root.remove_subtree("B")

# Виведення дерева після видалення
print("\nДерево після видалення:")
root.print_tree()
