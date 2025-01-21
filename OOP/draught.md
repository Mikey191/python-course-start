# Python OOP (Object Oriented Programming)

- Имя класса
- Атрибут класса
- Метод класса

- Инкапсуляция
- Наследование
- Полиморфизм

## Класс:

### Создание класса:

```python
class Point:
    color = "red"
    circle = 2
```

### Создание объекта класса:

```python
a = Point()
b = Point()
```

### Проверить принадлежность к типу:

```python
print(isinstance(a, Point))
```

## Атрибуты. Начало.

### Посмотреть атрибуты класса (принадлежат всем объектам класса):

```python
print(Point.__dict__)
```

### Посмотреть атрибуты конкретного объекта класса (атрибуты самого класса уже не входят в этот словарь)

```python
print(a.__dict__) # словарь будет пуст, потому что у конкретного экземпляра нет своих атрибутов, а только общие
```

### Способы создания новых атрибутов в классе:

```python
Point.type_pt = "disc" # создание нового атрибута
setattr(Point, "prop", 1) # создание нового атрибута
```

### Для изменения атрибутов можно использовать тот же способ:

```python
Point.type_pt = "any_disc" # создание нового атрибута
setattr(Point, "prop", 0) # создание нового атрибута
```

### Прочитать значение атрибута:

```python
print(Point.type_pt) # значение any_disc, выдаст ошибку если атрибута нет
print(getattr(Point, 'type_pt', False)) # значение any_disc, выдаст False если атрибута нет.
```

### Удалить атрибут:

```python
del Point.prop # удалит атрибут prop, если такого нет, возникает ошибка
delattr(Point, 'type_pt') # удалит атрибут type_pt
```

### Проверить, есть ли атрибут, по его имени:

```python
print(hasattr(Point, "type_pt"))
```

## Методы. Начало

### Параметр `self`. **Указывается в методе класса, который можно было бы вызывать из его экземпляров**.

```python
class Point:
    color = 'red'
    circle = 2

    def set_coords(self): # метод класса
        print("вызов метода set_coords")
```

#### Для вызова такого метода через класс, нам нужно первым аргументом указать экземпляр класса.

```python
fp = Point()
Point.set_coords(fp)
```

### Создание `setter` и `getter`. **Функции, которые устанавливают и дают доступ к атрибутам класса**:

```python
class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords():
        return (self.x, self.y)
```

## Магические методы step One

### `__init__` - **инициализатор объекта класса**. Вызывается сразу после создания экземпляра класса. Метод `__init__` вызывается для начальной инициализации созданного объекта.

```python
class Point:
    color = 'red'
    circle = 2

    def __init__(self):
        self.x = 0
        self.y = 0
```

### `__del__` **автоматически вызывается непосредственно перед уничтожением экземпляра класса**.

```python
class Point:
    color = "red"
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра: "+ str(self))
```

### `__new__`, вызывается непосредственно перед созданием объекта класса. `cls` – это ссылка на текущий класс `Point`.

```python
class Point:
    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))

    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y
```

#### Метод `__new__` должен возвращать адрес нового созданного объекта `super().__new__(cls)`.

**Функция `super()` возвращает ссылку на базовый класс и через нее мы вызываем метод `__new__` с одним первым аргументом**.

**Все классы автоматически и неявно наследуются от базового класса `object`**.

```python
class Point:
    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y
```

### Метод `__new__` для `Singleton` (паттерн проектирования для того, что бы в программе существовал только один экземпляр класса).

```python
class DataBase:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: # если значение равно `None`, то вызываем метод __new__ базового класса и тем самым разрешаем создание объекта.
            cls.__instance = super().__new__(cls)

        return cls.__instance # Иначе, возвращаем ссылку на ранее созданный экземпляр

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")
```

### Метод `__del__`. Продолжение предыдущего примера.

**Метод будет обнулять атрибут `__instance` перед уничтожением объекта, чтобы мы могли, при необходимости, создать новый**.

```python
class DataBase:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        self.__instance = None # устанавливает значение __instance = None

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")
```

## Режимы доступа public, private, protected. Сеттеры и геттеры

Доступ к данным в классе:

- `attribute` – **публичное свойство (`public`)**;
- `_attribute` – режим доступа `protected` (**служит для обращения внутри класса и во всех его дочерних классах**)
- `__attribute` – режим доступа `private` (**служит для обращения только внутри класса**).

```python
class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0

        if self.__check_value (x) and self.__check_value (y):
            self.__x = x
            self.__y = y

    def set_coord(self, x, y):
        if self.__check_value (x) and self.__check_value (y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    @classmethod
    def __check_value (cls, x):
        return type(x) in (int, float)
```

## Дескрипторы (data descriptor и non-data descriptor)

Дескриптор это класс, который содержит или один магический метод `__get__` Или класс, в котором дополнительно прописаны методы `__set__` и/или `__del__`.

**Дескрипторы не данных** `(non-data descriptor)` **не могут менять значения какого-либо свойства, так как не имеют сеттера и делитера**. Они имеют тот же приоритет доступа, что и обычные атрибуты класса. Они обычно имеют метод: `__get__`

Дескрипторы данных (`data descriptor`) могут как менять значение свойства, так и возвращать его. Они обычно имеют все три метода: `__get__`, `__set__`, `__del__`.

```python
# Дескриптор данных (data descriptor)
class Integer:
    # метод для установки имени
    def __set_name__(self, owner, name):
        # self - являлся ссылкой на создаваемый экземпляр класса
        # owner - ссылка на класс Point
        # name - имя атрибута
        self.name = "_" + name

    # геттер
    def __get__(self, instance, owner):
        # self - ссылка на объект дескриптора
        # instance - ссылка на созданный объект класса Point
        # owner - ссылка на класс Point
        # return instance.__dict__[self.name] # перепишим строку более стандартным методом
        return getattr(instance, self.name)

    # сеттер
    def __set__(self, instance, value):
        # self - ссылка на объект дескриптора
        # instance - ссылка на созданный объект класса Point
        # value - присваиваемое значение
        # instance.__dict__[self.name] = value # перепишим строку более стандартным методом
        setattr(instance, self.name, value)


class Point:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point(1, 2, 3)
print(pt.x) # 1
print(pt.y) # 2
print(pt.z) # 3
pt.x = 4
print(pt.x) # 4
```

