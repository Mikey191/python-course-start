## Урок 32: Функции `any()`, `all()`, `zip()`, `enumerate()`.

### 32.1 Функция `any()`

**Функция `any()` возвращает `True`, если хотя бы одно из значений в переданном итерируемом объекте является истинным. В противном случае она возвращает `False`**.

- **Проверка истинности элементов**:

  ```python
  responses = [False, False, True]
  print(any(responses))  # Результат: True
  ```

- **Есть ли хотя бы один элемент в списке, который больше 10**:

  ```python
  numbers = [1, 2, 3, 11, 5]
  result = any(num > 10 for num in numbers)
  print(result)  # Вывод: True
  ```

- **Использование `any()` с `lambda` и `map()`**.

  **Есть ли хотя бы одно четное число**:

  ```python
  numbers = [1, 3, 5, 7, 8]
  result = any(map(lambda x: x % 2 == 0, numbers))
  print(result)  # Вывод: True
  ```

### 32.2 Функция `all()`

**Функция `all()` проверяет, являются ли все элементы в итерируемом объекте истинными. Если все элементы истинные, функция возвращает `True`, в противном случае — `False`**.

- **Проверка всех элементов:**

  ```python
  grades = [True, True, True]
  print(all(grades))  # Результат: True
  ```

- **Проверить, все ли числа в списке положительные:**

  ```python
  numbers = [1, 2, 3, 4, 5]
  result = all(num > 0 for num in numbers)
  print(result)  # Вывод: True
  ```

- **Использование `all()` с `lambda` и `map()`**

  **Проверим, все ли числа в списке четные:**

  ```python
  numbers = [2, 4, 6, 8]
  result = all(map(lambda x: x % 2 == 0, numbers))
  print(result)  # Вывод: True
  ```

### 32.3 Функция `zip()`

**Функция `zip()` объединяет несколько итерируемых объектов в один, создавая пары элементов. Это особенно полезно, когда нужно работать с несколькими списками одновременно.**

- **Объединение списков в пары:**

  ```python
  names = ["Alice", "Bob", "Charlie"]
  scores = [85, 90, 78]
  result = list(zip(names, scores))
  print(result)  # Результат: [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
  ```

- **Создание словаря из двух списков:**

  ```python
  keys = ["name", "age", "city"]
  values = ["Alice", 30, "New York"]
  dictionary = dict(zip(keys, values))
  print(dictionary)  # Результат: {'name': 'Alice', 'age': 30, 'city': 'New York'}
  ```

- **Итерирование по нескольким объектам:**

  ```python
  dates = ["2023-01-01", "2023-01-02", "2023-01-03"]
  tasks = ["Meeting", "Workout", "Study"]
  for date, task in zip(dates, tasks):
      print(f"On {date}, you need to: {task}")
  # Результат:
  # On 2023-01-01, you need to: Meeting
  # On 2023-01-02, you need to: Workout
  # On 2023-01-03, you need to: Study
  ```

### 32.4 Функция `enumerate()`

**Функция `enumerate()` добавляет счетчик к итерируемому объекту и возвращает его в виде перечисления. Это полезно, когда нужно получить индекс элемента вместе с самим элементом.**

- **Пронумерованный вывод:**

  ```python
  tasks = ["Meeting", "Workout", "Study"]
  for index, task in enumerate(tasks, start=1):
      print(f"{index}. {task}")
  # Результат:
  # 1. Meeting
  # 2. Workout
  # 3. Study
  ```

- **Изменение значений по индексу:**

  ```python
  tasks = ["Meeting", "Workout", "Study"]
  for index, task in enumerate(tasks):
      if task == "Workout":
          tasks[index] = "Yoga"
  print(tasks)  # Результат: ['Meeting', 'Yoga', 'Study']
  ```

### Примеры близкие к реальным задачам.

1. **Проверка валидности данных с использованием `any()` и `all()`**.

   **Проверяется**:

   - Заполнены ли все данные для каждого пользователя.
   - Есть ли хотя бы один пользователь с ролью администратора.

   ```python
   users = [
       {"name": "Alice", "email": "alice@example.com", "role": "user"},
       {"name": "Bob", "email": "", "role": "admin"},
       {"name": "Charlie", "email": "charlie@example.com", "role": "user"},
   ]

   # Проверка: У каждого пользователя заполнены все данные
   all_data_filled = all(all(value for value in user.values()) for user in users)

   # Проверка: Есть ли хотя бы один пользователь с ролью администратора
   any_admin_present = any(user["role"] == "admin" for user in users)

   print(f"У всех пользователей заполнены все данные: {all_data_filled}")
   print(f"Есть ли хотя бы один администратор: {any_admin_present}")
   ```

2. **Нумерация задач для выдачи отчета с использованием `enumerate()`**

   **После проверки выводятся два списка**:

   - Список выполненных задач.
   - Список невыполненных задач.

   ```python
   tasks = [
       {"description": "Подготовить документы", "status": "Сделал"},
       {"description": "Провести совещание", "status": "Не сделал"},
       {"description": "Отправить отчет", "status": "Сделал"},
   ]

   # Сортируем задачи по статусу
   done_tasks = [task["description"] for task in tasks if task["status"] == "Сделал"]
   not_done_tasks = [task["description"] for task in tasks if task["status"] == "Не сделал"]

   # Выводим списки задач с нумерацией
   print("Сделанные задачи:")
   for index, task in enumerate(done_tasks, start=1):
       print(f"{index}. {task}")

   print("\nНевыполненные задачи:")
   for index, task in enumerate(not_done_tasks, start=1):
       print(f"{index}. {task}")
   ```

   **Результат**:

   ```
   Сделанные задачи:
   1. Подготовить документы
   2. Отправить отчет

   Невыполненные задачи:
   1. Провести совещание
   ```

