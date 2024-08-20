# python-course
## Настройка Pycharm для Python.
### 1. Установка Python
 - **Скачайте Python**: Перейдите на официальный сайт Python и скачайте последнюю версию для Windows.
 - **Установите Python**: Запустите установочный файл. Обязательно отметьте галочку "Add Python to PATH" перед нажатием на кнопку "Install Now". Это упростит доступ к Python из командной строки.
 - **Проверьте установку**: Откройте командную строку (cmd) и введите команду:
```
python --version
```

### 2. Установки PyCharm на Windows:
- Перейдите на **официальный сайт** PyCharm от JetBrains. Официальный сайт PyCharm от JetBrains: https://www.jetbrains.com/ru-ru/pycharm/download/?section=windows
- Скачайте последнюю версию **PyCharm Community Edition для Windows**.
- Запустите загруженный установщик PyCharm.
- Следуйте инструкциям на экране, чтобы завершить установку. Убедитесь, что вы выбрали правильную версию PyCharm (Community Edition или Professional) в соответствии с вашими потребностями.
- После завершения установки, запустите PyCharm.

### 3. Создания первого проекта в PyCharm:
- В меню выберите **"File"** (Файл) и затем **"New Project"** (Новый проект).
- В появившемся окне выберите **местоположение для вашего проекта** и **введите его название**.
- Нажмите кнопку **"Create"** (Создать) для создания проекта.

### 4. Запуск файла main.py
- **Первый способ**: Запуск через контекстное меню:
  - Откройте проект в PyCharm и найдите файл main.py в панели проекта.
  - Щелкните правой кнопкой мыши на файле и выберите пункт `Run 'main'`. Это запустит файл в терминале PyCharm.
- **Второй сопос**: Использование кнопки запуска: 
  - Откройте файл main.py в PyCarm.
  - В правом верхнем углу окна PyCharm вы увидите **зеленую кнопку запуска (треугольник)**. Нажмите на нее, чтобы запустить файл.
- **Третий способ**: Сочетания клавиш:
  - Вы можете использовать сочетание клавиш `Shift + F10`, чтобы запустить последний запущенный файл. Если main.py был последним, он запустится.

## Настройка VSCode для Python.
### 1. Установка Python
 - **Скачайте Python**: Перейдите на официальный сайт Python и скачайте последнюю версию для Windows.
 - **Установите Python**: Запустите установочный файл. Обязательно отметьте галочку "Add Python to PATH" перед нажатием на кнопку "Install Now". Это упростит доступ к Python из командной строки.
 - **Проверьте установку**: Откройте командную строку (cmd) и введите команду:
```
python --version
```

### 2. Установка Visual Studio Code
 - **Скачайте VSCode**: Перейдите на официальный сайт VSCode и скачайте установочный файл для Windows.
 - **Установите VSCode**: Запустите установочный файл и следуйте инструкциям на экране.

### 3. Установка расширения Python для VSCode
 - **Запустите VSCode**.
 - **Откройте Marketplace**: Нажмите на иконку расширений (или используйте сочетание клавиш Ctrl+Shift+X).
 - **Найдите расширение Python**: Введите "Python" в строке поиска и установите расширение от Microsoft.

### 4. Установка интерпритатора
 - **Откройте командную палитру**: Нажмите сочетание клавиш Ctrl + Shift + P. Это откроет командную палитру.
 - **Выберите интерпретатор**: Введите в командной палитре Python: Select Interpreter и выберите эту команду из списка. После этого появится список доступных интерпретаторов Python, установленных на вашем компьютере. Выберите нужный интерпретатор, который вы хотите использовать для вашего проекта.

### 5. Запуск файла main.py
 - **Первый способ**. Использование сочетания клавиш:
   - Нажмите F5, чтобы запустить файл с отладкой. Это откроет отладчик и выполнит ваш код.
   - Нажмите Ctrl + F5, чтобы запустить файл без отладки. Это выполнит ваш код в терминале.
 - **Второй способ**. Запуск через терминал:
   - Откройте встроенный терминал в VSCode, нажав Ctrl + (обратная кавычка).
   - Введите команду `python main.py` и нажмите Enter. Убедитесь, что у вас установлен Python и он добавлен в переменную окружения PATH.
 - **Третий способ**. Использование команды в меню:
   - Вы можете также запустить файл, выбрав в верхнем меню **Run (Запуск)** → **Run Without Debugging (Запустить без отладки)** или **Start Debugging (Начать отладку)**.

### 6. Создание виртуального окружения
 - **Создайте виртуальное окружение**: Откройте терминал в VSCode. Введите следующую команду: `python -m venv env`. Это создаст папку env в вашем проекте, где будет находиться виртуальное окружение.
  - **Активируйте виртуальное окружение**: В терминале введите следующую команду: `.\env\Scripts\activate` . Вы должны увидеть, что имя окружения (например, (env)) появилось перед командной строкой.

## *Что такое виртуальное окружение?
**Виртуальное окружение в Python** — это **изолированная среда**, которая позволяет **устанавливать и управлять зависимостями для конкретного проекта**, не влияя на глобальные настройки системы. Это особенно полезно, когда у вас есть несколько проектов, требующих разных версий библиотек или самого Python.