## Магические методы (dunder-методы) step 2

### Метод `__getattribute__`

Автоматически вызывается, когда идет считывание атрибута через экземпляр класса.

С помощью `__getattribute__` можем ограничить доступ к приватным свойствам `__x` и `__y` экземпляра класса.

```python
class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __getattribute__(self, item):
        if item == "_Point__x": # Явно запрещаем доступ к приватному атрибуту
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)


pt1 = Point(1, 2)

print(pt1.MIN_COORD)
print(pt1._Point__x) # Ошибка ValueError
```

### Метод `__setattr__`

Автоматически вызывается в момент присваивания атрибуту нового значения.

Внутри метода `__setattr__` нельзя менять свойства напрямую. Использование записи `self.__x = value` вместо `object.__setattr__(self, key, value)` вызовет `рекурсию` и программа завершит свою работу с ошибкой.

С помощью `__setattr__` можно запретим создание локального свойства с именем z:

```python
def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)
```

### Метод `__getattr__`

Автоматически вызывается, если идет обращение к несуществующему атрибуту.

Когда вызывается такой метод, то по дефолтному поведению он возвращает None.

Определи класс, в котором при обращении к несуществующим атрибутам возвращается значение `False`, а не возвращается `None`.

```python
def __getattr__(self, item):
    return False
```

### Метод `__delattr__`

Автоматически вызывается в момент удаления какого-либо атрибута из экземпляра класса.

```python
def __delattr__(self, item):
    print(f'Атрибут {item} удален!')
    object.__delattr__(self, item)
```

### Метод `__call__`. Функторы и классы-декораторы

Когда происходит вызов класса, то автоматически запускается магический метод `__call__`.

Упрощенная схема реализации метода `__call__`: сначала вызывается магический метод `__new__` для создания самого объекта в памяти устройства, а затем, метод `__init__` - для его инициализации. То есть, класс можно вызывать подобно функции благодаря встроенной для него реализации магического метода `__call__`.

Для объекта класса можно так же реализовать логику вызова, если мы в нем определим метод `__call__`.

Классы, экземпляры которых можно вызывать подобно функциям, получили название `функторы`.

```python
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__counter += 1
        return self.__counter

c = Counter()
c()
c()
res = c()
print(res) # 3
```

#### Использование класса с методом `__call__` вместо замыканий функций.

Мы можем объявить класс StripChars, который бы удалял вначале и в конце строки заданные символы:

```python
class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Аргумент должен быть строкой")
        return args[0].strip(self.__chars)

s1 = StripChars("?:!.; ")
res = s1(" Hello World! ")
print(res)
```

#### Реализация декораторов с помощью классов.

В инициализаторе сохраняем ссылку на функцию, которую декорируем, а в методе **call** принимаем один обязательный параметр x – точку, где вычисляется производная и dx – шаг изменения при вычислении производной.

```python
import math

class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

# Добавить декоратор можно двумя способами:
# первый
def df_sin(x):
    return math.sin(x)

df_sin = Derivate(df_sin)


# второй
@Derivate
def df_sin(x):
    return math.sin(x)
```

### Метод `__str__()`

**Магический метод для отображения информации об объекте класса для пользователей** (например, для функций print, str)

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

cat = Cat('Васька') # cat ## в терминале
```

### Метод `__repr__()`

**Магический метод для отображения информации об объекте класса в режиме отладки** (для разработчиков).

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

cat = Cat('Васька') # <class 'ex1.Cat'>: Васька ## В КОНСОЛЕ
```

### Метод `__len__()`

**Позволяет применять функцию `len()` к экземплярам класса**

```python
class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

p = Point(1, -2)
print(len(p)) # 2
```

### Метод `__abs__()`

**Позволяет применять функцию `abs()` к экземплярам класса**

```python
class Point:
    def __init__(self, *args):
        self.__coords = args

    def __abs__(self):
        return list( map(abs, self.__coords) )

p = Point(1, -2)
print(abs(p)) # [1, 2]
```

### Методы `__add__()`, `__sub__()`, `__mul__()`, `__truediv__()`

- `__add__()` – **для операции сложения**;
- `__sub__()` – **для операции вычитания**;
- `__mul__()` – **для операции умножения**;
- `__truediv__()` – **для операции деления**.

#### `__add__()`

```python
class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60  # секунды
        m = (self.seconds // 60) % 60  # минуты
        h = (self.seconds // 3600) % 24  # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    # метод класса для форматирования времени (добавляется незначащий первый ноль, если число меньше 10).
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    # метод для переопределения сложения объектов класса
    def __add__(self, other):
        if not isinstance(
            other, (int, Clock)
        ):  # Если второй операнд не целое число и не объект класса Clock - генерируем ошибку ArithmeticError
            raise ArithmeticError(
                "Правый операнд должен быть типом int или объектом Clock"
            )
        # Переменная, которая принимает значение в зависимости от типа данных второго операнда
        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc) # Возвращаем новый объект класса Clock


c1 = Clock(1000)
c2 = c1 + 120
print(c2.seconds, c2.get_time(), sep="\t")  # 1120    00:18:40
c3 = Clock(2000)
c4 = c2 + c3
print(c4.seconds, c4.get_time(), sep="\t")  # 3120    00:52:00
c5 = Clock(3000)
c6 = c2 + c4 + c5
print(c6.seconds, c6.get_time(), sep="\t")  # 7240    02:00:40
```

#### **Таблица Методов арифметических операторов**

```
|Оператор | Метод оператора           | Оператор | Метод оператора           |
+---------+---------------------------+----------+---------------------------+
|x + y    | __add__(self, other)      | x += y   | __iadd__(self, other)     |
|x - y    | __sub__(self, other)      | x -= y   | __isub__(self, other)     |
|x * y    | __mul__(self, other)      | x *= y   | __imul__(self, other)     |
|x / y    | __truediv__(self, other)  | x /= y   | __itruediv__(self, other) |
|x // y   | __floordiv__(self, other) | x //= y  | __ifloordiv__(self, other)|
|x % y    | __mod__(self, other)      | x %= y   | __imod__(self, other)     |
+----------------------------------------------------------------------------+
```

