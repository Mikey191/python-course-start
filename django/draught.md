# Python Django

# 1. Установка Django и создание проекта

## 1.1 Django, что это такое? Инструментальные средства

**Django ускоряет процесс создания приложений**, предоставляя множество встроенных инструментов: **системы управления пользователями**, **ORM для работы с базами данных**, **шаблонизатор**, **защиту от SQL-инъекций** и многое другое. Это делает его идеальным выбором для `бэкенд-разработчиков`.

### Инструменты для работы с Django

1. **Python**. Убедитесь, что на вашем компьютере установлен актуальный интерпретатор Python (рекомендуемая версия — Python 3.10 или новее). Загрузить его можно с официального сайта.

2. **Django**. Для установки используйте pip — пакетный менеджер Python. Команда для установки: `pip install django`. Убедитесь, что используется последняя стабильная версия. Проверить версию можно командой: `django-admin --version`

3. **Среда разработки (IDE)**. Для написания кода рекомендуется использовать PyCharm (версии Community или Professional). Это одна из самых популярных IDE для Python-разработки, особенно удобная для работы с Django. Скачать можно с сайта JetBrains.

4. **Инструменты для работы с базами данных**. `SQLite` (используется по умолчанию в Django). Для более крупных проектов можно использовать `PostgreSQL`, `MySQL` или другие реляционные базы данных. Рекомендуются клиенты, такие как `DBeaver` или `pgAdmin`, для управления базами данных.

5. **Управление файлами и каталогами**. Для `Windows` и `Linux` вы можете использовать такие инструменты, как `Far Manager` или `Total Commander`.

6. **Локальный сервер Django**. Django включает встроенный отладочный сервер, который позволяет разрабатывать и тестировать проекты на вашем компьютере. Для запуска используйте команду: `python manage.py runserver`. Сервер будет доступен по адресу `localhost:8000`. Это идеальный инструмент для начальной разработки и отладки.

## 1.2 Установка Django. Создание проекта

### **Установите Django**

```bash
pip install django
```

### **Создайте проект**

```bash
django-admin startproject myproject
```

Здесь `myproject` — **имя вашего проекта**.

### **Запуск тестового сервера**

Перейдите в папку проекта: `cd myproject`.

Запустите тестовый сервер:

```bash
python manage.py runserver
```

## 1.3 Модель MTV. Добавление первого приложения

Архитектурный паттерн `MTV` (`Model-Template-View`), обеспечивающий четкое разделение данных, их обработки и отображения.

1. **Маршрутизация запросов**
2. **Представления (`Views`)**
3. **Архитектура `MTV`**
   - **Модели (Model)**: определяет структуру данных и взаимодействует с базой.
   - **Шаблона (Template)**: определяет внешний вид страницы.
   - **Представления (View)**: обрабатывает логику запроса и объединяет модель с шаблоном.

### Добавление первого приложения

В Django сайт состоит из приложений. Каждое приложение представляет собой отдельный функциональный модуль.

**Например**:

- Приложение для отображения статей.
- Приложение для форума.
- Приложение для опросов.

### Создание нового приложения

```bash
python manage.py startapp women
```

- `startapp` — команда для создания приложения.
- `women` — имя приложения (выберите осмысленное название).

После выполнения команды в проекте появится папка women, содержащая файлы:

- `admin.py` — **настройка админ-панели**.
- `apps.py` — **конфигурация приложения**.
- `models.py` — **описание моделей базы данных**.
- `tests.py` — **тестовые сценарии**.
- `views.py` — **реализация представлений**.

### Регистрация приложения в проекте

Для работы приложения добавьте его в список `INSTALLED_APPS` в файле `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'women.apps.WomenConfig',
]
```

## 1.4 Маршрутизация и функции представления в Django

### Создание функции представления

Функция представления отвечает за обработку запросов и формирование ответов.

```python
# women/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница приложения women.")
```

- **`request`** — обязательный параметр, представляющий объект класса `HttpRequest`. Через него доступна информация о запросе, сессиях и куках.
- **Возвращаемое значение** — объект `HttpResponse`, формирующий заголовок ответа и его содержимое (в данном случае, строка).

### Связывание функции с маршрутом

Чтобы обработчик начал работать, нужно добавить маршрут в файл `urls.py`:

```python
# sitewomen/urls.py
from django.contrib import admin
from django.urls import path
from women.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', index),
]
```

- Первый параметр `path` — URL-суффикс (например, `'women/'`).
- Второй параметр — ссылка на функцию представления (в данном случае, `index`).
- Итоговый URL-адрес: `http://127.0.0.1:8000/women/`.

### Главная страница сайта

Для обработки запросов к главной странице (`/`) заменим маршрут `'women/'` на пустую строку:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cats/', views.categories),
]
```

Теперь функция `index` отвечает за главный маршрут: `http://127.0.0.1:8000/`.

### Независимость маршрутов приложения

1. Импортируем функцию `include`:

```python
# sitewomen/urls.py
from django.urls import path, include
```

2. Подключим маршруты приложения через `include`:

```python
# sitewomen/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),
]
```

3. Создадим файл `women/urls.py`:

```python
# women/urls.py
from django.urls import path
from women import views

urlpatterns = [
    path('', views.index),
    path('cats/', views.categories),
]
```

Теперь маршруты приложения независимы от основного файла `urls.py`.

- URL `http://127.0.0.1:8000/women/` — главная страница приложения.
- URL `http://127.0.0.1:8000/women/cats/` — статьи по категориям.

### Связь файлов

```
+--------------------+-------------------------------------------+
| Файл               | Роль                                      |
+--------------------+-------------------------------------------+
| `women/views.py`   | Определение функций представления         |
| `sitewomen/urls.py`| Главный файл маршрутов проекта            |
| `women/urls.py`    | Локальный файл маршрутов приложения       |
+--------------------+-------------------------------------------+
```

## 1.5 Отладка проекта Django в Pycharm

### Создание конфигурации в PyCharm

В меню PyCharm найдите и нажмите кнопку: `«Add Configurations…»` или `«Edit Configurations…»`.

В открывшемся окне нажмите кнопку `«+»` и выберите Python.

Заполните обязательные поля:

- `Name`: sitewomen (имя конфигурации, выберите по смыслу проекта).
- `Working directory`: укажите путь до корневой папки проекта, например: `D:\Python\Projects\django\sitewomen`(В этом поле вы также увидите текущую версию интерпретатора Python.).
- `Script path`: путь до файла manage.py вашего проекта, например: `D:\Python\Projects\django\sitewomen\manage.py.`
- `Parameters`: введите параметр runserver.

### Запуск проекта в режиме отладки

- Остановите работающий сервер (если он запущен через консоль или стандартным запуском). Это необходимо, так как порт (например, 8000) может быть занят другим процессом, и режим отладки не сможет использовать его.

- Переключитесь на созданную конфигурацию и нажмите Debug (значок насекомого).

## 1.6 Динамические URL. Пользовательские конвертеры

### Динамические URL с числовым параметром

Если необходимо передать параметр, например, идентификатор категории, создайте шаблон URL с числовым параметром. В `women/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),  # Числовой параметр
]
```

Затем в функции представления используйте этот параметр:

```python
from django.http import HttpResponse

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")
```

Теперь можно обращаться по адресам:

```
127.0.0.1:8000/cats/1/
127.0.0.1:8000/cats/2/
```

### Типы конвертеров в Django

- `str` – любая непустая строка (исключая `/`).
- `int` – положительное целое число, `включая 0`.
- `slug` – строка формата "слаг" (`латиница`, `цифры`, `-`, `_`).
- `uuid` – идентификатор формата `UUID`.
- `path` – любая непустая строка, включая `/`.

### Порядок маршрутов имеет значение

В случае смешанных типов конвертеров порядок важен. Например:

```python
urlpatterns = [
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
]
```

Если сначала указать slug, то он будет срабатывать всегда, так как число является частным случаем слага.

### Создание пользовательского конвертера

`Django` позволяет **регистрировать свои конвертеры для URL**. Например, создадим конвертер для четырехзначного года.

Создайте файл `converters.py` в приложении `women`:

```python
class FourDigitYearConverter:
    regex = "[0-9]{4}"  # Регулярное выражение для четырех цифр

    def to_python(self, value):
        return int(value)  # Преобразование в число

    def to_url(self, value):
        return f"{value:04d}"  # Преобразование в строку
```

В `urls.py` зарегистрируйте конвертер:

```python
from . import converters
from django.urls import register_converter

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('archive/<year4:year>/', views.archive),  # Использование пользовательского конвертера
]
```

В `views.py` реализовать функцию:

```python
def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
```

Теперь параметр `year` будет автоматически преобразован в целое число благодаря методу `to_python`. Убедитесь в этом, поставив точку останова в режиме отладки.

## 1.7 GET- и POST-запросы. Обработчики исключений запросов

### Структура GET-запросов

`GET-запросы` передают параметры через `URL-адрес`. Пример `URL` с параметрами:

```plaintext
http://127.0.0.1:8000/?name=Smith&category=books
```

**В этом URL**:

- Знак вопроса `?` обозначает начало параметров.
- Пары `ключ-значение`, такие как `name=Smith` и `category=books`, разделены амперсандом `&`.

`Параметры GET-запросов` используются для **передачи данных на сервер через адресную строку**.

### Извлечение параметров GET-запросов в Django

Для обработки параметров `GET-запросов` используется объект `request.GET`, который представляет собой словарь (`QueryDict`). Рассмотрим пример:

```python
from django.http import HttpResponse

def example_view(request):
    print(request.GET)  # Отображаем параметры в консоли
    return HttpResponse("<h1>Обработка GET-запросов</h1>")
```

Если выполнить запрос:

```plaintext
http://127.0.0.1:8000/?name=Smith&category=books
```

В консоли отобразится:

```plaintext
<QueryDict: {'name': ['Smith'], 'category': ['books']}>
```

### POST-запросы: Передача данных из форм

`POST-запросы` используются для **передачи данных из форм**. Данные доступны через объект `request.POST`.

**Пример**:

```python
def example_post_view(request):
    if request.POST:
        print(request.POST)  # Печатаем данные формы в консоли
    return HttpResponse("<h1>Обработка POST-запросов</h1>")
```

### Различие между `request.GET` и `request.POST` заключается в источнике данных:

- `GET` — параметры в `URL`.
- `POST` — **данные** формы, **переданные в теле запроса**.

### Обработка исключений запросов. Ошибка 404: Страница не найдена

При обращении к несуществующему пути сервер возвращает `ошибку 404`.

В режиме разработки (при `DEBUG = True`) в файле `settings.py` отображается отладочная информация.

Чтобы настроить поведение в боевом режиме (`DEBUG = False`), следует указать разрешенные хосты:

```python
# settings.py
ALLOWED_HOSTS = ['127.0.0.1']
```

Обработчик `404` можно переопределить в `urls.py`:

```python
# urls.py
handler404 = 'myapp.views.page_not_found'
```

Реализация функции `page_not_found`:

```python
from django.http import HttpResponseNotFound

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
```

Теперь сервер будет возвращать пользовательскую страницу `404`.

### Генерация исключений вручную

`Исключения 404` можно вызывать **вручную**.

**Пример**:

