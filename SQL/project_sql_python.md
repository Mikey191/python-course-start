# 🧠 Урок 1: **Введение в базы данных и SQL**

## 🔹 План урока

- Что такое `базы данных` и `зачем они нужны`
- `Различие` между `реляционными` и `нереляционными БД`
- `Что такое SQL` и где он используется
- `Обзор популярных СУБД`
- Особенности и `преимущества SQLite`
- Как устроена таблица: `строки`, `столбцы`, `типы данных`
- Примеры таблиц и схем
- Мини-пример SQL-запросов для наглядности (`SELECT`, `INSERT`)

## 1. Что такое базы данных и зачем они нужны

- **База данных** (БД) — это **организованная структура для хранения, управления и поиска данных**.
- Примеры из реальной жизни:
  - **Интернет-магазин** — хранит товары, заказы, клиентов.
  - **Приложение заметок** — хранит тексты, дату, метки.
- БД позволяют легко:
  - **находить нужные данные** (поиск)
  - **изменять** и **удалять** информацию
  - **объединять** и **анализировать** данные

## 2. Реляционные и нереляционные БД

### Реляционные (табличные):

- данные хранятся в таблицах, связи между таблицами выражаются через ключи.

### Примеры:

- `SQLite`,
- `MySQL`,
- `PostgreSQL`.

### Нереляционные (NoSQL):

- данные хранятся в виде `документов`, `пар ключ-значение`, `графов` и т.д.

### Примеры:

- `MongoDB`,
- `Redis`,
- `Cassandra`.

### Простой пример SQL-структуры

```sql
-- Таблица пользователей
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
);

-- Добавление записи
INSERT INTO users (name, email) VALUES ('Alice', 'alice@mail.com');
```

<img src='img/1.png' width=500>

#### 📌 Здесь всё строго: поля определены, данные хранятся в таблице, можно задать связи между таблицами.

### Простой пример NoSQL-структуры

```json
// Документ в коллекции "users"
{
  "name": "Alice",
  "email": "alice@mail.com",
  "orders": [
    {
      "product": "Phone",
      "price": 500
    },
    {
      "product": "Laptop",
      "price": 1200
    }
  ]
}
```

#### 📌 Здесь всё гибко: поле orders — это массив вложенных объектов. Мы не указываем типы данных заранее и можем добавлять/убирать поля на лету.

### Мы будем работать только с реляционной БД SQLite, как самой простой для старта.

## 3. Что такое SQL и где он используется

- `SQL` (Structured Query Language) — **язык для управления реляционными базами данных**.
- С помощью SQL можно:
  - **создавать таблицы**
  - **вставлять**, **удалять**, **обновлять** данные
  - **делать запросы к таблицам** (выборки)
  - **объединять данные** из разных таблиц
- SQL — индустриальный стандарт, используется почти во всех БД.

## 4. Обзор популярных СУБД

### Что такое СУБД?

**СУБД (Система управления базами данных)** — это программное обеспечение, которое позволяет:

- создавать и структурировать базы данных;
- сохранять, изменять, удалять и искать данные;
- управлять доступом к данным;
- обеспечивать целостность и безопасность информации.

#### Иными словами, СУБД — это промежуточное звено между пользователем (или программой) и самой базой данных. Она получает запросы, обрабатывает их и возвращает результат.

### Пример

Когда вы выполняете SQL-запрос (например, SELECT \* FROM users), вы не общаетесь напрямую с файлами — вместо этого:

- Запрос поступает в СУБД (например, SQLite или PostgreSQL).
- СУБД анализирует его, ищет нужные данные в базе.
- Возвращает результат.

### Популярные СУБД:

- `PostgreSQL` — мощная, надёжная, используется в крупных проектах.
- `MySQL` — быстрая, популярная, используется в веб-проектах.
- `SQLite` — лёгкая, встроенная, не требует установки сервера.
- `MS SQL Server`, `Oracle DB` — коммерческие, используются в крупных компаниях.

## 5. Особенности SQLite

- `Кроссплатформенность` (работает на Windows, macOS, Linux)
- `Малый вес` (несколько сотен КБ)
- `Не требует отдельного сервера`. Весь файл БД — это один `.sqlite3`
- `Очень прост в использовании через Python`
- `Поддерживает большинство SQL-запросов`
- `Идеальна для локальных проектов, прототипов и обучения`

## 6. Как устроена таблица: строки, столбцы, типы данных

- Таблица — это как Excel-лист:
  - `Столбцы` (columns) — названия полей: name, age, email
  - `Строки` (rows) — конкретные записи
- Типы данных:
  - `INTEGER` — целое число
  - `REAL` — число с плавающей точкой
  - `TEXT` — строка
  - `BLOB` — двоичные данные
  - `NULL` — отсутствие значения

## 7. Примеры таблиц и схем

### **Пример таблицы users**:

<img src="img/1.png" width=500>

### **Схема**:

- Таблица users состоит из 4 столбцов
- `id` — уникальный идентификатор
- `name`, `email` — текстовые поля
- `age` — число

## 8. Мини-примеры SQL-запросов

**Для наглядности покажем простые SQL-запросы**:

```sql
-- Создание таблицы
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
);

-- Вставка данных
INSERT INTO users (name, age, email) VALUES ('Alice', 25, 'alice@mail.com');

-- Получение данных
SELECT * FROM users;
```

# 🧠 Урок 2: **Работа с SQLiteStudio и файлом `db.sqlite3`**

## 🔹 План урока

- Установка `SQLiteStudio`
- Создание новой базы данных
- Создание таблицы `users`: подробный разбор полей
- Выполнение базовых `SQL-запросов` через `SQLiteStudio`:
- `INSERT`
- `SELECT`
- `UPDATE`
- `DELETE`
- Создание второй таблицы `orders` и установка `внешнего ключа`
- Визуализация связей между таблицами
- Импорт и экспорт данных
- Открытие существующего файла `db.sqlite3`

## 1. Установка SQLiteStudio

- Скачайте `SQLiteStudio` с официального сайта: `https://sqlitestudio.pl`
- Пример названия скаченного файла: `SQLiteStudio-3.4.17-windows-x64-installer.exe`
- Запустите файл
- Следуйте инструкциям во время установки.

## 2. Создание новой базы данных

- В меню `Database` → `Add a database`
- Нажмите "`New database`"
- Назовите файл `test_db.sqlite3` и сохраните его
- База появится в списке слева

## 3. Создание таблицы `users`: подробный разбор полей

- Правый клик по базе → `Create a table`
- Назовите таблицу `users`
- Добавьте поля кликнув два раза по пустой строке:

  - `id`: `INTEGER` Уникальный идентификатор записи `PK` (Primary Key), `AI` (Auto Increment)
    - Заполните поле `Column name` именем `id`
    - Поставить галочку на `Primary Key`
    - Нажмите кнопку `Configure`
    - Выберите `Autoincrement`
    - Поле `Data type` заполнится автоматически.