#### `__radd__()`

Для реализации команды: `c1 = 100 + c1`

```python
def __radd__(self, other):
        return self + other
```

#### `__iadd__()`

Для реализации команды: `c1 += 100`

```python
def __iadd__(self, other):
        print("__iadd__")
        # Если второй операнд не целое число и не объект класса Clock - генерируем ошибку ArithmeticError
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")
        # Переменная, которая принимает значение в зависимости от типа данных второго операнда
        sc = other if isinstance(other, int) else other.seconds
        self.seconds += sc

        return self # Возвращаем тот же объект класса (Отличие от реализации метода __add__())
```

#### `__sub__()`, `__mul__()`, `__truediv__()`

Остальные методы реализовываются по такой же схеме.

### Методы сравнений `__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__`

- `__eq__()` – **для равенства `==`**
- `__ne__()` – **для неравенства `!=`**
- `__lt__()` – **для оператора меньше `<`**
- `__gt__()` – **для оператора больше `>`**
- `__le__()` – **для оператора меньше или равно `<=`**
- `__ge__()` – **для оператора больше или равно `>=`**

```python
class Clock:
    __DAY = 86400   # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60            # секунды
        m = (self.seconds // 60) % 60    # минуты
        h = (self.seconds // 3600) % 24  # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    # Метод который объединяет проверку во всех переопределенных методах сравнения
    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        return other if isinstance(other, int) else other.seconds

    # Переопределение оператора ==, != (при != срабатывает инверсия: self.seconds != sc)
    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc
    # Переопределение оператора <, > (при > срабатывает изменение операндов местами)
    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc
    # Переопределение оператора <=, >= (при >= срабатывает изменение операндов местами)
    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)  # False
print(c1 != c2)  # True
print(c1 < c2)  # True
print(c1 > c2)  # False
print(c1 >= c2)  # False
print(c1 <= c2)  # True
```

### Метод `__hash__` и `__eq__`

**Функция `hash()` в Python возвращает числовой хэш объекта**.

**`Хэш` — это уникальное целое число, которое вычисляется на основе содержимого объекта и используется для быстрой проверки равенства и работы с хэш-таблицами, например, в словарях или множествах**.

```python
# Пример использования hash()
print(hash("hello"))  # Хэш строки
print(hash(42))       # Хэш числа
print(hash((1, 2, 3))) # Хэш кортежа
```

#### Хэшируемые и нехэшируемые объекты

1. **Хэшируемые объекты**:

   - **Неизменяемые типы данных, такие как `числа`, `строки`, `кортежи`** (с неизменяемыми элементами).
   - **Класс, экземпляры которого имеют `неизменяемые атрибуты`, могут быть хэшируемыми**.

2. **Нехэшируемые объекты**:

   - Изменяемые типы данных, такие как списки, множества и словари, поскольку их содержимое может изменяться, нарушая консистентность хэша.

#### Создание хэшируемого класса

Чтобы экземпляры пользовательского класса были хэшируемыми:

- Определите метод `__hash__` для вычисления хэша.
- Убедитесь, что класс неизменяем:
  - Установите атрибуты только при инициализации (в методе `__init__`).
  - Используйте неизменяемые структуры данных, такие как строки, числа, кортежи.
- Переопределите метод `__eq__` для корректного сравнения объектов, поскольку хэш и равенство связаны.

Пример: Хэшируемый класс

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        # Хэш от кортежа атрибутов
        return hash((self.x, self.y))

# Создание объектов
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

# Сравнение объектов
print(p1 == p2)  # True
print(p1 == p3)  # False

# Использование объектов в множестве
points = {p1, p2, p3}
print(points)  # {<Point object>, <Point object>} (p1 и p2 считаются одинаковыми)
```

#### Связь `__hash__` и `__eq__`

- **Если два объекта равны (по **eq**), их хэши должны быть одинаковыми**.
- **Если объекты не равны, их хэши могут быть одинаковыми, но это приводит к "коллизиям", которые обрабатываются хэш-таблицами**.

#### Практическое применение `hash()`

- Словари и множества: Использование объектов пользовательского класса в качестве ключей словаря или элементов множества.

  ```python
  class Point:
      def __init__(self, x, y):
          self.x = x
          self.y = y

      def __eq__(self, other):
          if isinstance(other, Point):
              return self.x == other.x and self.y == other.y
          return False

      def __hash__(self):
          # Хэш от кортежа атрибутов
          return hash((self.x, self.y))


  # Создание объектов
  p1 = Point(1, 2)
  p2 = Point(1, 2)
  p3 = Point(3, 4)

  # Использование экземпляров класса Point в качестве ключей словаря
  distances = {p1: 5.0, p3: 10.5}
  print(distances[p1])  # 5.0
  ```

- Оптимизация поиска: Сравнение хэшей используется для ускорения проверки равенства.
- Кэширование и мемоизация: Использование хэша объекта для кэширования результатов функций.

#### Важные замечания

- **Хэш неизменяемого объекта неизменяем**: **После создания объекта его хэш не должен меняться**. Если **класс позволяет изменять атрибуты, его экземпляры становятся непредсказуемыми в хэш-таблицах**.

- **Кортежи и хэшируемость**: Кортежи хэшируются, если все их элементы хэшируемы.
  ```python
  print(hash((1, "hello", 3.14)))  # Работает
  try:
      print(hash((1, [2, 3], 4)))  # Ошибка, список не хэшируем
  except TypeError as e:
      print(e)
  ```
- **Переопределение `__hash__` и `__eq__`**: Рекомендуется использовать **неизменяемые структуры данных** внутри метода `__hash__` для надёжности.

### Метод `__bool__`

В стандартном поведении функция bool() возвращает True для непустых объектов и False – для пустых.

Функция bool() всегда возвращает True для любых объектов пользовательского класса.

Но Мы можем переопределить ее поведение либо через магический метод **len**(), либо через метод **bool**():

- `__len__()` – вызывается функцией bool(), если не определен магический метод **bool**();
- `__bool__()` – вызывается в приоритетном порядке функцией bool().

#### Переопределяем поведение через функцию `__len__()`:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

p1 = Point(3, 4)
p2 = Point(0, 0)
print(bool(p1)) # True
print(bool(p2)) # False
```