```python
from django.http import Http404

def archive(request, year):
    if year > 2025:
        raise Http404("Год превышает допустимый диапазон")
    return HttpResponse(f"<h1>Архив {year}</h1>")
```

При вызове исключения сервер автоматически перенаправит пользователя на обработчик `page_not_found`.

### Обработка других ошибок

Аналогично можно переопределить обработчики других ошибок:

- `handler500` — ошибка сервера.
- `handler403` — доступ запрещен.
- `handler400` — невозможно обработать запрос.

Пример для 500-й ошибки:

```python
# urls.py
handler500 = 'myapp.views.server_error'
```

```python
# views.py
from django.http import HttpResponseServerError

def server_error(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')
```

### Django QueryDict

`request.GET` и `request.POST` реализованы на основе класса `QueryDict`.

Этот объект позволяет работать с несколькими значениями одного ключа и предоставляет методы:

- `get(key)` — получение значения.
- `getlist(key)` — получение списка всех значений ключа.
- `dict()` — преобразование в словарь Python.

**Пример**:

```python
def example_view(request):
    name = request.GET.get('name', 'Неизвестно')
    categories = request.GET.getlist('category')
    print(f"Имя: {name}, Категории: {categories}")
    return HttpResponse("Обработка параметров запроса")
```

### Http404 и обработчики ошибок

Класс `Http404` используется для генерации исключения. Он интегрируется с обработчиком `404` и перенаправляет пользователя.

**Пример использования**:

```python
def custom_view(request):
    if some_condition:
        raise Http404("Элемент не найден")
    return HttpResponse("<h1>Успешный запрос</h1>")
```

## 1.8 Перенаправления (redirect). Функция reverse

Django предоставляет несколько способов для реализации перенаправлений:

- **Функция `redirect()`** – гибкий способ для выполнения редиректов.
- **Классы `HttpResponseRedirect` и `HttpResponsePermanentRedirect`** – для явного указания кода перенаправления.
- **Функция `reverse()`** – для вычисления URL-адресов на основе имен маршрутов.

### Перенаправления с помощью функции redirect()

#### **Пример 1: Перенаправление на главную страницу (файл `views.py`)**

```python
from django.shortcuts import redirect
from django.http import HttpResponse

def archive(request, year):
    if year > 2023:
        return redirect('/')  # Редирект на главную страницу
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
```

#### **Пример 2: Указание постоянного редиректа с кодом `301`**

```python
def archive(request, year):
    if year > 2023:
        return redirect('/', permanent=True)  # Постоянный редирект
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
```

#### **Пример 3: Редирект на представление вместо `URL`**

```python
from .views import index

def archive(request, year):
    if year > 2023:
        return redirect(index, permanent=True)  # Редирект на функцию index
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
```

### Имена маршрутов и параметр name в path

#### **Пример: Добавление имен маршрутов (файл `urls.py`)**

```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Имя маршрута "home"
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  # Имя маршрута "cats"
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name='archive'),  # Имя маршрута "archive"
]
```

**Использование имени**:

```python
def archive(request, year):
    if year > 2023:
        return redirect('home', permanent=True)  # Перенаправление на маршрут "home"
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
```

### Классы `HttpResponseRedirect` и `HttpResponsePermanentRedirect`

Django предоставляет два класса для выполнения редиректов:

- `HttpResponseRedirect` – для временного перенаправления (`код 302`).
- `HttpResponsePermanentRedirect` – для постоянного перенаправления (`код 301`).

---

#### Пример: Использование HttpResponseRedirect (файл `views.py`)

```python
from django.http import HttpResponse, HttpResponseRedirect

def archive(request, year):
    if year > 2023:
        return HttpResponseRedirect('/')  # Редирект на главную страницу
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
```

Функция `redirect()` в своей работе использует эти классы, но более гибкая в использовании.

### Функция `reverse()`

Функция `django.urls.reverse()` используется для `вычисления URL-адреса` маршрута на `основе его имени и переданных параметров`.

#### Пример: Вычисление URL маршрута (файл `views.py`) и его использование.

**Вычисление маршрута**:

```python
from django.urls import reverse
from django.http import HttpResponseRedirect

def archive(request, year):
    if year > 2023:
        url_redirect = reverse('cats', args=('music', ))  # Вычисление URL маршрута "cats" с параметром "music"
        return HttpResponseRedirect(url_redirect)  # Редирект на вычисленный URL
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
```

**Использование вычисленного URL**:

```python
def archive(request, year):
    if year > 2023:
        url_redirect = reverse('cats', args=('music', ))  # Вычисление URL маршрута
        return redirect(url_redirect)  # Редирект на вычисленный URL
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
```

**Результат**:

Функция `reverse('cats', args=('music', ))` вычисляет `URL`:

```ruby
http://127.0.0.1:8000/cats/music/
```

# 2. Шаблоны

## 2.1 Введение в шаблоны Django: функции `render()` и `render_to_string()`

### Где хранить шаблоны

```
project_root/
│── women/
│   ├── templates/
│   │   ├── women/
│   │   │   ├── index.html
│   │   │   ├── about.html
```

Чтобы избежать конфликтов имен файлов, принято создавать подкаталог с именем самого приложения.

### Функция `render_to_string()`

Функция `render_to_string()` загружает шаблон, обрабатывает его и возвращает HTML-код в виде строки.

**Создадим файл `templates/women/index.html`**:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Главная страница</title>
  </head>
  <body>
    <h1>Главная страница</h1>
  </body>
</html>
```

**Используем функцию `render_to_string()`**:

```python
from django.template.loader import render_to_string

def index(request):
    t = render_to_string('women/index.html')
    return HttpResponse(t)
```

### Функция `render()`

Функция `render()` объединяет загрузку шаблона и формирование HTTP-ответа в одну строку кода:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'women/index.html')
```

Более краткая альтернатива использования функции `render_to_string`.

### Настройки шаблонизатора Django

Django использует встроенный шаблонизатор, указанный в файле `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Здесь важны два параметра:

- `DIRS` – позволяет указать нестандартные пути к шаблонам.
- `APP_DIRS` – если `True`, Django ищет шаблоны внутри приложений.

Если `APP_DIRS=False`, а `DIRS` пуст, при загрузке страницы появится ошибка `TemplateDoesNotExist`.

## 2.2 Передача данных (переменных) в шаблоны Django

Шаблоны в Django позволяют динамически изменять содержимое веб-страниц, подставляя в них значения переменных, полученных из представлений.

1. В файле шаблона (`index.html` или `about.html`) указываются переменные в двойных фигурных скобках `{{ ... }}`.
2. В представлении формируется словарь с данными и передается в шаблон.
3. Django автоматически подставляет значения переменных в соответствующие места в шаблоне.

### Передача одной переменной в шаблон

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    <h1>{{ title }}</h1>
  </body>
</html>
```

Теперь в представлении передадим эту переменную:

```python
def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'women/index.html', data)
```

При загрузке страницы вместо `{{ title }}` подставится строка "Главная страница".

### Обращение к коллекциям в шаблонах

Передавать переменные в шаблон нужно явно.

```python
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
    }
    return render(request, 'women/index.html', context=data)
```

Шаблон `index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    <p>{{ menu }}</p>
    <p>{{ float }}</p>
    <p>{{ lst }}</p>
    <p>{{ set }}</p>
    <p>{{ dict }}</p>
    <p>{{ obj }}</p>

    <h1>{{ title }}</h1>
  </body>
</html>
```

### Обращение к атрибутам объектов

Ключи словарей и атрибуты классов можно выводить через точку:

```html
<p>{{ dict.key_1 }}</p>
<p>{{ obj.a }}</p>
```

## 2.3 Стандартные шаблонные фильтры в Django

Фильтры - это удобный инструмент, позволяющий изменять отображение данных в шаблонах без необходимости изменять логику Python-кода.

### Основные принципы работы с фильтрами

Фильтры в Django применяются в шаблонах с использованием **вертикальной черты (`|`)**. Если фильтр принимает аргументы, они передаются через двоеточие `:`.

```html
<p>{{ number|add:"10" }}</p>
```

### Основные стандартные фильтры

- `add` – Прибавление чисел.
- `capfirst` – Заглавная буква в начале строки.
- `upper` и `lower` – Преобразование регистра.
- `cut` – Удаление фрагмента строки.
- `default` – Значение по умолчанию.
- `divisibleby` – Проверка делимости
- `first` и `last` – Первый и последний элементы списка
- `join` – Объединение списка в строку
- `length` – Длина списка
- `slugify` – Создание slug

### Использование фильтров в Python

Фильтры можно применять не только в шаблонах, но и в коде Python. Они доступны в модуле `django.template.defaultfilters`.

Пример использования `slugify` в Python:

```python
from django.template.defaultfilters import slugify

data = {
    'title': 'Главная страница',
    'url': slugify("The main page"),
}

print(data['url'])  # the-main-page
```

В шаблоне можно вывести `url` так:

```html
<p>{{ url }}</p>
```

## 2.4 Теги шаблонов в Django: if и for

### Использование тега `for`

**Допустим, у нас есть список данных о известных женщинах**:

```python
# Имитация базы данных
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]
```

**Создадим представление `index`, которое передаст эти данные в шаблон**:

```python
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': ['Главная', 'О сайте', 'Контакты'],
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)
```

**Теперь выведем этот список в шаблоне `index.html`**:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    <p>{{ menu|join:" | " }}</p>
    <h1>{{ title }}</h1>

    <ul>
      {% for p in posts %}
      <li>
        <h2>{{ p.title }}</h2>
        <p>{{ p.content }}</p>
        <hr />
      </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

### Добавление условия `if`

В текущем шаблоне выводятся все статьи, включая те, у которых `is_published` равно `False`. Давайте исправим это с помощью тега `if`:

```html
<ul>
  {% for p in posts %} {% if p.is_published %}
  <li>
    <h2>{{ p.title }}</h2>
    <p>{{ p.content }}</p>
    {% if not forloop.last %}
    <hr />
    {% endif %}
  </li>
  {% endif %} {% endfor %}
</ul>
```

- Проверяем `p.is_published`, чтобы скрыть неопубликованные статьи.
- Используем `{% if not forloop.last %}` для исключения последней горизонтальной черты (`<hr>`).

### Использование переменных `forloop`

- `forloop.counter` – номер текущей итерации (с 1);
- `forloop.counter0` – номер текущей итерации (с 0);
- `forloop.first` – `True` на первой итерации;
- `forloop.last` – `True` на последней итерации.

```html
<ul>
  {% for p in posts %} {% if p.is_published %}
  <li>
    <h2>{{ forloop.counter }}. {{ p.title }}</h2>
    <p>{{ p.content }}</p>
  </li>
  {% endif %} {% endfor %}
</ul>
```

## 2.5 Шаблонный тег url в Django

Шаблонный тег `url` позволяет динамически формировать ссылки на основе имен маршрутов, заданных в `urls.py`.

### Формирование ссылок в HTML

В HTML ссылки создаются с помощью тега `<a>`:

```html
<a href="URL-адрес страницы">Название ссылки</a>
```

### Использование шаблонного тега `url`

