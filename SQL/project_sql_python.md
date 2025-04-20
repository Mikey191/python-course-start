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
- ➕ Сравнение `SQLite` с остальными:
  - не требует сервера
  - весь файл БД — это один `.sqlite3`
  - идеальна для локальных проектов, прототипов и обучения

## 5. Особенности SQLite

- `Кроссплатформенность` (работает на Windows, macOS, Linux)
- `Малый вес` (несколько сотен КБ)
- `Не требует отдельного сервера`
- `Очень прост в использовании через Python`
- `Поддерживает большинство SQL-запросов`

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
- Создание таблицы users: подробный разбор полей
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

## 3. Создание таблицы users: подробный разбор полей

- Правый клик по базе → `Create a table`
- Назовите таблицу `users`
- Добавьте поля кликнув два раза по пустой строке:

  - `id`: `INTEGER` Уникальный идентификатор записи `PK` (Primary Key), `AI` (Auto Increment)
    - Заполните поле `Column name` именем `id`
    - Поставить галочку на `Primary Key`
    - Нажмите кнопку `Configure`
    - Выбирите `Autoincrement`
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

**Выполните все пункты в одном Python-скрипте**:

- Подключитесь к файлу базы данных `lesson3.sqlite3`
- Создайте таблицу `clients` со следующими полями:
  - `id (INTEGER, PK, AI)`
  - `name (TEXT)`
  - `email (TEXT)`
- Добавьте 3 клиента через `INSERT INTO ... VALUES (?, ?, ?)`
- Выведите список всех клиентов через `SELECT *`
- Обновите `email` одного клиента
- Удалите одного клиента
- Используя `fetchone()`, выведите первого клиента по алфавиту (сортировка по name)
- Оберните `UPDATE` и `DELETE` в `try/except` с `commit()` и `rollback()`
- Закройте соединение с базой

#
