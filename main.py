# from collections import Counter, defaultdict

# #  Создаем Counter с фруктами
# fruits_counter = Counter({"apple": 5, "banana": 3, "orange": 2})

# print(fruits_counter)  # Counter({'apple': 5, 'banana': 3, 'orange': 2})

# # Вычитаем количество фруктов
# fruits_counter.update(["apple", "apple", "apple", "banana", "banana", "orange"])
# print(fruits_counter)  # Counter({'apple': 8, 'banana': 5, 'orange': 3})

# dd = defaultdict(int)
# dd['missing']
# print(dd.default_factory)

# dd.default_factory = list
# dd['key']
# print(dd)

# Группировка
# dd = defaultdict(list)

# data = [("cat", 2), ("dog", 3), ("cat", 5), ("dog", 1)]

# for animal, count in data:
#     dd[animal].append(count)

# print(dd)

# # Подсчет
# words = "apple banana apple orange banana apple"
# dd = defaultdict(int)

# for word in words.split():
#     dd[word] += 1

# print(dd)

# from collections import defaultdict

# logs = [
#     ("2024-12-01", "192.168.1.1"),
#     ("2024-12-01", "192.168.1.2"),
#     ("2024-12-01", "192.168.1.1"),
#     ("2024-12-02", "192.168.1.3"),
#     ("2024-12-02", "192.168.1.2"),
#     ("2024-12-02", "192.168.1.3"),
# ]

# data_logs = defaultdict(lambda: defaultdict(int))

# for date, ip in logs:
#     data_logs[date][ip] += 1

# print(data_logs)

# from collections import OrderedDict

# od = OrderedDict()

# od['a'] = 1

# print(od)

# od = OrderedDict([('a',1), ('b', 2), ('c', 3)])
# od.move_to_end('b')
# print(od)

# od.move_to_end('c', last=False)
# print(od)

# od.update([('d', 4)])
# print(od)

# last_item = od.popitem()
# print(od)
# print(last_item)

# first_item = od.popitem(last=False)
# print(od)
# print(first_item)

# default_dict1 = {"1": 1, "2": 2}
# default_dict2 = {"2": 2, "1": 1}
# print(default_dict1 == default_dict2)

from collections import deque

dq = deque()
print(dq)
dq = deque([1,2,3,4,5])
print(dq)  # deque([1, 2, 3, 4, 5])
dq = deque((1,2,3,4,5))
print(dq)  # deque([1, 2, 3, 4, 5])
dq = deque({1,2,3,4,5})
print(dq)  # deque([1, 2, 3, 4, 5])
dq = deque('apple')
print(dq)  # deque(['a', 'p', 'p', 'l', 'e'])
dq = deque([1,2,3,4,5,6], maxlen=3)
print(dq)  # deque([4, 5, 6], maxlen=3)