- По аналогии добавьте остальные поля

  - `name`: `TEXT` Имя пользователя Просто текстовое поле
  - `age`: `INTEGER` Возраст Целое число
  - `email`: `TEXT` Электронная почта Уникальность не требуется

### Важно:

- `PK (Primary Key)` — уникальный идентификатор записи.
- `AI (Auto Increment)` — значение будет увеличиваться автоматически при вставке новых строк.

#### После создания нужных полей нажмите на `зеленую галочку` (Commit)

## 4. Выполнение базовых SQL-запросов через SQLiteStudio

Открой вкладку SQL Editor (Alt + E) и потренируйся выполнять следующие запросы:

### 🔸 Вставка записи

```sql
INSERT INTO users (name, age, email)
VALUES ('Alice', 25, 'alice@mail.com');
```

### 🔸 Выборка всех пользователей

```sql
SELECT * FROM users;
```

### 🔸 Обновление данных

```sql
UPDATE users
SET age = 26
WHERE name = 'Alice';
```

### 🔸 Удаление пользователя

```sql
DELETE FROM users
WHERE name = 'Alice';
```

#### Все запросы выполняются нажатием клавиши F9 или кнопки Execute SQL.

## 5. Создание таблицы orders и внешний ключ

Создаём таблицу `orders`, которая будет связана с users.

### Поля:

- `id`: INTEGER PK, AI
- `user_id`: INTEGER Внешний ключ, ссылается на users.id
- `product_name`: TEXT Название товара
- `price`: REAL Цена

### Как установить внешний ключ:

- В поле user_id открой вкладку Foreign key
- Укажи:

  - Table: users
  - Column: id

### 🔍 Что такое внешний ключ?

Внешний ключ (foreign key) — это связь между таблицами.

Он гарантирует, что в orders.user_id могут быть только значения, которые существуют в таблице users.id.

Это позволяет поддерживать целостность данных и строить связи "один ко многим" (один пользователь — много заказов).

## 6. Визуализация связей (Не смог найти в программе)

После создания обеих таблиц:

- ПКМ по базе → Show Graph of Tables
- Вы увидите схему: таблицы и стрелки-связи между ними.

## 7. Экспорт и импорт данных

### Экспорт:

- ПКМ по таблице → Export → Table as CSV

### Импорт:

- ПКМ по таблице → Import → Table from CSV

## 8. Открытие существующего файла db.sqlite3

- В меню Database → Add a database
- Найдите и откройте файл db.sqlite3
- Вы сможете просматривать структуру, выполнять запросы, экспортировать данные

## Практическое задание

1. Создайте новую базу данных с именем `practice.sqlite3`.  
   Убедитесь, что база появилась в списке слева.

2. Создайте таблицу `users` со следующими полями:

   - `id` — целое число, первичный ключ, автоинкремент
   - `name` — текст
   - `age` — целое число
   - `email` — текст

3. Добавьте в таблицу `users` три записи с разными значениями имени, возраста и электронной почты, используя `INSERT INTO`.

4. Выведите все записи из таблицы users с помощью `SELECT *`.  
   Убедитесь, что видите все три строки.

5. Обновите возраст одного из пользователей (например, того, у кого имя `John`), установив новый возраст с помощью `UPDATE`.

6. Удалите одного пользователя по его имени с помощью запроса `DELETE`.

7. Создайте таблицу `orders` со следующими полями:

   - `id` — целое число, PK, AI
   - `user_id` — внешний ключ, ссылается на users(id)
   - `product_name` — текст
   - `price` — число с плавающей точкой (REAL)

8. Добавьте две записи в таблицу `orders`, указав существующие `user_id` из таблицы `users`.

9. Экспортируйте таблицу `users` в `CSV-файл`, а затем импортируйте её обратно как новую таблицу `users_copy`. Проверьте, что данные в `users_copy` совпадают с оригинальными.

10. **Общее задание**:
    - Установите `SQLiteStudio`
    - Создайте базу данных `shop.sqlite3`
    - Создайте таблицу customers:
      - `id` (INTEGER, PK, AI)
      - `name` (TEXT)
      - `email` (TEXT)
    - Добавьте 3 записи в customers через SQL-запросы
    - Создайте таблицу orders:
      - `id` (INTEGER, PK, AI)
      - `customer_id` (INTEGER, внешний ключ к customers.id)
      - `product_name` (TEXT)
      - `amount` (REAL)
    - Добавьте 3 заказа, связанных с разными клиентами
    - Выполните следующие запросы:
      - `SELECT * FROM customers`;
      - `SELECT * FROM orders`;
      - `UPDATE имя одного клиента`
      - `DELETE один заказ`
    - Откройте визуализацию связей между таблицами
    - Экспортируйте таблицу orders в `CSV`
    - Импортируйте обратно из `CSV` в новую таблицу `orders_copy`

# 🧠 Урок 3: **Работа с SQLite в Python через sqlite3. Сырые SQL-запросы**

## 🔹 План урока

- Подключение к базе данных db.sqlite3 из Python
- Создание таблиц через Python
- Выполнение SQL-запросов:
  - SELECT
  - INSERT
  - UPDATE
  - DELETE
- Параметры в запросах и защита от SQL-инъекций (?)
- Обработка результатов: fetchone(), fetchall()
- Работа с транзакциями и commit()
- Обязательная практика

## 1. Как открыть db.sqlite3 в Python

```python
import sqlite3

conn = sqlite3.connect('db.sqlite3')  # Подключение к базе
cursor = conn.cursor()  # Создание курсора
```

- Файл будет создан, если его не существует.
- Все дальнейшие действия идут через `cursor.execute(...)`.

## 2. Создание таблицы через Python

**Пример таблицы `users`**:

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")
conn.commit()
```

`IF NOT EXISTS` — позволяет избежать ошибки, если таблица уже создана.

### ✅ Как в запросе установить уникальность поля

Чтобы сделать поле уникальным (например, email), нужно добавить `UNIQUE` при создании таблицы:

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT UNIQUE
)
""")
```

#### 📌 Теперь в таблице нельзя будет добавить двух пользователей с одинаковым email — SQLite выдаст ошибку.

### ✅ Как установить поле, в котором не может быть NULL

