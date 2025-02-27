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

# 6. Работа с админ-панелью

## 6.1 Подключение админ-панели. Регистрация моделей

Админ-панель подключена к проекту по умолчанию в файле настроек `settings.py` в списке `INSTALLED_APPS`.

В файле `urls.py` также уже прописан маршрут к админке

Мы можем перейти по адресу:

```
http://127.0.0.1:8000/admin/
```

### Переключить язык на русский

Для перехода необходимо в файле `settings.py` изменить константу `LANGUAGE_CODE`:

```python
LANGUAGE_CODE = 'ru-RU'
```

### Создание суперпользователя

Для входа в админку нужен аккаунт суперпользователя. Создадим его с помощью команды:

```sh
python manage.py createsuperuser
```

Затем заполняем поля:

- Имя пользователя: `root`
- Email: `root@mymail.ru`
- Пароль: `1234` (в реальных проектах используйте сложные пароли)

Теперь можно войти в админ-панель, используя эти данные.

### Регистрация моделей в админке

После входа в панель мы увидим два зарегистрированных приложения: «Группы» и «Пользователи». Однако наше приложение пока отсутствует. Чтобы добавить его, нужно зарегистрировать модель в `admin.py`.

Откроем `women/admin.py` и добавим следующие строки:

```python
from django.contrib import admin
from .models import Women

admin.site.register(Women)
```

#### Настройка отображения модели

В файле `women/models.py` добавим `verbose_name` и `verbose_name_plural`:

```python
class Women(models.Model):
    ...
    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
```

Теперь модель будет отображаться корректно.

#### Изменение названия приложения

В `women/apps.py`:

```python
from django.apps import AppConfig

class WomenConfig(AppConfig):
    name = 'women'
    verbose_name = 'Женщины мира'
```

После этих изменений админ-панель станет удобнее и понятнее.

## 6.2 Настройка отображения списка статей в админ-панели

### Добавление дополнительных полей в список статей

Для удобного просмотра списка статей в административной панели добавим в него дополнительные поля: `id`, `title`, `time_create` и `is_published`.

Для этого в файле `women/admin.py` создадим класс, унаследованный от `ModelAdmin`:

```python
from django.contrib import admin
from .models import Women

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')

admin.site.register(Women, WomenAdmin)
```

- **list_display** — определяет список полей, которые будут отображаться в админ-панели.
- **list_display_links** — указывает, какие поля будут активными ссылками для перехода к редактированию записи.

При этом `WomenAdmin` должен обязательно идти после определения модели `Women`.

### Использование декоратора `@admin.register`

Вместо явного вызова `admin.site.register()` можно использовать декоратор:

```python
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
```

### Сортировка записей в админке

Для сортировки записей по дате создания и заголовку добавим атрибут `ordering`:

```python
ordering = ['time_create', 'title']
```

Если требуется изменить порядок сортировки на убывающий, добавляем `-` перед полем:

```python
ordering = ['-time_create', 'title']
```

Такой порядок применяется **только в админ-панели** и не влияет на отображение записей в других частях проекта.

### Локализация названий полей

Чтобы вместо английских названий отображались русские, добавим `verbose_name` в `models.py`:

```python
class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Категория")
```

### Регистрация модели `Category`

По аналогии зарегистрируем вторую модель `Category` в `admin.py`:

```python
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
```

Добавим локализацию в `models.py`:

```python
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
```

### Редактирование полей прямо в списке

Добавим возможность редактирования поля `is_published` прямо в списке статей:

```python
list_editable = ('is_published', )
```

После обновления страницы можно изменять статус публикации прямо в списке.

**Важно!** Поля в `list_editable` не могут входить в `list_display_links`, иначе возникнет ошибка.

### Проблема с `choices` в `BooleanField`

Стандартный `BooleanField` не поддерживает `IntegerChoices`, поэтому для корректного отображения статуса исправим его так:

```python
is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                   default=Status.DRAFT, verbose_name="Статус")
```

### Отображение связанных полей

Добавим отображение категории:

```python
list_display = ('title', 'time_create', 'is_published', 'cat')
```

И возможность редактирования:

```python
list_editable = ('is_published', 'cat')
```

Теперь можно менять категорию статей прямо в списке.

### Настройка пагинации

Для удобства просмотра списка статей настроим количество записей на странице:

```python
list_per_page = 5
```

### Итоговая структура файлов

```
project/
│── women/
│   ├── admin.py  # Настройка отображения моделей в админке
│   ├── models.py  # Определение моделей Women и Category
│   ├── views.py  # Контроллеры (не затронуты в этом уроке)
│   ├── templates/
│   │   ├── admin/  # Шаблоны админки (если кастомизируем)
```

## 6.3 Пользовательские поля и действия в админ-панели Django

1. **Добавление пользовательского (нестандартного) поля в список статей** модели `Women`. Это поле не будет храниться в базе данных, а формироваться динамически на основе данных модели.
2. **Создание пользовательских действий** (actions), которые можно применять к выбранным записям в админ-панели.

### Определение нового поля

Перейдем в файл `women/admin.py` и в классе `WomenAdmin` определим метод, который будет генерировать дополнительную информацию о записи. Пусть он называется `brief_info`:

```python
from django.contrib import admin
from .models import Women

class WomenAdmin(admin.ModelAdmin):
    ...
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов."
```

- Метод `brief_info` принимает объект `women`, представляющий отдельную запись модели `Women`.
- Возвращает строку, содержащую длину контента статьи.
- Django автоматически передает в этот метод объект модели для каждой записи.

### Добавление метода в `list_display`

Теперь добавим этот метод в список отображаемых колонок `list_display`:

```python
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    list_editable = ('is_published', )
    ordering = ['-time_create', 'title']

    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов."
```

Теперь при обновлении админ-панели появится новый столбец **"brief_info"**.

### Задание заголовка колонки

Чтобы изменить отображаемое название колонки, используем декоратор `admin.display`:

```python
@admin.display(description="Краткое описание")
def brief_info(self, women: Women):
    return f"Описание {len(women.content)} символов."
```

Теперь в админ-панели заголовок колонки изменится на "Краткое описание".

### Сортировка по пользовательскому полю

Добавим возможность сортировки по этому полю:

```python
@admin.display(description="Краткое описание", ordering='content')
def brief_info(self, women: Women):
    return f"Описание {len(women.content)} символов."
```

Здесь `ordering='content'` указывает Django, что сортировка должна происходить на основе поля `content`.

Нельзя указывать пользовательские поля напрямую в `ordering`. Django выдаст ошибку. Сортировка возможна только на базе существующих полей модели.

### Добавление пользовательского действия

Теперь добавим в админ-панель возможность изменять статус статей на "Опубликовано".

```python
class WomenAdmin(admin.ModelAdmin):
    ...
    def set_published(self, request, queryset):
        queryset.update(is_published=Women.Status.PUBLISHED)

    actions = ['set_published']
```

- Метод `set_published` принимает два аргумента:
  - `request` — объект запроса;
  - `queryset` — набор записей, которые выбрал администратор.
- Вызывает `update()` для изменения статуса `is_published`.
- Добавляем метод в список `actions`, чтобы он появился в выпадающем списке действий.

### Изменение названия действия

Добавим декоратор `@admin.action`, чтобы изменить название действия:

```python
@admin.action(description="Опубликовать выбранные записи")
def set_published(self, request, queryset):
    queryset.update(is_published=Women.Status.PUBLISHED)
```

Теперь при выборе записей появится действие **"Опубликовать выбранные записи"**.

### Вывод сообщений после выполнения действия

Добавим отображение количества измененных записей:

```python
@admin.action(description="Опубликовать выбранные записи")
def set_published(self, request, queryset):
    count = queryset.update(is_published=Women.Status.PUBLISHED)
    self.message_user(request, f"Изменено {count} записи(ей).")
```

После выполнения команды администратор увидит сообщение о количестве обновленных записей.

### Добавление обратного действия ("Снять с публикации")

Также создадим обратное действие — снятие публикации:

```python
from django.contrib import messages

@admin.action(description="Снять с публикации выбранные записи")
def set_draft(self, request, queryset):
    count = queryset.update(is_published=Women.Status.DRAFT)
    self.message_user(request, f"{count} записи(ей) сняты с публикации!", messages.WARNING)
```

Здесь `messages.WARNING` указывает, что сообщение будет оформлено как предупреждение.

## 6.4 Панель поиска и панель фильтрации в админ-панели Django

### Добавление панели поиска

Панель поиска добавляется с помощью атрибута `search_fields` в классе `WomenAdmin`. Указываем в нем список полей, по которым следует выполнять поиск.

```python
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    list_editable = ('is_published', )
    ordering = ['-time_create', 'title']
    actions = ['set_published', 'set_draft']
    search_fields = ['title']
```

После добавления `search_fields`, при переходе в админ-панель появится поле поиска.

### Поиск по внешнему ключу

Если мы хотим добавить поиск по категориям. В `Women` есть внешний ключ `cat`. Однако если мы просто добавим его в `search_fields`:

```python
search_fields = ['title', 'cat']
```

Мы получим ошибку, так как поиск выполняется по конкретным полям, а не по самому внешнему ключу. Нам нужно указать конкретное поле связанной модели:

```python
search_fields = ['title', 'cat__name']
```

Теперь поиск будет работать по заголовкам и названиям категорий.

### Использование lookup'ов

В `search_fields` можно добавлять lookup'ы, например, искать только по началу строки:

```python
search_fields = ['title__startswith', 'cat__name']
```

Теперь поиск "Дж" покажет только записи, заголовок которых начинается с "Дж".

### Настройка панели фильтрации

Фильтрация в админ-панели добавляется с помощью атрибута `list_filter`. Например:

```python
list_filter = ['cat__name', 'is_published']
```

После обновления страницы справа появится панель фильтрации по категориям и статусу публикации.

### Создание собственного фильтра

Допустим, у нас есть поле `husband`, указывающее на мужа женщины (если он есть). Добавим фильтр для разделения записей на "Замужем" и "Не замужем".

Создадим класс фильтра перед `WomenAdmin`:

```python
class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        return queryset  # Пока фильтр ничего не делает
```

Добавляем фильтр в `list_filter`:

```python
list_filter = [MarriedFilter, 'cat__name', 'is_published']
```

После обновления страницы справа появится наш фильтр. Если кликнуть "Замужем", в URL добавится параметр `status=married`:

```
http://127.0.0.1:8000/admin/women/women/?status=married
```

#### Теперь реализуем сам фильтр:

```python
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)
```

Теперь при выборе фильтра в списке отобразятся только соответствующие записи.

## 6.5 Настройка формы редактирования записей в админ-панели Django

### Настройка списка отображаемых полей

По умолчанию Django отображает все редактируемые поля модели. Однако, если мы хотим явно задать, какие поля должны присутствовать в форме, можно использовать атрибут `fields`:

```python
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'slug']
```

В этом случае в форме отобразятся только три поля. Их порядок соответствует указанному в списке `fields`.

### Ошибка при сохранении записи

Допустим, мы пытаемся добавить новую запись:

- **title**: Екатерина Гусева
- **slug**: ekaterina-guseva
- **content**: Биография Екатерины Гусевой

После нажатия на кнопку «Сохранить» получаем ошибку, так как не заполнены обязательные поля, например, **категория** (cat). Чтобы избежать этой ошибки, добавим его в `fields`:

```python
fields = ['title', 'slug', 'content', 'cat']
```

Теперь запись успешно сохраняется.

### Исключение полей

Вместо явного указания `fields`, можно использовать атрибут `exclude`, чтобы убрать ненужные поля:

```python
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    exclude = ['tags', 'is_published']
```

Теперь на форме не будут отображаться поля **tags** и **is_published**, а остальные появятся автоматически.

### Поля только для чтения

Можно сделать некоторые поля доступными только для чтения с помощью `readonly_fields`:

```python
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'cat', 'husband']
    readonly_fields = ['slug']
```

В этом случае поле **slug** будет отображаться, но его нельзя будет редактировать.

В этом случае поле **slug** будет отображаться, но его нельзя будет редактировать.

### Автозаполнение поля slug

При добавлении новой записи поле `slug` будет пустым, и если попытаться сохранить запись дважды, возникнет ошибка из-за дублирования значений.

Мы можем исправить это, автоматически заполняя `slug` при сохранении.

Для этого переопределим метод `save()` в модели:

```python
from django.utils.text import slugify

class Women(models.Model):
    ...
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
```

Однако, `allow_unicode=True` приводит к сохранению русских символов, что может вызвать ошибки при открытии страницы. Исправить это можно с помощью функции транслитерации:

```python
def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
    return "".join(map(lambda x: d[x] if x in d else x, s.lower()))
```

И заменяем вызов `slugify(self.title, allow_unicode=True)` на:

```python
self.slug = slugify(translit_to_eng(self.title))
```

### Более простой способ автозаполнения `slug`

Он работает только в админ-панели.

В `WomenAdmin` указываем атрибут `prepopulated_fields`:

```python
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'cat', 'husband']
    prepopulated_fields = {"slug": ("title",)}
```

Теперь `slug` автоматически формируется из `title`.

### Улучшение работы с полем «Теги»

Поле **tags** связано с моделью **Tag** отношением «многие ко многим». По умолчанию Django использует список с возможностью выбора нескольких значений с зажатой клавишей **Ctrl**.

Мы можем улучшить этот интерфейс, используя `filter_horizontal`:

```python
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'cat', 'husband', 'tags']
    filter_horizontal = ['tags']
```

Также можно расположить списки вертикально, используя `filter_vertical`:

```python
filter_vertical = ['tags']
```

## 6.6 Настраиваем внешний вид админ-панели Django

### Поиск нужных шаблонов

Django использует шаблоны, расположенные в пакете `django.contrib.admin`. Основные файлы, отвечающие за структуру страницы админ-панели:

- `admin/index.html`
- `admin/base_site.html`
- `admin/base.html`
- `admin/app_list.html`

Чтобы переопределить эти файлы в нашем проекте, создадим папку `templates/admin` внутри нашего Django-приложения и поместим туда необходимые файлы.

### Создание собственного шаблона base_site.html. Создадим каталог для шаблонов

Создадим структуру папок в нашем Django-приложении:

```
sitewomen/
├── templates/
│   ├── admin/
│   │   ├── base_site.html
```

### Добавляем наш шаблон

В файл `base_site.html` скопируем содержимое оригинального шаблона, а затем внесём изменения:

```html
{% extends "admin/base.html" %} {% block title %}Моя админка{% endblock %} {%
block branding %}
<h1>Панель управления сайтом</h1>
{% endblock %}
```

Теперь при загрузке админки будет отображаться новый заголовок.

### Добавление своих CSS-стилей. Подключаем файл стилей

В `base_site.html` добавим блок `extrastyle`:

```html
{% load static %} {% block extrastyle %}
<link rel="stylesheet" href="{% static 'css/admin/admin.css' %}" />
{% endblock %}
```

### Создаём CSS-файл

Создадим новый файл `admin.css` в папке `static/css/admin`:

```
static/
├── css/
│   ├── admin/
│   │   ├── admin.css
```

Добавим в `admin.css` изменения:

```css
#header {
  background: #3f4137;
}

.module caption {
  background: #3f4137;
}

div.breadcrumbs {
  background: #6a6e5d;
}

.module h2,
.module caption,
.inline-group h2 {
  background: #6a6e5d;
}
```

Теперь заголовок админ-панели и другие элементы изменят цвет фона.

### Настройки `settings.py`

Чтобы Django мог находить статические файлы, добавим в `settings.py`:

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

# 7. Работа с формами

## 7.1 Что такое HTML-формы. Отправка данных по GET и POST-запросам

Формы являются неотъемлемой частью большинства сайтов. Они позволяют пользователям вводить данные, которые затем отправляются на сервер. Например, авторизация, регистрация, поиск, отправка сообщений и другие формы взаимодействия с сайтом.

Формы в HTML создаются с помощью тега `<form>` и могут содержать различные элементы ввода: текстовые поля, чекбоксы, списки, кнопки и т. д. Они используются для передачи данных на сервер, например, логина и пароля при входе на сайт.

### Создание формы в HTML

Рассмотрим базовую структуру формы:

```html
<form action="" method="get">
  <label for="username">Имя пользователя:</label>
  <input type="text" id="username" name="username" />

  <label for="password">Пароль:</label>
  <input type="password" id="password" name="password" />

  <button type="submit">Войти</button>
</form>
```

**Разбор кода**:

- `<form action="" method="get">` – создаёт форму, которая отправляет данные методом GET.
- `<label>` – предоставляет описание для элементов формы.
- `<input type="text">` – поле ввода текста.
- `<input type="password">` – поле ввода пароля (скрытые символы).
- `<button type="submit">` – кнопка для отправки формы.

### Отправка данных методом GET

Метод GET используется по умолчанию и передаёт данные через URL. Пример запроса после отправки формы:

```
http://example.com/login?username=admin&password=1234
```

Этот метод не подходит для отправки конфиденциальных данных (например, паролей), так как они видны в URL-адресе.

### Отправка данных методом POST

Метод POST передаёт данные в теле HTTP-запроса и не отображает их в URL. Пример формы с методом POST:

```html
<form action="" method="post">
  {% csrf_token %}
  <label for="username">Имя пользователя:</label>
  <input type="text" id="username" name="username" />

  <label for="password">Пароль:</label>
  <input type="password" id="password" name="password" />

  <button type="submit">Войти</button>
</form>
```

#### CSRF-токен

Django требует наличия `{% csrf_token %}` в формах, использующих метод POST, для защиты от межсайтовых атак (CSRF).

### Обработка данных формы в Django

#### Представление (views.py)

```python
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f"Полученные данные: {username}, {password}")
    return render(request, 'login.html')
```

**Разбор кода**:

- `request.method == 'POST'` – проверяет, что запрос выполнен методом POST.
- `request.POST.get('username')` – получает данные из формы.
- `HttpResponse` – возвращает полученные данные (в реальном приложении нужно обработать их безопасно).

## 7.2 Использование форм, не связанных с моделями в Django

Django предоставляет удобный механизм для работы с формами с помощью класса `Form`, который позволяет создавать формы без привязки к моделям. Это полезно, когда необходимо обрабатывать данные, не связанные напрямую с базой данных, например, при создании форм обратной связи, поиска или регистрации, где данные должны обрабатываться, но не сохраняться в стандартной модели Django.

### Где объявлять формы?

По традиции, формы объявляют в отдельном файле `forms.py` внутри приложения.

Создадим файл `women/forms.py` и импортируем пакет `forms`:

```python
from django import forms
from .models import Category, Husband
```

Теперь определим класс `AddPostForm`, который будет использоваться для добавления статей.

```python
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False)
```

Здесь мы определили несколько полей:

- `title`: текстовое поле.
- `slug`: поле для URL-идентификатора.
- `content`: текстовое поле с `Textarea` (многострочный ввод).
- `is_published`: флажок (по умолчанию обязательный, но мы сделали его необязательным).
- `cat`: выбор категории из модели `Category`.
- `husband`: выбор значения из модели `Husband` (необязательное поле).

### Отображение формы в шаблоне

После объявления формы ее можно передавать в представление `addpage()`.

**Например**:

```python
def addpage(request):
    form = AddPostForm()
    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})
```

Теперь подключим форму в `addpage.html`:

```html
<form action="" method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Добавить</button>
</form>
```

Здесь:

- `{% csrf_token %}` используется для защиты от CSRF-атак.
- `{{ form.as_p }}` выводит форму, оборачивая поля в `<p>`.
- `<button type="submit">` отправляет данные на сервер.

### Обработка данных формы в представлении

Теперь реализуем обработку данных формы в `addpage()`:

```python
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})
```

Как это работает?

1. При загрузке страницы отправляется `GET`-запрос, форма создается пустой.
2. При отправке данных `POST`-запросом:
   - Создается объект формы с данными `AddPostForm(request.POST)`.
   - Проверяются данные с помощью `is_valid()`.
   - Если валидация пройдена, выводится очищенный словарь данных `form.cleaned_data`.
3. Если заполнить форму неверно (например, ввести русские символы в поле `slug`), Django автоматически выведет ошибку валидации.

### Схема файлов проекта

- `women/forms.py` — определение класса формы.
- `women/views.py` — функция `addpage`, отвечающая за обработку формы.
- `women/templates/women/addpage.html` — HTML-шаблон с отображением формы.

## 7.3 Отображение полей формы. Сохранение переданных данных в БД

При создании формы в Django названия полей по умолчанию отображаются на английском языке. Чтобы изменить это, можно использовать атрибут `label` внутри определения формы:

```python
from django import forms
from .models import Category, Husband

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок")
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(), required=False, label="Контент")
    is_published = forms.BooleanField(required=False, initial=True, label="Статус")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категории")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label="Не замужем", label="Муж")
```

Дополнительно можно:

- Установить галочку `is_published` по умолчанию (`initial=True`)
- Добавить `empty_label` в `ModelChoiceField`, чтобы вместо пустого значения отображались заданные строки

### Ручное отображение полей формы

В шаблоне можно выводить форму вручную, указывая поля с их атрибутами:

```html
<label class="form-label" for="{{ form.title.id_for_label }}"
  >{{ form.title.label }}: </label
>{{ form.title }}
<div class="form-error">{{ form.title.errors }}</div>
```

Аналогично для остальных полей:

```html
<label class="form-label" for="{{ form.slug.id_for_label }}"
  >{{ form.slug.label }}: </label
>{{ form.slug }}
<div class="form-error">{{ form.slug.errors }}</div>
```

Чтобы вывести ошибки формы, связанных не с конкретными полями, добавим вверху:

```html
<div class="form-error">{{ form.non_field_errors }}</div>
```

### Отображение формы через цикл

Чтобы избежать дублирования кода, можно использовать `for`:

```html
<div class="form-error">{{ form.non_field_errors }}</div>
{% for f in form %}
<label class="form-label" for="{{ f.id_for_label }}">{{ f.label }}: </label>{{ f
}}
<div class="form-error">{{ f.errors }}</div>
{% endfor %}
```

### Настройка виджетов

Стили можно добавлять непосредственно в форму с помощью `widget`:

```python
title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label="Контент")
```

Так можно задавать классы, размеры и другие HTML-атрибуты.

### Тестирование формы

Если отправить пустую форму, Django автоматически проверяет поля:

```python
{'title': 'example', 'slug': 'example-url', 'content': '', 'is_published': True, 'cat': <Category: Актрисы>, 'husband': None}
```

Если данные некорректны (например, в `slug` введены русские буквы), будет выведено сообщение об ошибке, а форма не будет обработана.

### Сохранение данных в БД

После валидации данных можно сохранить их в БД:

```python
if form.is_valid():
    try:
        Women.objects.create(**form.cleaned_data)
        return redirect('home')
    except:
        form.add_error(None, 'Ошибка добавления поста')
```

- `form.cleaned_data` содержит проверенные данные формы
- `Women.objects.create(**form.cleaned_data)` создаёт новую запись
- В случае ошибки вызывается `form.add_error(None, 'Ошибка добавления поста')`
- После успешного добавления пользователя перенаправляет на главную страницу (`redirect('home')`).

### Итоговая схема файлов

- `forms.py`: определение формы `AddPostForm`
- `views.py`: обработка формы, валидация и сохранение
- `template.html`: отображение формы
- `models.py`: определение моделей `Women`, `Category`, `Husband`

**Связи между файлами**:

- `views.py` импортирует `AddPostForm` из `forms.py`
- `views.py` передаёт `form` в контекст шаблона `template.html`
- `models.py` содержит модели для полей формы
- `forms.py` использует `Category.objects.all()` и `Husband.objects.all()` для выбора данных в `ModelChoiceField`

## 7.4 Валидация полей формы. Создание пользовательского валидатора

Каждое поле формы проверяется на корректность данных перед тем, как они попадут в базу данных. Поля формы Django имеют встроенные параметры, позволяющие задавать различные ограничения.

Например, параметр `min_length` задает минимальную длину вводимого текста:

```python
from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=5,
        label="Заголовок",
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
```

Значение `min_length` будет проверяться как на уровне HTML, так и на уровне Django.

Если стандартные сообщения об ошибках нас не устраивают, можно задать их вручную через `error_messages`:

```python
class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=5,
        label="Заголовок",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        error_messages={
            'min_length': 'Слишком короткий заголовок',
            'required': 'Без заголовка - никак',
        }
    )
```

### Дополнительные валидаторы

Поля форм и моделей Django поддерживают атрибут `validators`, который принимает список классов-валидаторов.

Пример использования встроенных валидаторов:

```python
from django.core.validators import MinLengthValidator, MaxLengthValidator

class AddPostForm(forms.Form):
    slug = forms.SlugField(
        max_length=255,
        label="URL",
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(100),
        ]
    )
```

Если стандартные сообщения не подходят, можно задать свои:

```python
slug = forms.SlugField(
    max_length=255,
    label="URL",
    validators=[
        MinLengthValidator(5, message="Минимум 5 символов"),
        MaxLengthValidator(100, message="Максимум 100 символов"),
    ]
)
```

### Создание пользовательского валидатора

Иногда встроенных валидаторов недостаточно. В таком случае можно создать свой класс валидации.

Наш валидатор будет проверять, чтобы в поле были только русские буквы, цифры, дефис и пробел.

```python
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- "

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."

    def __call__(self, value):
        if not set(value) <= set(self.ALLOWED_CHARS):
            raise ValidationError(self.message)
```

Подключаем валидатор в форму:

```python
class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=5,
        label="Заголовок",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        validators=[RussianValidator()],
        error_messages={
            'min_length': 'Слишком короткий заголовок',
            'required': 'Без заголовка - никак',
        }
    )
```

При вводе латинских символов форма выдаст сообщение об ошибке.

### Валидация с помощью метода `clean_`

Если требуется создать валидатор только для одного поля, можно использовать метод `clean_<имя_поля>`:

```python
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5, label="Заголовок")

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- "
        if not set(title) <= set(ALLOWED_CHARS):
            raise ValidationError("Должны быть только русские символы, дефис и пробел.")
        return title
```

Этот метод вызывается автоматически во время валидации формы.

### Как работает механизм валидации в Django

1. Данные отправляются на сервер.
2. Django выполняет стандартную валидацию (например, `max_length`, `min_length`).
3. Если стандартная валидация пройдена, запускаются пользовательские валидаторы.
4. Если все проверки пройдены, данные сохраняются в БД.

## 7.5 Формы, связанные с моделями в Django

Когда форма предполагает тесное взаимодействие с моделью, лучше напрямую связать её с этой моделью.

### Использование `ModelForm`

Перейдем в файл `women/forms.py` и унаследуем `AddPostForm` от `forms.ModelForm`. Внутри объявим вложенный класс `Meta`, определяющий связь формы с моделью и список используемых полей:

```python
from django import forms
from .models import Women

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = '__all__'  # Все поля, кроме заполняемых автоматически
```

- Атрибут `model` связывает форму с моделью `Women`
- Атрибут `fields='__all__'` указывает, что форма должна включать все поля модели, кроме тех, которые заполняются автоматически

**Однако рекомендуется явно прописывать список полей**:

```python
fields = ['title', 'slug', 'content', 'is_published', 'cat', 'husband', 'tags']
```

### Настройка отображения полей формы

Для стилизации формы можно использовать атрибут `widgets` в `Meta`:

```python
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
```

### Добавление `empty_label` к спискам

Для полей выбора (`ModelChoiceField`) можно установить `empty_label`, чтобы обозначить пустое значение:

```python
from .models import Category, Husbands

class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категории")
    husband = forms.ModelChoiceField(queryset=Husbands.objects.all(), required=False, empty_label="Не замужем", label="Муж")

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'husband', 'tags']
        labels = {'slug': 'URL'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
```

### Сохранение формы в базе данных

Так как `ModelForm` автоматически создаёт метод `save()`, в `views.py` можно заменить `Women.objects.create(**form.cleaned_data)` на:

```python
form.save()
```

Функция `add_page`:

```python
def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        "menu": menu,
        "title": "Добавление статьи",
        'form': form
    }
    return render(request, "women/addpage.html", data)
```

Django также встроенно обрабатывает ошибки, например, если введён неуникальный `slug`, будет выведено соответствующее сообщение.

### Создание собственных валидаторов формы

Если встроенные проверки недостаточны, можно добавить кастомные валидаторы. Например, ограничим длину `title` до 50 символов:

```python
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')
        return title
```

### Схематическое представление структуры файлов

```
project_root/
│── women/
│   │── models.py   # Определение моделей (Women, Category, Husbands)
│   │── forms.py    # Определение формы AddPostForm
│   │── views.py    # Представление addpage(), использующее form.save()
│   │── templates/
│   │   │── women/
│   │   │   ├── addpage.html   # HTML-шаблон формы
│   │── urls.py     # Добавление маршрута для addpage
```

## 7.6 Загрузка (upload) файлов на сервер в Django

### Базовая HTML-форма для загрузки файлов

создадим HTML-форму для загрузки файлов. Эта форма будет прикреплена к существующему маршруту:

`http://127.0.0.1:8000/about/`

В шаблоне `about.html` после заголовка `<h1>` добавим следующую форму:

```html
<form action="" method="post" enctype="multipart/form-data">
  {% csrf_token %}
  <p><input type="file" name="file_upload" /></p>
  <p><button type="submit">Отправить</button></p>
</form>
```

**Обратите внимание:**

- Атрибут `enctype="multipart/form-data"` обязателен. Без него файлы не будут передаваться на сервер.
- Поле `<input type="file" name="file_upload">` позволяет пользователю выбрать файл.
- Используем `{% csrf_token %}` для защиты от CSRF-атак.

### Обработка загружаемого файла в представлении

Теперь настроим обработчик файла в представлении `about()`. В нем проверим, какие данные приходят при отправке формы. Добавим функцию `handle_uploaded_file()`, которая будет сохранять файл на сервере:

```python
def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
```

**Бывает ошибка в пути `uploads/{f.name}`. Тогда путь надо поменять**:

```python
def handle_uploaded_file(f):
    with open(f"sitewomen/uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
```

Метод `chunks()` используется для обработки больших файлов, так как он загружает их по частям, а не целиком.

Обновим представление:

```python
def about(request):
    if request.method == "POST":
        handle_uploaded_file(request.FILES['file_upload'])
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})
```

При первой попытке загрузки мы можем столкнуться с ошибкой из-за отсутствия каталога `uploads`. Создадим его вручную в корне проекта.

### Улучшение обработки загрузки с `FileField`

Наш текущий метод обработки файлов имеет ряд недостатков:

- Отсутствие валидации: если файл не выбран, возникнет ошибка.
- Отсутствие стандартного способа работы с формами Django.

**Используем Django Forms для решения этих проблем. В файле `forms.py` добавим класс**:

```python
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Файл")
```

**Обновим представление**:

```python
def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
    else:
        form = UploadFileForm()

    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu, 'form': form})
```

**Обновим шаблон `about.html`**:

```html
<form action="" method="post" enctype="multipart/form-data">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Отправить</button>
</form>
```

Теперь форма автоматически проверяет вводимые данные.

**Добавим проверку перед сохранением файла**:

```python
def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm()

    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu, 'form': form})
```

Теперь, если пользователь не выберет файл, Django выведет сообщение об ошибке.

### Уникальные имена загружаемых файлов

Проблема: файлы с одинаковыми именами будут перезаписывать друг друга. Решим это с помощью модуля `uuid`:

```python
import uuid

def handle_uploaded_file(f):
    name, ext = f.name.rsplit('.', 1)
    unique_name = f"{name}_{uuid.uuid4()}.{ext}"
    with open(f"uploads/{unique_name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
```

Теперь файлы получают уникальные имена и не затирают друг друга.

### Загрузка изображений с `ImageField`

Иногда необходимо загружать только изображения. Для этого используется `ImageField`, который является расширением `FileField`. Обновим `forms.py`:

```python
class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Изображение")
```

Теперь форма принимает только изображения, а файлы других типов будут отклонены.

## 7.7 Загрузка файлов с использованием моделей в Django

Разберём, как связать загружаемые файлы с моделями базы данных, чтобы хранить информацию о загруженных файлах, таких как имя, пользователь, загрузивший файл, дата загрузки и другие параметры.

### Определение модели для хранения файлов

Для начала создадим модель в файле `women/models.py`, которая будет хранить ссылки на загруженные файлы:

```python
from django.db import models

class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')
```

- Используется `FileField` из `models`, а не `forms`. Это поле создаёт соответствующую колонку в таблице БД.
- Параметр `upload_to='uploads_model'` указывает каталог, в который будут загружаться файлы.

После создания модели необходимо выполнить миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Обработка загрузки файлов через представления

Перейдём в `women/views.py` и изменим функцию `about()`, чтобы загружать файлы в модель:

```python
from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadFiles

def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()

    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu, 'form': form})
```

- Форма получает данные из `request.FILES`.
- После проверки данных создаётся объект модели `UploadFiles`, который сохраняет ссылку на файл в БД.
- При загрузке файла Django автоматически создаст папку `uploads_model` и сохранит туда файл. В базе данных появится запись с путём к файлу.

### Настройка глобальной директории для загружаемых файлов

В файле `settings.py` укажем единую папку для хранения загружаемых файлов:

```python
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

Теперь файлы будут загружаться в `media/uploads_model`. Чтобы проверить, удалим старые файлы и перезапустим сервер, затем загрузим новый файл.

### Добавление изображений к постам

Сейчас файлы загружаются через обычные формы, но в Django можно использовать `ModelForm`, привязанные к модели. Добавим поле `photo` в модель `Women`:

```python
class Women(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")
```

- `ImageField` автоматически проверяет, что загруженный файл — изображение.
- `upload_to="photos/%Y/%m/%d/"` создаёт подпапки по дате загрузки (год, месяц, день).

После изменений создадим и выполним миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Обновление шаблонов

В файле `addpage.html` добавим атрибут `enctype` в форму:

```html
<form method="post" enctype="multipart/form-data"></form>
```

### Обновление форм в `women/forms.py`

Включим поле `photo` в список полей формы `AddPostForm`:

```python
fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags']
```

### Изменение представления `addpage()` в `women/views.py`

Добавим обработку файлов:

```python
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})
```

Теперь файлы загружаются в `media/photos/YYYY/MM/DD/` и связываются с постами.

### Итоговая схема файлов

- `women/models.py` — создание моделей (`UploadFiles`, `Women`).
- `women/views.py` — обработка загрузки файлов в функциях `about()` и `addpage()`.
- `women/forms.py` — форма `UploadFileForm`, расширенная `AddPostForm`.
- `templates/women/addpage.html` — добавление `enctype="multipart/form-data"`.
- `settings.py` — настройка `MEDIA_ROOT` и `MEDIA_URL`.

## 7.8 Отображение загруженных изображений в HTML-документе и админ-панели

**В этом разделе мы рассмотрим, как**:

- Работать с загруженными изображениями в Django;
- Корректно отображать изображения в шаблонах;
- Подключать статические файлы в Django;
- Добавлять миниатюры изображений в админ-панель.

### Работа с полем ImageField

При загрузке изображения в модель Django оно сохраняется в виде объекта `ImageFieldFile`, который содержит несколько полезных атрибутов и методов. Один из них – `url`, который предоставляет путь к загруженному файлу.

Открываем Django Shell:

```bash
python manage.py shell_plus
```

Проверяем загруженный файл:

```python
w = Women.objects.all()[0]
print(w.photo)  # путь к файлу
print(w.photo.url)  # URL-адрес файла
```

### Отображение изображения в шаблоне post.html

Добавляем проверку наличия фото перед заголовком поста:

```html
{% if post.photo %}
<img class="img-article-left" src="{{ post.photo.url }}" />
{% endif %}
```

Если изображение не загружается, проверяем вкладку «Network» в браузере. Скорее всего, сервер не может найти загруженные файлы, поскольку не настроена раздача медиа-файлов.

### Настройка отображения медиа-файлов

В файле `settings.py` добавляем:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

В `urls.py` конфигурации проекта:

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Теперь файлы раздаются корректно в режиме отладки.

### Отображение изображений в списке постов (index.html)

Добавляем перед заголовком поста:

```html
{% if p.photo %}
<p><img class="img-article-left thumb" src="{{ p.photo.url }}" /></p>
{% endif %}
```

### Отображение миниатюр в админ-панели

В файле `admin.py` изменяем класс администратора:

```python
from django.utils.safestring import mark_safe

