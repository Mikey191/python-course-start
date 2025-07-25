## Урок 4. Логический тип Bool. Операторы сравнения

### 4.1 Логический тип

**Логический тип bool** в языке программирования Python используется для представления **логических значений** и имеет два возможных значения: `True (истина)` и `False (ложь)`.

### 4.2 Операторы сравнения

**Операторы сравнения** позволяют **сравнивать значения** и **возвращать логический результат**:

- `==` - равно.
- `!=` - не равно.
- `>` - больше.
- `<` - меньше.
- `>=` - больше или равно.
- `<=` - меньше или равно.

**Результатом** оператора сравнения является логическое значение `True` или `False`.

```python
a = int(input())
b = int(input())
print(a == b)
print(a > b)
print(a <= b)
```

### 4.3 Преобразование в логический тип

- В Python можно преобразовать **другие типы данных** в **логический тип с помощью функции `bool()`**.
- Значения, которые преобразуются в `False`, включают **`пустые строки`, `числа равные нулю`, `пустые контейнеры` (списки, кортежи, словари) и значение `None`**.

  ```python
  a = None
  b = ""
  d = 0

  print(bool(a)) # False
  print(bool(b)) # False
  print(bool(d)) # False
  ```

- Все остальные значения преобразуются в `True`.

  ```python
  a = "Строка"
  c = 1

  print(bool(a)) # True
  print(bool(c)) # True
  ```

### 4.4 Преобразования типов данных

- **Преобразование в целый тип данных**: Для преобразования в целый тип данных используется функция `int()`.

  ```python
  # преобразование строки в целый тип данных:
  num_str = "42"  # строка, содержащая число
  num_int = int(num_str)  # преобразование в целое число
  print(num_int)  # вывод: 42

  # преобразование дробного числа в целый тип данных:
  float_num = 3.99  # дробное число
  int_num = int(float_num)  # преобразование в целое число
  print(int_num)  # вывод: 3

  # преобразование булевого значения в целый тип данных:
  bool_value = True  # булевое значение
  int_value = int(bool_value)  # преобразование в целое число
  print(int_value)  # вывод: 1

  # преобразование входящей строки:
  user_input = input("Введите целое число: ")  # пользователь вводит число
  user_number = int(user_input)  # преобразование в целое число
  print(f"Вы ввели число: {user_number}")  # преобразованное целое число

  # преобразование не возможно:
  num_str = "abc"  # строка, не содержащая числа
  num_int = int(num_str)  # попытка преобразования в целое число
  print(num_int)  # Это вызовет ошибку ValueError
  ```

- **Преобразование в дробный тип данных**: Для преобразования в дробный тип данных используется функция `float()`.

  ```python
  # преобразование строки в дробный тип данных:
  float_str = "3.14"  # строка, содержащая дробное число
  float_num = float(float_str)  # преобразование в дробное число
  print(float_num)  # вывод: 3.14

  # преобразование целого числа в дробный тип данных:
  int_num = 5  # целое число
  float_num = float(int_num)  # преобразование в дробное число
  print(float_num)  # вывод: 5.0

  # преобразование булевого значения в дробный тип данных:
  bool_value = False  # булевое значение
  float_value = float(bool_value)  # преобразование в дробное число
  print(float_value)  # вывод: 0.0

  # преобразование входящей строки
  user_input = input("Введите дробное число: ")  # пользователь вводит дробное число
  user_float = float(user_input)  # преобразование в дробное число
  print(f"Вы ввели дробное число: {user_float}")  # преобразованное дробное число

  # преобразование не возможно
  float_str = "3.14abc"  # строка, не являющаяся корректным дробным числом
  float_num = float(float_str)  # попытка преобразования в дробное число
  print(float_num)  # Это вызовет ошибку ValueError
  ```

- **Преобразование в строчный тип данных**: Для преобразования в строчный тип данных используется функция `str()`.

  ```python
  # преобразование целого числа в строчный тип данных:
  int_num = 42  # целое число
  str_num = str(int_num)  # преобразование в строку
  print(str_num)  # вывод: "42"

  # преобразования дробного числа в строчный тип данных:
  float_num = 2.718  # дробное число
  str_float = str(float_num)  # преобразование в строку
  print(str_float)  # вывод: "2.718"

  # преобразования булевого значения в строчный тип данных:
  bool_value = True  # булевое значение
  str_bool = str(bool_value)  # преобразование в строку
  print(str_bool)  # вывод: "True"
  ```