Запустим программу и видим значение `True`, а также сообщение `«__len__»`. То есть, был вызван метод `__len__()` и, так как он **вернул не нулевое значение**, то функция `bool()` интерпретировала его как `True`. Если установить нулевые координаты ожидаемо получим `False`

#### Переопределяем поведение через функцию `__bool__()`:

Объект будет считаться правдивым (истинным), если его координаты равны.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y


def isGoodPoint(p):
    if p:
        return "Объект дает True"
    else:
        return "Объект дает False"


p1 = Point(10, 20)
p2 = Point(0, 0)
p3 = Point(1, 10)

print(isGoodPoint(p1))  # False
print(isGoodPoint(p2))  # True
print(isGoodPoint(p3))  # False
```

### Методы `__getitem__`, `__setitem__` и `__delitem__`

- `__getitem__(self, item)` – **получение значения по ключу item**;
- `__setitem__(self, key, value)` – **запись значения value по ключу key**;
- `__delitem__(self, key)` – **удаление элемента по ключу key**.

#### Метод `__getitem__`

Создадим класс для представления студентов и формируем экземпляр.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

s1 = Student('Сергей', [5, 5, 3, 2, 5])
print(s1.marks[2]) # 3
print(s1[2]) # Ошибка
```

Для того, что бы строка `print(s1[2])` не выдавала ошибку нам нужно переопределить метод `__getitem__()`. В самом методе можен обработать некотоые ошибки.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        # Проверка типа данных переменной item
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")
        # Проверка длины списка и добавление в него недостающих элементов если переданный индекс больше количества элементов в списке
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")