@admin.display(description="Изображение")
def post_photo(self, women: Women):
    if women.photo:
        return mark_safe(f"<img src='{women.photo.url}' width=50>")
    return "Без фото"
```

Добавляем `post_photo` в `list_display`:

```python
list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
```

Теперь в админке отображаются миниатюры изображений.

### Отображение миниатюры в форме редактирования

Добавляем `post_photo` в `readonly_fields`, чтобы оно не редактировалось:

```python
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'husband', 'tags']
    readonly_fields = ['post_photo']
```

# 8. Классы представлений

## 8.1 Введение в CBV (Class Based Views). Классы View и TemplateView

Классы представлений (`CBV` - `Class-Based Views`) позволяют структурировать код в объектно-ориентированном стиле.

CBV чаще применяются на практике, поскольку их использование делает код более читаемым, переиспользуемым и удобным в поддержке.

### Класс View

Все классы представлений в Django наследуются от базового класса `View`, который предоставляет базовую функциональность для обработки запросов.

Основные методы:

- `get(self, request)`: обработка GET-запросов
- `post(self, request)`: обработка POST-запросов

**Пример объявления класса View:**

```python
from django.views import View
from django.shortcuts import render, redirect
from .forms import AddPostForm

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]

class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        return render(request, 'women/addpage.html', {
            'menu': menu,
            'title': 'Добавление статьи',
            'form': form
        })

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'women/addpage.html', {
            'menu': menu,
            'title': 'Добавление статьи',
            'form': form
        })
```

### Подключение класса View к маршрутам

В файле `urls.py` добавляем маршрут:

```python
from django.urls import path
from .views import AddPage

urlpatterns = [
    path('addpage/', AddPage.as_view(), name='add_page'),
]
```

### Класс TemplateView

`TemplateView` - это CBV, который предназначен для отображения HTML-шаблона. Используется, если в представлении не требуется сложная логика обработки.

```python
from django.views.generic import TemplateView

class WomenHome(TemplateView):
    template_name = 'women/index.html'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': Women.published.all().select_related('cat'),
        'cat_selected': 0,
    }
```

### Подключаем в `urls.py`:

```python
urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
]
```

### Использование метода get_context_data

Для передачи динамических данных в шаблон можно переопределить метод `get_context_data`:

```python
class WomenHome(TemplateView):
    template_name = 'women/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        context['posts'] = Women.published.all().select_related('cat')
        context['cat_selected'] = int(self.request.GET.get('cat_id', 0))
        return context
```

## 8.2 Класс ListView в Django

Класс `ListView`, предназначен для отображения списков записей из базы данных.

### Импорт класса ListView

В начале импортируем `ListView`:

```python
from django.views.generic import ListView
```

И укажем его в качестве базового класса:

```python
class WomenHome(ListView):
    ...
```

Если запустить сервер и открыть главную страницу, появится ошибка. Это связано с тем, что `ListView` ожидает данные из базы данных. Поэтому нужно определить атрибут `model`:

```python
class WomenHome(ListView):
    model = Women
```

Это аналогично следующему SQL-запросу:

```sql
SELECT * FROM women;
```

Django автоматически ищет шаблон с именем `<имя_приложения>/<имя_модели>_list.html`, в данном случае `women/women_list.html`. Если его нет, возникнет ошибка `TemplateDoesNotExist`.

### Использование собственного шаблона

Чтобы указать конкретный шаблон, используем `template_name`:

```python
class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
```

Но теперь список статей не отображается. По умолчанию `ListView` передает записи в переменную `object_list`. Поэтому в шаблоне нужно заменить `posts` на `object_list`, либо задать собственное имя:

```python
class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
```

Теперь в шаблоне можно снова использовать `posts`.

### Передача дополнительных данных

Дополнительные данные можно передавать через `extra_context`:

```python
class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0,
    }
```

Но `extra_context` работает только для статичных данных. Для динамических значений переопределим метод `get_context_data()`:

```python
class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        context['cat_selected'] = 0
        return context
