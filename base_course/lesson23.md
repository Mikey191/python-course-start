## Урок 23. Генераторы списков. Условия в генераторах списков. Вложенные генераторы списков

### 23.1 Генератор списка

**Генераторы списков** в языке Python - это **компактный** способ **создания списков** на основе других списков или итерируемых объектов. Они позволяют создавать новый список, применяя выражение к каждому элементу исходного списка или итерируемого объекта. Генераторы списков предоставляют более краткий и эффективный способ создания списков по сравнению с использованием обычных циклов.

### 23.2 Синтаксис генератора списка

**[выражение for элемент in исходный-список/итерируемый-объект]**

- **выражение** - это выражение, которое будет применено к каждому элементу исходного списка или итерируемого объекта.
- **элемент** - это переменная, которая будет использоваться для представления каждого элемента исходного списка или итерируемого объекта.
- **исходный*список/итерируемый*объект** - это список или итерируемый объект, на основе которого будет создан новый список.

**Пример**:

```python
# Пример 1: Создание списка чисел от 1 до 10
numbers = [i for i in range(1, 11)]
# Результат: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Пример 2: Создание списка квадратов чисел от 1 до 10
squares = [i**2 for i in range(1, 11)]
# Результат: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 23.3 Создание списка с помощью обычного цикла и создание списка с помощью генератора списков.

**Создание списка с помощью обычного цикла** и **создание списка с помощью генератора списков** позволяют **создавать списки**, но **существуют некоторые различия в синтаксисе и подходе**.

При использовании обычного цикла, вы должны объявить пустой список, затем использовать цикл для итерации по элементам исходного списка или итерируемого объекта, и внутри цикла добавлять элементы в новый список с помощью метода `append()`.

**Пример**:

```python
# Создание списка чисел от 1 до 10 с помощью обычного цикла
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)
```

При использовании **генератора списков**, вы можете **создать новый список в одной строке**, **применяя выражение к каждому элементу исходного списка** или **итерируемого объекта**.

**Пример**:

```python
# Создание списка чисел от 1 до 10 с помощью генератора списков
numbers = [i for i in range(1, 11)]
print(numbers)
```

**Оба подхода дают одинаковый результат, но генераторы списков обычно считаются более краткими и эффективными**.

### 23.4 Генератор списков с использованием input().split()

Генератор списков с использованием `input().split()` позволяет создавать список на основе введенных пользователем значений, разделенных пробелами.

```python
# Ввод чисел с клавиатуры и создание списка
numbers = [int(i) for i in input().split()]
```

В этом примере мы используем `input().split()` для получения ввода от пользователя. `input()` считывает строку, а `split()` разделяет эту строку на отдельные значения, используя пробел в качестве разделителя. Затем мы используем генератор списка `[int(i) for i in input().split()]`, чтобы преобразовать каждое значение в целое число и создать список из этих чисел.

### 23.5 Генератор списка с условием.

**Генератор списка с условием** позволяет **создавать список** на основе определенного условия.
**Синтаксис**:

**[выражение for элемент in исходный-список/итерируемый-объект if условие]**

- **выражение** - это выражение, которое будет применено к каждому элементу исходного списка или итерируемого объекта.
- **элемент** - это переменная, которая будет использоваться для представления каждого элемента исходного списка или итерируемого объекта.
- **исходный*список/итерируемый*объект** - это список или итерируемый объект, на основе которого будет создан новый список.
- **условие (необязательно)** - это условие, которое определяет, должен ли быть включен элемент в новый список.

```python
# Список городов
cities = ['Москва', 'Санкт-Петербург', 'Нью-Йорк', 'Лондон', 'Париж', 'Мадрид']
# Создание списка городов, начинающихся с буквы "М"
filtered_cities = [city for city in cities if city.startswith('М')]
print(filtered_cities)
```

В этом примере мы используем генератор списка `[city for city in cities if city.startswith('М')]`, чтобы создать новый список, содержащий только города, которые начинаются с буквы "М". Мы проверяем каждый элемент `city` в списке `cities` с помощью условия `city.startswith('М')`, и только те элементы, которые удовлетворяют условию, включаются в новый список `filtered_cities`.

```python
# Список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Создание списка четных чисел
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
```

В этом примере мы используем генератор списка `[num for num in numbers if num % 2 == 0]`, чтобы создать новый список, содержащий только четные числа из списка `numbers`. Мы проверяем каждое число `num` в списке `numbers` с помощью условия `num % 2 == 0`, и только четные числа включаются в новый список `even_numbers`.

**Генераторы списков с условием позволяют более компактно и эффективно создавать списки на основе определенных условий**.

### 23.6 Несколько циклов for в генераторах списков.

В языке Python можно использовать **вложенные циклы for в генераторах списков для создания списков с более сложной структурой** или для выполнения операций над элементами вложенных списков.

#### Вложенные циклы for в генераторе списка

**Пример 1**: **Вложенные циклы for в генераторе списка**

```python
# Создание списка с парами чисел от 1 до 3
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
# Результат: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
print(pairs)
```

В этом примере мы используем два вложенных цикла `for` в генераторе списка `[(x, y) for x in range(1, 4) for y in range(1, 4)]`, чтобы создать список с парами чисел от 1 до 3. Первый цикл `for x in range(1, 4)` перебирает значения x от 1 до 3, а второй цикл `for` y `in range(1, 4)` перебирает значения y от 1 до 3. Каждая комбинация `(x, y)` добавляется в список `pairs`.

**Пример 2**: **Преобразование двумерного списка в одномерный с помощью вложенных циклов for в генераторе списка**

```python
# Преобразование двумерного списка в одномерный
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
# Результат: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flat_list)
```

В этом примере мы используем два вложенных цикла `for` в генераторе списка `[num for row in matrix for num in row]`, чтобы преобразовать двумерный список `matrix` в одномерный список `flat_list`. Первый цикл `for row in matrix` перебирает строки в списке `matrix`, а второй цикл `for num in row` перебирает числа в каждой строке. Каждое число добавляется в список `flat_list`.

### 23.7 Вложенные генераторы списков.

**Вложенные генераторы списков** в языке Python позволяют **создавать списки с более сложной структурой или выполнять операции над элементами вложенных списков**. Они позволяют **использовать вложенные циклы и условия внутри генератора списка для создания более гибких и мощных выражений**.

**Пример 1**: **Получение двумерного списка с помощью вложенного генератора списков**

```python
# Получение двумерного списка с помощью вложенного генератора списков
matrix = [[i+j for j in range(3)] for i in range(3)]
# Результат: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
print(matrix)
```

В этом примере мы используем вложенный генератор списков `[[i+j for j in range(3)] for i in range(3)]`, чтобы создать двумерный список `matrix`. Внешний генератор списка `for i in range(3)` перебирает значения i от 0 до 2, а внутренний генератор списка `for j in range(3)` перебирает значения j от 0 до 2. Каждое значение `i+j` добавляется во внутренний список, и в результате получается двумерный список.

**Пример 2**: **Возвести все значения двумерного списка в квадрат с помощью вложенного генератора списков**

```python
# Возвести все значения двумерного списка в квадрат с помощью вложенного генератора списков
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squared_matrix = [[num**2 for num in row] for row in matrix]
# Результат: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
print(squared_matrix)
```

В этом примере мы используем вложенный генератор списков `[[num**2 for num in row] for row in matrix]`, чтобы возвести все значения двумерного списка `matrix` в **квадрат**. Внешний генератор списка `for row in matrix` перебирает строки в списке `matrix`, а внутренний генератор списка `for num in row` перебирает значения в каждой строке. Каждое значение `num**2` добавляется во внутренний список, и в результате получается двумерный список `squared_matrix`.

**Пример 3**: **Транспонирование матрицы с использованием вложенных генераторов**

```python
# Транспонирование матрицы с использованием вложенных генераторов
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Результат: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(transposed_matrix)
```

В этом примере мы используем вложенный генератор списков `[[row[i] for row in matrix] for i in range(len(matrix[0]))]`, чтобы выполнить **транспонирование матрицы**. Внешний генератор списка `for i in range(len(matrix[0]))` перебирает индексы столбцов, а внутренний генератор списка `for row in matrix` перебирает строки. Каждый элемент `row[i]` добавляется во внутренний список, и в результате получается транспонированная матрица `transposed_matrix`.

**Пример 4**: **Генератор списка в качестве итерируемого объекта в генераторе списка**

```python
# Пример: Создание списка кубов чисел от 1 до 5 с использованием вложенного генератора списков
cubes = [num ** 3 for num in [value + 1 for value in range(5)]]
# Результат: [1, 8, 27, 64, 125]
print(cubes)
```

В этом примере внутренний генератор списка `[value + 1 for value in range(5)]` создает список чисел от 1 до 5, а внешний генератор списка `num ** 3 for num in [...]` возводит каждое число из внутреннего списка в куб и формирует итоговый список кубов.

### Вопросы:

1. Что такое генератор списка в Python?
2. Какие преимущества предоставляют генераторы списков по сравнению с обычными циклами?
3. Как создать список чисел от 1 до 10 с использованием генератора списка?
4. Какие операции можно выполнять над элементами вложенных списков с помощью вложенных генераторов списков?
5. Какие условия можно добавить в генератор списка для фильтрации элементов?
6. Можно ли использовать генератор списка в качестве итерируемого объекта в другом генераторе списка?

### Задачи:

1. На вход программе подаются вещественные числа, записанные через пробел. Необходимо их прочитать и сохранить в списке lst. Затем, используя генератор списков сформировать новый список lst_abs из модулей чисел списка lst. Список lst_abs вывести на экран.

2. На вход программе подается семизначное целое положительное число. Необходимо его прочитать и с помощью генератора списков сформировать список lst_in, содержащий цифры этого числа. Полученный список вывести на экран.

3. На вход программе подается натуральное число `N`. Прочитайте его и с помощью генератора списков сформируйте двумерный список размером `N x N`, состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). Полученный двумерный список вывести на экран.

4. На вход программе подается строка с названиями городов, записанных через пробел. Необходимо прочитать эту строку и сформировать список с помощью генератора списков, содержащий названия городов длиной более пяти символов. Элементы полученного списка вывести в одну строчку через пробел. **Пример вводимой строки**: `Казань Уфа Москва Челябинск Омск Тур Самара`.

5. На вход программе подается натуральное число `n`. Необходимо его прочитать и сформировать список с помощью генератора списков, состоящий из делителей числа n (включая и само число n). Элементы полученного списка вывести в одну строчку через пробел. Делителями числа `n` называются целые числа, которые делят `n` нацело (без остатка).

6. На вход программе подается натуральное число `N`. Необходимо его прочитать и сгенерировать вложенный список с помощью генератора списков, размером `N x N`, где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки и так до N-й строки. Результат вывести на экран.

7. Объявите в программе следующий список:

   ```python
   matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 8, 7, 6],
     [5, 4, 3, 2],
   ]
   ```

   С помощью генератора списков необходимо преобразовать список matrix в одномерный так, чтобы значения элементов шли в обратном порядке. Результат отобразить в виде строки из чисел, записанных через пробел.

8. Объявите в программе следующий список из строк:

   ```python
   str_lst = [
     'Я помню чудное мгновенье:',
     'Передо мной явилась ты',
     'Как мимолетное виденье',
     'Как гений чистой красоты'
   ]
   ```

   Необходимо преобразовать его в двумерный список lst_words, где каждая строка представляется списком из слов (слова разделяются пробелом), но сохранять слова только длиной более трех символов. Решить данную задачу следует с использованием генератора списков. Результат отобразить на экран.

9. На вход программе поступает матрица:

   ```python
   matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [5, 4, 3],
   ]
   ```

   Нужно транспонировать `matrix` (строки заменяются на столбцы) и результат сохранить в списке `result` и вывести на экран.
