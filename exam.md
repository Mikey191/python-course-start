# Вопросы на экзамен:
1. Что такое переменная в Python? Какие правила существуют для именования переменных в Python?
2. Какие основные типы данных существуют в Python с которыми мы работали?
3. Каковы основные параметры функции print()? Как можно изменить разделитель между элементами при выводе?
4. Что делает функция input() и какой тип данных она возвращает?
5. Что такое логический тип и какие значения он может принимать?
6. Каковы основные операторы сравнения?
7. Каковы базовые операции над строками? Как преобразовать число в строку?
8. Что такое преобразование типов? Как любой тип данных преобразовать в строчный тип данных?
9. Как вычислить длину строки?
10. Что такое индекс в строке и как он используется в Python? Что произойдет, если вы попытаетесь получить символ строки по индексу, который выходит за пределы длины строки?
11. Как использовать отрицательные индексы для доступа к символам строки?
12. Основные методы строк для преобразования регистра?
13. Основные методы строк для поиска и замены подстрок?
14. Основные методы строк для проверки содержимого строки?
15. Основные методы для разделения и объединения строк?
16. Что такое экранирование символов? Какие основные спецсимволы для строк существуют?
17. Что такое f-строки и как они работают? Как можно использовать выражения внутри f-строк?
18. Что такое список в Python? Как создать список в Python?
19. Как узнать количество элементов в списке? Как объединить два списка в один? Как проверить, содержится ли элемент в списке?
20. Методы для добавления элементов в список?
21. Методы для удаления элементов из списка?
22. Метод для сортировки списка? Чем он отличается от функции sorted()?
23. Как создать многомерный список с 2-мя измерениями в Python?
24. Как получить доступ к элементу вложенного списка, используя двойную индексацию?
25. Что такое оператор if в Python и для чего он используется? Какой общий синтаксис оператора if?
26. Что такое конструкция if-elif-else и в чем ее отличие от простого if-else? Как можно использовать конструкцию if-elif-else для проверки, является ли число положительным, отрицательным или нулем?
27. Что такое тернарный условный оператор? Каков синтаксис тернарного условного оператора?
28. Что такое циклы в программировании? Какие циклы есть в Python?
29. Чем отличается цикл for от цикла while?
30. Что такое Заголовок цикла? Что такое Тело Цикла? Что такое Итерация?
31. Что такое цикл for в Python и как он работает?
32. Для чего используется функция range() в цикле for? Для чего может использоваться функция len() в цикле for?
33. Как можно использовать цикл for для перебора элементов списка?
34. Какой оператор используется для немедленного прерывания выполнения цикла? Какой оператор используется для пропуска текущей итерации цикла и перехода к следующей?
35. Как работает else в цикле for? Когда он выполняется, а когда нет? Чем отличается поведение блока else в цикле for от конструкции if...else?

# Задачи. Уровень junior
1. Напишите программу, которая принимает имя пользователя и выводит приветствие: "Привет, имя_пользователя!".
2. Создай переменную с целым числом 52. Преобразуйте это число в строку и объедините его с текстом "Ответ: число". Выведите результат.
3. Напишите программу, которая запрашивает строку и вычисляет ее длину. Выведите результат.
4. Напишите программу, которая запрашивает строку. Получите символ строки с индексом 2. Выведите результат.
5. Напишите программу, которая принимает строку, разбивает её по пробелам и выводит список слов.
6. Используйте конструкцию if-elif-else, чтобы определить, положительное, отрицательное или нулевое введенное число.

# Задачи. Уровень middle
1. Создайте список с элементами [1, 2, 3, 4, 5]. Удалите элемент со значением 3 и выведите обновленный список.
2. Напишите программу, которая запрашивает строку и проверяет, содержится ли в ней подстрока "Python". Выведите 'Да', если содержится, и 'Нет' — если нет.
3. Напишите программу, которая запрашивает строку. Используйте цикл for для перебора символов этой строки. Выведите каждый символ и его индекс в новой строке Например: Символ 'a' с индексом '0'.
4. Напишите программу, которая запрашивает строку с числами записанными через пробел. Преобразуйте строку в список чисел. Выведите только четные числа из списка.
5. Пользователь вводит два числа, причем первое всегда меньше второго. Используя цикл while найдите суммы чисел в диапазоне от первого числа до второго числа включительно. Выведите результат.
6. Напишите программу, которая находит минимальное значение в списке [5, 7, 2, 8, 4] используя цикл. Функции min() или max() использовать нельзя.
7. Напишите программу, которая принимает список чисел и создает новый список, содержащий квадраты четных чисел из исходного списка.

# Задачи. Уровень senior
1. Напишите программу, которая создает таблицу умножения (от 1 до 10) с использованием вложенного цикла for.
2. Создайте двумерный список (3x3), заполненный единицами с использованием вложенного цикла. Во вложенных списках под четными индексами замените еденицы под нечетным индексом на двойки. Во вложенном списке под нечетным индексом замените еденицы под четными индексами на двойки. Выведите результат.
3. Напишите программу, которая считает количество гласных и согласных букв в введенной строке. Гласные буквы: аеёиоуыэюя.