### Основные характеристики виртуального окружения:
- **Изоляция зависимостей**: Каждое виртуальное окружение имеет свои **собственные библиотеки и зависимости**, что предотвращает конфликты между проектами. Например, если один проект требует библиотеку **версии 1.0**, а другой — **версии 2.0**, вы можете создать два отдельных окружения для каждого проекта.
- **Управление версиями Python**: Виртуальные окружения позволяют **использовать разные версии Python** для разных проектов. Это особенно важно, если ваш код зависит от специфических функций или изменений в разных версиях Python.
- **Удобство разработки**: Создание виртуального окружения **упрощает процесс установки и удаления зависимостей**, так как все изменения происходят в рамках этого окружения.


## Урок 1. Переменные, оператор присваивания. Типы данных.
### Переменные.
**Переменная** - это имя, которое используется для хранения значения. Она представляет собой **ссылку на объект в памяти компьютера**. Переменные в Python могут содержать различные типы данных.  

**Имена переменных** могут состоять из **букв (как строчных, так и заглавных)**, **цифр** и **символа подчеркивания**.  
**Имя переменной не может начинаться с цифры**.  

Python является **регистрозависимым языком**, поэтому переменные **myVar**, **myvar** и **MYVAR** будут **считаться разными переменными**.

**Пример создания переменной**:
```python
a = 7
```
- `a` - это **имя переменной**. 
- `=` - это **оператор присваивания**. Он позволяет присвоить переменной определенное значение или ссылку на объект.
- `7` - это объект на который ссылается **а**. 

### Оператор присваивания
**Оператор присваивания** в Python — это символ `=`, который используется для **присвоения значения переменной**. Он позволяет **сохранить данные в переменной**, чтобы затем можно было использовать это значение в программе. 

Когда вы используете оператор присваивания, вы **указываете переменную слева** от знака `=` и **значение или выражение справа**.

**Оператор присваивания необходим для**:
1. `Сохранения данных`: Вы можете сохранять значения, которые будете использовать позже в коде.
```python
x = 5
```
2. `Изменения значений`: Вы можете изменять значения переменных в процессе выполнения программы.
```python
x = 5
x = x + 2  # Теперь x будет равно 7
```
3. `Работы с выражениями`: Вы можете присваивать результат вычислений переменным.
```python
a = 3
b = 4
c = a + b  # c теперь равно 7
```

### Переменные в Python являются ссылками на объекты.
В языке **Python** переменные **не хранят сами объекты**, а лишь **ссылаются** на них с определенными значениями. Это означает, что **одной переменной можно присваивать объекты разных типов данных**. Например, вы можете создать переменную x и присвоить ей значение числа, а затем изменить ее значение, присвоив ей строку или другой объект. 

В Python переменные являются **ссылками на объекты**, и их значения могут изменяться в процессе выполнения программы.

Например:
```python
x = 10
print(x)  # Вывод: 10

x = "Hello, world!"
print(x)  # Вывод: Hello, world!

x = [1, 2, 3]
print(x)  # Вывод: [1, 2, 3]
```

### Функция id()
Каждый объект в Python имеет свой **уникальный идентификатор**, который можно получить с помощью функции **id()**. Идентификатор представляет собой **целое число, которое гарантированно уникально для каждого объекта во время его существования**.

Например:
```python
a = 2
b = a 
c = b

print(id(a)) # Вывод: 140719720362824
print(id(b)) # Вывод: 140719720362824
print(id(c)) # Вывод: 140719720362824
```
**Идентификаторы** у всех трех переменных будут **одинаковы**. Это говорит о том, что эти **три переменные** ссылаються на **один объект**.

### Функция type()
Функция **type()** в языке Python используется для получения **типа объекта**. Она возвращает информацию о **типе данных**, к которому принадлежит **объект**.

Например:
```python
x = 5
print(type(x))  # Вывод: <class 'int'>

y = "Hello"
print(type(y))  # Вывод: <class 'str'>

z = True
print(type(z))  # Вывод: <class 'bool'>
```

### Типы данных в Python
**Типы данных** в языках программирования — это категории, которые определяют, какие **значения могут храниться в переменных** и **какие операции могут быть выполнены с этими значениями**. В Python существует несколько основных типов данных, с которыми вы будете работать на начальном этапе изучения языка:
1. `Целые числа (int)`: Этот тип данных используется для хранения **целых чисел**, как положительных, так и отрицательных. `Например, 5, -3, 42`.
2. `Числа с плавающей запятой (float)`: Этот тип данных предназначен для хранения **чисел с дробной частью**. `Например, 3.14, -0.001, 2.0`.
3. `Строки (str)`: Строки представляют собой последовательности символов и используются для хранения текстовой информации. Строки заключаются в одинарные или двойные кавычки. `Например, "Привет", 'Python'`.
4. `Логический тип (bool)`: Этот тип данных может принимать только два значения: `True (истина)` и `False (ложь)`. Он часто используется для выполнения условий и логических операций.

