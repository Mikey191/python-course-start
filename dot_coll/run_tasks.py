import json
import random
from pathlib import Path

# Пути к файлам
TASKS_FILE = "tasks.json"
STUDENTS_FILE = "students.json"
OUTPUT_DIR = Path("students_tasks")

# Создаём папку для файлов, если её нет
OUTPUT_DIR.mkdir(exist_ok=True)

# Загружаем задачи
with open(TASKS_FILE, "r", encoding="utf-8") as f:
    tasks_data = json.load(f)

# Загружаем студентов
with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
    students = json.load(f)[1]  # внутри списка

# Функция выбора случайных задач
def get_random_tasks(task_list, count):
    return random.sample(task_list, count)

# Для каждого студента создаём файл
for full_name in students:
    # Разделяем ФИО
    parts = full_name.split()
    last_name = parts[0]
    first_name = parts[1]
    patronymic = parts[2] if len(parts) > 2 else ""

    # Имя файла
    filename = f"{last_name}{first_name}.txt"
    file_path = OUTPUT_DIR / filename

    # Выбираем задачи
    easy_tasks = get_random_tasks(tasks_data["easy"], 5)
    medium_tasks = get_random_tasks(tasks_data["medium"], 4)
    hard_tasks = get_random_tasks(tasks_data["hard"], 2)

    # Формируем содержимое
    content_lines = [
        f"Студент: {full_name}\n",
        "Легкие задачи:",
    ]
    for i, task in enumerate(easy_tasks, start=1):
        content_lines.append(f"{i}. {task['task']}")

    content_lines.append("\nСредние задачи:")
    for i, task in enumerate(medium_tasks, start=1):
        content_lines.append(f"{i}. {task['task']}")

    content_lines.append("\nТяжелые задачи:")
    for i, task in enumerate(hard_tasks, start=1):
        content_lines.append(f"{i}. {task['task']}")

    # Записываем в файл
    with open(file_path, "w", encoding="utf-8") as out:
        out.write("\n".join(content_lines))

print(f"✅ Файлы успешно созданы в папке: {OUTPUT_DIR.resolve()}")
