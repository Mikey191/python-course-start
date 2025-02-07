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
