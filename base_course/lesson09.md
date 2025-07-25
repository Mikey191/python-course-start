## Урок 9. Форматирование строк. F-строки. Сырые строки

### 9.1 Форматирование и Формирование строк.

**Форматирование строк** в Python относится к процессу **создания строки, в которой значения переменных вставляются в определенные места с использованием заполнителей**.

Это позволяет контролировать **формат вывода и вставлять значения различных типов данных в строку**.

В Python существует несколько способов форматирования строк, таких как метод `format()` и `f-строки (f-strings)`.

**Формирование строк** в Python относится к процессу **создания строки путем объединения нескольких значений или переменных**.

Это может быть достигнуто с помощью `оператора конкатенации (+)` или `метода join()`.

C оператором конкатенации `+` и методом `join()` мы уже знакомы.

### 9.2 Способы Форматирования строк.

- **Использование метода `format()`**:  
  Метод **format()** позволяет вставлять значения переменных в строку, используя заполнители {}.  
  **Например**:
  ```python
  name = "John"
  age = 25
  message = "Меня зовут {} и мне {} лет.".format(name, age)
  ```
- **Использование `f-строк (f-strings)`**:  
  **F-строки** - это новый способ форматирования строк, доступный в Python 3.6 и выше.  
  Они позволяют вставлять **значения переменных** непосредственно в строку, используя выражение в фигурных скобках `{}`.  
  **Например**:

  ```python
  # Вставка переменных:
  name = "John"
  age = 25
  message = f"Меня зовут {name} и мне {age} лет."
  print(message)

  # Использование выражений:
  a = 5
  b = 10
  result = f"Сумма {a} и {b} равна {a + b}."
  print(result)
  ```

### 9.3 Сырые строки.

**Сырые строки** - это строки, в которых **специальные символы не интерпретируются и остаются в их исходном виде**. Они задаются с помощью префикса `r` **перед открывающей кавычкой строки**.

**Примеры**:

- **Избегание экранирования специальных символов**: В сырых строках специальные символы, такие как обратная косая черта `(\)`, не экранируются.  
  Это может быть полезно, например, **при работе с путями файлов в операционной системе Windows**, где обратная косая черта используется в путях файлов.  
  **Пример**:
  ```python
  path = r'C:\Users\Username\Documents\file.txt'
  print(path)
  ```
- **Удобное использование регулярных выражений**: Регулярные выражения часто содержат специальные символы, которые могут быть интерпретированы в обычных строках.  
  Использование сырых строк позволяет избежать необходимости экранирования специальных символов в регулярных выражениях.  
  **Пример**:
  ```python
  import re
  pattern = r'\d+'  # Ищем одну или более цифр
  ```
- **Сохранение форматирования**: Сырые строки также сохраняют все пробелы и отступы, что может быть полезно, например, при создании многострочных текстовых блоков или сохранении форматирования в SQL-запросах.  
  **Пример**:
  ```python
  query = r'''
  SELECT *
  FROM table
  WHERE condition = 'value'
  '''
  ```

### Вопросы:

1. Каковы основные способы форматирования строк в Python?
2. Что такое f-строки и как они работают?
3. Как можно использовать выражения внутри f-строк?
4. Что такое сырые строки и в чем их отличие от обычных строк?

### Задачи:

1. На вход программе подаются следующие данные (каждое с новой строки):

   - имя (строка);
   - фамилия (строка);
   - возраст (целое положительное число).  
     Необходимо прочитать эти данные и, используя строковый метод format, сформировать новую строку по шаблону:
     `Уважаемый <имя> <фамилия>! Поздравляем Вас с <возраст>-летием!`
     Результат вывести на экран (без кавычек).

2. На вход программе подаются габариты изделия (целые числа): ширина, глубина, высота, записанные в одну строчку через пробел. Необходимо прочитать эти числа и с помощью метода format, используя ключи в качестве имен переменных, сформировать строку по шаблону:
   `Габариты: <ширина> x <глубина> x <высота>`
   Полученную строку вывести на экран (без кавычек).

3. На вход программе подаются два целых числа, записанных в одну строку через пробел. Необходимо прочитать эти числа и сформировать новую **F-строку** со значениями прочитанных чисел, записанных по возрастанию через пробел. Полученную строку вывести на экран.

4. На вход программе подаются следующие данные (каждое с новой строки):

   - курс доллара (вещественное значение);
   - число рублей (целое число) для обмена рублей на доллары.  
     Необходимо прочитать эти данные и вычислить целое количество получаемых долларов (с отбрасыванием дробной части) и сформировать строку, по шаблону:
     `Вы можете получить <долларов>$ за <число рублей> рублей по курсу <курс доллара>`.
     Вывести полученную строку на экран (без кавычек).

5. Используя **raw-строки**, задайте строку, содержащую путь к файлу `"main.py"` вашего проекта. Выведите эту строку на экран.