```

### Переопределение выборки записей

По умолчанию `ListView` получает все записи модели. Если нужно изменить выборку, переопределяем `get_queryset()`:

```python
class WomenHome(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.published.all().select_related('cat')
```

### Класс ListView для категорий

Создадим аналогичный `ListView` для категорий:

```python
class WomenCategory(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = f'Категория - {cat.name}'
        context['menu'] = menu
        context['cat_selected'] = cat.id
        return context

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')
```

Настроим маршрут в `urls.py`:

```python
path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category')
```

Если указать несуществующую категорию, страница будет пустой. Для отображения ошибки 404 добавим `allow_empty = False`:

```python
class WomenCategory(ListView):
    allow_empty = False
```

### Итоговая схема файлов

1. **views.py**:
   - `WomenHome(ListView)`: главная страница
   - `WomenCategory(ListView)`: категории
2. **urls.py**:
   - `path('', WomenHome.as_view(), name='home')`
   - `path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category')`
3. **templates/women/index.html**:
   - Использует `posts` вместо `object_list`

## 8.3 Класс DetailView в Django

### Объявление класса ShowPost

Создадим новый класс `ShowPost`, унаследованный от `DetailView`:

```python
class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
```

Мы здесь сразу указали два атрибута:

- `model` – указывает, с какой моделью работает представление;
- `template_name` – указывает путь к шаблону, который будет использоваться для отображения.

### Обновление маршрутов

Теперь заменим маршрут `show_post()` в файле `women/urls.py`:

```python
path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
```

### Исправление ошибки AttributeError

При попытке просмотра поста возникнет ошибка `AttributeError`. Это происходит потому, что `DetailView` ищет запись по `pk` или `slug`, а у нас маршрут использует `post_slug`. Решить проблему можно двумя способами:

1. Изменить параметр маршрута на `slug`.
2. Добавить в `ShowPost` атрибут:

```python
slug_url_kwarg = 'post_slug'
```

Если в маршруте использовался бы `id`, то потребовалось бы указать `pk_url_kwarg = 'post_id'`.

### Передача переменной в шаблон

По умолчанию `DetailView` передает в шаблон объект с именем `object` и его название в нижнем регистре (`women`). Если в шаблоне используется `post`, добавим атрибут:

```python
context_object_name = 'post'
```

Теперь переменная `post` доступна в `post.html`, и данные отображаются корректно.

### Добавление заголовка и меню

Добавим заголовок `title` и меню:

```python
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context
```

### Фильтрация опубликованных записей

Сейчас можно открыть статью независимо от её статуса публикации. Это можно исправить, переопределив метод `get_object()`:

```python
    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])
```

Метод `get_object_or_404()` ищет запись с переданным `slug` среди опубликованных записей (`Women.published`). Если запись не найдена, будет вызвана ошибка 404.

## 8.4 Класс FormView в Django

Класс `FormView` предназначен для упрощения отображения и обработки HTML-форм.

### Замена базового класса View на FormView

Ранее мы создавали класс **AddPage**, унаследованный от **View**, для отображения формы добавления статей. Однако, правильнее использовать **FormView**, так как он специально предназначен для работы с формами. Объявим новый класс:

```python
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import AddPostForm

class AddPage(FormView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
```

- `form_class` — ссылка на класс формы, используемой в представлении.
- `template_name` — путь к шаблону, в котором отображается форма.
- `success_url` — маршрут для перенаправления после успешной отправки формы.
- `reverse_lazy('home')` — используется вместо `reverse('home')`, так как `reverse()` не работает при загрузке модуля, если маршрут еще не зарегистрирован.

#### Почему `reverse_lazy`?

Функция `reverse_lazy()` позволяет избежать ошибки, возникающей при загрузке модуля, если маршрут **'home'** еще не определен. Она вычисляет маршрут **только в момент его использования**, а не заранее.

### Добавление контекста в шаблон

Если мы откроем страницу `/addpage/`, то заметим, что не отображается меню и заголовок страницы. Добавим их с помощью атрибута **extra_context**:

```python
class AddPage(FormView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Добавление статьи',
    }
```

Теперь при рендеринге шаблона будут передаваться дополнительные переменные.

### Обработка данных формы

Попробуем добавить статью, но после отправки форма не сохраняет данные в базе. Это связано с тем, что **FormView** сам по себе только отображает форму и проверяет её корректность, но не сохраняет данные. Для этого нужно переопределить метод `form_valid()`:

```python
class AddPage(FormView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Добавление статьи',
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
```

- `form_valid(self, form)`: метод вызывается после успешной проверки данных.
- `form.save()`: сохраняет данные в базу.
- `return super().form_valid(form)`: вызывает метод базового класса для выполнения стандартного поведения (перенаправления на `success_url`).

Если в форме есть дополнительные проверки, их можно выполнить перед вызовом `super().form_valid(form)`.

### Передача данных в шаблон

Django автоматически передает форму в шаблон через переменную `form`. Если в шаблоне указано другое имя переменной, форма не отобразится.

Пример кода в `addpage.html`:

```html
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Добавить</button>
</form>
```

При этом важно, чтобы в шаблоне **form** был именно таким же, как переданный Django.

### Схема взаимосвязей файлов

- `views.py`

  ```python
  from django.views.generic.edit import FormView
  from django.urls import reverse_lazy
  from .forms import AddPostForm

  class AddPage(FormView):
      form_class = AddPostForm
      template_name = 'women/addpage.html'
      success_url = reverse_lazy('home')
      extra_context = {
          'menu': menu,
          'title': 'Добавление статьи',
      }

      def form_valid(self, form):
          form.save()
          return super().form_valid(form)
  ```

- `forms.py`

  ```python
  from django import forms
  from .models import Post

  class AddPostForm(forms.ModelForm):
      class Meta:
          model = Post
          fields = ['title', 'slug', 'content', 'is_published']
  ```

- `urls.py`

  ```python
  from django.urls import path
  from .views import AddPage

  urlpatterns = [
      path('addpage/', AddPage.as_view(), name='addpage'),
  ]
  ```

- `models.py`

  ```python
  from django.db import models

  class Post(models.Model):
      title = models.CharField(max_length=255)
      slug = models.SlugField(unique=True)
      content = models.TextField()
      is_published = models.BooleanField(default=True)
  ```

- `addpage.html`

  ```html
  {% extends 'base.html' %} {% block content %}
  <h1>{{ title }}</h1>
  <form method="post">
    {% csrf_token %} {{ form.as_p }}
    <button type="submit">Добавить</button>
  </form>
  {% endblock %}
  ```

## 8.5 Классы CreateView и UpdateView в Django

Django предоставляет мощные инструменты для работы с формами и моделями в виде обобщенных классов представлений (Generic Class-Based Views, CBV). Одними из наиболее часто используемых классов являются `CreateView` и `UpdateView`, предназначенные соответственно для создания и редактирования объектов в базе данных.

### Класс CreateView

Класс `CreateView` позволяет упростить создание новых записей в базе данных, автоматически подставляя соответствующую модель и форму. Он берет на себя:

- обработку GET-запросов (выводит форму для заполнения);
- обработку POST-запросов (сохраняет данные в базу и выполняет перенаправление);
- проверку валидности формы;
- перенаправление на указанный `success_url` либо `get_absolute_url()` модели.

Рассмотрим, как можно заменить стандартный `FormView` классом `CreateView`.

```python
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Women
from .forms import AddPostForm

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Добавление статьи',
    }
```

После запуска сервера результат останется прежним.

### Использование CreateView без формы

Можно не определять `form_class`, а использовать модель напрямую:

```python
class AddPage(CreateView):
    model = Women
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
    extra_context = {
        'menu': menu,
        'title': 'Добавление статьи',
    }
```

Здесь `fields = '__all__'` означает, что в форму попадут все поля модели `Women`. Однако, если требуется ограниченный список полей, можно указать их явно:

```python
fields = ['title', 'slug', 'content', 'is_published', 'cat']
```

Если исключить обязательное поле, например `cat`, то при отправке формы возникнет ошибка.

### Класс UpdateView

`UpdateView` предназначен для редактирования существующих записей. Он работает аналогично `CreateView`, но автоматически заполняет форму данными существующего объекта.

Создадим представление для редактирования статьи:

```python
from django.views.generic import UpdateView

class UpdatePage(UpdateView):
    model = Women
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Редактирование статьи',
    }
```

Отличия от `CreateView`:

- `model` указывает, с какой таблицей работаем;
- `fields` определяет список редактируемых полей;
- форма автоматически заполняется существующими значениями из базы данных.

### Добавление маршрута для редактирования с помощью атрибута `pk`

В файле `urls.py` добавляем маршрут для редактирования:

```python
from django.urls import path
from .views import UpdatePage

urlpatterns = [
    path('edit/<int:pk>/', UpdatePage.as_view(), name='edit_page'),
]
```

Перейдя по адресу `http://127.0.0.1:8000/edit/1/`, увидим форму с загруженными данными статьи с `id=1`.

### Использование `slug` вместо `id`

Если нужно выбирать записи по `slug`, изменяем маршрут:

```python
path('edit/<slug:slug>/', UpdatePage.as_view(), name='edit_page')
```

### Схема взаимосвязей файлов:

- `views.py` – содержит классы `AddPage` и `UpdatePage`
- `urls.py` – содержит маршруты
- `models.py` – содержит модель `Women`
- `forms.py` – содержит форму `AddPostForm`
- `templates/women/addpage.html` – шаблон формы

## 8.6 Mixins как способ улучшения программного кода

Идея паттерна миксинов заключается в том, что они позволяют повторно использовать определенный функционал в разных классах, не нарушая принципы наследования.

### Пример использования миксинов

```python
class LegsMixin:
    def has_legs(self):
        return True

class CoverRectMixin:
    def cover_shape(self):
        return "rectangular"

class CoverRoundMixin:
    def cover_shape(self):
        return "round"

class BackMixin:
    def has_back(self):
        return True

class Table(LegsMixin, CoverRectMixin):
    pass

class RoundTable(LegsMixin, CoverRoundMixin):
    pass

class Chair(LegsMixin, CoverRectMixin, BackMixin):
    pass
```

### Использование миксинов в Django

В Django миксины позволяют избежать дублирования кода, добавляя общий функционал к классам представлений. Например, вынесем наполнение шаблонов стандартной информацией в отдельный миксин `DataMixin`.

### Определение DataMixin

Обычно вспомогательные классы в Django определяют в файле `utils.py`. Создадим этот файл и добавим туда следующий код:

```python
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context
```

Этот миксин определяет метод `get_mixin_context()`, который добавляет в контекст шаблона меню и другие стандартные параметры.

### Использование DataMixin в представлениях

Теперь применим этот миксин в представлениях:

```python
from django.views.generic import ListView, DetailView
from .utils import DataMixin
from .models import Women

class WomenHome(DataMixin, ListView):
    model = Women

    def get_context_data(self, *, object_list=None, **kwargs):
        return self.get_mixin_context(super().get_context_data(**kwargs), title='Главная страница', cat_selected=0)
```

Здесь `get_context_data()` вызывает `get_mixin_context()` для объединения стандартного контекста с дополнительными параметрами.

### Оптимизация с использованием extra_context

Можно ещё больше оптимизировать код, добавив поддержку `extra_context`:

```python
class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    def get_mixin_context(self, context, **kwargs):
        if self.title_page:
            context['title'] = self.title_page
        context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context
```

Теперь в представлениях можно просто указывать `title_page`:

```python
class AddPage(DataMixin, CreateView):
    model = Women
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Добавление статьи'
```

### Схема файлов

- `utils.py`:
  - Определяет `DataMixin`.
- `models.py`:
  - Определяет модель `Women`.
- `views.py`:
  - Импортирует `DataMixin` из `utils.py`.
  - Наследует представления от `DataMixin`.

## 8.7 Введение в пагинацию. Класс Paginator

«Пагинация» (от лат. pagina – страница) позволяет представлять длинные списки данных на нескольких страницах, чтобы HTML-документ не был слишком громоздким, а пользователю было удобнее ориентироваться.

### Пример работы класса Paginator

Предположим, у нас есть список имен известных женщин:

```python
women = ['Анджелина Джоли', 'Дженнифер Лоуренс', 'Джулия Робертс', 'Марго Робби', 'Ума Турман',
         'Ариана Гранде', 'Бейонсе', 'Кэтти Перри', 'Рианна', 'Шакира']
```

Допустим, мы хотим отображать их по три имени на странице.

Для начала импортируем `Paginator`:

```python
from django.core.paginator import Paginator
```

Создадим экземпляр класса `Paginator`:

```python
p = Paginator(women, 3)
```

Теперь мы можем использовать различные свойства:

```python
print(p.count)  # Число элементов в списке (10)
print(p.num_pages)  # Число страниц (4)
print(list(p.page_range))  # Итератор номеров страниц [1, 2, 3, 4]
```

Получение первой страницы:

```python
p1 = p.page(1)  # Первая страница
print(p1.object_list)  # ['Анджелина Джоли', 'Дженнифер Лоуренс', 'Джулия Робертс']
print(p1.has_next())  # True
print(p1.has_previous())  # False
print(p1.has_other_pages())  # True
print(p1.next_page_number())  # 2
```

### Использование Paginator в Django

Если в проекте Django используются функции-представления, необходимо вручную создавать объект `Paginator` и определять номер текущей страницы.

Пример кода представления `about()`:

```python
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Women

def about(request):
    contact_list = Women.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'women/about.html', {'page_obj': page_obj, 'title': 'О сайте'})
```

Здесь:

- Мы получаем все записи `Women.published.all()`.
- Создаем объект `Paginator`, передавая ему список и количество элементов на странице.
- Получаем номер текущей страницы из `GET` параметра.
- Создаем объект `page_obj`, который передаем в шаблон.

### Отображение пагинации в шаблоне

В файле `about.html`:

```django
{% for contact in page_obj %}
<p>{{ contact }}</p>
{% endfor %}
```

Чтобы отобразить ссылки на номера страниц:

```django
<nav>
    <ul>
        {% for p in page_obj.paginator.page_range %}
        <li>
            <a href="?page={{ p }}">{{ p }}</a>
        </li>
        {% endfor %}
    </ul>
</nav>
```

Этот код формирует ссылки на страницы. Переход на страницу возможен через `?page=N` в URL.

Если передать некорректный параметр (`?page=abc`), будет отображена первая страница, а при указании слишком большого номера — последняя страница.

## 8.8 Пагинация с использованием ListView в Django

В Django механизм пагинации встроен, и достаточно просто указать количество элементов на странице с помощью атрибута:

```python
paginate_by = N
```

где `N` - количество элементов на одной странице.

### Добавление пагинации в `ListView`

Создадим представление `WomenHome`, используя `ListView`, и добавим атрибут `paginate_by`:

```python
from django.views.generic import ListView
from .models import Women

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    paginate_by = 3
```

Теперь главная страница будет отображать только три записи на странице.

### Отображение пагинации в шаблоне

В `base.html` добавим блок навигации:

```html
{% block navigation %}{% endblock %}
```

Теперь, в `index.html` пропишем код для вывода номеров страниц:

```html
<nav class="list-pages">
  <ul>
    {% for p in paginator.page_range %}
    <li class="page-num">
      <a href="?page={{ p }}">{{ p }}</a>
    </li>
    {% endfor %}
  </ul>
</nav>
```

Здесь `paginator` - объект, который автоматически создаётся в шаблоне `ListView`, а `page_obj` содержит данные текущей страницы.

Теперь при обновлении страницы появятся номера страниц.

### Пагинация в категориях

Если открыть рубрики, пагинация исчезает. Это происходит, потому что в классе `WomenCategory` нет атрибута `paginate_by`.

Чтобы не дублировать код, создадим `DataMixin`, где определим `paginate_by`:

```python
class DataMixin:
    paginate_by = 3
```

Теперь можно унаследовать `WomenHome` и `WomenCategory` от `DataMixin`:

```python
class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
```

Теперь пагинация применяется ко всем страницам.

### Удаление ссылки на текущую страницу

Добавим условие в `index.html`, чтобы текущий номер страницы не был ссылкой:

```html
<nav class="list-pages">
  <ul>
    {% for p in paginator.page_range %} {% if page_obj.number == p %}
    <li class="page-num page-num-selected">{{ p }}</li>
    {% else %}
    <li class="page-num">
      <a href="?page={{ p }}">{{ p }}</a>
    </li>
    {% endif %} {% endfor %}
  </ul>
</nav>
```

### Ограничение количества номеров страниц

Если страниц много, выведем только два номера слева и справа от текущей страницы:

```html
{% for p in paginator.page_range %} {% if page_obj.number == p %}
<li class="page-num page-num-selected">{{ p }}</li>
{% elif p >= page_obj.number|add:-2 and p <= page_obj.number|add:2 %}
<li class="page-num">
  <a href="?page={{ p }}">{{ p }}</a>
</li>
{% endif %} {% endfor %}
```

### Добавление ссылок «вперед» и «назад»

Добавим ссылку на предыдущую страницу:

```html
{% if page_obj.has_previous %}
<li class="page-num">
  <a href="?page={{ page_obj.previous_page_number }}">&lt;</a>
</li>
{% endif %}
```

И на следующую:

```html
{% if page_obj.has_next %}
<li class="page-num">
  <a href="?page={{ page_obj.next_page_number }}">&gt;</a>
</li>
{% endif %}
```

### Итоговая схема файлов

- **views.py**
  - `WomenHome` (унаследован от `DataMixin` и `ListView`)
  - `DataMixin` (определяет `paginate_by`)
- **templates/base.html**
  - Блок `{% block navigation %}{% endblock %}`
- **templates/index.html**
  - Код пагинации с `paginator` и `page_obj`

# 9. Авторизация и регистрация

## 9.1 Введение в авторизацию пользователей в Django

Django предоставляет встроенные инструменты для работы с пользователями, включая их аутентификацию, авторизацию и управление сессиями.

- **Authentication (аутентификация)** – процесс проверки личности пользователя. Чаще всего это проверка пары логин/пароль.
- **Authorization (авторизация)** – процесс проверки прав доступа к закрытым частям сайта после успешной аутентификации.
- **Session (сессия)** – механизм хранения информации о пользователе между запросами, например, идентификатор пользователя.

Когда пользователь вводит логин и пароль, Django проверяет их на соответствие данным в базе. Если они совпадают, создается сессия, и все последующие запросы Django воспринимает как запросы от авторизованного пользователя.

Если пользователь не авторизован, ему будет предложена форма входа, где необходимо ввести учетные данные.

### Таблица `auth_user`

Django автоматически создает таблицы для работы с пользователями при запуске проекта. Основная из них – `auth_user`. Она содержит:

- `username` – имя пользователя
- `password` – хеш пароля
- `email` – почта
- `is_active` – активен ли пользователь
- `is_superuser` – флаг суперпользователя

Помимо `auth_user`, есть вспомогательные таблицы:

- `auth_permission` – хранит разрешения пользователей
- `auth_group` – управляет группами пользователей

Django позволяет настраивать и расширять модель пользователя, если встроенных полей недостаточно.

### Создание приложения авторизации

Разместим весь функционал авторизации в отдельном приложении `users`. Для его создания выполним команду:

```bash
python manage.py startapp users
```

Подключим его в `INSTALLED_APPS` в `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "users.apps.UsersConfig",
]
```

Также в `MIDDLEWARE` должны присутствовать:

```python
MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
]
```

### Маршруты авторизации

Создадим файл `users/urls.py` и пропишем маршруты:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
```

Теперь определим представления в `users/views.py`:

```python
from django.http import HttpResponse

def login_user(request):
    return HttpResponse("login")

def logout_user(request):
    return HttpResponse("logout")
```

Подключим маршруты `users` в главный `urls.py` проекта:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls', namespace="users")),
]
```

Добавим `app_name` в `users/urls.py`, чтобы избежать конфликтов имен:

```python
app_name = "users"
```

Теперь можно обращаться к маршруту авторизации через `users:login`.

## 9.2 Авторизация пользователей. Функции authenticate() и login()

Функции `authenticate()` и `login()` используются для проверки учетных данных пользователя и его входа в систему.

### Создание формы входа

Для начала создадим форму авторизации вручную. Добавим файл `forms.py` в приложение `users` и определим класс `LoginUserForm`:

```python
from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
```

### Создание шаблона страницы авторизации

Далее создадим шаблон для отображения формы. Внутри приложения `users` создадим каталог `templates/users` и разместим в нем файл `login.html`:

```html
{% extends 'base.html' %} {% block content %}
<h1>Авторизация</h1>

<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <p><button type="submit">Войти</button></p>
</form>
{% endblock %}
```

### Добавление представления для обработки формы

Теперь изменим функцию `login_user()` в файле `users/views.py`, чтобы передавать форму в шаблон:

```python
def login_user(request):
    form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})
```

### Реализация авторизации. Функция authenticate()

Функция `authenticate()` проверяет учетные данные пользователя. Она принимает `username` и `password`, ищет пользователя в базе данных и возвращает объект пользователя, если учетные данные верны, иначе `None`.

```python
from django.contrib.auth import authenticate

user = authenticate(request, username='user1', password='mypassword')
if user is not None:
    print("Пользователь найден")
else:
    print("Ошибка авторизации")
```

### Реализация авторизации. Функция login()

Функция `login()` выполняет вход пользователя в систему, создавая соответствующую сессию. Вызов `login(request, user)` сохраняет информацию о пользователе в сессии, позволяя ему оставаться авторизованным на сайте.

```python
from django.contrib.auth import login

if user is not None:
    login(request, user)
    print("Пользователь вошел в систему")
```

### Обновление представления login_user

Теперь обновим `login_user()`, добавив обработку данных формы:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})
```

- Проверяем, является ли запрос `POST`.
- Если форма корректна, извлекаем данные (`cleaned_data`).
- Аутентифицируем пользователя с `authenticate()`.
- Если пользователь найден и активен, выполняем вход через `login()`.
- Перенаправляем пользователя на главную страницу.

### Реализация выхода из системы

Для выхода пользователя используем функцию `logout()`, которая удаляет данные о пользователе из сессии. После вызова `logout()`, сессия пользователя завершается, и происходит перенаправление на страницу входа.

```python
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
```

### Структура файлов проекта

```
project_root/
│── users/
│   ├── forms.py        # Форма авторизации
│   ├── views.py        # Представления login_user() и logout_user()
│   ├── urls.py         # Маршруты для авторизации
│   ├── templates/
│   │   ├── users/
│   │   │   ├── login.html   # Шаблон страницы входа
│   ├── models.py       # (если потребуется расширение модели пользователя)
│
│── templates/
│   ├── base.html       # Общий базовый шаблон
│
│── project_root/
│   ├── settings.py     # Настройки проекта
│   ├── urls.py         # Глобальные маршруты
```

## 9.3 Шаблонные контекстные процессоры в Django

Мы знаем, что в Django рекомендуется делать приложения максимально независимыми друг от друга. Поэтому лучше всего отображение меню организовать в базовом шаблоне и передавать объект меню в виде списка. Это можно реализовать несколькими способами.

### Использование пользовательского тега

Создадим пользовательский тег в файле `women_tags.py`, который будет передавать список меню:

```python
from django import template
from women.utils import menu

