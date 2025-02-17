from bs4 import BeautifulSoup


class DOMNode:
    """
    Клас для представлення вузла DOM-дерева.

    Атрибути:
        tag (str): Назва HTML-тега.
        text (str): Текстовий вміст тега (якщо є).
        children (list[DOMNode]): Список дочірніх вузлів.
    """

    def __init__(self, tag: str, text: str = "") -> None:
        self.tag: str = tag
        self.text: str = text.strip()
        self.children: list[DOMNode] = []

    def add_child(self, child: "DOMNode") -> None:
        """
        Додає дочірній вузол.

        Параметри:
            child (DOMNode): Дочірній вузол.
        """
        self.children.append(child)

    def search_by_tag(self, tag: str) -> list[str]:
        """
        Шукає всі тексти всередині вказаного тега.

        Параметри:
            tag (str): Назва тега для пошуку.

        Повертає:
            list[str]: Список текстів, знайдених у вказаних тегах.
        """
        result = []
        if self.tag == tag and self.text:
            result.append(self.text)
        for child in self.children:
            result.extend(child.search_by_tag(tag))
        return result

    def print_tree(self, level: int = 0) -> None:
        """
        Виводить DOM-дерево у вигляді ієрархії.

        Параметри:
            level (int): Поточний рівень відступу (використовується для рекурсії).
        """
        print(" " * (level * 2) + f"<{self.tag}> {self.text}")
        for child in self.children:
            child.print_tree(level + 1)


def build_dom_tree(soup) -> DOMNode:
    """
    Рекурсивно будує дерево DOM із BeautifulSoup-об'єкта.

    Параметри:
        soup (BeautifulSoup): Об'єкт парсера HTML.

    Повертає:
        DOMNode: Кореневий вузол DOM-дерева.
    """
    root = DOMNode(soup.name, soup.string if soup.string else "")
    for child in soup.children:
        if child.name:
            root.add_child(build_dom_tree(child))
    return root


# Читаємо HTML-файл
with open("lesson_tree_hw.html", "r", encoding="windows-1251") as file:
    html_content = file.read()

# Парсимо HTML
soup = BeautifulSoup(html_content, "html.parser")
dom_tree = build_dom_tree(soup)

# Виводимо DOM-дерево
print("DOM-дерево:")
dom_tree.print_tree()

# Пошук тексту в тегах <h2>
found_texts = dom_tree.search_by_tag("h2")
print("\nТексти в <h2>:")
for text in found_texts:
    print(text)