В Django можно динамически формировать URL с помощью имен маршрутов, заданных в файле `urls.py`.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),
]
```

Создание представления `show_post`. В файле `views.py` добавим обработчик маршрута:

```python
from django.http import HttpResponse

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
```

Используем тег `url` для динамического формирования ссылок в шаблоне `index.html`:

```html
<p><a href="{% url 'post' p.id %}">Читать пост</a></p>
```

Таким образом, любое изменение маршрутов в `urls.py` автоматически отразится в шаблонах без необходимости их редактирования.

### Формирование главного меню

Добавим маршруты в `urls.py`:

```python
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
]
```

Добавим меню в `views.py`:

```python
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]
```

Дополнительно создадим представления-заглушки:

```python
def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")
```

Теперь выведем главное меню в шаблоне `index.html`:

```html
<ul>
  <li><a href="{% url 'home' %}">Главная</a></li>
  {% for m in menu %} {% if not forloop.last %}
  <li>{% else %}</li>
  <li class="last">
    {% endif %}
    <a href="{% url m.url_name %}">{{ m.title }}</a>
  </li>
  {% endfor %}
</ul>
```

## 2.6 Наследование шаблонов (extends). Тег include

Дублирование кода в шаблонах ведет к усложнению поддержки и снижению масштабируемости проекта.

Если необходимо изменить меню или структуру страницы, придется вносить исправления сразу в нескольких файлах, что увеличивает вероятность ошибок.

Допустим имеется два файла `index.html` и `about.html`. В них присутствует дублирование кода: `заголовок`, `меню` и `базовая структура` **повторяются в каждом файле**. Это нарушает принцип **`DRY` (Don't Repeat Yourself)**.

- `index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    <ul>
      <li><a href="{% url 'home' %}">Главная</a></li>
      {% for m in menu %} {% if not forloop.last %}
      <li>{% else %}</li>
      <li class="last">
        {% endif %}
        <a href="{% url m.url_name %}">{{ m.title }}</a>
      </li>
      {% endfor %}
    </ul>
    <h1>{{ title }}</h1>
    <ul>
      {% for post in posts %}
      <li>
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
      </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

- `about.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    <ul>
      <li><a href="{% url 'home' %}">Главная</a></li>
      {% for m in menu %} {% if not forloop.last %}
      <li>{% else %}</li>
      <li class="last">
        {% endif %}
        <a href="{% url m.url_name %}">{{ m.title }}</a>
      </li>
      {% endfor %}
    </ul>
    <h1>{{ title }}</h1>
  </body>
</html>
```

### Создание базового шаблона

Создадим директорию `templates` в корне проекта `sitewomen` и добавим в нее файл `base.html` (`sitewomen/templates/base.html`):

#### `base.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    <ul>
      <li><a href="{% url 'home' %}">Главная</a></li>
      {% for m in menu %} {% if not forloop.last %}
      <li>{% else %}</li>
      <li class="last">
        {% endif %}
        <a href="{% url m.url_name %}">{{ m.title }}</a>
      </li>
      {% endfor %}
    </ul>
    {% block content %}{% endblock %}
  </body>
</html>
```

Строка `{% block content %}{% endblock %}` определяет блок контента, который может быть **переопределён в дочерних шаблонах**. **Это ключевая часть механизма наследования шаблонов в Django**.

**Функционал наследования** шаблонов в Django **поддерживается** благодаря тегу `{% block %}`, который используется для определения блоков контента, доступных для переопределения в дочерних шаблонах.

Однако **имя блока**, например `content`, **является произвольным** и **задаётся разработчиком**. То есть, не обязательно использовать именно `block content`, вы можете назвать блок любым именем, например, `block main`, `block body`, или даже `block my_custom_block`.

#### Новый `index.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>{{ title }}</h1>
<ul>
  {% for post in posts %}
  <li>
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

#### Новый `about.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>{{ title }}</h1>
<p>Этот сайт содержит информацию о различных известных женщинах.</p>
{% endblock %}
```

### Добавление каталога шаблонов в `settings.py`

Чтобы Django мог находить `base.html`, нужно прописать путь в `settings.py`. Это изменение актуально только для глобальных шаблонов, а не для тех, что находятся в папках приложения:

Чтобы Django мог находить `base.html`, нужно прописать путь в `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    },
]
```

### Включение фрагментов с помощью `{% include %}`

Предположим, мы хотим повторно использовать навигационное меню на нескольких страницах. Вместо дублирования кода создадим отдельный файл `nav.html`.

1. Создадим файл `women/templates/women/includes/nav.html`

```html
<nav>
  <a href="#">Актрисы</a> | <a href="#">Певицы</a> |
  <a href="#">Спортсменки</a>
</nav>
```

2. Подключим его в `index.html`

```html
{% extends 'base.html' %} {% block content %} {% include
'women/includes/nav.html' %}
<h1>{{ title }}</h1>
<ul>
  {% for post in posts %}
  <li>
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
  </li>
  {% endfor %}
</ul>
{% include 'women/includes/nav.html' %} {% endblock %}
```

### Особенности `{% include %}`

1. **Доступ к переменным**: Подключенный шаблон имеет доступ к переменным основного шаблона.
2. **Запрет передачи данных**: Если нужно запретить передачу данных, используем `only`:
   ```html
   {% include 'women/includes/nav.html' only %}
   ```
   Например, если в `base.html` есть переменная `menu`, а в `nav.html` она не используется, то `only` предотвратит её передачу и уменьшит потенциальные конфликты.
3. **Передача отдельных параметров**: Можно передавать параметры через `with`:
   ```html
   {% include 'women/includes/nav.html' with title='Заголовок' %}
   ```

## 2.7 Подключение статических файлов в Django

Корректное подключение статических файлов позволяет:

- Улучшить внешний вид страниц с помощью CSS.
- Добавить динамическое поведение с помощью JavaScript.
- Использовать изображения и другие медиафайлы.

Однако, есть нюансы в зависимости от режима работы Django:

- **Режим отладки (DEBUG=True)** – Django автоматически ищет файлы в папках `static` установленных приложений.
- **Режим эксплуатации (DEBUG=False)** – Статические файлы должны находиться в общей папке проекта.

### Настройка статических файлов в Django

Для работы со статическими файлами Django использует три ключевых параметра в `settings.py`:

```python
STATIC_URL = '/static/'  # URL-префикс для статических файлов

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Папка для сбора статических файлов (используется при collectstatic)

STATICFILES_DIRS = [
    BASE_DIR / 'static'  # Дополнительные пути для поиска статических файлов
]
```

Кроме того, в `INSTALLED_APPS` обязательно должно присутствовать приложение `django.contrib.staticfiles`:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    ...
]
```

Если его нет, статические файлы работать не будут.

### Организация структуры статических файлов

```
women/
│── static/
│   ├── women/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │   │   ├── scripts.js
│   │   ├── images/
│   │   │   ├── logo.png
```

### Подключение статических файлов в шаблонах

Для использования статических файлов в шаблоне необходимо сначала загрузить тег `static`:

```django
{% load static %}
```

После этого можно подключать файлы:

```django
<link rel="stylesheet" type="text/css" href="{% static 'women/css/styles.css' %}">
<script src="{% static 'women/js/scripts.js' %}"></script>
<img src="{% static 'women/images/logo.png' %}" alt="Logo">
```

При рендеринге страницы Django автоматически подставит корректные пути, например:

```html
<link rel="stylesheet" type="text/css" href="/static/women/css/styles.css" />
```

### Сбор статических файлов для продакшена

При развертывании на сервере все статические файлы должны быть собраны в одну папку. Для этого используется команда:

```sh
python manage.py collectstatic
```

Она копирует файлы из `static` всех приложений в `STATIC_ROOT`. На сервере веб-сервер (например, Nginx) будет обслуживать эти файлы напрямую.

### Работа в режиме DEBUG=False

При отключенном отладочном режиме (`DEBUG=False`) Django не раздает статические файлы по умолчанию. Для локального тестирования можно использовать команду:

```sh
python manage.py runserver --insecure
```

Однако, в боевом режиме веб-сервер (например, Nginx или Apache) должен быть настроен на раздачу этих файлов из `STATIC_ROOT`.

## 2.8 Пользовательские теги шаблонов. Декораторы `simple_tag` и `inclusion_tag`

Django позволяет определять два типа пользовательских тегов:

- `simple_tag` — простые теги, возвращающие данные.
- `inclusion_tag` — включающие теги, рендерящие отдельные шаблоны.

### Создание `simple_tag`

`simple_tag` позволяет выполнять операции и возвращать данные непосредственно в шаблон.

#### Пошаговая реализация:

- В файле `women/views.py` определяем коллекцию `cats_db`:
  ```python
  cats_db = [
      {'id': 1, 'name': 'Актрисы'},
      {'id': 2, 'name': 'Певицы'},
      {'id': 3, 'name': 'Спортсменки'},
  ]
  ```
- Создаем каталог `templatetags` в приложении `women`.
- Добавляем в этот каталог файл `__init__.py`, чтобы сделать его пакетом.
- Создаем новый файл `women_tags.py`. Импортируем нужные модули, определяем функцию, которая будет возвращать список категорий:

  ```python
  from django import template
  import women.views as views

  register = template.Library()

  @register.simple_tag()
  def get_categories():
      return views.cats_db
  ```

- В `base.html` загружаем теги:
  ```django
  {% load women_tags %}
  ```
- Используем тег в шаблоне:
  ```django
  {% get_categories as categories %}
  <ul>
      {% for cat in categories %}
          <li><a href="#">{{ cat.name }}</a></li>
      {% endfor %}
  </ul>
  ```

#### Тег можно переименовать, задав имя в декораторе:

```python
@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db
```

Использование переименованного пользовательского тега:

```django
{% getcats as categories %}
<ul>
    {% for cat in categories %}
        <li><a href="#">{{ cat.name }}</a></li>
    {% endfor %}
</ul>
```

### Создание `inclusion_tag`

`inclusion_tag` позволяет возвращать отрендеренный шаблон.

- В `women_tags.py` добавляем:
  ```python
  @register.inclusion_tag('women/list_categories.html')
  def show_categories():
      return {"cats": views.cats_db}
  ```
- Создаем шаблон `women/list_categories.html`:

  ```django
  {% for cat in cats %}
      <li><a href="{% url 'category' cat.id %}">{{ cat.name }}</a></li>
  {% endfor %}
  ```

- Используем тег в `base.html`:

  ```django
  {% show_categories %}
  ```

### Передача параметров в теги

- Модифицируем функцию `show_categories`:

  ```python
  @register.inclusion_tag('women/list_categories.html')
  def show_categories(cat_selected=0):
      return {"cats": views.cats_db, "cat_selected": cat_selected}
  ```

- В `list_categories.html` добавляем выделение активной категории:

  ```django
  {% for cat in cats %}
      {% if cat.id == cat_selected %}
          <li class="selected">{{ cat.name }}</li>
      {% else %}
          <li><a href="{% url 'category' cat.id %}">{{ cat.name }}</a></li>
      {% endif %}
  {% endfor %}
  ```

- Вызываем тег с параметром в `base.html`:

  ```django
  {% show_categories cat_selected %}
  ```

- Передаем `cat_selected` в контекст представлений:

  ```python
  def index(request):
      return render(request, 'women/index.html', {"cat_selected": 0})

  def show_category(request, cat_id):
      return render(request, 'women/index.html', {"cat_selected": cat_id})
  ```