### 4.5 Операторы `and` `or` `not`

Операторы `and`, `or` и `not` используются для **выполнения логических операций** и **манипуляций с логическими значениями**.

- Оператор `and` выполняет **логическое "и"** между двумя операндами. Он возвращает **`True`, если оба операнда являются истинными**, и **`False` в противном случае**.
- Оператор `or` выполняет **логическое "или"** между двумя операндами. Он возвращает **`True`, если хотя бы один из операндов является истинным**, и **`False` в противном случае**.
- Оператор `not` выполняет **логическое отрицание операнда**. Он возвращает **`True`, если операнд является ложным**, и **`False`, если операнд является истинным**.

**Пример**:

```python
x = 5
y = 10

print(x > 0 and y > 20)  # Выводит False
print(x > 0 or y > 20)  # Выводит True
print(not x > 0)  # Выводит False
```

### 4.6 Приоритет операторов

**Приоритет операторов** определяет порядок выполнения операций в выражениях.

#### Таблица приоритетов операторов:

1. `**` - оператор возведения в степень имеет самый высокий приоритет.
2. `*`, `/`, `//`, `%` - операторы умножения, деления, целочисленного деления и остатка от деления имеют одинаковый приоритет и выполняются слева направо.
3. `+`, `-` - операторы сложения и вычитания также имеют одинаковый приоритет и выполняются слева направо.
4. `<`, `>`, `<=`, `>=` - операторы сравнения имеют одинаковый приоритет и выполняются слева направо.
5. `==`, `!=` - операторы равенства и неравенства имеют одинаковый приоритет и выполняются слева направо.
6. `not` - оператор логического отрицания выполняется перед операндом.
7. `and` - оператор логического И выполняется слева направо.
8. `or` - оператор логического ИЛИ выполняется слева направо.

### Вопросы:

1. Что такое логический тип и какие значения он может принимать?
2. Каковы основные операторы сравнения? Приведите примеры их использования.
3. Как происходит преобразование других типов данных в логический тип с помощью функции `bool()`?
4. Что делает оператор `and` и как он работает?
5. Как работает оператор `or`?
6. Что делает оператор `not` и как он изменяет логическое значение?
7. Каков приоритет операторов `and`, `or` и `not` в Python?
8. Как можно использовать логические операторы для проверки нескольких условий одновременно?

### Задание:

1. Напишите программу, которая запрашивает у пользователя два числа и выводит `True`, если первое число больше второго или `False` в противном случае.

2. Создайте программу, которая принимает на вход строку и проверяет, является ли она пустой. Выведите `True`, если строка пустая, и `False` в противном случае.

3. Напишите программу, которая запрашивает у пользователя логическое значение (пустая или не пустая строка) и выводит его отрицание.

4. Напишите программу, которая принимает три целых числа от пользователя и выводит, является ли хотя бы одно из них положительным.

5. Создайте программу, которая запрашивает у пользователя число и определяет, является ли оно четным или нечетным. (Используйте оператор `%` в сочетании с логическим оператором `==`).

6. Допишите текст программы. `a` - это вещественное число (с плавающей точкой). Программа должна выводит `True`, если целая часть числа `a` **кратна трём**, и `False` если не кратна.

   ```python
   a = float(input("Введите число: "))
   # продолжите программу
   ```

7. Допишите текст программы. `x` - это стоимость книги. Определите является ли дробное значение (число после запятой) больше 50. В консоль вывести `True` если больше и `False` если нет.

   ```python
   x = float(input("Введите стоимость книги: "))
   # продолжите программу
   ```

8. Допишите текст программы. `a`, `b`, `c` - предполагаемые **длины сторон треугольника**. Определите, действительно ли треугольник с такими сторонами может существовать (**Сумма длин двух произвольных сторон всегда должна быть больше третьей стороны**)? В консоль вывести `True`, если треугольник формируется и `False` - в противном случае.
   ```python
   a = int(input("Введите первую сторону треугольника: "))
   b = int(input("Введите вторую сторону треугольника: "))
   c = int(input("Введите третью сторону треугольника: "))
   # продолжите программу
   ```