Для этого используется ключевое слово `NOT NULL`:

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT NOT NULL UNIQUE
)
""")
```

#### 📌 Теперь поля name и email обязательны — при попытке вставить NULL SQLite выбросит ошибку.

## 3. Выполнение SQL-запросов

### ✅ INSERT — Добавление данных

```python
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
               ("Alice", 25, "alice@example.com"))
conn.commit()
```

### ✅ SELECT — Получение данных

```python
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
for user in users:
    print(user)
```

#### ✅ Что такое `fetchall()`?

Метод `fetchall()` извлекает все строки результата последнего `SELECT-запроса` и возвращает список кортежей.

```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

Если в таблице 3 записи, `fetchall()` вернёт `список из 3 кортежей`.

#### ✅ Какие ещё есть методы выборки?

- `fetchone()`: Возвращает первую строку результата (или None, если строк нет).
- `fetchmany(size)`: Возвращает список из size строк. Если меньше — вернёт сколько есть.
- `fetchall()`: Возвращает все строки результата запроса.

#### 🔍 Примеры:

```python
# fetchone
cursor.execute("SELECT * FROM users")
print(cursor.fetchone())  # Только первая строка

# fetchmany
cursor.execute("SELECT * FROM users")
print(cursor.fetchmany(2))  # Первые две строки

# fetchall
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # Все строки
```

### ✅ UPDATE — Обновление данных

```python
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
conn.commit()
```

### ✅ DELETE — Удаление данных

```python
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
conn.commit()
```

## 4. Как изменить поля таблицы, если она уже создана?

Для изменения таблицы используется `ALTER TABLE`. Например:

### ➕ Добавить новое поле:

```python
cursor.execute("ALTER TABLE users ADD COLUMN phone TEXT")
conn.commit()
```

#### Теперь у всех пользователей будет новое поле `phone`, по умолчанию `NULL`.

### 📝 Переименовать таблицу:

```python
cursor.execute("ALTER TABLE users RENAME TO customers")
conn.commit()
```

### 🚫 Удалить столбец нельзя напрямую в SQLite (до версии 3.35)

**Нужно**:

- Создать новую таблицу без ненужного поля.
- Перенести туда данные.
- Удалить старую таблицу.
- Переименовать новую в старое имя.

## 5. Изменить существующее поле

В SQLite `нельзя изменить уже созданное поле напрямую` — например, добавить NOT NULL, UNIQUE или изменить тип данных поля в существующей таблице.

### 🔧 Как обойти это ограничение?

Нужно выполнить пересоздание таблицы.

**Общий алгоритм такой**:

- Создаём новую таблицу с нужными свойствами.
- Копируем данные из старой таблицы.
- Удаляем старую таблицу.
- Переименовываем новую в имя старой.

### 🛠 Пример: добавить UNIQUE к полю email, которого не было

Допустим, изначально таблица была создана так:

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")
```

### Теперь хотим, чтобы email стал UNIQUE и NOT NULL.

#### 1. Создаём новую таблицу с нужными ограничениями:

```python
cursor.execute("""
CREATE TABLE users_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT NOT NULL UNIQUE
)
""")
```

#### 2. Копируем данные из старой таблицы (если данные валидные):

```python
cursor.execute("""
INSERT INTO users_new (id, name, age, email)
SELECT id, name, age, email FROM users
""")
```

#### ⚠️ Если в старой таблице были дублирующиеся email или NULL, произойдёт ошибка.

#### 3. Удаляем старую таблицу:

```python
cursor.execute("DROP TABLE users")
```

#### 4. Переименовываем новую:

```python
cursor.execute("ALTER TABLE users_new RENAME TO users")
conn.commit()
```

## 6. Примеры с параметрами (?) и защита от SQL-инъекций

**Никогда не вставляй значения в `SQL-запросы` через `f-строки` или конкатенацию** — только через `?`.

### ⚠️ Неправильно:

```python
# Уязвимо к SQL-инъекциям!
name = "Bob"
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
```

### Правильно:

```python
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

## 7. Работа с транзакциями

Все изменения нужно сохранять через `conn.commit()`.

### При ошибках можно откатить:

```python
conn.rollback()
```

### Рекомендуется использовать конструкцию `try/except`:

```python
try:
    cursor.execute("UPDATE users SET age = age + 1")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Ошибка:", e)
```

## 8. Дополнительная информация

После окончания работы обязательно закрывай соединение:

```python
conn.close()
```

### Можно использовать менеджер контекста:

```python
with sqlite3.connect('db.sqlite3') as conn:
    cursor = conn.cursor()
    ...
```

## 9. 💻 Примеры кода (всё вместе) - `функции` + `main()` + `try/except` + `with`

```python
import sqlite3


def create_table(cursor):
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE NOT NULL
        )
        """)
    except Exception as e:
        print("Ошибка создания таблицы:", e)


def insert_user(cursor, name, age, email):
    try:
        cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
                       (name, age, email))
    except Exception as e:
        print("Ошибка вставки:", e)


def show_users(cursor):
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            print(user)
    except Exception as e:
        print("Ошибка выборки:", e)


def update_user_age(cursor, name, new_age):
    try:
        cursor.execute("UPDATE users SET age = ? WHERE name = ?", (new_age, name))
    except Exception as e:
        print("Ошибка обновления:", e)


def delete_user(cursor, name):
    try:
        cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    except Exception as e:
        print("Ошибка удаления:", e)


def main():
    try:
        with sqlite3.connect("db.sqlite3") as conn:
            cursor = conn.cursor()

            create_table(cursor)
            insert_user(cursor, "Bob", 30, "bob@example.com")
            show_users(cursor)
            update_user_age(cursor, "Bob", 31)
            delete_user(cursor, "Bob")

            # commit не обязателен в with, но лучше оставить для наглядности
            conn.commit()

    except Exception as e:
        print("Ошибка при работе с базой данных:", e)


if __name__ == "__main__":
    main()