# 3. Введение в ORM и модели

## 3.1 Что такое БД, SQL и ORM. Создание первой модели

Django поддерживает работу со следующими СУБД:

- PostgreSQL
- MariaDB
- MySQL
- Oracle
- SQLite

### ORM в Django

`ORM (Object-Relational Mapping)` в Django позволяет абстрагироваться от SQL и работать с базой данных через классы и объекты Python.

Он обеспечивает универсальность кода, позволяя изменять БД без замены логики.

### Настройка БД в Django

В Django база данных настраивается в `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Создание первой модели

В `models.py` опишем модель:

```python
from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
```

### Описание полей

- `id` (создается автоматически)
- `title` - строковое поле с ограничением в 255 символов
- `content` - текстовое поле
- `time_create` - время создания
- `time_update` - время обновления
- `is_published` - флаг публикации

### Типы полей в модели Django ORM:

#### 1. Числовые поля

- `IntegerField()` – целое число (от -2147483648 до 2147483647).
- `PositiveIntegerField()` – положительное целое число.
- `BigIntegerField()` – большое целое число (от -9223372036854775808 до 9223372036854775807).
- `FloatField()` – число с плавающей точкой.
- `DecimalField(max_digits=10, decimal_places=2)` – десятичное число с точной арифметикой.

#### 2. Поля для дат и времени

- `DateField(auto_now_add=True)` – поле даты без времени.
- `TimeField(auto_now=True)` – поле времени без даты.

#### 3. Логические и булевые поля

- `NullBooleanField()` (устарело, вместо него `BooleanField(null=True)`)

#### 4. Поля для связи между моделями

- `ForeignKey(Model, on_delete=models.CASCADE)` – связь "один ко многим".
- `OneToOneField(Model, on_delete=models.CASCADE)` – связь "один к одному".
- `ManyToManyField(Model)` – связь "многие ко многим".

#### 5. Поля для файлов и изображений

- `FileField(upload_to='uploads/')` – поле для загрузки файлов.
- `ImageField(upload_to='images/')` – поле для загрузки изображений.

#### 6. JSON-поле

- `JSONField()` – поле для хранения JSON-данных.

#### 7. Уникальные и специальные поля

- `SlugField(unique=True)` – поле для ЧПУ URL (например, post-title).
- `UUIDField(default=uuid.uuid4, unique=True)` – поле для уникального идентификатора.
- `EmailField()` – поле для хранения email-адреса.
- `URLField()` – поле для хранения URL.

### Какой тип выбрать?

- **Если нужно хранить короткий текст** – `CharField(max_length=...)`.
- **Если длинный текст** – `TextField()`.
- **Если дата/время** – `DateTimeField()`, `DateField()`, `TimeField()`.
- **Если булевый флаг** – `BooleanField()`.
- **Если число** – `IntegerField()`, `FloatField()`, `DecimalField()`.
- **Если изображение** – `ImageField()`.
- **Если отношения между моделями** – `ForeignKey`, `OneToOneField`, `ManyToManyField()`.

**Полный список полей можно найти в документации**

## 3.2 Создание и запуск файлов миграций в Django

Механизм миграций позволяет автоматически формировать и изменять структуру базы данных с помощью специальных файлов миграций.

Миграция — это специальный Python-файл (модуль), который содержит инструкции на уровне ORM-интерфейса для создания или изменения структуры базы данных.

Django использует миграции как систему управления версиями схемы БД, позволяя:

- Создавать новые таблицы
- Изменять уже существующие таблицы (добавление/удаление столбцов, изменение их свойств)
- Управлять связями между таблицами
- Откатывать изменения к предыдущей версии

Миграции хранятся в папке `migrations` внутри каждого приложения Django и отслеживают изменения в моделях с момента последнего выполнения миграции.

### Генерация файла миграции

Открываем терминал и из корневого каталога проекта выполняем команду:

```bash
python manage.py makemigrations
```

После выполнения этой команды Django создаст новый файл миграции внутри каталога `migrations` нашего приложения (`women`). **Команда `makemigrations` **обязательно** выполняется каждый раз после изменения моделей. В противном случае изменения не будут применены в БД**.

```python
# women/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
```

### Просмотр SQL-кода миграции

```bash
python manage.py sqlmigrate women 0001
```

Где `women` — название приложения, а `0001` — номер миграции (без `_initial.py`).

Пример вывода SQL-запроса:

```sql
CREATE TABLE "women_women" (
    "id" bigint NOT NULL PRIMARY KEY,
    "title" varchar(255) NOT NULL,
    "content" text NOT NULL,
    "time_create" datetime NOT NULL,
    "time_update" datetime NOT NULL,
    "is_published" bool NOT NULL DEFAULT true
);
```

### Применение миграций к базе данных

```bash
python manage.py migrate
```

При первом запуске Django применит **все** необходимые миграции, включая те, которые относятся к стандартным приложениям (`auth`, `admin`, `sessions` и т. д.).

**Пример таблицы в БД**:

```
| id | title      | content        | time_create      | time_update      | is_published |
|----|-------     |---------       |-------------     |-------------     |------------- |
| 1  | "Статья 1" | "Текст статьи" | 2024-01-01 10:00 | 2024-01-01 10:00 | True         |
```

### Удаление и откат миграций

```bash
python manage.py migrate women 0000
```

Где `0000` означает удаление всех миграций и возврат к начальному состоянию.

Если необходимо удалить **конкретную** миграцию, сначала удаляем файл из `migrations`, затем выполняем:

```bash
python manage.py migrate women имя_предыдущей_миграции
```

### Схема файлов и взаимодействий

1. **Модель**: `women/models.py`

   ```python
   from django.db import models

   class Women(models.Model):
       title = models.CharField(max_length=255)
       content = models.TextField(blank=True)
       time_create = models.DateTimeField(auto_now_add=True)
       time_update = models.DateTimeField(auto_now=True)
       is_published = models.BooleanField(default=True)
   ```

2. **Генерация миграции**:

   ```bash
   python manage.py makemigrations
   ```

   - Создает `women/migrations/0001_initial.py`

3. **Просмотр SQL-запроса**:

   ```bash
   python manage.py sqlmigrate women 0001
   ```

4. **Применение миграции**:

   ```bash
   python manage.py migrate
   ```

   - Изменения фиксируются в БД.

5. **Откат миграции**:
   ```bash
   python manage.py migrate women 0000
   ```

## 3.3 Понятие CRUD. Добавление записей в таблицу БД. Модуль django-extensions

Базовые операции для работы с таблицей:

- **Create** – создание;
- **Read** – чтение;
- **Update** – обновление;
- **Delete** – удаление.

### Добавление записей в таблицу с помощью Django ORM

- **Открытие Django shell**:
  ```bash
  python manage.py shell
  ```
- **Импорт модели**:
  ```python
  from women.models import Women
  ```
- **Создание объекта модели**:
  ```python
  w1 = Women(title='Анджелина Джоли', content='Биография Анджелины Джоли')
  ```
- **Сохранение объекта в БД**:
  ```python
  w1.save()
  ```
- Альтернативный способ создания записей
  ```python
  w2 = Women()
  w2.title = 'Энн Хэтэуэй'
  w2.content = 'Биография Энн Хэтэуэй'
  w2.save()
  ```

### Просмотр SQL-запросов

Django позволяет просматривать выполняемые SQL-запросы:

```python
from django.db import connection
print(connection.queries)
```

Чтобы создать новую запись и сразу выполнить SQL-запрос, можно использовать `create()`:

```python
Women.objects.create(title='Джулия Робертс', content='Биография Джулии Робертс')
```

### Установка `ipython` для улучшенной консоли

```bash
pip install ipython
```

Запускаем Django shell с улучшенными возможностями:

```bash
python manage.py shell
```

### Установка django-extensions

```bash
pip install django-extensions
```

Добавим его в `INSTALLED_APPS` в `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_extensions',
]
```

После установки доступна расширенная консоль `shell_plus`, которая автоматически импортирует все модели и показывает SQL-запросы:

```bash
python manage.py shell_plus --print-sql
```

```python
a = Women(title="Екатерина Гусева", content="Биография Екатерины Гусевой")
a.save()
```

**Результат**:

```sql
INSERT INTO women_women (title, content, time_create, time_update, is_published) VALUES ('Екатерина Гусева', 'Биография Екатерины Гусевой', '2025-01-24 12:00:00', '2025-01-24 12:00:00', 1);
```

## 3.4 Методы выбора записей из таблиц. Fields lookups

### Менеджер записей `objects`

Для работы будем использовать Django shell_plus, который позволяет автоматически импортировать модели.

```bash
python manage.py shell_plus --print-sql
```

Каждая модель Django содержит специальный объект `objects`, который является экземпляром `Manager`. Этот объект предоставляет методы для работы с базой данных.

```python
Women.objects
```

С помощью `objects` можно выполнять различные операции с записями, такие как создание, выборка, обновление и удаление данных.

### Создание записей

Метод `create()`, который автоматически сохраняет данные в базе:

```python
w = Women.objects.create(title='Ума Турман', content='Биография Ума Турман')
w.pk  # Получим ID записи, например, 5
```

### Выборка всех записей. Метод `all()`

#### Получить все записи можно с помощью метода `all()`:

```python
Women.objects.all()
```

Вывод:

```bash
<QuerySet [<Women: Women object (1)>, <Women: Women object (2)>, ...]>
```

#### Получение одной записи по индексу:

```python
w = Women.objects.all()[0]
print(w.title, w.content)
```

#### Получение нескольких записей с помощью среза:

```python
ws = Women.objects.all()[:3]
print(ws)
```

### Фильтрация записей. Метод `filter()`

Метод `filter()` позволяет выбирать записи по заданному критерию:

```python
Women.objects.filter(title='Энн Хэтэуэй')
```

SQL-запрос, который формируется:

```sql
SELECT * FROM women_women WHERE title = 'Энн Хэтэуэй';
```

Если совпадений нет, то возвращается пустой `QuerySet`

### lookup в Django.

`Lookup` — это способ фильтрации данных в запросах к базе данных через ORM (Object-Relational Mapping). Они позволяют **задавать условия для полей модели**, например, проверять точное совпадение, частичное совпадение, диапазоны значений и т.д.

`lookup` всегда применяется к полю модели, чтобы уточнить критерии фильтрации.

Для этого используется синтаксис `<имя_поля>__<lookup>`.

Двойное подчеркивание (`__`) соединяет имя поля и название lookup'а.

#### Пример lookup:

```python
Book.objects.filter(title__exact="Django Unchained")
```

**Здесь**:

- `title` — это имя поля модели Book.
- `exact` — это lookup, который проверяет точное совпадение значения.

### Некоторые распространенные lookup-выражения:

#### Выборка записей с `id >= 2`:

```python
Women.objects.filter(pk__gte=2)
```

#### Выборка по части строки с `contains`:

```python
Women.objects.filter(title__contains='ли')
```

#### Если нужен поиск без учета регистра:

```python
Women.objects.filter(title__icontains='ЛИ')
```

Но SQLite не поддерживает `icontains` для кириллических символов.

#### Выборка по нескольким значениям (`in`):

```python
Women.objects.filter(pk__in=[2, 5, 11, 12])
```

#### Объединение условий (`AND`):

```python
Women.objects.filter(pk__in=[2, 5, 11, 12], is_published=1)
```

### Исключение записей. Метод `exclude()`

Метод `exclude()` выбирает записи, которые **не** соответствуют указанному условию:

```python
Women.objects.exclude(pk=2)
```

### Выборка одной записи. Метод `get()`

Метод `get()` выбирает **только одну** запись:

```python
Women.objects.get(pk=2)
```

Если записей больше одной или не найдено — возникает ошибка:

```python
Women.objects.get(pk__gte=2)  # Ошибка, если записей несколько
```

## 3.5 Сортировка, изменение и удаление записей в Django ORM

### Сортировка записей

Метод `order_by()` используется для сортировки записей по указанному полю:

```python
Women.objects.all().order_by('title')
```

Можно записать этот же запрос так:

```python
Women.objects.order_by('title')
```

Этот запрос создаст SQL-запрос с ключевым словом `ORDER BY`, выполняя сортировку по возрастанию (ASC).

### Сортировка с фильтрацией

Можно комбинировать `order_by()` с `filter()`:

```python
Women.objects.filter(pk__lte=4).order_by('title')
```

Этот запрос сначала отбирает записи, у которых `id` меньше или равен 4, а затем сортирует их по `title`.

### Сортировка по убыванию

Чтобы отсортировать записи по убыванию, добавляем `-` перед названием поля:

```python
Women.objects.order_by('-time_update')
```

### Задание сортировки по умолчанию (Meta)

В модели можно задать сортировку по умолчанию через класс `Meta`:

```python
class Women(models.Model):
    ...
    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def __str__(self):
        return self.title