register = template.Library()

@register.simple_tag
def get_menu():
    return menu
```

Затем используем этот тег в `base.html`:

```django
{% get_menu as menu %}
```

Теперь меню автоматически передается в шаблон, и можно убрать его передачу из класса `DataMixin` в `women/utils.py`.

### Контекстные процессоры

Однако если требуется передавать независимые данные во все шаблоны, лучше использовать **шаблонные контекстные процессоры**.

Контекстный процессор — это функция, которая возвращает словарь с данными, автоматически доступными во всех шаблонах проекта.

В `settings.py`, в списке `context_processors`, можно увидеть уже подключенные процессоры, например:

```python
'context_processors': [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]
```

### Создание собственного контекстного процессора

Создадим файл `context_processors.py` в приложении `users` и определим в нем функцию, передающую меню:

```python
from women.utils import menu

def get_women_context(request):
    return {'mainmenu': menu}
```

Добавим этот процессор в `settings.py`:

```python
'users.context_processors.get_women_context'
```

Теперь в `base.html` можно использовать `mainmenu`:

```django
{% for m in mainmenu %}
    <li><a href="{% url m.url_name %}">{{ m.title }}</a></li>
{% endfor %}
```

После этого `get_menu` можно удалить.

### Доработка главного меню

Теперь нужно доработать шаблон, убрав из меню пункт `login`, так как его будем обрабатывать отдельно. В `base.html` меню будет формироваться так:

```django
{% block mainmenu %}
<div class="header">
    <ul id="mainmenu" class="mainmenu">
        <li class="logo"><a href="{% url 'home' %}"><div class="logo"></div></a></li>
        {% for m in mainmenu %}
            <li><a href="{% url m.url_name %}">{{ m.title }}</a></li>
        {% endfor %}
        <li class="last"><a href="{% url 'users:login' %}">Войти</a></li>
    </ul>
</div>
{% endblock mainmenu %}
```

### Проверка авторизации пользователя

Доработаем меню, чтобы оно отображало имя авторизованного пользователя или предлагало войти в систему.

```django
{% if user.is_authenticated %}
    <li class="last">{{ user.username }} | <a href="{% url 'users:logout' %}">Выйти</a></li>
{% else %}
    <li class="last"><a href="{% url 'users:login' %}">Войти</a> | <a href="#">Регистрация</a></li>
{% endif %}
```

Здесь используется объект `user`, который автоматически передается в шаблон благодаря контекстному процессору `django.contrib.auth.context_processors.auth`.

## 9.4 Классы LoginView, LogoutView и AuthenticationForm

- **LoginView** — стандартный класс представления для авторизации пользователей.
- **LogoutView** — стандартный класс для выхода из системы.
- **AuthenticationForm** — стандартный класс формы обработки аутентификации.

### Класс LoginView

Класс **LoginView** заменяет написанную ранее вручную функцию `login_user()`. Реализуем его следующим образом:

```python
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class LoginUser(LoginView):
    form_class = AuthenticationForm  # Используем стандартную форму аутентификации
    template_name = 'users/login.html'  # Шаблон для отображения страницы
    extra_context = {'title': "Авторизация"}  # Дополнительные данные в шаблон
```

- `form_class = AuthenticationForm` — мы используем стандартную форму аутентификации.
- `template_name = 'users/login.html'` — указываем путь к HTML-шаблону формы входа.
- `extra_context = {'title': "Авторизация"}` — передаем дополнительный контекст в шаблон.

### Подключение маршрута

Добавим маршрут в `users/urls.py`:

```python
from django.urls import path
from .views import LoginUser

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
]
```

### Изменение адреса перенаправления после входа

По умолчанию после успешного входа пользователя перенаправляют на `http://127.0.0.1:8000/accounts/profile/`. Чтобы изменить этот адрес, переопределим метод `get_success_url`:

```python
from django.urls import reverse_lazy

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('home')  # Перенаправление на главную страницу
```

Альтернативный способ — задать в `settings.py`:

```python
LOGIN_REDIRECT_URL = 'home'
```

Дополнительно в `settings.py` можно задать:

- `LOGIN_URL = 'login'` — если пользователь не авторизован, он будет перенаправлен на страницу входа.
- `LOGOUT_REDIRECT_URL = 'home'` — перенаправление после выхода из системы.

### Улучшение формы авторизации

Класс **LoginView** обрабатывает ошибки входа и передает их в форму. Улучшим отображение ошибок в `login.html`:

```html
<div class="form-error">{{ form.non_field_errors }}</div>
{% for f in form %}
<p><label for="{{ f.id_for_label }}">{{ f.label }}:</label> {{ f }}</p>
<div class="form-error">{{ f.errors }}</div>
{% endfor %}
```

Чтобы улучшить стиль формы, создадим `users/forms.py` и определим `LoginUserForm`, расширяя `AuthenticationForm`:

```python
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
```

Можно также использовать `Meta`:

```python
from django.contrib.auth import get_user_model

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
```

### Параметр `next`

Добавим скрытое поле `next` в `login.html`:

```html
<input type="hidden" name="next" value="{{ next }}" />
```

Если URL содержит `?next=/addpage/`, пользователь после авторизации будет перенаправлен на `/addpage/`. Это полезно для интернет-магазинов, где после входа покупатель сразу попадает на страницу оформления заказа.

### Класс LogoutView

Заменим функцию `logout_user()` стандартным классом **LogoutView**:

```python
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
]
```

## 9.5 Декоратор login_required и класс LoginRequiredMixin

### Ограничение доступа к функциям представлений

В файле `women/views.py` у нас уже есть функция `about()`, которая отвечает за страницу «О сайте». Чтобы закрыть ее от неавторизованных пользователей, достаточно добавить декоратор `login_required`:

```python
from django.contrib.auth.decorators import login_required

@login_required
def about(request):
    ...  # Логика представления
```

Если теперь запустить веб-сервер и попытаться открыть эту страницу без авторизации, произойдет автоматическое перенаправление на URL:

```
http://127.0.0.1:8000/accounts/login/?next=/about/
```

Обратите внимание на параметр `next`. Благодаря ему, после успешной авторизации пользователь сразу будет перенаправлен на страницу «О сайте».

### Настройка параметра LOGIN_URL

На данный момент возникает проблема: Django выполняет автоматическое перенаправление на несуществующий URL. Чтобы исправить это, в файле `settings.py` необходимо определить параметр `LOGIN_URL`:

```python
LOGIN_URL = 'users:login'
```

Теперь, при попытке доступа к странице «О сайте», пользователь будет перенаправлен на страницу авторизации, где фреймворк автоматически добавит параметр `next`.

### Использование параметра `login_url` в декораторе

