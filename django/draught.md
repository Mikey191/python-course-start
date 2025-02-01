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