```

Теперь запрос `Women.objects.all()` автоматически вернёт записи в порядке убывания `time_create`.

### Изменение записей

Чтобы изменить запись, сначала получаем объект, затем меняем его поля и сохраняем:

```python
wu = Women.objects.get(pk=2)
wu.title = 'Марго Робби'
wu.content = 'Биография Марго Робби'
wu.save()
```

SQL-запрос, выполняемый в базе данных:

```sql
UPDATE "women_women" SET "title" = 'Марго Робби', "content" = 'Биография Марго Робби' WHERE "id" = 2;
```

### Массовое обновление записей

Если нужно обновить сразу несколько записей, используем `update()`:

```python
Women.objects.update(is_published=0)
```

Этот запрос изменит значение `is_published` для всех записей.

### Изменение записей с фильтрацией

```python
Women.objects.filter(pk__lte=4).update(is_published=1)
```

> **Важно:** Метод `update()` нельзя применять к срезам `QuerySet`, например `Women.objects.all()[:4].update(is_published=1)`, это вызовет ошибку.

Также `update()` нельзя применять к одиночному объекту:

```python
Women.objects.get(pk=5).update(is_published=1)  # Ошибка!
```

### Удаление записей

Удаление записей выполняется в два шага:

1. Выбираем записи с `filter()`:

```python
wd = Women.objects.filter(pk__gte=5)
```

2. Удаляем записи:

```python
wd.delete()
```

Этот запрос удалит все записи, у которых `id` больше или равен 5.

> **Важно:** Метод `delete()` нельзя вызывать у одиночных объектов `get()`, только у `QuerySet`.

## 3.6 Слаги (slug) в URL-адресах. Метод get_absolute_url()

Slug – это уникальный фрагмент URL-адреса, связанный с конкретной записью.

```
https://example.com/post/osnovnye-metody-strok
```

Здесь slug – это "osnovnye-metody-strok", который определяет статью в БД.

### Добавление Slug в модель

Добавим поле `slug` в модель `Women`.

```python
class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, db_index=True, blank=True, default='')
```

Выполняем команды:

```sh
python manage.py makemigrations
python manage.py migrate
```

Заполним slug для существующих записей:

```python
python manage.py shell_plus

for w in Women.objects.all():
    w.slug = 'slug-'+str(w.pk)
    w.save()
```

После выполнения приводим поле `slug` в модели в окончательный вид:

```python
slug = models.SlugField(max_length=255, db_index=True, unique=True)
```

Выполняем команды:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Доступ к статьям по Slug

Обновим `women/urls.py`, чтобы статьи загружались по slug:

```python
path('post/<slug:post_slug>/', views.show_post, name='post'),
```

Обновим функцию `show_post` в `views.py`:

```python
def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    return render(request, 'women/post.html', {'post': post})
```

Теперь статьи доступны по URL, например:

```
http://127.0.0.1:8000/post/slug-1/
```

### Метод get_absolute_url()

Для формирования ссылок со slug в модели добавим метод `get_absolute_url`:

```python
from django.urls import reverse

class Women(models.Model):
    ...
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
```

Теперь в шаблоне `index.html` ссылки можно формировать так:

```html
<p class="link-read-post"><a href="{{ p.get_absolute_url }}">Читать пост</a></p>
```

**Зачем нужен get_absolute_url()?**

- Позволяет централизованно управлять изменениями URL в одном месте.
- Используется Django для построения ссылок, например, в админке.

## 3.7 Создание пользовательского менеджера модели

### Реализация собственного менеджера

В файл `models.py` приложения `women` и объявим новый класс менеджера. В классе создаём метод `get_queryset()`, который переопределяет стандартный метод базового класса `models.Manager`, добавляя фильтрацию записей по полю `is_published`:

```python
from django.db import models

class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)
```

### Использование менеджера в модели

В классе `Women` создадим объект нового менеджера. Важно учитывать, что если в модели объявлен хотя бы один пользовательский менеджер, стандартный `objects` перестаёт существовать, поэтому его нужно прописывать явно.

```python
class Women(models.Model):
    ...
    objects = models.Manager()
    published = PublishedModel()

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
```

### Использование нового менеджера в представлениях

Изменения в функции `index()`:

```python
def index(request):
    posts = Women.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'women/index.html', context=data)
```

Аналогично используем его в `show_category()`:

```python
def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': Women.published.all(),
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)
```

Убираем условие проверки в `index.html`:

```django
{% for p in posts %}
    <li><h2>{{p.title}}</h2>
{% autoescape off %}
{{p.content|linebreaks|truncatewords:40}}
{% endautoescape %}
    <div class="clear"></div>
    <p class="link-read-post"><a href="{{ p.get_absolute_url }}">Читать пост</a></p>
    </li>
{% endfor %}
```

### Перечисляемое поле (Enum в Django)

Для создания перечисления используем Django `IntegerChoices`:

```python
class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    is_published = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
```

### Обновление менеджера с использованием `Status`

```python
class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)
```

### Создание миграции

```sh
python manage.py makemigrations
python manage.py migrate
```

# 4. Связи между таблицами

## 4.1 Типы связей между моделями в Django: ForeignKey, ManyToManyField, OneToOneField

### Зачем нужны связи между таблицами?

Допустим, у нас есть модель статей, и для каждой статьи нужно хранить категорию, к которой она относится. Если бы мы хранили всю информацию в одной таблице, то пришлось бы дублировать название категории в каждой строке. Это привело бы к следующим проблемам:

- Сложность редактирования (если мы захотим изменить название категории, придется менять каждую запись).
- Затруднение поиска (фильтрация по текстовым полям выполняется медленнее, чем по числовым идентификаторам).
- Избыточность данных (повторяющаяся информация занимает больше места в базе данных).

Чтобы избежать этих проблем, данные разделяют на несколько таблиц, связывая их между собой. Такой подход называется **нормализацией** и позволяет:

- Уменьшить дублирование данных.
- Облегчить редактирование информации.
- Ускорить выполнение запросов.

### Типы связей между моделями в Django

1. **ForeignKey** – связь «многие к одному» (Many to One).
2. **ManyToManyField** – связь «многие ко многим» (Many to Many).
3. **OneToOneField** – связь «один к одному» (One to One).

### ForeignKey (многие к одному)

Этот тип связи используется, когда одна запись в одной таблице может быть связана с несколькими записями в другой таблице.

Создадим две модели: `Category` и `Article`, где `Article` содержит внешний ключ (`ForeignKey`) на `Category`.

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

- **Category** содержит поля `name` (название категории) и `slug` (уникальный идентификатор).
- **Article** имеет поле `category`, которое является внешним ключом (`ForeignKey`). Оно указывает, к какой категории принадлежит статья.
- `on_delete=models.CASCADE` означает, что если категория будет удалена, все связанные статьи тоже удалятся.

### ManyToManyField (многие ко многим)

Этот тип связи используется, когда одна запись может быть связана с несколькими записями из другой таблицы и наоборот.

```python
class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name
```

- **Student** и **Teacher** связаны через `ManyToManyField`, что создаст промежуточную таблицу.
- Django автоматически создаст связь между студентами и преподавателями без необходимости вручную создавать таблицу связей.
- В базе данных создастся промежуточная таблица (`student_teachers`), содержащая два поля: `student_id` и `teacher_id`.

### OneToOneField (один к одному)

Этот тип связи используется, когда одна запись в одной таблице может быть связана только с одной записью в другой таблице.

```python
class Citizen(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Passport(models.Model):
    citizen = models.OneToOneField(Citizen, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.citizen.name} - {self.passport_number}"
```

- **Citizen** – основная таблица.
- **Passport** содержит `OneToOneField`, что означает, что у каждого гражданина может быть только один паспорт.
- `on_delete=models.CASCADE` гарантирует, что если гражданин удаляется, его паспорт также удаляется.

### Схема связей между моделями

- **ForeignKey** (многие к одному): `Article` → `Category` (одна категория может иметь несколько статей).
- **ManyToManyField** (многие ко многим): `Student` ↔ `Teacher` (многие студенты могут иметь много преподавателей).
- **OneToOneField** (один к одному): `Citizen` → `Passport` (у каждого гражданина есть только один паспорт).

## 4.2 Связь Many-to-One (многие к одному) с ForeignKey в Django

Связь "многие к одному" (Many-to-One) используется в реляционных базах данных для создания отношений между таблицами, где множество записей в одной таблице могут ссылаться на одну запись в другой.

В Django ORM это реализуется с помощью поля `ForeignKey`.

### Определение ForeignKey

Поле `ForeignKey` требует два обязательных параметра:

- **`to`** – модель, с которой связывается поле (можно указать как строку, если модель определена ниже по коду);
- **`on_delete`** – определяет, что происходит при удалении записи в первичной модели.

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

class Women(models.Model):
    name = models.CharField(max_length=100)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
```

### Опции on_delete

```bash
+---------------------------------------------------------------------+
| Значение       | Описание                                           |
|----------------|----------------------------------------------------|
| `CASCADE`      | Удаляет все связанные записи.                      |
| `PROTECT`      | Запрещает удаление, если есть связанные записи.    |
| `SET_NULL`     | Присваивает `NULL` связанным записям.              |
| `SET_DEFAULT`  | Устанавливает значение по умолчанию.               |
| `SET(<value>)` | Устанавливает определенное пользователем значение. |
| `DO_NOTHING`   | Никаких действий не выполняется.                   |
+---------------------------------------------------------------------+
```

### Создание и применение миграций

После добавления нового поля `cat` необходимо выполнить миграции:

```sh
python manage.py makemigrations
```

Возможна ошибка, если в таблице `Women` уже есть записи, так как поле `cat` не может быть пустым. Решение:

```python
cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
```

После этого:

```sh
python manage.py makemigrations
python manage.py migrate
```

Теперь таблицы `women_category` и `women_women` в базе данных содержат связь `cat_id`.

Заполняем категории:

```sh
python manage.py shell_plus
```

```python
Category.objects.create(name='Актрисы', slug='aktrisy')
Category.objects.create(name='Певицы', slug='pevicy')
```

Обновляем поле `cat_id` для всех записей:

```python
w_list = Women.objects.all()
w_list.update(cat_id=1)
```

Затем удаляем `null=True` и выполняем миграцию:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Проверка работы параметра on_delete

#### `PROTECT`

```python
c = Category.objects.get(pk=1)
c.delete()  # Ошибка ProtectedError
```

Категорию удалить нельзя, пока есть связанные женщины.

#### `CASCADE`

Меняем `on_delete`:

```python
cat = models.ForeignKey('Category', on_delete=models.CASCADE)
```

Теперь удаление категории удалит всех женщин, связанных с ней:

```python
c = Category.objects.get(pk=1)
c.delete()
```

## 4.3 ORM-команды для связи many-to-one

### Работа с ORM через shell

- Читаем запись с `id=1` из таблицы `Women`:

  ```python
  w = Women.objects.get(pk=1)
  ```

- Теперь объект `w` содержит данные из таблицы `Women`:

  ```python
  w.title  # 'Анджелина Джоли'
  w.time_create  # datetime.datetime(2023, 6, 15)
  ```

- Атрибут `cat_id` показывает ID связанной категории:

  ```python
  w.cat_id  # 1
  ```

- Обращение к `w.cat` выполняет дополнительный SQL-запрос и возвращает объект `Category`:

  ```python
  w.cat.name  # 'Актрисы'
  ```

### Получение связанных записей через первичную модель

- Можно извлекать все записи из `Women`, относящиеся к категории `Category`:

  ```python
  c = Category.objects.get(pk=1)
  c.women_set.all()
  ```

- Чтобы изменить `women_set`, задаем параметр `related_name` в `ForeignKey`:

  ```python
  class Women(models.Model):
      cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
  ```

- Теперь доступ к связанным записям осуществляется так:

  ```python
  c.posts.all()
  ```

- Можно применять фильтры:

  ```python
  c.posts.filter(is_published=1)
  ```

### Фильтрация по внешнему ключу

- Выбираем записи по категории:

  ```python
  Women.objects.filter(cat_id=1)
  ```

- Фильтр `in` для нескольких категорий:

  ```python
  Women.objects.filter(cat__in=[1, 2])
  Women.objects.filter(cat_id__in=[1, 2])
  ```

- Или передаем объекты:

  ```python
  cats = Category.objects.all()
  Women.objects.filter(cat__in=cats)
  ```

### Выборка записей по полям связанных моделей

- Фильтрация по `slug`:

  ```python
  Women.objects.filter(cat__slug='aktrisy')
  ```

- Фильтрация по `name`:

  ```python
  Women.objects.filter(cat__name='Певицы')
  ```

- Фильтрация с `contains`:

  ```python
  Women.objects.filter(cat__name__contains='ы')
  ```

- Фильтрация категорий по заголовкам связанных записей:

  ```python
  Category.objects.filter(posts__title__contains='ли').distinct()
  ```

## 4.4 Отображение постов по рубрикам в Django

### Изменение маршрута в `urls.py`

Поменяем маршрут в `women/urls.py`, чтобы вместо числового идентификатора (int) использовать slug и в URL будет использоваться slug вместо id, что делает ссылки более читаемыми и SEO-дружественными:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
]
```

### Обновление представления `show_category` в `views.py`

Перейдём в `women/views.py` и изменим функцию `show_category()`:

```python
from django.shortcuts import render, get_object_or_404
from .models import Women, Category


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)
```

Здесь мы:

- Получаем объект `Category` по его `slug`, выбрасывая ошибку 404, если он не найден.
- Извлекаем все статьи, относящиеся к данной категории.
- Формируем словарь `data` для передачи в шаблон.
- Передаём данные в `index.html`.

### Изменение пользовательского шаблонного тега

Рубрики выводятся с помощью пользовательского тега `show_categories()`, определённого в `women_tags.py`. Заменим получение рубрик из статической коллекции `cats_db` на чтение из таблицы `Category`:

```python
from django import template
from women.models import Category