Вместо `LOGIN_URL` можно задать адрес страницы авторизации непосредственно в декораторе:

```python
@login_required(login_url='/admin/')
def about(request):
    ...  # Логика представления
```

В этом случае пользователь будет перенаправлен на страницу `/admin/`. Приоритет данного параметра выше, чем `LOGIN_URL`.

### Ограничение доступа в классах представлений. Использование LoginRequiredMixin

Когда мы имеем дело с представлениями на основе классов (`class-based views`), вместо декоратора `login_required` используется миксин `LoginRequiredMixin`.

Допустим, у нас есть представление `AddPage`, которое отвечает за добавление новых статей. Чтобы разрешить доступ только авторизованным пользователям, добавим `LoginRequiredMixin`:

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    ...  # Логика представления
```

Теперь, если неавторизованный пользователь попытается открыть эту страницу, его автоматически перенаправит на форму авторизации.

### Указание URL-адреса в `login_url`

По аналогии с декоратором `login_required`, можно задать URL-адрес для перенаправления, переопределив атрибут `login_url`:

```python
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    login_url = '/admin/'
```

Теперь доступ к странице будет открыт только после авторизации в админ-панели.

### Добавление авторства статей

Теперь, когда доступ к странице добавления статей ограничен, было бы логично привязать каждую статью к ее автору. Для этого в модели `Women` добавим поле `author`:

```python
from django.contrib.auth import get_user_model
from django.db import models

class Women(models.Model):
    ...  # Остальные поля
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True, default=None)
```

Здесь `get_user_model()` возвращает текущую модель пользователя (лучший способ работы с пользователями в Django). Параметр `on_delete=models.SET_NULL` означает, что если автор статьи будет удален, поле `author` примет значение `NULL`.

### Применение миграций

После внесения изменений в модель необходимо выполнить миграции:

```sh
python manage.py makemigrations
python manage.py migrate
```

Теперь в таблице `women` появится поле `author_id`.

### Автоматическое назначение автора

Осталось сделать так, чтобы при добавлении статьи поле `author` заполнялось автоматически. Для этого переопределим метод `form_valid()` в представлении `AddPage`:

```python
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    ...

    def form_valid(self, form):
        w = form.save(commit=False)  # Создаем объект, но не сохраняем в БД
        w.author = self.request.user  # Присваиваем текущего пользователя
        return super().form_valid(form)  # Сохраняем объект
```

Метод `form_valid()` вызывается, когда форма успешно прошла валидацию. Здесь мы:

1. Сохраняем объект `form` в памяти (`commit=False`).
2. Назначаем `author` текущего пользователя (`self.request.user`).
3. Вызываем родительский метод `form_valid()`, который завершает сохранение данных.

### Отображение автора статьи в шаблоне

Теперь, когда статьи привязаны к авторам, отобразим имя автора в шаблоне `index.html`:

```html
<p class="first">
  Категория: {{ p.cat.name }} | автор: {{ p.author.username|default:"неизвестен"
  }}
</p>
```

Если у статьи есть автор, будет отображаться его `username`. В противном случае будет показан текст «неизвестен».

## 9.6 Регистрация пользователей через функции представления

У нас уже есть ссылка "Регистрация" в меню, теперь создадим для нее маршрут, функцию представления и шаблон по аналогии с авторизацией.

### Шаблон формы регистрации: Файл: `users/templates/users/register.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>Регистрация</h1>
<form method="post">
  {% csrf_token %}
  <input type="hidden" name="next" value="{{ next }}" />
  {{ form.as_p }}
  <p><button type="submit">Регистрация</button></p>
</form>
{% endblock %}
```

Этот шаблон идентичен тому, что мы использовали для авторизации.

### Форма регистрации. Файл: `users/forms.py`

```python
from django import forms
from django.contrib.auth import get_user_model

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
```

Документация Django по модели `User`: https://docs.djangoproject.com/en/4.2/topics/auth/default/

### Функция представления. Файл: `users/views.py`

```python
from django.shortcuts import render
from .forms import RegisterUserForm

def register(request):
    form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
```

### Маршруты. Файл: `users/urls.py`

```python
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
```

### Файл: `base.html` (добавление ссылки)

```html
<li class="last">
  <a href="{% url 'users:login' %}">Войти</a> |
  <a href="{% url 'users:register' %}">Регистрация</a>
</li>
```

Запустим сервер и перейдем по ссылке "Регистрация", чтобы проверить форму.

### Проверка данных формы

Добавим метод `clean_password2()`, который проверит совпадение паролей:

```python
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password2']
```

Также проверим уникальность email:

```python
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email
```

### Реализация регистрации. Файл: `users/views.py`

Теперь реализуем логику регистрации в представлении:

```python
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
```

Пароли хранятся в зашифрованном виде (хэши), а `set_password()` кодирует их перед сохранением.

### Завершение регистрации. Файл: `users/templates/users/register_done.html`

```html
{% extends 'base.html' %} {% block content %}
<h1>Добро пожаловать!</h1>
<p>
  Вы успешно зарегистрировались! Для входа перейдите по
  <a href="{% url 'users:login' %}">ссылке</a>.
</p>
{% endblock %}
```

### Схема файловой структуры

```
project/
│── users/
│   ├── templates/
│   │   ├── users/
│   │   │   ├── register.html
│   │   │   ├── register_done.html
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│── templates/
│   ├── base.html
```

## 9.7 Класс UserCreationForm

Переход от функции представления `register()` к классу представления, а также разберем использование стандартного класса `UserCreationForm` для создания нового пользователя.

### Определение формы регистрации

Перейдем в файл `users/forms.py` и создадим класс `RegisterUserForm` на основе `UserCreationForm`:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email
```

- **Наследование от `UserCreationForm`**

  - `UserCreationForm` – встроенная форма Django для регистрации нового пользователя.
  - Мы расширяем ее, добавляя кастомные поля и валидацию.

- **Настройка отображения полей формы**

  - Используем `forms.CharField`, `forms.PasswordInput` для изменения внешнего вида.
  - Атрибут `widget=forms.TextInput(attrs={'class': 'form-input'})` задает CSS-класс, который позволит стилизовать поля формы.

- **Метод `clean_email`**
  - Проверяет, существует ли уже указанный email в базе.
  - Если email занят, выбрасывает `ValidationError`.

### Улучшение шаблона формы

Шаблон `register.html`:

```html
<form method="post">
  {% csrf_token %}
  <input type="hidden" name="next" value="{{ next }}" />
  <div class="form-error">{{ form.non_field_errors }}</div>
  {% for f in form %}
  <p>
    <label class="form-label" for="{{ f.id_for_label }}">{{ f.label }}:</label>
    {{ f }}
  </p>
  <div class="form-error">{{ f.errors }}</div>
  {% endfor %}
  <p><button type="submit">Регистрация</button></p>
</form>
```

### Создание представления регистрации

Заменим функцию представления `register` на класс `RegisterUser`. Перейдем в `users/views.py` и добавим:

```python
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': "Регистрация"}
```

- **Наследование от `CreateView`**

  - `CreateView` – обобщенное представление Django для создания объектов модели.
  - Само обрабатывает валидацию формы и сохранение в базу данных.

- **`form_class = RegisterUserForm`**

  - Указываем, что используем нашу кастомную форму `RegisterUserForm`.

- **`template_name = 'users/register.html'`**

  - Определяет, какой HTML-шаблон использовать для отображения формы.

- **`success_url = reverse_lazy('users:login')`**

  - После успешной регистрации пользователя перенаправляет на страницу входа.

- **`extra_context = {'title': "Регистрация"}`**

  - Передает в шаблон дополнительный контекст с заголовком страницы.

-

### Настройка маршрута

Добавим маршрут в `users/urls.py`:

```python
from django.urls import path
from .views import RegisterUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
]
```

### Структура файлов и импортов

```
users/
│── forms.py  # Определение кастомной формы RegisterUserForm
│── views.py  # Создание представления RegisterUser на основе CreateView
│── urls.py   # Определение маршрута для регистрации
│── templates/
│   ├── users/
│   │   ├── register.html  # Шаблон формы регистрации
```

## 9.8 Авторизация через email. Профайл пользователя

### Базовый механизм аутентификации в Django

По умолчанию Django использует `ModelBackend` для аутентификации пользователей по паре логин (username) и пароль (password).

В файле `settings.py` можно явно указать используемый бэкенд аутентификации:

```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
```

Класс `ModelBackend` наследуется от `BaseBackend`, который определяет два ключевых метода:

- `authenticate(request, username=None, password=None, **kwargs)`: выполняет аутентификацию пользователя по `username` и `password`. Возвращает объект пользователя либо `None`, если пользователь не найден.
- `get_user(user_id)`: получает объект пользователя по `user_id`.

### Создание собственного бэкенда аутентификации по E-mail

Мы создадим свой бэкенд, позволяющий входить в систему по адресу электронной почты. Для этого создадим файл `authentication.py` в приложении `users` и определим класс `EmailAuthBackend`:

```python
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None
```

Теперь подключим наш бэкенд в `settings.py`:

```python
AUTHENTICATION_BACKENDS = [
    'users.authentication.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```

### Добавление метода `get_user()`

```python
    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
```

Теперь пользователи смогут входить в систему по E-mail.

### Создание профиля пользователя. Определение шаблона профиля

Создадим файл `users/templates/users/profile.html`:

```html
{% extends 'base.html' %} {% block content %}
<h1>Профиль</h1>
<form method="post">
  {% csrf_token %}
  <div class="form-error">{{ form.non_field_errors }}</div>
  {% for f in form %}
  <p><label for="{{ f.id_for_label }}">{{ f.label }}:</label> {{ f }}</p>
  <div class="form-error">{{ f.errors }}</div>
  {% endfor %}
  <p><button type="submit">Сохранить</button></p>
</form>
{% endblock %}
```

### Определение формы `ProfileUserForm`

```python
from django import forms
from django.contrib.auth import get_user_model

class ProfileUserForm(forms.ModelForm):
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }
```

### Определение представления `ProfileUser`

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import ProfileUserForm

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
```

### Определение маршрута `users/urls.py`

```python
from django.urls import path
from .views import ProfileUser

app_name = 'users'
urlpatterns = [
    path('profile/', ProfileUser.as_view(), name='profile'),
]
```

### Добавление ссылки в меню `base.html`

```html
<li class="last">
  <a href="{% url 'users:profile' %}">{{ user.email }}</a> |
  <a href="{% url 'users:logout' %}">Выйти</a>
</li>
```

### Схема файлов и импортов

- **`authentication.py`** → `EmailAuthBackend`
- **`settings.py`** → `AUTHENTICATION_BACKENDS`
- **`forms.py`** → `ProfileUserForm`
- **`views.py`** → `ProfileUser`
- **`urls.py`** → `path('profile/', ProfileUser.as_view(), name='profile')`
- **`profile.html`** → шаблон профиля

## 9.9 Изменение пароля пользователя в Django: PasswordChangeView и PasswordChangeDoneView

В данном уроке мы добавим этот функционал, используя классы представлений Django.

### Классы Django для смены пароля

Django предоставляет два встроенных класса для изменения пароля пользователя:

- `PasswordChangeView` — обрабатывает форму смены пароля.
- `PasswordChangeDoneView` — отображает страницу успешного изменения пароля.

### Настройка маршрутов

По умолчанию `PasswordChangeView` использует:

- шаблон: `registration/password_change_form.html`
- класс формы: `PasswordChangeForm`
- редирект на маршрут с именем `password_change_done`

Настроим маршруты в `users/urls.py`:

```python
from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/<int:pk>/', views.ProfileUser.as_view(), name='profile'),
]
```

### Добавление ссылки в шаблон профиля

В файле `users/templates/users/profile.html` добавим ссылку для смены пароля:

```html
<hr />
<p><a href="{% url 'password_change' %}">Сменить пароль</a></p>
```

После этого, при переходе по ссылке, мы попадем в стандартную форму смены пароля Django, но нам нужна своя кастомная форма.

### Создание шаблона формы смены пароля

Создадим файл `users/templates/users/password_change_form.html` со следующим содержимым:

```html
{% extends 'base.html' %} {% block content %}
<h1>Изменение пароля</h1>
<form method="post">
  {% csrf_token %}
  <div class="form-error">{{ form.non_field_errors }}</div>
  {% for f in form %}
  <p>
    <label class="form-label" for="{{ f.id_for_label }}">{{ f.label }}: </label
    >{{ f }}
  </p>
  <div class="form-error">{{ f.errors }}</div>
  {% endfor %}
  <p><button type="submit">Изменить пароль</button></p>