```

## Практическое задание

1. **Создание и подключение к базе**  
   Создай `Python-скрипт`, который:

   - Подключается к базе данных `lesson3.sqlite3`;
   - Создаёт `курсор`;
   - Создаёт таблицу `products` с полями:
     - `id` (целое, автоинкремент, первичный ключ),
     - `title` (строка, не NULL),
     - `price` (целое число),
     - `sku` (строка, уникальное поле).

2. **Вставка данных с параметрами**  
   Добавь в таблицу `3 товара` с разными значениями. Используй `?` вместо подстановки строк (`никаких f-строк`). Не забудь `commit()`.

3. **Выборка данных**  
   Выведи все товары из таблицы `products`, используя:

   - `fetchall()` — выведи весь список;
   - `fetchone()` — выведи только первый товар;
   - `fetchmany(2)` — выведи два товара.

4. **Уникальность поля**  
   Попробуй добавить товар с тем же значением `sku`, что и у одного из уже добавленных. Проверь, выдаст ли `SQLite ошибку`. Оберни `execute` в `try/except` и выведи `сообщение об ошибке`.

5. **Обновление данных**  
   Обнови `цену товара` по его `title`. Например, если был товар `"Ноутбук"`, увеличь его цену на `1000`. Выведи результат до и после обновления.

6. **Удаление данных**
   `Удалите один товар` по его `sku`. Убедись, что он исчез из таблицы, выполнив `SELECT`.

7. **Добавление нового столбца**
   Добавь в таблицу `products` новый столбец `category` (строка). После этого обнови все товары и добавь им категорию, используя `UPDATE`.

8. **Работа с транзакциями**  
   Создай ситуацию, при которой `происходит ошибка` (например, вставка товара с `NULL` в обязательное поле или дубликатом `sku`). Используй `try/except`, `rollback()` и `commit()` в связке.

9. **Пересоздание таблицы**  
   Сделай всё по инструкции:

   - Создай новую таблицу `products_new` с теми же полями, но добавь ограничение `NOT NULL` на поле `price`.
   - Перенеси туда данные из `products`.
   - Удали старую таблицу и переименуй новую обратно в `products`.

10. **Использование функций**  
    Оформи код из заданий 1–6 в виде `функций`:

    - `create_table(cursor)`
    - `insert_product(cursor, title, price, sku)`
    - `show_products(cursor)`
    - `update_price(cursor, title, new_price)`
    - `delete_product(cursor, sku)`
    - И напиши функцию `main()` с подключением через `with`, где вызываются эти функции.

# 🧠 Урок 4: **Связи между таблицами в SQL. Практика через Python**

## 🔹 План урока

- Теория: ключи (`PRIMARY KEY`, `FOREIGN KEY`) и типы связей
- `Один к одному`
- `Один ко многим`
- `Многие ко многим`
- Создание таблиц с внешними ключами через Python
- `INSERT` с учетом связей
- `JOIN-запросы`: `INNER JOIN`, `LEFT JOIN` — и их выполнение через Python
- **Пример проекта**: `пользователи → заказы → товары`

## 1. Теория: ключи и связи

- `PRIMARY KEY` — уникальный идентификатор записи в таблице.
- `FOREIGN KEY` — внешний ключ, который указывает на PRIMARY KEY другой таблицы.
- Основные типы связей:
  - `Один к одному` (1:1)
  - `Один ко многим` (1:N)
  - `Многие ко многим` (M:N)

## 2. Связь "Один к одному"

### 📌 Пример: таблица users и user_profiles

```python
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE user_profiles (
    user_id INTEGER PRIMARY KEY,
    bio TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")
```

- Один пользователь — один профиль.
- Поле `user_id` в `user_profiles` и есть внешний ключ на `users(id)`.

## 3. Связь "Один ко многим"

### 📌 Пример: users → orders (один пользователь может иметь много заказов)

```python
cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    item TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")
```

## 4. Связь "Многие ко многим"

### 📌 Пример: orders ↔ products через order_products

```python
cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE order_products (
    order_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    PRIMARY KEY (order_id, product_id)
)
""")
```

- Один заказ может содержать много товаров.
- Один товар может находиться в нескольких заказах.

### 🔧 Контекст: связь «многие ко многим»

Когда одна запись в таблице `orders` может быть связана с несколькими товарами из таблицы `products`, и наоборот — один товар может быть в нескольких заказах, мы используем **промежуточную таблицу** (или "связующую таблицу").

### 📌 Разбор по частям:

1. `order_id INTEGER`:

   - Создаётся поле `order_id` — это будет `внешний ключ`, который указывает на `id заказа` из таблицы `orders`.

2. `product_id INTEGER`:

   - Создаётся поле `product_id` — это `внешний ключ на id` товара из таблицы `products`.

3. `FOREIGN KEY (order_id) REFERENCES orders(id)`

   - Говорим, что `order_id` — это внешний ключ (`foreign key`), который связан с полем `id` таблицы `orders`.

   - Если попытаться вставить `order_id`, которого нет в таблице `orders`, — будет ошибка. Это гарантирует целостность данных.

4. `FOREIGN KEY (product_id) REFERENCES products(id)`

   - То же самое: `product_id` ссылается на `id` в таблице `products`.

5. `PRIMARY KEY (order_id, product_id)`

   - **Вот это ключевая строка.**

   - **Что происходит**:

     - Мы объявляем `составной первичный ключ`.
     - Это значит, что вместе `order_id` и `product_id` в одной строке образуют `уникальную пару`.
     - То есть `нельзя будет вставить одну и ту же пару дважды`. Например:

       ```text
       (order_id=3, product_id=5)  ✅ — добавится
       (order_id=3, product_id=5)  ❌ — ошибка (такая пара уже есть)
       ```

     - Зачем это нужно:
       - Чтобы не было дублирующих записей в таблице связей. Один и тот же товар не может быть привязан к одному заказу дважды — это логично, и система это будет проверять.

### 🧠 Краткое резюме:

- В `PRIMARY KEY (order_id, product_id)` — обе колонки вместе формируют ключ.
- Это означает: `уникальность сочетаний заказа и товара`.
- Это `удобно для промежуточных таблиц` в связи многие ко многим.
- Составной ключ `помогает избежать повторных связей между одними и теми же объектами`.

## 5. INSERT с учетом связей

**Пример: добавить заказ пользователя**.

Вставить пользователя в таблицу `users`, и затем вставить заказ в таблицу `orders`, который должен `ссылаться на этого пользователя`.

```python
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
user_id = cursor.lastrowid

cursor.execute("INSERT INTO orders (user_id, item) VALUES (?, ?)", (user_id, "Book"))
```

### 🔍 Что делает cursor.lastrowid

```python
user_id = cursor.lastrowid
```

- `cursor.lastrowid` возвращает `ID` (значение автоинкрементного поля PRIMARY KEY) той записи, которая была вставлена последней через этот курсор.
- В данном случае — это `id пользователя "Alice"`, автоматически созданный SQLite при вставке.

### 🔄 Зачем это нужно?

Когда работаешь со связанными таблицами, ты часто сначала добавляешь родительскую запись, получаешь её `ID` и используешь этот `ID`, чтобы вставить зависимые записи (например, заказы пользователя).

**Это особенно важно, если**:

- ты не знаешь заранее `ID` (он автоинкрементный);
- тебе нужно поддерживать связи через внешний ключ (`FOREIGN KEY`).

### 🚨 Особенности lastrowid

- Работает `только для последней вставки`, сделанной через этот курсор.
- Работает только для таблиц, где есть `AUTOINCREMENT` или `INTEGER PRIMARY KEY`.
- Если ты вставляешь несколько строк сразу, `lastrowid` будет `ID первой вставленной строки`.

## 6. Как реализовать полную вставку в связанной структуре: `Пользователь → Заказ → Товары`

### Шаг 1. Таблицы

```python
import sqlite3

with sqlite3.connect("shop.db") as conn:
    cursor = conn.cursor()

    # Таблица пользователей
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    # Таблица заказов
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    # Таблица товаров
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )
    """)

    # Связующая таблица: заказы <-> товары (многие ко многим)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_products (
        order_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (product_id) REFERENCES products(id),
        PRIMARY KEY (order_id, product_id)
    )
    """)
```

### 🧩 Шаг 2. Вставка пользователя

```python
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
user_id = cursor.lastrowid  # Получаем ID только что вставленного пользователя
```

### 📦 Шаг 3. Создание заказа для пользователя

```python
cursor.execute("INSERT INTO orders (user_id) VALUES (?)", (user_id,))
order_id = cursor.lastrowid  # Получаем ID созданного заказа
```

### 🛒 Шаг 4. Вставка товаров (если они ещё не существуют)

```python
products = [("Book", 10.0), ("Pen", 2.5), ("Notebook", 5.0)]
product_ids = []

for name, price in products:
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    product_ids.append(cursor.lastrowid)  # Сохраняем ID каждого товара
```

### 🔗 Шаг 5. Связывание товаров с заказом

```python
for product_id in product_ids:
    cursor.execute("INSERT INTO order_products (order_id, product_id) VALUES (?, ?)", (order_id, product_id))
```

### ✅ Финальный код

```python
import sqlite3

with sqlite3.connect("shop.db") as conn:
    cursor = conn.cursor()

    # Вставка пользователя
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    user_id = cursor.lastrowid

    # Вставка заказа
    cursor.execute("INSERT INTO orders (user_id) VALUES (?)", (user_id,))
    order_id = cursor.lastrowid

    # Добавление товаров
    products = [("Book", 10.0), ("Pen", 2.5), ("Notebook", 5.0)]
    product_ids = []
    for name, price in products:
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        product_ids.append(cursor.lastrowid)

    # Связь заказ <-> товары
    for product_id in product_ids:
        cursor.execute("INSERT INTO order_products (order_id, product_id) VALUES (?, ?)", (order_id, product_id))

    conn.commit()
```

### ✅ Пример: пользователь уже есть

Допустим, в таблице уже есть `"Alice"` — мы найдем её `ID`, а дальше создадим заказ от её имени.

Мы не вставляем нового пользователя, а находим его `ID` по имени (или `email'у`, `username'у` — зависит от проекта).

```python
import sqlite3

with sqlite3.connect("shop.db") as conn:
    cursor = conn.cursor()

    # 1. Получаем user_id по имени
    cursor.execute("SELECT id FROM users WHERE name = ?", ("Alice",))
    result = cursor.fetchone()

    if result:
        user_id = result[0]  # ID существующего пользователя

        # 2. Создаем заказ
        cursor.execute("INSERT INTO orders (user_id) VALUES (?)", (user_id,))
        order_id = cursor.lastrowid

        # 3. Вставляем товары
        products = [("Pencil", 1.5), ("Eraser", 0.9)]
        product_ids = []

        for name, price in products:
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            product_ids.append(cursor.lastrowid)

        # 4. Связываем заказ с товарами
        for product_id in product_ids:
            cursor.execute("INSERT INTO order_products (order_id, product_id) VALUES (?, ?)", (order_id, product_id))

        conn.commit()
    else:
        print("Пользователь не найден!")
```

#### 🔍 Обрати внимание:

- `cursor.fetchone()` — возвращает None, если пользователь не найден. Поэтому нужен `if result`.
- Поиск по `name` — только если ты уверен, что имя уникально. Обычно лучше использовать `логин`, `email` или `ID` напрямую.

## 7. JOIN-запросы: теоретически и на Python

### Что такое `JOIN`?

`JOIN` — это способ объединить данные из двух (или более) таблиц, основываясь на логической связи между ними. Чаще всего — по FOREIGN KEY.

### Что делает `JOIN`?

Это внутреннее соединение (`INNER JOIN`). Оно показывает только те записи, где найдена пара в обеих таблицах.

### **Пример 1: JOIN (INNER JOIN по умолчанию): найти все заказы и имена пользователей**

```python
cursor.execute("""
SELECT users.name, orders.item
FROM orders
JOIN users ON users.id = orders.user_id
""")

for row in cursor.fetchall():
    print(row)
```

### 📘 Пошаговое объяснение:

1. `FROM orders` — основная таблица: берём все строки из orders.

2. `JOIN users` — присоединяем таблицу users.

3. `ON users.id = orders.user_id` — условие соединения: берём только те строки, где `orders.user_id` совпадает с `users.id`.

4. `SELECT users.name, orders.item` — выбираем конкретные поля: имя пользователя и заказ.

5. `fetchall()` — возвращает список кортежей с результатами запроса.

### **Пример 2: LEFT JOIN (или LEFT OUTER JOIN): показать всех пользователей даже без заказов**

```python
cursor.execute("""
SELECT users.name, orders.item
FROM users
LEFT JOIN orders ON users.id = orders.user_id
""")
```

### 📘 Пошаговое объяснение:

1. `FROM users` — основная таблица теперь users.

2. `LEFT JOIN orders` — присоединяем таблицу orders, включая всех пользователей, даже если заказов у них нет.

3. `ON users.id = orders.user_id` — соединяем по соответствию ID.

4. `SELECT users.name, orders.item` — выводим имя пользователя и заказ (если есть).

#### Что делает LEFT JOIN?

`LEFT JOIN` показывает всех пользователей, даже если у них нет заказов. Для таких пользователей значения из orders будут `NULL`.

### Сравнение типов JOIN

- `INNER JOIN`: Только совпадающие записи (оба поля не NULL)
- `LEFT JOIN`: Все из левой таблицы, + совпадающие из правой, если есть
- `RIGHT JOIN`: Все из правой таблицы, + совпадающие из левой (в SQLite нет, эмулируется)
- `FULL JOIN`: Все записи из обеих таблиц (SQLite не поддерживает напрямую, нужен UNION)

## 💡 Дополнительная информация

`SQLite` не применяет внешние ключи по умолчанию. Обязательно включать:

```python
cursor.execute("PRAGMA foreign_keys = ON")
```

## 💻 Примеры: модель «Пользователи → Заказы → Товары»

**Код** включает `создание таблиц`, `добавление данных` и `выборку с JOIN + GROUP_CONCAT`, чтобы отобразить список товаров по каждому заказу.

```python
import sqlite3

# Подключаемся к базе данных (если файла нет — создастся)
conn = sqlite3.connect("lesson4.sqlite3")
cursor = conn.cursor()

# Включаем поддержку внешних ключей в SQLite (по умолчанию отключена)
cursor.execute("PRAGMA foreign_keys = ON")

# Удаляем таблицы, если они уже существуют (чтобы начать "с нуля")
cursor.execute("DROP TABLE IF EXISTS order_products")  # Промежуточная таблица между заказами и товарами
cursor.execute("DROP TABLE IF EXISTS orders")          # Таблица заказов
cursor.execute("DROP TABLE IF EXISTS products")        # Таблица товаров
cursor.execute("DROP TABLE IF EXISTS users")           # Таблица пользователей

# Создаем таблицу пользователей
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный ID (автоматически увеличивается)
    name TEXT                              -- Имя пользователя
)
""")