s1 = Student('Сергей', [5, 5, 3, 2, 5])
print(s1.marks[2]) # 3
print(s1[2]) # 3
```

#### Метод `__setitem__`

Для изменения оценок стедента по индексу нужно переопределить метод `__setitem__()`.

Установим дополнительное поведение для этого метода, если индекс выходит за пределы, то мы будем расширять имеющийся список значениями `None`, и на позицию нужного индекса присваивать переданное значение:

```python

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - en(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __getitem__(self, item):
        # Проверка типа данных переменной item
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")
        # Проверка длины списка и добавление в него недостающих элементов если переданный индекс больше количества элементов в списке
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

s1[10] = 4
print(s1.marks) # [5, 5, 3, 2, 5, None, None, None, None, None, 4]
```

#### Метод `__delitem__`

Метод `__delitem__` вызывается при удалении элемента из списка. Переопределим в нашем классе этот метод:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        del self.marks[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - en(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __getitem__(self, item):
        # Проверка типа данных переменной item
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")
        # Проверка длины списка и добавление в него недостающих элементов если переданный индекс больше количества элементов в списке
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

s1 = Student('Сергей', [5, 5, 3, 2, 5])
del s1[2]
print(s1.marks) # [5, 5, 2, 5]
```

### Методы `__iter__` и `__next__`

- `__iter__(self)` – **получение итератора для перебора объекта**
- `__next__(self)` – **переход к следующему значению и его считывание**

Рассмотрим использование этих методов на реализации класса, похожего на `range()`. Класс будет генерировать арифметическую прогрессию.

```python
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start # Сохраняем начальное значение в атрибуте экземпляра.
        self.stop = stop # Сохраняем конечное значение в атрибуте экземпляра.
        self.step = step # Сохраняем шаг в атрибуте экземпляра.

    def __next__(self):
        if self.value + self.step < self.stop: # Проверяем, не превышает ли следующее значение конечное значение.
            self.value += self.step # Увеличиваем текущее значение на шаг.
            return self.value # Возвращаем текущее значение.
        else:
            raise StopIteration # Если следующее значение превышает конечное значение, вызываем исключение и Останавливаем итерацию.

    def __iter__(self):
        self.value = self.start - self.step # Сбрасываем текущее значение до начального.
        return self # Возвращаем сам объект как итератор.

fr = FRange(0, 2, 0.5)
for elem in fr1:
    print(elem)
# Вывод:
# 0.0
# 0.5
# 1.0
# 1.5
```

#### Разбор метода `__iter__` в классе FRange:

`self.value` - **это возвращаемое текущее значение в методе `__next__`**.

```python
self.value = self.start - self.step
```

**Что делает эта строчка в методе `__iter__`**:

- **инициализируем текущее значение, чтобы оно было меньше начального**.
- **сбрасываем текущее значение до начального**.

#### инициализируем текущее значение, чтобы оно было меньше начального

Инициализация текущего значения (`self.value`) как `self.start - self.step` позволяет **начать итерацию с первого значения, которое будет возвращено методом `__next__`**.

Это **важно**, потому что **при первом вызове `__next__` текущее значение должно быть увеличено на шаг, чтобы получить `первое значение в диапазоне` (В примере - это `0`)**.

Если бы мы просто инициализировали `self.value` равным `self.start`, то первое значение, возвращаемое методом `__next__`, было бы равно `self.start + self.step` (В примере первое значение было бы `0.5`), что не соответствует ожидаемому поведению итератора.

#### сбрасываем текущее значение до начального

Метод `__iter__` должен **подготавливать объект к новой итерации**. **Сброс текущего значения (`self.value`) до начального позволяет начать итерацию заново**.

**Это особенно важно, если итератор уже использовался, и мы хотим повторно пройти по тому же диапазону**.

**Без этого сброса, если бы мы вызвали `__iter__` после завершения итерации, метод `__next__` не смог бы вернуть значения, так как текущее значение уже было бы больше или равно конечному значению**.

#### Пример класса FRange2D для формирования таблиц значений:

```python
class FRange2D:
    # Определяем класс FRange2D, который будет представлять двумерный диапазон значений.

    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.fr = FRange(start, stop, step)  # Создаем экземпляр FRange для одномерного диапазона.
        self.rows = rows  # Сохраняем количество строк в атрибуте экземпляра.

    def __iter__(self):
        self.value_row = 0  # Инициализируем строку, с которой будем начинать итерацию.
        return self  # Возвращаем сам объект как итератор.

    def __next__(self):
        if self.value_row < self.rows: # Проверяем, не превышает ли текущая строка общее количество строк.
            self.value_row += 1  # Увеличиваем номер текущей строки на 1.
            return iter(self.fr)  # Возвращаем итератор для одномерного диапазона FRange.
        else: # Если текущая строка превышает общее количество строк, вызываем исключение.
            raise StopIteration  # Останавливаем итерацию.

# Создаем объект класса FRange2D с заданными параметрами.
fr = FRange2D(0, 2, 0.5, 4)

# Цикл для перебора значений класса FRange2D.
for row in fr:
    # Для каждой строки, получаем итератор для одномерного диапазона FRange.
    for x in row:
        print(x, end=" ")
    print()

# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
```

#### Разбор методов `__iter__` и `__next__` в классе FRange2D:

##### Почему значение `self.value_row = 0`, а не `-1`?

В классе FRange текущее значение инициализировалось как `self.start - self.step`, чтобы при первом вызове `__next__` получить первое значение. Однако в классе `FRange2D` логика немного другая.

Значение `self.value_row` инициализируется как `0`, потому что мы хотим, чтобы первая итерация возвращала первый ряд (индекс 0).

В методе `__next__` мы проверяем, меньше ли `self.value_row` общего количества строк (`self.rows`). Если это так, мы увеличиваем `self.value_row` на 1 и возвращаем итератор для `self.fr`.

Таким образом, при первой итерации `self.value_row` будет равно `1`, а при следующем вызове `__next__` будет возвращен итератор для `FRange`, который соответствует текущему ряду.

#### Почему метод `__next__` возвращает `iter(self.fr)` не смотря на то, что сам объект `fr` является итератором?

Объект `self.fr` (`экземпляр класса FRange`) действительно является итератором, так как он реализует методы `__iter__` и `__next__`. Однако, когда мы вызываем `iter(self.fr)`, мы получаем новый итератор для `self.fr`.

Это важно, потому что каждый раз, когда мы вызываем `__next__` в `FRange2D`, мы хотим получить новый итератор для одномерного диапазона, который будет использоваться для перебора значений в текущем ряду.

Таким образом, возвращая `iter(self.fr)`, мы обеспечиваем, что каждый раз, когда мы перебираем строки в `FRange2D`, мы получаем новый итератор для `FRange`, который может быть использован для получения значений в текущем ряду. Это позволяет избежать проблем с состоянием итератора, который может быть исчерпан, если мы не создадим новый итератор для каждой строки.

## Наследование и полиморфизм

### Наследование в объектно-ориентированном программировании

Наследование — это один из ключевых принципов объектно-ориентированного программирования (ООП), который позволяет создавать новые классы на основе существующих. Это позволяет повторно использовать код и организовывать его более эффективно.

В наследовании классы могут зависеть друг от друга. Базовый класс (или родительский) предоставляет общие свойства и методы, которые могут быть использованы в дочерних классах (или производных). Это создает иерархию классов, где дочерние классы наследуют функциональность базового класса.

Давайте рассмотрим пример, в котором мы не только переопределяем метод, но и добавляем новые свойства в дочерние классы.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора базового класса
        self.breed = breed  # Новое свойство для класса Dog

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Вызов конструктора базового класса
        self.color = color  # Новое свойство для класса Cat

    def speak(self):
        return "Meow!"

# Создаем объекты
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")

# Вызываем методы и свойства
print(f"{dog.name} is a {dog.breed} and says: {dog.speak()}")  # Вывод: Buddy is a Golden Retriever and says: Woof!
print(f"{cat.name} is a {cat.color} cat and says: {cat.speak()}")  # Вывод: Whiskers is a Tabby cat and says: Meow!
```

- **Базовый класс `Animal`**: Содержит конструктор, который инициализирует имя животного и метод speak, который возвращает общий звук.
- **Дочерний класс `Dog`**: В конструкторе добавляется новое свойство breed, которое указывает породу собаки. Метод speak переопределяется для возвращения звука, характерного для собак.
- **Дочерний класс `Cat`**: В конструкторе добавляется новое свойство color, которое указывает цвет кошки. Метод speak переопределяется для возвращения звука, характерного для кошек.

#### Объяснение работы поиска свойств (методов) внутри класса при их вызове

Когда вы вызываете метод или обращаетесь к свойству объекта, Python сначала ищет его в самом объекте. Если он не найден, Python ищет в классе, к которому принадлежит объект. Если метод или свойство не найдены в классе, поиск продолжается в родительских классах (если они есть). Это называется **поиск по цепочке наследования**.

#### Переопределение

Переопределение — это процесс, при котором дочерний класс предоставляет свою реализацию метода, который уже определен в базовом классе. Это позволяет изменять или расширять поведение базового класса. Например, метод speak в классе Dog переопределяет метод speak из класса Animal, чтобы вернуть звук, характерный для собак.

#### Как следует конструировать наследование?

- Определите базовый класс с общими свойствами и методами.
- Создавайте дочерние классы, которые наследуют от базового класса и добавляют свои уникальные свойства и методы.
- Избегайте избыточности: не дублируйте код, если он может быть вынесен в базовый класс.

### Функция `issubclass()`. Наследование от встроенных типов и от `object`

В Python все пользовательские классы по умолчанию наследуются от базового класса `object`, если явно не указано иное.

Это означает, что даже если вы не указываете родительский класс, ваш класс все равно будет являться подклассом `object`.

Это наследование обеспечивает доступ к базовым методам и свойствам, таким как `__str__`, `__repr__` и другим, которые определены в классе `object`.

```python
class MyClass:
    pass

print(issubclass(MyClass, object))  # Вывод: True
```

#### Функция `issubclass()`. Отличие от функции `isinstance()`

Функция `issubclass(class, classinfo)` проверяет, является ли класс `class` подклассом (прямым или косвенным) класса `classinfo`. Она возвращает `True`, если это так, и `False` в противном случае.

В отличие от `isinstance()`, которая проверяет, является ли объект экземпляром указанного класса или его подкласса, `issubclass()` работает только с классами, а не с объектами.

```python
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # Вывод: True
print(isinstance(Dog(), Animal))  # Вывод: True
print(isinstance(Animal, Dog))  # Вывод: False
```

#### Наследование от встроенных типов данных

Python позволяет создавать пользовательские классы, которые наследуют от встроенных типов данных, таких как `list`, `dict`, и других. Это позволяет расширять функциональность встроенных типов, добавляя свои методы и свойства.

```python
class MyList(list):
    def sum(self):
        return sum(self)

my_list = MyList([1, 2, 3])
print(my_list.sum())  # Вывод: 6
```

Рассмотрим пример, в котором мы создаем класс `CustomDict`, наследующий от встроенного типа `dict`. Этот класс будет добавлять метод для получения ключей, которые имеют значения больше определенного порога.

```python
class CustomDict(dict):
    def filter_by_value(self, threshold):
        return {k: v for k, v in self.items() if v > threshold}

# Создаем объект CustomDict
my_dict = CustomDict({'a': 1, 'b': 5, 'c': 3})

# Используем новый метод
filtered_dict = my_dict.filter_by_value(2)
print(filtered_dict)  # Вывод: {'b': 5, 'c': 3}
```

### Наследование. Функция super() и делегирование

#### Расширение базового класса

**Расширение базового класса** — это процесс создания нового класса (`дочернего`), который наследует свойства и методы существующего класса (`родительского`) и может добавлять новые функциональности или изменять существующие.

Это позволяет повторно использовать код и добавлять новые возможности без изменения базового класса.

```python
class Vehicle:
    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def honk(self):
        return "Car honks!"

# Создаем объект Car
my_car = Car()
print(my_car.start())  # Вывод: Vehicle started
print(my_car.honk())   # Вывод: Car honks!
```

#### Переопределение

Переопределение — это процесс, при котором дочерний класс предоставляет свою реализацию метода, который уже определен в родительском классе. Это позволяет изменять или расширять поведение базового класса.

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Создаем объект Dog
my_dog = Dog()
print(my_dog.speak())  # Вывод: Woof!
```

#### Последовательность вызовов магических методов: `__call__` -> `__new__` -> `__init__`

- `__call__`: Определяет, каким образом создается объект (вызывается у метакласса).
- `__new__`: Создает новый экземпляр класса.
- `__init__`: Инициализирует созданный экземпляр (устанавливает начальные значения атрибутов).

#### Функция super()

Функция `super()` возвращает временный объект, который позволяет обращаться к методам родительского класса. Это особенно полезно в контексте многократного наследования, так как она обеспечивает правильный порядок вызова методов в соответствии с порядком разрешения методов (MRO). Функция `super()` заменяет обращение к базовому классу напрямую (`Geom.__init__(self, ...)`)

```python
class Geom:
    def __init__(self, name):
        self.name = name

class Line(Geom):
    def __init__(self, name, length):
        super().__init__(name)  # Вызов инициализатора Geom
        self.length = length

line = Line("Линия", 10)
print(line.name, line.length)  # Линия 10
```

#### Делегирование с помощью функции `super()`.

Делегирование — это процесс, при котором один объект передает выполнение определенной задачи другому объекту.

В контексте наследования это может означать использование `super()` для вызова методов родительского класса, что позволяет дочернему классу использовать функциональность родителя.

```python
class Base:
    def show(self):
        return "Base class"

class Derived(Base):
    def show(self):
        return super().show() + " - Derived class"

# Создаем объект Derived
derived = Derived()
print(derived.show())  # Вывод: Base class - Derived class
```

#### Порядок вызова функции super().

При вызове `super()` в методе `__init__` важно делать его первой строчкой, чтобы гарантировать, что инициализация родительского класса происходит до выполнения кода дочернего класса. Это позволяет избежать ошибок, связанных с использованием свойств, которые могут быть определены в родительском классе.

**Неправильный пример**:

```python
class Geom:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = "default"

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        self.fill = fill  # Переопределение базового атрибута
        super().__init__(x1, y1, x2, y2)

rect = Rect(1, 2, 3, 4, "red")
print(rect.fill)  # default (переопределение затерялось)
```

**Правильный пример**:

```python
class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)  # Вызов базового инициализатора
        self.fill = fill

rect = Rect(1, 2, 3, 4, "red")
print(rect.fill)  # red
```

### Наследование и режимы доступа: private и protected атрибуты

- `private (__attribute)`: Атрибуты с двумя подчеркиваниями недоступны за пределами класса, в котором они определены. Они имеют префикс класса, где были созданы, и не могут быть переопределены в дочерних классах.

- `protected (_attribute)`: Атрибуты с одним подчеркиванием являются защищенными. Их использование допустимо внутри класса и его дочерних классов. Хотя protected не ограничивает доступ, оно сигнализирует, что к атрибуту следует обращаться осторожно.

#### Пример демонстрирует поведение этих режимов при создании атрибутов и методов, а также объясняет, когда их использование оправдано.

```python
# Базовый класс Geom
class Geom:
    name = "Geometry"  # Обычный публичный атрибут уровня класса

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор Geom для {self.__class__.__name__}")

        # Приватные атрибуты (доступны только внутри класса Geom)
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        # Защищенный атрибут (можно использовать в дочерних классах)
        self._is_valid = self.__verify_coords()

    def __verify_coords(self):
        """Приватный метод для проверки координат"""
        return all(0 <= coord <= 100 for coord in (self.__x1, self.__y1, self.__x2, self.__y2))

    def get_coords(self):
        """Метод для получения координат"""
        return (self.__x1, self.__y1, self.__x2, self.__y2)

# Дочерний класс Rect
class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill="red"):
        super().__init__(x1, y1, x2, y2)  # Вызов инициализатора базового класса
        self._fill = fill  # Защищённый атрибут (может использоваться в других методах)

    def get_properties(self):
        """Метод для получения свойств прямоугольника"""
        coords = self.get_coords()  # Используем метод из базового класса
        return {
            "coordinates": coords,
            "fill_color": self._fill,
            "valid": self._is_valid  # Доступ к защищённому атрибуту
        }

# Создаем объект дочернего класса Rect
rect = Rect(10, 20, 30, 40)

# Вывод локальных атрибутов объекта
print(rect.__dict__)  # Видим приватные и защищенные атрибуты с соответствующими префиксами

# Получение свойств прямоугольника
print(rect.get_properties())

# Попытка напрямую обратиться к приватным атрибутам вызовет ошибку:
# print(rect.__x1)  # AttributeError

# Но защищённые атрибуты доступны:
print(rect._fill)  # red
```

#### Вывод программы

```python
Инициализатор Geom для Rect
{'_Geom__x1': 10, '_Geom__y1': 20, '_Geom__x2': 30, '_Geom__y2': 40, '_is_valid': True, '_fill': 'red'}
{'coordinates': (10, 20, 30, 40), 'fill_color': 'red', 'valid': True}
red
```

#### Комментарии к примеру

- `Приватные атрибуты` (**x1, **y1, и т.д.) имеют префикс \_Geom, так как они определены в базовом классе Geom. Доступ к ним возможен только через методы базового класса.
- `Защищенные атрибуты` (\_is_valid, \_fill) используются в дочернем классе Rect, что упрощает взаимодействие между классами.
- `Приватные методы` (\_\_verify_coords) также недоступны за пределами базового класса, что исключает их случайное использование в дочерних классах.
- `Публичные методы` (например, get_coords) позволяют корректно взаимодействовать с приватными данными.

### Множественное наследование

Множественное наследование в Python позволяет создавать дочерний класс, наследующий свойства и методы сразу от нескольких базовых классов.

Это полезно в случаях, когда требуется комбинировать функциональность разных классов, например, при реализации миксинов (mixins).

#### Основные особенности:

- Классы перечисляются через запятую в порядке наследования.
- Python использует алгоритм MRO (Method Resolution Order) для определения порядка обхода базовых классов.
- Для корректной работы инициализаторов при множественном наследовании используется объект super(), делегирующий вызовы между классами по цепочке MRO.
- Для предотвращения конфликтов рекомендуется проектировать вспомогательные классы так, чтобы их инициализаторы принимали только параметр self.

#### Пример: Интернет-магазин с миксинами

Рассмотрим задачу создания интернет-магазина, где необходимо добавить возможность логирования к основным товарам.

```python
# Базовый класс товаров
class Goods:
    def __init__(self, name, weight, price):
        print("Инициализация Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"Товар: {self.name}, вес: {self.weight} кг, цена: {self.price} руб.")

# Миксин для логирования
class MixinLog:
    ID = 0

    def __init__(self):
        print("Инициализация MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"Товар с ID {self.id} продан.")

# Класс ноутбуков с множественным наследованием
class NoteBook(Goods, MixinLog):
    def __init__(self, name, weight, price):
        super().__init__(name, weight, price)  # Делегируем вызов следующим классам в MRO
        MixinLog.__init__(self)  # Явный вызов инициализатора MixinLog

# Создаем объект и работаем с ним
notebook = NoteBook("Acer Aspire", 2.0, 45000)
notebook.print_info()
notebook.save_sell_log()

# Вывод цепочки MRO
print(NoteBook.__mro__)
```

#### Разбор примера

- **Класс Goods**:

  - Определяет общие свойства для товаров: name, weight, price.
  - Реализует метод print_info() для вывода информации о товаре.

- **Класс MixinLog**:

  - Независимая функциональность для логирования операций.
  - Хранит уникальные идентификаторы (id) для каждого товара.

- **Класс NoteBook**:

  - Наследует свойства и методы обоих базовых классов.
  - Использует super().**init**() для делегирования вызовов по цепочке MRO.
  - Явно вызывает MixinLog.**init**(), так как super() не охватывает все базовые классы автоматически.

- **MRO (Method Resolution Order)**:

  - Метод **mro** выводит порядок обхода классов:

```arduino
(<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>, <class 'object'>)
```

#### Выводы

- Множественное наследование позволяет комбинировать функциональность разных классов.
- Корректная работа инициализаторов требует учета порядка MRO и использования super().
- Миксины — удобный инструмент для добавления дополнительной логики без изменения основной структуры классов.

### Коллекция `__slots__` и ее взаимодействие с property и наследованием

#### Коллекция `__slots__`:

- Ограничивает список локальных свойств экземпляров класса.
- Исключает создание атрибута `__dict__`, что:
- Уменьшает объем памяти, занимаемый экземпляром.
- Ускоряет доступ к локальным свойствам.
- Определяется как кортеж строк с именами допустимых свойств.

#### Использование `__slots__`:

**Пример**:

```python
class Point2D:
    __slots__ = ('x', 'y')
```

- Экземпляры класса могут содержать только атрибуты, указанные в `__slots__`.
- Работает только с локальными свойствами экземпляров, а не с атрибутами самого класса.

#### Работа `__slots__` с property:

- property позволяет добавлять свойства с логикой (геттеры, сеттеры) в классы с **slots**.
- Можно использовать приватные атрибуты в **slots** для хранения данных, а через property управлять их доступом.

**Пример**:

```python
class Point2D:
    __slots__ = ('x', 'y', '__length')

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value
```

#### Особенности `__slots__` при наследовании:

- По умолчанию `__slots__` базового класса не наследуется дочерними классами.
- Если в дочернем классе явно указать `__slots__ = ()`, ограничения будут унаследованы.

Для добавления новых атрибутов в дочернем классе `__slots__` можно расширить:

```python
class Point3D(Point2D):
    __slots__ = ('z',)
```

При этом сохраняются ограничения базового класса.

#### Преимущества и ограничения `__slots__`:

- Преимущества:
  - Экономия памяти.
  - Ускорение доступа к локальным атрибутам.
- Ограничения:
  - Нельзя использовать экземпляры с динамически добавляемыми атрибутами.
  - `__slots__` не совместим с множественным наследованием.

## Исключения и менеджеры контекста

### Блоки try/except

Исключения — это ошибки, возникающие во время выполнения программы, которые приводят к её остановке.

- **Исключения времени исполнения**: Например, деление на ноль (ZeroDivisionError) или обращение к несуществующей переменной (NameError).
- **Исключения синтаксиса**: Например, нарушение правил написания кода (`SyntaxError`).

#### Зачем обрабатывать исключения?

Исключения времени исполнения могут привести к внезапной остановке программы. Обработка исключений позволяет предотвратить это и обработать ошибки корректно.

#### Основной механизм обработки исключений: блок try/except

- Код, который может вызвать исключение, помещается в блок `try`.
- Возможные ошибки обрабатываются в блоке `except`.

**Примеры**:

```python
try:
    file = open("myfile.txt")
except FileNotFoundError:
    print("Невозможно открыть файл")
```

#### Обработка нескольких исключений

Каждый тип исключения можно обрабатывать отдельно с помощью нескольких блоков `except`.

**Можно указать несколько исключений через запятую**:

```python
except (ZeroDivisionError, ValueError):
    print("Ошибка")
```

#### Использование объекта исключения

Исключения можно связать с переменной для получения дополнительной информации:

```python
except ZeroDivisionError as z:
    print(z)
```

#### Иерархия классов исключений

Все исключения наследуются от базового класса `BaseException`, чаще используются классы из ветки `Exception`.
Более общие классы (например, `Exception`) обрабатывают все исключения из их поддерева, поэтому их нужно ставить после более специфичных:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Делить на ноль нельзя")
except Exception:
    print("Общая ошибка")
```

#### Универсальный блок except

Если не указать конкретный класс исключения, блок except перехватит любые ошибки:

```python
try:
    x = 10 / 0
except:
    print("Ошибка")
```

#### Итог:

Обработка исключений — это важный механизм для управления ошибками в программе. Используя блоки `try/except`, можно перехватывать и корректно обрабатывать ошибки, предотвращая внезапную остановку программы.

### Обработка исключений. Блоки finally и else

#### Блок else

Выполняется только если в блоке try не произошло исключений.

**Пример**:

```python
try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as z:
    print("Ошибка деления на ноль:", z)
except ValueError as z:
    print("Ошибка ввода:", z)
else:
    print("Исключений не произошло")
```

Ввод корректных данных выведет: Исключений не произошло. Если ошибка есть, блок else не выполнится.

#### Блок finally

Выполняется всегда после блока try, независимо от возникновения исключений. Используется для завершающих действий, таких как освобождение ресурсов.

**Пример**:

```python
try:
    f = open("myfile.txt", "w")
    f.write("hello")
except FileNotFoundError as z:
    print("Файл не найден:", z)
finally:
    f.close()
    print("Файл закрыт")
```

Даже при ошибке файл будет закрыт.

#### Особенность работы finally

Блок finally выполняется до оператора return.

**Пример**:

```python
def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError:
        return 0, 0
    finally:
        print("finally выполняется до return")
```

Ввод некорректных данных выведет: finally выполняется до return, затем (0, 0).

#### Вложенные блоки try / except

Позволяют гибко обрабатывать ошибки в разных частях программы.

**Пример**:

```python
try:
    x, y = map(int, input().split())
    try:
        res = x / y
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
except ValueError:
    print("Ошибка: Некорректный ввод")
```

#### Контекстные менеджеры как альтернатива finally

Для работы с файлами вместо finally часто используют with open:

```python
try:
    with open("myfile.txt", "w") as f:
        f.write("hello")
except FileNotFoundError:
    print("Файл не найден")
```

#### Выводы:

- Блок `else` выполняется при отсутствии ошибок.
- Блок `finally` всегда выполняется, подходит для освобождения ресурсов.
- Вложенные конструкции обеспечивают гибкую обработку ошибок.
- Контекстные менеджеры упрощают работу с ресурсами.

### Инструкция raise и пользовательские исключения

#### Оператор raise

Оператор raise используется для явного создания исключений в Python. Пример:

```python
raise ZeroDivisionError("Деление на ноль")
```

Можно указать класс исключения без параметров:

```python
raise ZeroDivisionError
```

Или использовать заранее созданный экземпляр:

```python
e = ZeroDivisionError("Деление на ноль")
raise e
```

**Важно**: объект после `raise` должен быть экземпляром класса, унаследованного от **BaseException**.

#### Когда нужен raise?

`raise` применяется для обработки ситуаций, которые Python не обрабатывает автоматически. Например, если данные не отправлены на принтер:

```python
class PrintData:
    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception("Принтер не отвечает")
    def send_to_print(self, data):
        return False
```

Попытка отправить данные вызовет исключение:

```python
p = PrintData()
p.send_data("123")  # Exception: Принтер не отвечает
```

#### Создание пользовательских исключений

Для пользовательских исключений создаются классы, наследуемые от Exception. Пример:

```python
class PrinterError(Exception):
    """Ошибка принтера"""
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f"Ошибка: {self.message}"
```

Использование:

```python
raise PrinterError("Принтер не отвечает")
```

#### Иерархия пользовательских исключений

Можно создавать общие и конкретные исключения:

```python
class PrinterError(Exception):
    """Общее исключение для принтера"""
class PrinterConnectionError(PrinterError):
    """Ошибка соединения с принтером"""
```

Обработка разных типов ошибок:

```python
try:
    raise PrinterConnectionError("Проблема соединения")
except PrinterConnectionError as e:
    print(e)  # Проблема соединения
except PrinterError:
    print("Общая ошибка принтера")
```

#### Расширение функциональности

Пользовательские классы исключений можно дополнять кастомной логикой, например, конструктором с аргументами или переопределением `__str__`.

#### Основной вывод: Использование `raise` и пользовательских исключений позволяет гибко управлять обработкой ошибок, улучшая читаемость и структуру кода.
