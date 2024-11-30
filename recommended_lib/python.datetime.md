# Библиотека `datetime`

## Что делает эта библиотека?

**Библиотека `datetime`** предоставляет **классы и функции** для работы с **датами и временем**. Она позволяет **выполнять операции с датами**, **форматировать их**, **вычислять временные интервалы** и **преобразовывать их в удобные форматы**.

## Классы:

- `datetime.datetime`: **Представляет дату и время** (включает год, месяц, день, часы, минуты, секунды и микросекунды).
- `datetime.date`: **Представляет только дату** (год, месяц, день).
- `datetime.time`: **Представляет только время** (часы, минуты, секунды и микросекунды).
- `datetime.timedelta`: **Используется для представления разницы между двумя моментами времени**.

## Часто используемые методы:

- `datetime.now()`: **Возвращает текущие дату и время**.
- `datetime.today()`: **Возвращает текущую дату**.
- `datetime.strptime(string, format)`: **Преобразует строку в объект datetime на основе указанного формата**.
- `datetime.strftime(format)`: **Преобразует объект datetime в строку с указанным форматом**.
- `datetime.combine(date, time)`: **Объединяет дату и время в объект datetime**.

## Функции для работы с интервалами:

- `timedelta(days=0, seconds=0, ...)`: Создает интервал времени.
- `Операции с timedelta` (сложение, вычитание).

## Часто используемые атрибуты:

- `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`: **Атрибуты объектов datetime или date**.
- `weekday()`: Возвращает день недели (0 — понедельник, 6 — воскресенье).

## Пример использования. Автоматизация сроков сдачи проекта.

Рассчитывает дату сдачи проекта.

- `start_date`: строка в формате `'YYYY-MM-DD'` (дата начала проекта).
- `duration_days`: количество дней на выполнение проекта.
- `return`: строка с рассчитанной датой завершения.

    ```python
    from datetime import datetime, timedelta

    def calculate_deadline(start_date, duration_days):
        # Преобразуем строку в объект datetime
        start = datetime.strptime(start_date, "%Y-%m-%d")
        # Рассчитываем дату завершения
        deadline = start + timedelta(days=duration_days)
        # Форматируем результат
        return deadline.strftime("Дата завершения: %d.%m.%Y")

    # Пример вызова функции
    start_date = "2024-11-01"
    duration_days = 30
    print(calculate_deadline(start_date, duration_days))
    ```

## Пример использования. Проверка времени выполнения скрипта

```python
from datetime import datetime

def heavy_computation():
    for _ in range(10**6):
        pass

# Фиксируем стартовое время
start_time = datetime.now()

# Выполняем задачу
heavy_computation()

# Фиксируем конечное время
end_time = datetime.now()

# Рассчитываем разницу во времени
execution_time = end_time - start_time

print(f"Скрипт выполнился за {execution_time}.")
```

## Пример использования. Напоминание о событиях.

Устанавливает напоминание за 10 минут до события.

- `event_time_str`: строка с временем события в формате `'YYYY-MM-DD HH:MM:SS'`.

    ```python
    from datetime import datetime, timedelta

    def schedule_reminder(event_time_str):
        # Преобразуем строку в объект datetime
        event_time = datetime.strptime(event_time_str, "%Y-%m-%d %H:%M:%S")
        # Рассчитываем время напоминания
        reminder_time = event_time - timedelta(minutes=10)

        print(f"Напоминание установлено на {reminder_time.strftime('%d.%m.%Y %H:%M:%S')}.")

    # Пример
    event_time = "2024-11-18 15:30:00"
    schedule_reminder(event_time)
    ```

## Чем полезна datetime?
- **Работа с датами и временем в реальном мире**, например, автоматизация расписаний, расчет сроков, напоминания.
- **Удобное форматирование для взаимодействия с пользователем и базами данных**.
- **Вычисления временных интервалов для отчетов и аналитики**.