# Создаем таблицу заказов
cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный ID заказа
    user_id INTEGER,                       -- ID пользователя, сделавшего заказ
    FOREIGN KEY (user_id) REFERENCES users(id)  -- Внешний ключ на таблицу пользователей
)
""")

# Создаем таблицу товаров
cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный ID товара
    name TEXT                              -- Название товара
)
""")

# Создаем промежуточную таблицу для связи "многие ко многим" между заказами и товарами
cursor.execute("""
CREATE TABLE order_products (
    order_id INTEGER,                           -- ID заказа
    product_id INTEGER,                         -- ID товара
    FOREIGN KEY (order_id) REFERENCES orders(id),    -- Внешний ключ на таблицу заказов
    FOREIGN KEY (product_id) REFERENCES products(id),-- Внешний ключ на таблицу товаров
    PRIMARY KEY (order_id, product_id)               -- Композитный первичный ключ (уникальная пара заказ-товар)
)
""")

# 📥 Добавление данных:

# Добавляем пользователя по имени (Bob)
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))

# Добавляем два товара: Keyboard и Mouse
cursor.execute("INSERT INTO products (name) VALUES (?)", ("Keyboard",))
cursor.execute("INSERT INTO products (name) VALUES (?)", ("Mouse",))

# Добавляем заказ от пользователя с ID = 1 (в нашем случае это Bob)
# Сохраняем ID заказа, чтобы потом использовать его
order_id = cursor.execute("INSERT INTO orders (user_id) VALUES (?)", (1,)).lastrowid