### Задачи:

1. **Проверка, есть ли хотя бы одно четное число в списке**
   Дано:

   ```python
   numbers = [3, 7, 8, 11, 6, 9]
   ```

   Используйте функцию `any()` для проверки, есть ли в списке хотя бы одно четное число.

2. **Проверка, что все элементы списка строки**
   Дано:

   ```python
   items = ["apple", "banana", "cherry", "45"]
   ```

   Используйте функцию all() для проверки, что все элементы списка — строки.

3. **Создание пар из двух списков с помощью `zip()`**
   Дано:

   ```python
   names = ["John", "Jane", "Alice", "Bob"]
   ages = [23, 29, 22, 35]
   ```

   Используйте функцию zip() для объединения их в список пар (кортежей).

4. **Пронумерованный вывод списка**
   Дано:

   ```python
   tasks = ["Prepare report", "Review code", "Send email", "Update documentation"]
   ```

   Используйте функцию enumerate() для вывода всех задач с нумерацией.

5. **Проверка, есть ли хотя бы одно число больше 20**
   Дано:

   ```python
   numbers = [12, 8, 19, 22, 17]
   ```

   Используйте функцию any() для проверки, есть ли в списке хотя бы одно число больше 20.

6. **Проверка, что все числа в списке положительные**
   Дано:

   ```python
   numbers = [12, 15, 7, 22, 35]
   ```

   Используйте функцию all() для проверки, что все числа в списке положительные.

7. **Объединение списка с индексами с помощью `enumerate()`**
   Дано:

   ```python
   products = ["milk", "bread", "cheese", "butter"]
   ```

   Используйте функцию enumerate() для создания списка, где каждому продукту присвоен индекс.

8. **Создание словаря из двух списков с использованием `zip()`**
   Дано:

   ```python
   students = ["Alice", "Bob", "Charlie", "David"]
   grades = [85, 92, 78, 90]
   ```

   Используйте функцию zip() для создания словаря, где ключами будут имена, а значениями — оценки.

9. **Проверка, что все элементы больше 10 и четные**
   Дано:

   ```python
   numbers = [12, 14, 18, 22]
   ```

   Используйте функцию all() и lambda, чтобы проверить, что все элементы списка больше 10 и четные.

10. **Итерация по нескольким спискам одновременно с использованием `zip()`**
    Дано:

    ```python
    employees = ["John", "Jane", "Alice", "Bob"]
    salaries = [50000, 60000, 55000, 65000]
    ```

    Используйте zip() для печати всех сотрудников и их зарплат на одной строке.

11. **Проверка валидности данных пользователя**
    Дано:

    ```python
    users = [
        {"name": "John", "age": 28, "role": "admin", "email": "john@example.com"},
        {"name": "Jane", "age": 35, "role": "user", "email": "jane@example.com"},
        {"name": "Alice", "age": 22, "role": "user", "email": "alice@example.com"},
        {"name": "Bob", "age": 40, "role": "user", "email": ""}
    ]
    ```

    Используйте функции any() и all(), чтобы проверить:

    - Все ли данные о пользователе заполнены?
    - Есть ли среди пользователей администратор?

12. **Проверка паролей на соответствие требованиям**
    Дано:

    ```python
    passwords = ["123456", "Password123", "qwerty", "Admin123!"]
    ```

    Используйте функцию all() и lambda для проверки, что каждый пароль в списке:

    - Имеет длину больше 8 символов.
    - Содержит хотя бы одну цифру и одну букву разного регистра.

13. **Обработка списка покупок с условиями**
    Дано:

    ```python
    purchases = [
        {"item": "laptop", "price": 1200, "category": "electronics"},
        {"item": "apple", "price": 2, "category": "food"},
        {"item": "desk", "price": 150, "category": "furniture"},
        {"item": "phone", "price": 900, "category": "electronics"}
    ]
    ```

    Используйте функцию all() с lambda для проверки, что все покупки принадлежат одной категории. Также проверьте, есть ли хотя бы одна покупка, стоящая больше 1000 (используя any()).

14. **Нумерация задач для отчета с условием**
    Дано:

    ```python
    tasks = [
        {"task": "Prepare report", "status": "Done"},
        {"task": "Review code", "status": "Not done"},
        {"task": "Send email", "status": "Done"},
        {"task": "Update documentation", "status": "Not done"}
    ]
    ```

    Используйте enumerate() для пронумерованного списка задач и разделите задачи на выполненные и невыполненные, выводя их отдельно.

15. **Итерация по списку с фильтрацией и проверкой данных**
    Дано:

    ```python
    users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 18},
        {"name": "Charlie", "age": 22},
        {"name": "David", "age": 17}
    ]
    ```

    Используйте zip(), чтобы объединить список с возрастами и список с именами. Затем с помощью any() и all() проверьте:

    - Есть ли пользователи младше 18 лет.
    - Все ли пользователи старше 25 лет.
