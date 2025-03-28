class Vertex:
    def __init__(self, key: int):
        """
        Инициализация вершины графа.

        :param key: Ключ вершины (уникальный идентификатор).
        """
        self.key = key  # Ключ вершины
        self.connected_to = {}  # Словарь для хранения смежных вершин и веса ребра

    def add_new_vertex(self, vertex, weight):
        """
        Добавление нового ребра с указанной вершиной и весом.

        :param vertex: Вершина, с которой добавляется связь.
        :param weight: Вес ребра между текущей вершиной и переданной.
        """
        self.connected_to[vertex] = weight  # Добавляем вершину и её вес в словарь

    def get_connection(self):
        """
        Получение всех смежных вершин.

        :return: Список пар (вершина, вес) смежных вершин.
        """
        return self.connected_to.items()  # Возвращаем пары ключ-значение

    def get_key(self):
        """
        Получение ключа вершины.

        :return: Ключ вершины.
        """
        return self.key  # Возвращаем ключ вершины

    def return_weight(self, vertex):
        """
        Получение веса ребра между данной вершиной и указанной.

        :param vertex: Вершина, для которой требуется получить вес ребра.
        :return: Вес ребра.
        """
        return self.connected_to[vertex]  # Возвращаем вес ребра для указанной вершины


class Graph:
    def __init__(self):
        """
        Инициализация графа.

        Граф представляет собой словарь, где ключами являются ключи вершин,
        а значениями - объекты класса Vertex.
        """
        self.dict = {}  # Словарь для хранения всех вершин графа

    def add_new_vertex(self, key: int):
        """
        Добавление новой вершины в граф.

        :param key: Ключ новой вершины.
        :return: Объект добавленной вершины.
        """
        self.dict[key] = Vertex(key)  # Создаем новую вершину и добавляем в словарь
        return self.dict[key]  # Возвращаем добавленную вершину

    def get_vertex(self, key):
        """
        Получение вершины по её ключу.

        :param key: Ключ вершины.
        :return: Объект вершины.
        """
        return self.dict[key]  # Возвращаем вершину по ключу

    def add_Edge(self, from_vertex, to_vertex, weight_beatween):
        """
        Добавление ребра между двумя вершинами с указанным весом.

        :param from_vertex: Ключ начальной вершины.
        :param to_vertex: Ключ конечной вершины.
        :param weight_beatween: Вес ребра между вершинами.
        """
        # Добавляем ребро от начальной вершины к конечной с заданным весом
        self.dict[from_vertex].add_new_vertex(self.dict[to_vertex], weight_beatween)

    def get_graph(self):
        """
        Вывод всех ребер графа.

        Для каждой вершины выводим её ключ и все смежные вершины с их весами.
        """
        for index, value in self.dict.items():
            # Для каждой вершины из графа
            for ind, val in value.connected_to.items():
                # Для каждой смежной вершины и её веса
                print(
                    f'Index: {index}: value {ind.get_key()}:{val}'  # Выводим информацию о смежной вершине
                )

    def __str__(self):
        """
        Возвращает строковое представление графа.

        :return: Строка с представлением графа.
        """
        return f'Graph: {self.dict}'  # Возвращаем строку с представлением всех вершин и их смежных вершин


# Создаем граф
graph = Graph()

# Добавляем вершины с ключами от 0 до 5
for i in range(6):
    graph.add_new_vertex(i)

# Добавляем ребра между вершинами с указанными весами
graph.add_Edge(0, 1, 5)
graph.add_Edge(0, 5, 2)
graph.add_Edge(1, 2, 8)
graph.add_Edge(2, 3, 8)
graph.add_Edge(3, 4, 8)

# Выводим информацию о графе
graph.get_graph()