</form>
{% endblock %}
```

### Создание кастомной формы смены пароля

Определим свою форму на основе `PasswordChangeForm`, изменив отображение полей:

```python
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
```

### Создание представления для смены пароля

Теперь создадим собственное представление, использующее новую форму и перенаправляющее пользователя после успешного изменения пароля:

```python
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': "Изменение пароля"}
```

Подключим его в маршруты:

```python
path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
```

### Создание шаблона успешного изменения пароля

Создадим файл `users/templates/users/password_change_done.html`:

```html
{% extends 'base.html' %} {% block content %}
<h1>Пароль успешно изменен!</h1>
<p>
  Вы успешно изменили пароль.
  <a href="{% url 'profile' %}">Вернуться в профиль.</a>
</p>
{% endblock %}
```

### Настройка представления для успешной смены пароля

Обновим маршрут `password_change_done`:

```python
path('password-change/done/', PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
```

### Итоговая схема взаимодействия файлов

- **Маршруты (`urls.py`)**:
  - `password-change/` → `UserPasswordChange`
  - `password-change/done/` → `PasswordChangeDoneView`
- **Представления (`views.py`)**:
  - `UserPasswordChange` использует `UserPasswordChangeForm` и шаблон `password_change_form.html`
- **Формы (`forms.py`)**:
  - `UserPasswordChangeForm` основан на `PasswordChangeForm`
- **Шаблоны (`templates/users/`)**:
  - `password_change_form.html` — форма смены пароля
  - `password_change_done.html` — подтверждение смены пароля

## 9.10 Восстановление пароля. Идея алгоритма

### Последовательность действий

1. Пользователь нажимает на ссылку «Забыли пароль?», которая ведет на маршрут `password-reset/`.
2. Открывается страница с формой для ввода email-адреса, привязанного к аккаунту.
3. После отправки формы пользователь перенаправляется на страницу `password-reset/done/`, где отображается уведомление о том, что письмо отправлено.
4. В почтовом ящике пользователь получает письмо со специальной ссылкой для восстановления пароля.
5. При переходе по ссылке открывается страница `password-reset-confirm/uidb64/token/`, где пользователь вводит новый пароль.
6. После успешного изменения пароля происходит редирект на страницу `password-reset-complete/`, сообщающую об успешном изменении пароля.

Таким образом, если пользователь помнит email и имеет доступ к почтовому ящику, он может восстановить доступ к аккаунту.

### Настройка консольного почтового бэкенда

Для тестирования отправки писем в процессе разработки настроим Django так, чтобы письма отображались в консоли. Это удобно, так как не требует реального почтового сервера.

В файле `settings.py` добавляем:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

По умолчанию Django использует `SMTP backend`, но мы пока оставим консольный бэкенд.

### Проверка работы почтового бэкенда

Запускаем Django shell:

```sh
python manage.py shell
```

Импортируем функцию `send_mail`:

```python
from django.core.mail import send_mail
```

Отправляем тестовое письмо:

```python
send_mail(
    "Восстановление пароля",
    "Перейдите по ссылке для восстановления пароля.",
    "admin@mysite.com",
    ["user@example.com"],
)
```

В консоли отобразится следующее сообщение:

```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
To: user@example.com
Date: Sun, 10 Feb 2025 12:00:00 -0000
Message-ID: <123456@mysite.com>

Перейдите по ссылке для восстановления пароля.
```

## 9.11 Реализация алгоритма восстановления пароля в Django

Для реализации будем использовать встроенные классы Django:

- `PasswordResetView`
- `PasswordResetDoneView`
- `PasswordResetConfirmView`
- `PasswordResetCompleteView`

Также создадим соответствующие шаблоны и обновим маршруты в `urls.py`.

### Создание шаблонов форм

Создадим шаблон формы для запроса восстановления пароля `password_reset_form.html`:

```html
{% extends 'base.html' %} {% block content %}
<h1>Восстановление пароля</h1>
<form method="post">
  {% csrf_token %} {% for f in form %}
  <p>
    <label class="form-label" for="{{ f.id_for_label }}">{{ f.label }}: </label>
    {{ f }}
  </p>
  <div class="form-error">{{ f.errors }}</div>
  {% endfor %}
  <p><button type="submit">Сбросить по E-mail</button></p>
</form>
{% endblock %}
```

Создадим шаблон `password_reset_done.html`, который отображается после отправки email:

```html
{% extends "base.html" %} {% block content %}
<h1>Сброс пароля</h1>
<p>Инструкции по сбросу пароля отправлены на вашу почту.</p>
<p>Если письмо не пришло, проверьте папку "Спам".</p>
{% endblock %}
```

### Добавление маршрутов в `urls.py`

В файле `users/urls.py` добавим маршруты:

```python
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    path('password-reset/',
         PasswordResetView.as_view(template_name="users/password_reset_form.html"),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),
]
```

Добавим ссылку на восстановление пароля в `login.html`:

```html
<p><a href="{% url 'users:password_reset' %}">Забыли пароль?</a></p>
```

Запустим сервер и проверим форму. При отправке формы получим ошибку, что маршрут `password_reset_confirm` не определен. Добавим недостающие маршруты.

### Создание шаблонов для сброса пароля

Создадим `password_reset_confirm.html` для ввода нового пароля:

```html
{% extends 'base.html' %} {% block content %}
<h1>Новый пароль</h1>
<form method="post">
  {% csrf_token %}
  <div class="form-error">{{ form.non_field_errors }}</div>
  {% for f in form %}
  <p>
    <label class="form-label" for="{{ f.id_for_label }}">{{ f.label }}: </label>
    {{ f }}
  </p>
  <div class="form-error">{{ f.errors }}</div>
  {% endfor %}
  <p><button type="submit">Сохранить</button></p>
</form>
{% endblock %}
```

Создадим `password_reset_complete.html`:

```html
{% extends 'base.html' %} {% block content %}
<h1>Пароль изменен</h1>
<p>
  Вы успешно сменили пароль. Теперь можете
  <a href="{% url 'users:login' %}">войти</a>.
</p>
{% endblock %}
```

Обновим `users/urls.py`, добавив недостающие маршруты:

```python
path('password-reset/<uidb64>/<token>/',
     PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
     name='password_reset_confirm'),
path('password-reset/complete/',
     PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
     name='password_reset_complete'),
```

### Обновление email-шаблона

Ошибка `NoReverseMatch` возникает из-за стандартного `password_reset_email.html`, который использует тег:

```html
{% url 'password_reset_confirm' uidb64=uid token=token %}
```

Обновим шаблон, добавив пространство имен:

```html
{{ protocol }}://{{ domain }}{% url 'users:password_reset_confirm' uidb64=uid
token=token %}
```

Обновим маршрут `PasswordResetView`, добавив `email_template_name` и `success_url`:

```python
path('password-reset/',
     PasswordResetView.as_view(
         template_name="users/password_reset_form.html",
         email_template_name="users/password_reset_email.html",
         success_url=reverse_lazy("users:password_reset_done")
     ),
     name='password_reset'),
```

Обновим `PasswordResetConfirmView`, добавив `success_url`:

```python
path('password-reset/<uidb64>/<token>/',
     PasswordResetConfirmView.as_view(
         template_name="users/password_reset_confirm.html",
         success_url=reverse_lazy("users:password_reset_complete")
     ),
     name='password_reset_confirm'),
```

После этого можно повторить процесс сброса пароля и убедиться, что все работает корректно.

### Итоговая схема файлов

1. **Шаблоны (`users/templates/users/`)**:

   - `password_reset_form.html` – форма ввода email
   - `password_reset_done.html` – сообщение об отправке email
   - `password_reset_confirm.html` – форма ввода нового пароля
   - `password_reset_complete.html` – сообщение об успешном изменении пароля
   - `password_reset_email.html` – шаблон письма

2. **Маршруты (`users/urls.py`)**:

   - `password-reset/` → `PasswordResetView`
   - `password-reset/done/` → `PasswordResetDoneView`
   - `password-reset/<uidb64>/<token>/` → `PasswordResetConfirmView`
   - `password-reset/complete/` → `PasswordResetCompleteView`

3. **Обновления в `login.html`**:
   - Добавлена ссылка на восстановление пароля.

## 9.12 Настройка почтового сервера по SMTP-протоколу

В качестве примера рассмотрим использование почтового сервера компании Яндекс.

### Разрешение работы почтовых клиентов с аккаунтом

Первым делом в аккаунте почты Яндекса перейдите в расширенные настройки и далее в «Почтовые программы». Поставьте галочки в разделе «Разрешить доступ к почтовому ящику с помощью почтовых клиентов»:

1. Откройте Яндекс.Почту.
2. Перейдите в настройки почты.
3. Откройте раздел «Почтовые программы».
4. Активируйте опцию «Разрешить доступ к почтовому ящику с помощью почтовых клиентов».

### Генерация пароля для приложения

Чтобы избежать ошибки аутентификации и правильно настроить SMTP для Яндекс.Почты, необходимо сгенерировать пароль для приложения. Этот пароль позволит Django аутентифицироваться на сервере Яндекса.

1. Перейдите в свой Яндекс ID по ссылке: [id.yandex.ru/security/app-passwords](https://id.yandex.ru/security/app-passwords)
2. В разделе «Пароли приложений» выберите «Почта».
3. Введите название приложения, например, `DjangoApp`.
4. Система сгенерирует пароль — **обязательно сохраните его**, так как он показывается только один раз.

### Настройка параметров SMTP в Django

После получения пароля, укажем настройки почтового сервера в файле `settings.py`:

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "djangocourse@yandex.ru"
EMAIL_HOST_PASSWORD = "ваш_сгенерированный_пароль"
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER
```

#### Разбор параметров:

- `EMAIL_BACKEND` — определяет используемый бэкенд отправки почты.
- `EMAIL_HOST` — SMTP-сервер Яндекса.
- `EMAIL_PORT` — порт 465 используется для безопасного соединения (SSL).
- `EMAIL_HOST_USER` — почтовый адрес, с которого отправляются письма.
- `EMAIL_HOST_PASSWORD` — сгенерированный пароль для приложения.
- `EMAIL_USE_SSL` — включает SSL для безопасного соединения.
- `DEFAULT_FROM_EMAIL`, `SERVER_EMAIL`, `EMAIL_ADMIN` — задают отправителя писем.

Больше информации можно найти в документации Django:
[https://docs.djangoproject.com/en/4.2/topics/email/#email-backends](https://docs.djangoproject.com/en/4.2/topics/email/#email-backends)

### Проверка восстановления пароля

После настройки SMTP, протестируем форму восстановления пароля в Django. Для этого:

1. Перейдите на страницу:
   ```
   http://127.0.0.1:8000/users/password-reset/
   ```
2. Введите email, который есть в базе данных.
3. Нажмите «Сбросить пароль».
4. Откройте почту и проверьте письмо со ссылкой на восстановление.
5. Перейдите по ссылке и установите новый пароль.
6. Попробуйте войти с новым паролем.

Если все прошло успешно, значит, SMTP-бэкенд настроен правильно.