# Добавляем товар "Keyboard" (product_id = 1) в заказ
cursor.execute("INSERT INTO order_products (order_id, product_id) VALUES (?, ?)", (order_id, 1))

# Добавляем товар "Mouse" (product_id = 2) в тот же заказ
cursor.execute("INSERT INTO order_products (order_id, product_id) VALUES (?, ?)", (order_id, 2))

# Сохраняем изменения в базе данных
conn.commit()

# 📤 Получение данных: имя пользователя, номер заказа и список товаров в этом заказе
cursor.execute("""
SELECT users.name AS user_name,
       orders.id AS order_id,
       GROUP_CONCAT(products.name, ', ') AS products_list  -- Собираем все товары в строку через запятую
FROM users
JOIN orders ON users.id = orders.user_id
JOIN order_products ON orders.id = order_products.order_id
JOIN products ON order_products.product_id = products.id
GROUP BY orders.id  -- Группируем по заказу, чтобы получить одну строку на заказ
ORDER BY orders.id
""")

# Выводим результат
for row in cursor.fetchall():
    print(f"Пользователь: {row[0]}, Заказ №{row[1]}, Товары: {row[2]}")

# Закрываем соединение
conn.close()
```

## Практическое задание

1. **Создай две таблицы со связью "один к одному"**  
   Создай таблицы `clients` и `client_profiles`, где у каждого клиента может быть только один профиль. Укажи соответствующий внешний ключ и проверь, что связь работает.

2. **Реализуй "один ко многим": клиенты → заказы**  
   Создай таблицы `clients` и `orders`, где один клиент может иметь много заказов. Добавь по крайней мере двух клиентов и по несколько заказов каждому.

3. **Создай таблицы для связи "многие ко многим"**  
   Создай таблицы `courses`, `students` и промежуточную таблицу `student_courses`. Один студент может проходить несколько курсов, и один курс может иметь много студентов.

4. **Добавь данные с использованием lastrowid**  
   Вставь новую запись в таблицу `clients`, получи её `ID` с помощью `lastrowid`, и используй его, чтобы добавить заказ этого клиента в таблицу `orders`.

5. **Создай заказ с несколькими товарами**  
   Создай таблицы `orders`, `products` и `order_products`. Добавь один заказ и свяжи его с тремя различными товарами.

6. **Запрети повторные связи в промежуточной таблице**  
   Продемонстрируй, что нельзя добавить одну и ту же пару (`order_id, product_id`) в таблицу `order_products` дважды. Убедись, что используется составной первичный ключ.

7. **Сделай INNER JOIN через Python**  
   Выведи всех клиентов и их заказы с помощью `INNER JOIN`. Используй Python-код для выполнения запроса и распечатай результат.

8. **Используй LEFT JOIN через Python**  
   Сделай `LEFT JOIN`, чтобы вывести всех клиентов, даже если у них пока нет заказов. Выведи имя клиента и, если есть, название заказа.

9. **Добавь товары и посчитай общее число заказанных товаров**  
   Вставь несколько заказов и свяжи их с товарами. Напиши `SQL-запрос` через Python, который считает, `сколько раз каждый товар был заказан`.

10. **`Проект`: реализуй полную цепочку "пользователь → заказ → товары"**

    - Сделай полный скрипт:

      - Вставь нового пользователя,
      - Создай заказ,
      - Добавь новые товары,
      - Свяжи заказ с товарами. Убедись, что всё записано в базу и связи работают корректно.

# 🧠 Урок 5: Создание CRUD-приложения через Python + SQLite (ручной способ)

## 🔹 План урока

- Что такое `CRUD`
- База данных: `клиенты`, `заказы`, `товары`
- Создание `консольного меню`
- Реализация функций: `Create`, `Read`, `Update`, `Delete`
- Ввод данных и взаимодействие с таблицами
- Примеры кода
- Практическое задание

## 1. Что такое CRUD?

**`CRUD` — это аббревиатура, описывающая базовые операции с данными в приложениях**:

- `Create` — создание записей
- `Read` — чтение (просмотр)
- `Update` — обновление
- `Delete` — удаление

**Каждое приложение, работающее с базой данных, реализует эти четыре действия**.

## 2. Функция для подключения к базе данных

Для начала создадим отдельную функцию, которая будет подключаться к SQLite-базе данных и возвращать соединение и курсор.

Это поможет повторно использовать её в других функциях.

```python
import sqlite3

def get_connection():
    conn = sqlite3.connect("shop.db")  # создаёт файл shop.db, если его нет
    cursor = conn.cursor()
    return conn, cursor