register = template.Library()

@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected_id}
```

### Обновление шаблона `list_categories.html`

Изменим код в `list_categories.html` для правильного отображения рубрик:

```html
{% for cat in cats %} {% if cat.id == cat_selected %}
<li class="selected">{{ cat.name }}</li>
{% else %}
<li><a href="{{ cat.get_absolute_url }}">{{ cat.name }}</a></li>
{% endif %} {% endfor %}
```

### Добавление метода `get_absolute_url()` в модель Category

Чтобы ссылки генерировались автоматически, добавим в модель `Category` метод `get_absolute_url()`:

```python
from django.urls import reverse
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name
```

### Обновление шаблона `index.html`

Добавим в шаблон `index.html` перед заголовком статьи блок с названием категории и временем её последнего обновления:

```html
<li>
  <div class="article-panel">
    <p class="first">Категория: {{ p.cat.name }}</p>
    <p class="last">Дата: {{ p.time_update|date:"d-m-Y H:i:s" }}</p>
  </div>
</li>
```

## 4.5 Связь Many-to-Many (многие ко многим) в Django

Связь "многие ко многим" (Many-to-Many) широко применяется в базах данных и позволяет устанавливать ассоциации между множеством записей одной таблицы и множеством записей другой таблицы. В Django это реализуется с помощью поля `ManyToManyField`.

### Реализация Many-to-Many

- **Определение модели тегов**: В файле `women/models.py` создадим новую модель `TagPost` для хранения тегов.

  ```python
  from django.db import models

  class TagPost(models.Model):
      tag = models.CharField(max_length=100, db_index=True)
      slug = models.SlugField(max_length=255, unique=True, db_index=True)

      def __str__(self):
          return self.tag
  ```

- **Добавление связи Many-to-Many**: В модели `Women` добавим новое поле `tags`.

  ```python
  class Women(models.Model):
      title = models.CharField(max_length=255)
      slug = models.SlugField(max_length=255, unique=True)
      tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
  ```

  Важно:

  - Мы передаем `'TagPost'` в виде строки, потому что модель `TagPost` объявлена позже.
  - `on_delete` не используется для `ManyToManyField`.

- Создание и применение миграций:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

  После этого в базе данных появятся две таблицы:

  - `women_tagpost` – хранит теги.
  - `women_women_tags` – вспомогательная таблица, связывающая статьи и теги.

### Добавление тегов в базу через ORM Django

Открываем Django Shell:

```bash
python manage.py shell_plus
```

Создаем теги:

```python
TagPost.objects.create(tag='Блондинки', slug='blonde')
TagPost.objects.create(tag='Брюнетки', slug='brunetky')
TagPost.objects.create(tag='Оскар', slug='oskar')
```

### Присвоение тегов статьям через ORM Django

Получаем статью с `id=1`:

```python
a = Women.objects.get(pk=1)
```

Получаем нужные теги:

```python
tag_br = TagPost.objects.get(slug='brunetky')
tag_o = TagPost.objects.get(slug='oskar')
tag_v = TagPost.objects.get(slug='visokie')
```

Добавляем теги статье:

```python
a.tags.set([tag_br, tag_o, tag_v])
```

### Удаление тегов через ORM Django

```python
a.tags.remove(tag_o)
```

### Получение связанных данных через ORM Django

Получаем все теги статьи:

```python
a.tags.all()
```

Получаем все статьи, связанные с тегом `Брюнетки`:

```python
tag_br.tags.all()
```

### Добавление статьи с тегами через ORM Django

Нельзя создать новую статью и сразу передать ей теги:

```python
# Ошибка!
Women.objects.create(title='Ариана Гранде', slug='ariana-grande', tags=[tag_br, tag_v])
```

Правильный способ:

```python
w = Women.objects.create(title='Ариана Гранде', slug='ariana-grande')
w.tags.set([tag_br, tag_v])
```

## 4.6 Добавление тегов на сайт

### Создание маршрута для тегов

Добавим новый маршрут для отображения списка статей по выбранному тегу. Откроем файл `women/urls.py` и внесем в `urlpatterns` следующую строку:

```python
urlpatterns = [
    ...
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
]
```

### Добавление метода `get_absolute_url` в модель TagPost

В файле `women/models.py` создадим модель `TagPost`, если ее еще нет, и добавим метод `get_absolute_url()` для формирования URL-адреса:

```python
from django.db import models
from django.urls import reverse

class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.tag
```

### Создание представления для отображения статей по тегу

В файле `women/views.py` объявим функцию `show_tag_postlist`, которая будет обрабатывать запросы к тегу и выводить список статей, связанных с ним:

```python
from django.shortcuts import render, get_object_or_404
from .models import Women, TagPost


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)
```

### Добавление параметра `cat_selected` в index

Чтобы правильно обрабатывать выбор тегов, изменим функцию `index()`:

```python
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': Women.published.all(),
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=data)
```

### Создание шаблонного тега для отображения списка тегов в сайдбаре

Создадим файл `women/women_tags.py` (если его нет) и зарегистрируем новый шаблонный тег:

```python
from django import template
from women.models import TagPost

register = template.Library()

@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {"tags": TagPost.objects.all()}
```

### Создание шаблона `list_tags.html`

В файле `women/templates/women/list_tags.html` добавим следующий код:

```html
{% if tags %}
<p>Теги:</p>
<ul class="tags-list">
  {% for t in tags %}
  <li><a href="{{t.get_absolute_url}}">{{t.tag}}</a></li>
  {% endfor %}
</ul>
{% endif %}
```

### Подключение списка тегов в базовый шаблон

Теперь добавим вызов нашего шаблонного тега в `base.html`:

```html
<li>{% show_all_tags %}</li>
```

После этого при загрузке страницы в сайдбаре должен появиться список тегов.

### Добавление списка тегов в шаблон статьи

В шаблоне `women/post.html` добавим отображение тегов, привязанных к конкретной статье:

```html
{% extends 'base.html' %} {% block breadcrumbs %}
<!-- Теги -->
{% with post.tags.all as tags %} {% if tags %}
<ul class="tags-list">
  <li>Теги:</li>
  {% for t in tags %}
  <li><a href="{{t.get_absolute_url}}">{{t.tag}}</a></li>
  {% endfor %}
</ul>
{% endif %} {% endwith %} {% endblock %}
```

### Схема взаимодействия файлов

1. **`women/urls.py`** — добавляет маршрут для тегов.
2. **`women/models.py`** — содержит модель `TagPost` с методом `get_absolute_url()`.
3. **`women/views.py`** — содержит представление `show_tag_postlist`, обрабатывающее теги.
4. **`women/women_tags.py`** — содержит шаблонный тег `show_all_tags()`.
5. **`women/templates/women/list_tags.html`** — выводит список тегов.
6. **`women/templates/base.html`** — содержит вызов `{% show_all_tags %}`.
7. **`women/templates/women/post.html`** — отображает теги статьи.

## 4.7 Связь One-To-One (Один к одному)

Связь One-To-One (один к одному) в реляционных базах данных подразумевает, что одна запись в одной таблице может соответствовать только одной записи в другой таблице.

### Определение моделей

Для демонстрации связи `One-To-One` создадим новую модель `Husband`, которая будет хранить информацию о муже:

```python
from django.db import models