```python
import random
import time

# Список студентов РПО-1
# students = []

# Список студентов РПО-2
students = []

# Список вопросов
questions = [
    "Что такое переменная в Python? Какие правила существуют для именования переменных в Python?",
    "Какие основные типы данных существуют в Python с которыми мы работали?",
    "Каковы основные параметры функции print()? Как можно изменить разделитель между элементами при выводе?",
    "Что делает функция input() и какой тип данных она возвращает?",
    "Что такое логический тип и какие значения он может принимать?",
    "Каковы основные операторы сравнения?",
    "Каковы базовые операции над строками? Как преобразовать число в строку?",
    "Что такое преобразование типов? Как любой тип данных преобразовать в строчный тип данных?",
    "Как вычислить длину строки?",
    "Что такое индекс в строке и как он используется в Python? Что произойдет, если вы попытаетесь получить символ строки по индексу, который выходит за пределы длины строки?",
    "Как использовать отрицательные индексы для доступа к символам строки?",
    "Основные методы строк для преобразования регистра?",
    "Основные методы строк для поиска и замены подстрок?",
    "Основные методы строк для проверки содержимого строки?",
    "Основные методы для разделения и объединения строк?",
    "Что такое экранирование символов? Какие основные спецсимволы для строк существуют?",
    "Что такое f-строки и как они работают? Как можно использовать выражения внутри f-строк?",
    "Что такое список в Python? Как создать список в Python?",
    "Как узнать количество элементов в списке? Как объединить два списка в один? Как проверить, содержится ли элемент в списке?",
    "Методы для добавления элементов в список?",
    "Методы для удаления элементов из списка?",
    "Метод для сортировки списка? Чем он отличается от функции sorted()?",
    "Как создать многомерный список с 2-мя измерениями в Python?",
    "Как получить доступ к элементу вложенного списка, используя двойную индексацию?",
    "Что такое оператор if в Python и для чего он используется? Какой общий синтаксис оператора if?",
    "Что такое конструкция if-elif-else и в чем ее отличие от простого if-else? Как можно использовать конструкцию if-elif-else для проверки, является ли число положительным, отрицательным или нулем?",
    "Что такое тернарный условный оператор? Каков синтаксис тернарного условного оператора?",
    "Что такое циклы в программировании? Какие циклы есть в Python?",
    "Чем отличается цикл for от цикла while?",
    "Что такое Заголовок цикла? Что такое Тело Цикла? Что такое Итерация?",
    "Что такое цикл for в Python и как он работает?",
    "Для чего используется функция range() в цикле for? Для чего может использоваться функция len() в цикле for?",
    "Как можно использовать цикл for для перебора элементов списка?",
    "Какой оператор используется для немедленного прерывания выполнения цикла? Какой оператор используется для пропуска текущей итерации цикла и перехода к следующей?",
    "Как работает else в цикле for? Когда он выполняется, а когда нет? Чем отличается поведение блока else в цикле for от конструкции if...else?",
]

# Задачи уровня junior
junior_tasks = [
    "Напишите программу, которая принимает имя пользователя и выводит приветствие: 'Привет, имя_пользователя!'.",
    "Создайте переменную с целым числом 52. Преобразуйте это число в строку и объедините его с текстом 'Ответ: число'. Выведите результат.",
    "Напишите программу, которая запрашивает строку и вычисляет ее длину. Выведите результат.",
    "Напишите программу, которая запрашивает строку. Получите символ строки с индексом 2. Выведите результат.",
    "Напишите программу, которая принимает строку, разбивает её по пробелам и выводит список слов.",
    "Используйте конструкцию if-elif-else, чтобы определить, положительное, отрицательное или нулевое введенное число.",
]

# Задачи уровня middle
middle_tasks = [
    "Создайте список с элементами [1, 2, 3, 4, 5]. Удалите элемент со значением 3 и выведите обновленный список.",
    "Напишите программу, которая запрашивает строку и проверяет, содержится ли в ней подстрока 'Python'. Выведите 'Да', если содержится, и 'Нет' — если нет.",
    "Напишите программу, которая запрашивает строку. Используйте цикл for для перебора символов строки. Выведите каждый символ и его индекс. Например: Символ 'a' с индексом '0'",
    "Напишите программу, которая запрашивает строку с числами через пробел. Преобразуйте строку в список чисел и выведите четные числа.",
    "Пользователь вводит два числа, причем первое всегда меньше второго. Используя цикл while найдите суммы чисел в диапазоне от первого числа до второго числа включительно. Выведите результат.",
    "Напишите программу, которая находит минимальное значение в списке [5, 7, 2, 8, 4] используя цикл. Функции min() или max() использовать нельзя.",
    "Напишите программу, которая принимает список чисел и создает новый список, содержащий квадраты четных чисел из исходного списка.",
]

# Задачи уровня senior
senior_tasks = [
    "Напишите программу, которая создает таблицу умножения (от 1 до 10) с использованием вложенного цикла for.",
    "Создайте двумерный список (3x3), заполненный единицами с использованием вложенного цикла. Во вложенных списках под четными индексами замените еденицы под нечетным индексом на двойки. Во вложенном списке под нечетным индексом замените еденицы под четными индексами на двойки. Выведите результат.",
    "Напишите программу, которая считает количество гласных и согласных букв в введенной строке. Гласные буквы: аеёиоуыэюя.",
]


# Выбор случайных вопросов и задач
def random_questions(questions: list):
    c_questions = questions.copy()
    random_questions = []
    for _ in range(3):
        random_question = random.choice(c_questions)
        random_questions.append(random_question)
        c_questions.remove(random_question)
    return random_questions


# Вывод студентов, вопросы и задачи
while students:
    lst_random_questions = random_questions(questions)
    random_junior_task = random.choice(junior_tasks)
    random_middle_task = random.choice(middle_tasks)
    random_senior_task = random.choice(senior_tasks)
    time.sleep(1)
    student = random.choice(students)
    print(f"\nСтудент: {student}")
    students.remove(student)
    print("Вопросы на экзамен:")
    for index in range(len(lst_random_questions)):
        print(f"\t{index+1}. {lst_random_questions[index]}")
    print("Задача уровня Junior:")
    print(f"\t{random_junior_task}")
    print("Задача уровня Middle:")
    print(f"\t{random_middle_task}")
    print("Задача уровня Senior:")
    print(f"\t{random_senior_task}")
```