```

## 3. Структура базы: клиенты, заказы, товары

Создадим 3 таблицы:

### Таблица `clients`:

- `id` INTEGER Уникальный идентификатор клиента (PRIMARY KEY, AUTOINCREMENT)
- `name` TEXT Имя клиента (NOT NULL)

### Таблица `products`

- `id` INTEGER Уникальный ID товара (PRIMARY KEY, AUTOINCREMENT)
- `title` TEXT Название товара (NOT NULL)

### Таблица orders

- `id` INTEGER Уникальный ID заказа (PRIMARY KEY, AUTOINCREMENT)
- `client_id` INTEGER ID клиента, внешний ключ на clients(id)
- `product_id` INTEGER ID товара, внешний ключ на products(id)
- `quantity` INTEGER Количество заказанного товара (NOT NULL)

#### **`orders` будет содержать связи между клиентами и продуктами.**

## 4. Код для создания таблиц

Теперь напишем функцию, которая создаёт все три таблицы.

Важно, чтобы порядок создания учитывал наличие внешних ключей (поэтому clients и products создаются до orders).

```python
def create_tables():
    conn, cursor = get_connection()

    try:
        # Включаем поддержку внешних ключей
        cursor.execute("PRAGMA foreign_keys = ON")

        # Таблица клиентов
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)

        # Таблица товаров
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
        """)

        # Таблица заказов
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
        """)

        conn.commit()
        print("Все таблицы успешно созданы.")

    except Exception as e:
        print("Ошибка при создании таблиц:", e)
        conn.rollback()

    finally:
        conn.close()
```

Каждый пункт меню вызывает определённую функцию, работающую с базой.

## 4. Использование функций

Разделим всё по функциям, каждая из которых будет выполнять одну конкретную задачу:

### 🔧 Общие замечания

**Все функции используют**:

- подключение к БД через `get_connection()`
- автоматическое закрытие соединения (`finally`)
- базовую обработку ошибок

### 1. ✅ Добавить клиента

```python
def add_client(name):
    conn, cursor = get_connection()
    try:
        cursor.execute("INSERT INTO clients (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Клиент '{name}' успешно добавлен.")
    except Exception as e:
        print("Ошибка при добавлении клиента:", e)
        conn.rollback()
    finally:
        conn.close()
```

### 2. ❌ Удалить клиента по ID

```python
def delete_client(client_id):
    conn, cursor = get_connection()
    try:
        cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
        conn.commit()
        print(f"Клиент с ID {client_id} удалён.")
    except Exception as e:
        print("Ошибка при удалении клиента:", e)
        conn.rollback()
    finally:
        conn.close()
```

### 3. ✏️ Изменить имя клиента

```python
def update_client(client_id, new_name):
    conn, cursor = get_connection()
    try:
        cursor.execute("UPDATE clients SET name = ? WHERE id = ?", (new_name, client_id))
        conn.commit()
        print(f"Имя клиента с ID {client_id} изменено на '{new_name}'.")
    except Exception as e:
        print("Ошибка при изменении клиента:", e)
        conn.rollback()
    finally:
        conn.close()
```

### 4. 📄 Показать всех клиентов

```python
def show_all_clients():
    conn, cursor = get_connection()
    try:
        cursor.execute("SELECT id, name FROM clients")
        clients = cursor.fetchall()
        print("Список клиентов:")
        for client in clients:
            print(f"ID: {client[0]}, Имя: {client[1]}")
    except Exception as e:
        print("Ошибка при выводе клиентов:", e)
    finally:
        conn.close()
```

### 5. ➕ Добавить заказ

```python
def add_order(client_id, product_id, quantity):
    conn, cursor = get_connection()
    try:
        cursor.execute("""
            INSERT INTO orders (client_id, product_id, quantity)
            VALUES (?, ?, ?)
        """, (client_id, product_id, quantity))
        conn.commit()
        print("Заказ успешно добавлен.")
    except Exception as e:
        print("Ошибка при добавлении заказа:", e)
        conn.rollback()
    finally:
        conn.close()
```

### 6. 🗑 Удалить заказ по ID

```python
def delete_order(order_id):
    conn, cursor = get_connection()
    try:
        cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
        conn.commit()
        print(f"Заказ с ID {order_id} удалён.")
    except Exception as e:
        print("Ошибка при удалении заказа:", e)
        conn.rollback()
    finally:
        conn.close()
```

### 7. 🔄 Изменить заказ (по ID)

```python
def update_order(order_id, client_id, product_id, quantity):
    conn, cursor = get_connection()
    try:
        cursor.execute("""
            UPDATE orders
            SET client_id = ?, product_id = ?, quantity = ?
            WHERE id = ?
        """, (client_id, product_id, quantity, order_id))
        conn.commit()
        print(f"Заказ с ID {order_id} обновлён.")
    except Exception as e:
        print("Ошибка при обновлении заказа:", e)
        conn.rollback()
    finally:
        conn.close()
```

### 8. 📋 Показать все заказы с JOIN

```python
def show_all_orders():
    conn, cursor = get_connection()
    try:
        cursor.execute("""
            SELECT
                orders.id,
                clients.name,
                products.title,
                orders.quantity
            FROM orders
            JOIN clients ON orders.client_id = clients.id
            JOIN products ON orders.product_id = products.id
        """)
        orders = cursor.fetchall()
        print("Список заказов:")
        for order in orders:
            print(f"ID заказа: {order[0]}, Клиент: {order[1]}, Товар: {order[2]}, Кол-во: {order[3]}")
    except Exception as e:
        print("Ошибка при выводе заказов:", e)
    finally:
        conn.close()
```

## 5. 📁 Структура файлов проекта **"Консольное CRUD-приложение"**

```graphql
crud_app/
│
├── database/
│   ├── __init__.py
│   ├── connection.py        # Подключение к БД
│   └── schema.py            # Создание таблиц
│
├── crud/
│   ├── __init__.py
│   ├── clients.py           # CRUD-функции для клиентов
│   └── orders.py            # CRUD-функции для заказов
│
├── main.py                  # Точка входа и меню
```

### 🔧 `database/connection.py`

```python
import sqlite3

def get_connection():
    conn = sqlite3.connect("app.db")
    return conn, conn.cursor()
```

### 🔧 `database/schema.py`

```python
from .connection import get_connection