class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
```

### Добавим связь `One-To-One` в модель `Women`:

```python
class Women(models.Model):
    ...
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True, blank=True, related_name='woman')
    ...
```

Здесь мы:

- Используем `OneToOneField` для связи с моделью `Husband`.
- Указываем `on_delete=models.SET_NULL`, чтобы при удалении мужа поле становилось `NULL`.
- Добавляем `related_name='woman'`, чтобы можно было обращаться к объекту `Women` через `Husband`.

После добавления моделей необходимо создать миграции и применить их:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Работа с данными

- Создадим несколько записей в модели `Husband` через Django shell:

  ```python
  h1 = Husband.objects.create(name="Брэд Питт", age=59)
  h2 = Husband.objects.create(name="Том Акерли", age=31)
  h3 = Husband.objects.create(name="Дэниэл Модер")
  h4 = Husband.objects.create(name="Кук Марони")
  ```

- Распределим мужей по женщинам. Например, получим объект `Women` с `pk=1`:

```python
w1 = Women.objects.get(pk=1)
print(w1.husband)  # Выведет None
```

- Назначим `h1` (Брэда Питта) в качестве мужа `w1`:

```python
w1.husband = h1
w1.save()
```

- Теперь можно проверить:

```python
print(w1.husband)  # Брэд Питт
print(h1.woman)  # Женщина, связанная с Брэдом Питтом
```

- Можно установить связь с другой стороны:

  ```python
  w2 = Women.objects.get(pk=2)
  h2.woman = w2
  w2.save()
  ```

  Важно! Мы сохраняем `w2`, так как `husband_id` находится именно в таблице `Women`.

- Попробуем назначить `h2` (Тома Акерли) другой женщине:

  ```python
  w3 = Women.objects.get(pk=3)
  w3.husband = h2
  w3.save()
  ```

  Получим ошибку:

  ```plaintext
  IntegrityError: UNIQUE constraint failed: women_women.husband_id
  ```

- Чтобы назначить `h2` новой женщине `w3`, сначала нужно убрать его у `w2`:

  ```python
  w2.husband = None
  w2.save()

  w3.husband = h2
  w3.save()
  ```

  Теперь `h2` связан с `w3`.

- Через объект `Women` можно получить данные мужа:

  ```python
  print(w1.husband.name)  # Брэд Питт
  print(w1.husband.age)  # 59
  ```

  Можно менять данные напрямую через объект `husband`:

  ```python
  w1.husband.age = 30
  w1.husband.save()
  ```

  Теперь `Брэд Питт` имеет возраст `30` лет.

### Структура файлов и зависимостей

#### Основные файлы:

- `models.py` – содержит модели `Women` и `Husband`.
- `migrations/` – папка с миграциями.
- `manage.py` – используется для работы с Django.

#### Взаимосвязи:

- `Women.husband` → `Husband`
- `Husband.woman` ← `Women`

# 5. Погружение в ORM Django

## 5.1 ORM-команды с классом Q в Django

При работе с `filter()` в ORM Django мы можем передавать несколько условий через запятую. Однако это всегда формирует логический оператор `AND`:

```python
Women.objects.filter(pk__in=[2, 5, 7, 10], is_published=True)
```

Этот код приведет к следующему SQL-запросу:

```sql
WHERE ("women_women"."is_published" AND "women_women"."id" IN (2, 5, 7, 10))
```

Если нам нужно использовать `OR` или `NOT`, на помощь приходит класс `Q` из `django.db.models`.

### Основные операторы класса `Q`

- `&` — логическое И (приоритет 2)
- `|` — логическое ИЛИ (приоритет 1 — самый низкий)
- `~` — логическое НЕ (приоритет 3 — самый высокий)

### Примеры использования

Перед началом работы импортируем `Q`:

```python
from django.db.models import Q
```

#### Пример 1: Использование `OR` (`|`)

Если объединить условия с `Q` то в результат попадут записи, у которых `id < 5` **ИЛИ** `cat_id = 2`.

```python
Women.objects.filter(Q(pk__lt=5) | Q(cat_id=2))
```

#### Пример 2: Использование `AND` (`&`)

Тот же запрос, но с логическим `AND`:

```python
Women.objects.filter(Q(pk__lt=5) & Q(cat_id=2))
```

#### Пример 3: Использование `NOT` (`~`)

Отбираем записи, у которых не `id >= 5` или `cat_id = 2`:

```python
Women.objects.filter(~Q(pk__lt=5) | Q(cat_id=2))
```

### Комбинированные запросы

Мы можем комбинировать `Q` с обычными аргументами:

```python
Women.objects.filter(Q(pk__in=[1, 2, 5]) | Q(cat_id=2), title__icontains="ра")
```

Этот запрос приведет к SQL-запросу:

```sql
WHERE (("women_women"."id" IN (1, 2, 5) OR "women_women"."cat_id" = 2) AND "women_women"."title" LIKE '%ра%' ESCAPE '\')
```

Но такой код вызовет ошибку:

```python
Women.objects.filter(title__icontains="ра", Q(pk__in=[1, 2, 5]) | Q(cat_id=2))
```

Потому что `Q`-объекты должны быть указаны перед обычными аргументами или включены в `Q`:

```python
Women.objects.filter(Q(title__icontains="ра"), Q(pk__in=[1, 2, 5]) | Q(cat_id=2))
```

Если нам нужно убрать дополнительные скобки вокруг `OR`, используем `Q` так:

```python
Women.objects.filter(Q(pk__in=[1, 2, 5]) | Q(cat_id=2) & Q(title__icontains="ра"))
```

### Итоговая схема работы с классом `Q`

1. **Импортируем `Q`**:

   ```python
   from django.db.models import Q
   ```

2. **Используем `|`, `&`, `~` для сложных условий**:

   ```python
   Women.objects.filter(Q(pk__in=[1, 2, 5]) | Q(cat_id=2) & Q(title__icontains="ра"))
   ```

3. **Сначала пишем `Q`, затем обычные аргументы**:
   ```python
   Women.objects.filter(Q(pk__lt=5) | Q(cat_id=2), title__icontains="ра")
   ```

## 5.2 Методы выбора записей в Django ORM: first(), last(), exists(), count()

### Методы first() и last()

- Метод `first()` возвращает первую запись в выборке.
- Метод `last()` возвращает последнюю запись в выборке.

```python
Women.objects.first()
```

Этот метод выбирает первую запись на основе сортировки, определенной в модели или явно заданной:

```python
Women.objects.order_by("pk").first()
Women.objects.order_by("-pk").first()
```

Для получения последней записи используется `last()`:

```python
Women.objects.order_by("pk").last()
Women.objects.filter(pk__gt=5).last()
```

### Методы latest() и earliest()

При наличии полей с датой и временем можно использовать `latest()` и `earliest()`, чтобы выбрать запись с самой поздней или самой ранней датой соответственно:

```python
Women.objects.earliest("time_update")
Women.objects.latest("time_update")
```

Эти методы полезны, когда необходимо получить самую раннюю или позднюю запись в выборке:

```python
Women.objects.order_by('title').earliest("time_update")
```

### Методы `get_previous_by_` и `get_next_by_`

Для выбора предыдущей или следующей записи относительно текущей используется `get_previous_by_` и `get_next_by_`, где в качестве параметра указывается поле с датой или временем.

```python
w = Women.objects.get(pk=2)
w.get_previous_by_time_update()
w.get_next_by_time_update()
```

Можно также добавить фильтр при получении предыдущей записи:

```python
w.get_previous_by_time_update(pk__gt=6)
```

### Методы exists() и count()

Методы `exists()` и `count()` позволяют:

- Проверять существование записей в выборке (`exists()`)
- Получать количество записей в наборе (`count()`)

#### 5.1. Метод exists()

Создадим новую категорию и проверим, есть ли связанные записи:

```python
Category.objects.create(name="Спортсменки", slug="sportsmenki")
```

Эта категория пока пуста. Проверим, есть ли связанные посты:

```python
c3 = Category.objects.get(pk=3)
c3.posts.exists()
```

Если `related_name='posts'` не указано в `ForeignKey`, то обращаться к записям следует так:

```python
c3.women_set.exists()
```

Если категория пуста, метод вернет `False`, иначе `True`.

#### 5.2. Метод count()

Метод `count()` позволяет узнать количество записей в наборе данных:

```python
c2 = Category.objects.get(pk=2)
c2.posts.count()
```

Альтернативный способ получения количества записей:

```python
Women.objects.filter(cat=c2).count()
```

### Оптимизация работы с exists() и count()

Методы `exists()` и `count()` выполняются быстрее, чем `len(queryset)`, потому что они выполняют SQL-запрос на уровне базы данных без загрузки объектов Python.

**Пример неоптимального кода:**

```python
if len(Women.objects.filter(cat=c2)) > 0:
    print("Есть записи")
```

Этот код загружает все объекты, что неэффективно. Лучше использовать `exists()`:

```python
if Women.objects.filter(cat=c2).exists():
    print("Есть записи")
```

### **Выводы:**

- `exists()` используется для быстрого определения наличия записей.
- `count()` позволяет получить количество записей без загрузки данных.
- Использование этих методов ускоряет выполнение запросов и снижает нагрузку на базу данных.

## 5.3 Класс F, Value и метод annotate() в Django ORM

Класс `F` используется, когда нам нужно использовать значение другого поля.

Использование `F` предотвращает возможные коллизии при одновременном обновлении данных несколькими пользователями.

```python
from django.db.models import F
Women.objects.filter(pk__gt=F("cat_id"))
```

Этот код вернет все записи, где `pk` больше, чем `cat_id`. SQL-запрос будет выглядеть так:

```sql
SELECT ... FROM "women_women" WHERE "women_women"."id" > "women_women"."cat_id"
```

### Использование класса F для обновления данных

Модель `Husband`, в которой мы храним количество браков для каждого мужчины:

```python
class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
```

Увеличим значение `m_count` у всех записей:

```python
Husband.objects.update(m_count=F("m_count") + 1)
```

SQL-запрос, который сформирует Django ORM:

```sql
UPDATE "women_husband" SET "m_count" = ("women_husband"."m_count" + 1)
```

Также можно обновить одно конкретное поле:

```python
h = Husband.objects.get(pk=1)
h.m_count = F("m_count") + 1
h.save()
```

### Метод annotate()

Метод `annotate()` позволяет формировать дополнительные вычисляемые поля в выборке.

Добавим булево поле `is_married`:

```python
from django.db.models import Value

lst = Husband.objects.all().annotate(is_married=Value(True))
```

Поле `is_married` не существует в базе данных, но добавляется в выборку динамически.

### Использование F в annotate()

Вместо константного значения можно использовать `F` для работы с существующими полями:

```python
lst = Husband.objects.all().annotate(is_married=F("m_count"))
```

Теперь `is_married` будет содержать те же значения, что и `m_count`.

Можно также выполнить математические вычисления:

```python
lst = Husband.objects.all().annotate(work_age=F("age") - 20)
```

Результат:

```
['id', 'name', 'age', 'm_count', 'work_age']
[1, 'Брэд Питт', 30, 4, 10]
[2, 'Том Акерли', 31, 1, 11]
[3, 'Дэниэл Модер', 54, 0, 34]
```

Можно создать сразу несколько новых полей:

```python
lst = Husband.objects.all().annotate(work_age=F("age") - 20, salary=F("age") * 1.10)
```

Еще один пример, где вычисления выполняются на основе нескольких полей:

```python
lst = Husband.objects.all().annotate(salary=F("age") * 1.10 - F("m_count") * 5)
```

### Заключение

- `F` позволяет работать с полями модели в выражениях.
- `Value` используется для аннотирования выборки статическими значениями.
- `annotate()` позволяет добавлять вычисляемые поля на основе `F` и `Value`.
- Использование `F` предотвращает коллизии при обновлении данных.

## 5.4 Агрегирующие функции Count, Sum, Avg, Max, Min. Метод values()

Django ORM предоставляет механизм агрегации данных через функции Count, Sum, Avg, Max и Min. Они используются в методе `aggregate()`, который возвращает словарь с вычисленными значениями.

### Метод count()

Метод `count()` используется для подсчёта числа записей в таблице. Например, для модели `Women`:

```python
Women.objects.count()
```

Это формирует SQL-запрос с функцией `COUNT()` на уровне базы данных:

```sql
SELECT COUNT(*) AS "__count" FROM "women_women"
```

Преимущество такого подхода – отсутствие необходимости загружать все данные в память. Подсчёт выполняется непосредственно в базе данных.

### Основные агрегирующие функции

Для работы с агрегатными функциями необходимо импортировать их из `django.db.models`:

```python
from django.db.models import Count, Sum, Avg, Max, Min
```

Применение этих функций в `aggregate()` возвращает словарь с вычисленным значением. Например, найдём минимальный возраст мужчин в модели `Husband`:

```python
Husband.objects.aggregate(Min("age"))
```

Результат:

```python
{'age__min': 30}
```

Имя ключа формируется как имя поля, два подчеркивания и название агрегирующей функции.

### Комбинированные агрегации

Можно использовать несколько агрегирующих функций одновременно:

```python
Husband.objects.aggregate(Min("age"), Max("age"))
```

Результат:

```python
{'age__min': 30, 'age__max': 101}
```

Чтобы задать пользовательские ключи:

```python
Husband.objects.aggregate(young=Min("age"), old=Max("age"))
```

Результат:

```python
{'young': 30, 'old': 101}
```

### Выполнение математических операций

С агрегированными значениями можно выполнять арифметические операции:

```python
Husband.objects.aggregate(res=Sum("age") - Avg("age"))
```

Здесь `res` обязателен, так как автоматического ключа не генерируется.

Примеры других агрегирующих операций:

```python
Women.objects.aggregate(Avg("id"))
```

С фильтрацией:

```python
Women.objects.filter(pk__gt=2).aggregate(res=Count("cat_id"))
```

Этот запрос подсчитает количество записей, у которых `id > 2`.

### Метод values()

Метод `values()` используется для выборки конкретных полей из базы данных. Например, если нужно получить только `title` и `cat_id`:

```python
Women.objects.values("title", "cat_id").get(pk=1)
```

Если требуется получить поле из связанной таблицы:

```python
Women.objects.values("title", "cat__name").get(pk=1)
```

Django ORM создаст SQL-запрос с `JOIN`:

```sql
SELECT "women_women"."title", "women_category"."name"
FROM "women_women"
INNER JOIN "women_category" ON ("women_women"."cat_id" = "women_category"."id")
WHERE "women_women"."id" = 1 LIMIT 21
```

### Ленивые запросы ORM

Django ORM использует ленивую загрузку. Запрос выполняется только при непосредственном доступе к данным:

```python
w = Women.objects.values("title", "cat__name")
```

Пока SQL-запрос не отправляется, но при итерации:

```python
for p in w:
    print(p["title"], p["cat__name"])
```

Django выполнит один SQL-запрос, получая все необходимые данные. Это делает ORM Django высокоэффективным инструментом работы с базой данных.

## 5.5 Группировка записей в Django ORM

### Пример группировки записей

Для подсчета количества постов в каждой категории можно воспользоваться следующим запросом:

```python
from django.db.models import Count

Women.objects.values("cat_id").annotate(Count("id"))
```

Графически это можно представить так:

1. Записи группируются по `cat_id`.
2. Для каждой группы выполняется подсчет количества записей.

Метод `values("cat_id")` формирует группы по `cat_id`, а `annotate(Count("id"))` выполняет подсчет количества записей в каждой группе.

При необходимости можно изменить имя параметра `id__count`, задав его явно в методе `annotate()`:

```python
Women.objects.values('cat_id').annotate(total=Count('id'))
```

### Фильтрация сгруппированных данных

Группировка записей позволяет не только агрегировать данные, но и фильтровать их. Например, отберем категории, у которых количество постов больше нуля:

```python
lst = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
```

В результате SQL-запрос группирует записи по `id`, `name`, `slug`, добавляя к ним дополнительное поле `total`.

Отобразим результаты в консоли:

```python
for i, x in enumerate(lst):
    if i == 0:
        print(list(x.__dict__)[1:])
    print(list(x.__dict__.values())[1:])
```

Выходные данные:

```
['id', 'name', 'slug', 'total']
[1, 'Актрисы', 'aktrisy', 5]
[2, 'Певицы', 'pevicy', 5]
```

По аналогии можно отобрать все теги из таблицы `TagPost`, которым соответствует хотя бы одна статья:

```python
lst = TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)
```

### Оптимизация сложных запросов

Запросы с группировкой и агрегатными функциями могут быть ресурсоемкими. Перед их использованием стоит оценить необходимость выполнения вычислений на стороне СУБД. Иногда проще получить список данных и обработать его в Python.

### Применение группировки в шаблонах Django

Для отображения только значащих тегов обновим функцию `show_all_tags()` в `women_tags.py`:

```python
from django import template
from django.db.models import Count
from women.models import TagPost