**Примеры использования типов данных**:
```python
# Пример целого числа
age = 25  # int

# Пример числа с плавающей запятой
height = 1.75  # float

# Пример строки
name = "Алексей"  # str

# Пример логического типа
is_student = True  # bool
```

### Типизация
**Типизация** - это концепция, связанная с определением **типов данных в программировании**. Она определяет, **какие типы данных могут быть использованы в языке программирования** и **как эти типы взаимодействуют друг с другом**.

В языках программирования **типизация** может быть **динамической** или **статической**.
- **Динамическая типизация** означает, что **тип** переменной определяется **автоматически** на основе значения, которое ей присваивается.
- **Статическая типизация**, напротив, требует **явного объявления типов переменных** и **проверки их соответствия во время компиляции**.

В Python используется **динамическая типизация**, что означает, что **тип переменной определяется автоматически** на основе значения, которое ей присваивается. В отличие от языков с явной типизацией, в Python вам не нужно объявлять тип переменной явно.

## Вопросы:
1. Что такое переменная в Python?
2. Какие правила существуют для именования переменных в Python?
3. Что делает оператор присваивания?
4. Что делает функция id()?
5. Что делает функция type()?
6. Можно ли функции id присвоить число 7 (id = 7)?
7. Какие основные типы данных существуют в Python?
8. Что такое типизация в Python и как она влияет на работу с переменными и данными?


## Урок 2. Числа. Операции над числами.
### Числовые типы данных
В **Python** существуют **различные типы чисел**.  
Вот некоторые из них:
- **Целые числа (int)**: представляют целочисленные значения, например, 0, -1, 100 и т.д.
- **Вещественные числа (float)**: представляют числа с плавающей точкой, такие как 0.5, -3.14, 2.71828 и т.д.
- **Комплексные числа (complex)**: представляются в виде **x + yj**, где **x** и **y** - это **вещественные числа**, а **j** - мнимая единица. Например, **3 + 2j**, **-1.5 + 0.5j** и т.д.

**Например**:
```python
x = 10  # Целое число
y = 3.14  # Вещественное число
z = 2 + 3j  # Комплексное число

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
```
### Операции над типами данных
1. **Сложение (`+`)**: оператор сложения используется для сложения двух чисел. Например:
```python
x = 5 + 3
print(x)  # Выводит: 8

y = 2
z = 5
res = y + z
print(res) # Выводит: 7
```
2. **Вычитание (`-`)**: оператор вычитания используется для вычитания одного числа из другого. Например:

```python
y = 10 - 4
print(y)  # Выводит: 6

y = 2
z = 5
res = y - z
print(res) # Выводит -3
```

3. **Умножение (`*`)**: оператор умножения используется для умножения двух чисел. Например:
```python
z = 2 * 6
print(z)  # Выводит: 12

y = 2
z = 5
res = y * z
print(res) # Выводит 10
```
4. **Деление (`/`)**: оператор деления используется для деления одного числа на другое. В результате получается число с плавающей точкой (float). Например:
```python
a = 10 / 3
print(a)  # Выводит: 3.3333333333333335

y = 2
z = 5
res = y / z
print(res) # Выводит 0.4
```
5. **Целочисленное деление (`//`)**: оператор целочисленного деления возвращает целую часть от деления одного числа на другое. Например:
```python
x = 10 // 3
print(x)  # Выводит: 3

y = 2
z = 5
res = y // z
print(res) # Выводит 0
```
6. **Остаток от деления (`%`)**: оператор остатка от деления возвращает остаток от деления одного числа на другое. Например:
```python
y = 10 % 3
print(y)  # Выводит: 1

y = 2
z = 5
res = y % z
print(res) # Выводит 4
```
7. **Возведение в степень (`**`)**: оператор возведения в степень используется для возведения числа в определенную степень. Например:
```python
z = 2 ** 3
print(z)  # Выводит: 8

y = 2
z = 5
res = y % z
print(res) # Выводит 32
```
### Сокращенная запись операторов
**Сокращенная запись оператора** - это специальный синтаксис, который позволяет выполнять операцию и присваивание значения переменной в одной строке кода.
```python
x = 5
x += 3
print(x)  # Выводит: 8
```
Сокращенную запись оператора можно использовать с любым из семи перечисленных выше операторов.
## Вопросы:
1. К какому типу данных относится int?
2. К какому типу данных относится float?
3. Как называется оператор `+`?
4. Как называется оператор `-`?
5. Как называется оператор `*`?
6. Как называется оператор `/`?
7. Как называется оператор `//`?
8. Как называется оператор `%`?
9. Как называется оператор `**`?
10. Что выведит строка `print(7.0 + 2)`?
11. Что выведит строка `print(2 ** 4)`?
12. Что выведит строка `print(32 / 2 ** 4)`?
13. Что выведит строка `print(11 % 3)`?
14. Что выведит строка `print(21 // 4)`?
15. Какой тип данных мы увидим, выполнив строчку `print(type(8/2))`?
16. Чему будет равно k?
    ```python
    k = 8
    k *= 2
    print(k)
    ```
17. Чему будет равно i?
    ```python
    i = 2
    i += 3
    print(i)
    ```