def create_tables():
    conn, cursor = get_connection()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (client_id) REFERENCES clients(id),
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        """)
        conn.commit()
        print("Таблицы успешно созданы.")
    except Exception as e:
        print("Ошибка при создании таблиц:", e)
    finally:
        conn.close()
```

### 🔧 `crud/clients.py`

```python
from database.connection import get_connection

def add_client(name):
    conn, cursor = get_connection()
    try:
        cursor.execute("INSERT INTO clients (name) VALUES (?)", (name,))
        conn.commit()
        print("Клиент добавлен.")
    except Exception as e:
        print("Ошибка:", e)
        conn.rollback()
    finally:
        conn.close()

def delete_client(client_id):
    conn, cursor = get_connection()
    try:
        cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
        conn.commit()
        print("Клиент удалён.")
    except Exception as e:
        print("Ошибка:", e)
        conn.rollback()
    finally:
        conn.close()

def update_client(client_id, new_name):
    conn, cursor = get_connection()
    try:
        cursor.execute("UPDATE clients SET name = ? WHERE id = ?", (new_name, client_id))
        conn.commit()
        print("Клиент обновлён.")
    except Exception as e:
        print("Ошибка:", e)
        conn.rollback()
    finally:
        conn.close()

def show_all_clients():
    conn, cursor = get_connection()
    try:
        cursor.execute("SELECT * FROM clients")
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print("Ошибка:", e)
    finally:
        conn.close()
```

### 🔧 `crud/orders.py`

```python
from database.connection import get_connection

def add_order(client_id, product_id, quantity):
    conn, cursor = get_connection()
    try:
        cursor.execute("INSERT INTO orders (client_id, product_id, quantity) VALUES (?, ?, ?)",
                       (client_id, product_id, quantity))
        conn.commit()
        print("Заказ добавлен.")
    except Exception as e:
        print("Ошибка:", e)
        conn.rollback()
    finally:
        conn.close()

def delete_order(order_id):
    conn, cursor = get_connection()
    try:
        cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
        conn.commit()
        print("Заказ удалён.")
    except Exception as e:
        print("Ошибка:", e)
        conn.rollback()
    finally:
        conn.close()

def update_order(order_id, client_id, product_id, quantity):
    conn, cursor = get_connection()
    try:
        cursor.execute("""
            UPDATE orders
            SET client_id = ?, product_id = ?, quantity = ?
            WHERE id = ?
        """, (client_id, product_id, quantity, order_id))
        conn.commit()
        print("Заказ обновлён.")
    except Exception as e:
        print("Ошибка:", e)
        conn.rollback()
    finally:
        conn.close()

def show_all_orders():
    conn, cursor = get_connection()
    try:
        cursor.execute("""
            SELECT orders.id, clients.name, products.title, orders.quantity
            FROM orders
            JOIN clients ON orders.client_id = clients.id
            JOIN products ON orders.product_id = products.id
        """)
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print("Ошибка:", e)
    finally:
        conn.close()
```

### 🧠 `main.py`

```python
from database.schema import create_tables
from crud.clients import add_client, delete_client, update_client, show_all_clients
from crud.orders import add_order, delete_order, update_order, show_all_orders

def menu():
    print("\n=== Меню ===")
    print("1. Добавить клиента")
    print("2. Удалить клиента")
    print("3. Изменить клиента")
    print("4. Показать всех клиентов")
    print("5. Добавить заказ")
    print("6. Удалить заказ")
    print("7. Изменить заказ")
    print("8. Показать все заказы")
    print("9. Выход")

def main():
    create_tables()

    while True:
        menu()
        choice = input("Выберите пункт: ")

        if choice == "1":
            name = input("Имя клиента: ")
            add_client(name)
        elif choice == "2":
            client_id = int(input("ID клиента: "))
            delete_client(client_id)
        elif choice == "3":
            client_id = int(input("ID клиента: "))
            new_name = input("Новое имя: ")
            update_client(client_id, new_name)
        elif choice == "4":
            show_all_clients()
        elif choice == "5":
            client_id = int(input("ID клиента: "))
            product_id = int(input("ID товара: "))
            quantity = int(input("Количество: "))
            add_order(client_id, product_id, quantity)
        elif choice == "6":
            order_id = int(input("ID заказа: "))
            delete_order(order_id)
        elif choice == "7":
            order_id = int(input("ID заказа: "))
            client_id = int(input("Новый ID клиента: "))
            product_id = int(input("Новый ID товара: "))
            quantity = int(input("Новое количество: "))
            update_order(order_id, client_id, product_id, quantity)
        elif choice == "8":
            show_all_orders()
        elif choice == "9":
            print("Выход.")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
```

## 🛠 Практическая работа: **Реализация CRUD для таблицы products**

### 🎯 Цель задания:

Закрепить навыки работы с SQLite, модулями Python и CRUD-операциями. 

Вы научитесь создавать, читать, обновлять и удалять данные в таблице products, а также интегрировать эти функции в общее приложение с консольным интерфейсом.

### 📋 Условия:

В предыдущих заданиях у вас уже реализованы:

- Функция подключения к базе данных
- Создание таблиц `clients`, `orders`, `products`
- CRUD-функции для `clients` и `orders`
- Основной интерфейс в `main.py`

#### Теперь вы должны реализовать такую же логику для таблицы products.

### 📦 Структура проекта:

Ваш проект уже содержит следующую структуру:

```pgsql
crud_app/
├── database/
│   ├── connection.py
│   └── schema.py
│
├── crud/
│   ├── clients.py
│   ├── orders.py
│   └── products.py   ← создать этот файл
│
├── main.py
```

## ✅ Что нужно сделать:

## 1. Создайте модуль `crud/products.py`. В нем реализуйте следующие функции:

### 🔹 1.1. add_product(title)

- Задача: 
    - Добавить новый товар в таблицу `products`.
- Пояснение:
    - Вставить название товара в базу
    - Используйте параметризированный SQL-запрос

### 🔹 1.2. delete_product(product_id)

- Задача: 
    - Удалить товар по его ID
- Пояснение:
    - Удалите строку из таблицы products по ID
    - Добавьте проверку на наличие строки (по желанию)

### 🔹 1.3. update_product(product_id, new_title)

- Задача: 
    - Обновить название товара
- Пояснение:
    - Используйте SQL UPDATE
    - Передайте новый заголовок

### 🔹 1.4. show_all_products()

- Задача: 
    - Вывести список всех товаров
- Пояснение:
    - Используйте SQL SELECT
    - Выведите все строки таблицы products с ID и названием

### Импортируйте эти функции в main.py

Добавьте пункты в консольное меню:

```markdown
10. Добавить товар
11. Удалить товар
12. Изменить товар
13. Показать все товары
```

Реализуйте обработку этих пунктов, вызывая соответствующие функции из `crud/products.py`.

### 💡 Подсказки:

- Повторите структуру функций из `clients.py` и `orders.py`
- Используйте блоки `try-except-finally` для обработки ошибок
- Не забудьте закрыть соединение с БД после каждой операции
- В `main.py` добавьте импорты из `crud.products`