register = template.Library()

@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {"tags": TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}
```

Запускаем сервер и теперь отображаются только теги, имеющие статьи.

Аналогично поступим с рубриками:

```python
@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {"cats": cats, "cat_selected": cat_selected_id}
```

Теперь видны только заполненные рубрики.

### Вычисления на стороне СУБД

Django содержит набор встроенных функций для выполнения вычислений в базе данных.

Эти функции представляют собой обертки над SQL-функциями и включают работу со строками, датами, математические операции и др.

Использование этих функций является рекомендуемой практикой, так как СУБД оптимизирована для их выполнения.

### Пример: вычисление длины строки

Импортируем функцию `Length`:

```python
from django.db.models.functions import Length
```

Аннотируем поле `len_name`, чтобы вычислить длину имени в таблице `Husband`:

```python
lst = Husband.objects.annotate(len_name=Length('name'))
```

Выведем результат:

```python
for i in lst:
    print(i.name, i.len_name)
```

Результат:

```
Брэд Питт 9
Том Акерли 10
Дэниэл Модер 12
Кук Марони 10
Сергей Балакирев 16
```

### Другие полезные функции

- `Upper` / `Lower` – преобразование строки в верхний / нижний регистр.
- `Concat` – объединение строк.
- `ExtractYear`, `ExtractMonth`, `ExtractDay` – извлечение частей даты.
- `Round` – округление чисел.
- `Log`, `Exp`, `Power` – математические вычисления.

## 5.6 Оптимизация сайта с Django Debug Toolbar

### Для чего использовать Django Debug Toolbar

С помощью `Django Debug Toolbar` можно проверить:

- скорость работы приложения;
- нагрузку на СУБД (частоту и сложность запросов);
- корректность возвращаемых пользователю данных.

#### Установка и настройка

- Установка:

```bash
pip install django-debug-toolbar
```

- В файле `settings.py` нужно зарегистрировать приложение, добавив в `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
```

- В этом же файле в коллекции `MIDDLEWARE` нужно прописать:

```python
MIDDLEWARE = [
    ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```

- В `settings.py` добавляем коллекцию `INTERNAL_IPS`:

```python
INTERNAL_IPS = [
    '127.0.0.1',
]
```

- В файле `urls.py` пакета конфигурации (`myproject/urls.py`) добавляем маршрут:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
```

### Использование Debug Toolbar

Запускаем тестовый веб-сервер, переходим на главную страницу сайта, и справа отображается панель Debug Toolbar.

На панели можно увидеть:

- версию Django;
- время формирования страницы;
- количество SQL-запросов;
- список используемых шаблонов;
- и другие метрики.

Если кликнуть на SQL-запросы, можно увидеть их подробности, включая ORM-команды и сгенерированные SQL-запросы.

### Оптимизация запросов

При анализе Debug Toolbar можно заметить, что один и тот же SQL-запрос выполняется несколько раз. Это связано с тем, что в шаблоне используется отложенный запрос:

```html
<p class="first">Категория: {{ p.cat.name }}</p>
```

Django по умолчанию использует **ленивые запросы** (Lazy Queries). Они выполняются только при обращении к данным. Однако, когда таких обращений много, число SQL-запросов резко возрастает.

#### Django предлагает два метода оптимизации:

- `select_related(key)` – загружает связанные данные по внешнему ключу (ForeignKey) одним SQL-запросом.
- `prefetch_related(key)` – загружает связанные данные для полей ManyToManyField.

Используем `select_related` в представлении `index()`:

```python
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': Women.published.all().select_related('cat'),
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', data)
```

Теперь, благодаря **"жадной" загрузке**, Django сразу подтягивает связанные данные, избегая дублирующихся SQL-запросов.

После обновления страницы можно заметить сокращение числа SQL-запросов в Debug Toolbar.

### Оптимизация других представлений

- **Функция `show_category()`**:

```python
def show_category(request, cat_id):
    posts = Women.published.filter(cat_id=cat_id).select_related('cat')
    context = {
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context)
```

- **Функция `show_tag_postlist()`**:

```python
def show_tag_postlist(request, tag_slug):
    posts = Women.published.filter(tags__slug=tag_slug).prefetch_related('tags')
    context = {
        'posts': posts,
        'tag_selected': tag_slug,
    }
    return render(request, 'women/index.html', context)
```

### Разбор функционала Django Debug Toolbar

- **Versions** – версия Django и Python.
- **Time** – общее время рендеринга страницы.
- **Settings** – текущие настройки Django.
- **Headers** – HTTP-заголовки запроса.
- **Request** – параметры запроса (GET/POST).
- **SQL** – список выполненных SQL-запросов.
- **Templates** – список использованных шаблонов.
- **Static Files** – загруженные статические файлы.
- **Signals** – обработанные сигналы Django.

### Итоговая схема подключения Debug Toolbar

1. Устанавливаем пакет `django-debug-toolbar`.
2. Добавляем `debug_toolbar` в `INSTALLED_APPS`.
3. Регистрируем `DebugToolbarMiddleware` в `MIDDLEWARE`.
4. Указываем `INTERNAL_IPS = ['127.0.0.1']`.
5. Добавляем `path("__debug__/", include("debug_toolbar.urls"))` в `urls.py`.
6. Анализируем SQL-запросы и оптимизируем их с `select_related` и `prefetch_related`.
