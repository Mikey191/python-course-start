"""
Содание класса для реализации односвязного списка
"""


class Node:
    def __init__(self, data):
        self.data = data  # Данные, хранящиеся в узле
        self.next = None  # Ссылка на следующий узел, изначально None


class LinkedList:
    def __init__(self):
        self.head = None  # Ссылка на первый узел (голову списка)

    def add_to_front(self, data):
        """
        Метод для добавления элемента в начало списка
        """
        node = Node(data)  # Создаем новый узел
        node.next = self.head  # Новый узел ссылается на текущую голову
        self.head = node  # Новый узел становится головой списка

    def print_list(self):
        """
        Метод для вывода в консоль всех элементов списка
        """
        current = self.head  # Начинаем с головы списка
        while current:  # Пока текущий узел не равен None
            print(f"{current.data} -> ", end=" ")  # Выводим данные текущего узла
            current = current.next  # Переходим к следующему узлу
        print(None)  # Выводим "None", чтобы обозначить конец списка

    def add_to_end(self, data):
        """
        Метод для добавления элемента в конец списка
        """
        new_node = Node(data)  # Создаем новый узел с переданными данными
        if not self.head:  # Проверяем, пуст ли список
            self.head = new_node  # Если список пуст, новый узел становится головой
            return  # Завершаем выполнение метода
        current = self.head  # Начинаем с головы списка
        while current.next:  # Пока есть следующий узел
            current = current.next  # Переходим к следующему узлу
        current.next = new_node  # Присоединяем новый узел к последнему узлу списка

    def delete_node(self, data):
        """
        Метод для удаления элемента по его значению
        """
        if not self.head:  # Проверяем, пуст ли список
            print("linked list is empty")  # Сообщаем, что список пуст
            return  # Завершаем выполнение метода
        if self.head.data == data:  # Проверяем, совпадают ли данные головы с искомыми
            node_to_delete = self.head  # Сохраняем узел для удаления
            self.head = (
                self.head.next
            )  # Удаляем голову, перемещая указатель на следующий узел
            del node_to_delete  # Удаляем узел из памяти
            return  # Завершаем выполнение метода
        current = self.head  # Начинаем с головы списка
        while (
            current.next and current.next.data != data
        ):  # Ищем узел с искомыми данными
            current = current.next  # Переходим к следующему узлу
        if current.next:  # Если нашли узел с искомыми данными
            node_to_delete = current  # Сохраняем узел для удаления
            current.next = current.next.next  # Пропускаем удаляемый узел
            del node_to_delete  # Удаляем узел из памяти
            return  # Завершаем выполнение метода
        print(
            "data is not found"
        )  # Если узел не найден сообщаем, что элемент не найден


node = Node(10)  # Пример: создание узла
print(node.data, node.next)  # Вывод: 10 None

linked_list = LinkedList()  # Пример: создание пустого списка
print(linked_list.head)  # Вывод: None
linked_list.add_to_front(10)  # Добавление новго узла
linked_list.add_to_front(20)  # Добавление новго узла
linked_list.add_to_front(30)  # Добавление новго узла
print(linked_list.head.data)  # Вывод: 30
linked_list.print_list()  # 30 ->  20 ->  10 ->  None
linked_list.add_to_end(40)
linked_list.add_to_end(40)
linked_list.print_list()  # 30 ->  20 ->  10 ->  40 ->  40 ->  None
linked_list.delete_node(10)
linked_list.delete_node(100)
linked_list.print_list()  # 30 ->  20 ->  40 ->  40 ->  None
