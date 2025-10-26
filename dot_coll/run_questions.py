import json
import random
import os

# Пути к файлам
QUESTIONS_FILE = "questions.json"
STUDENTS_FILE = "students.json"
OUTPUT_DIR = "questions"

# Загружаем вопросы
with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    questions_data = json.load(f)[0]  # Внутри массива один объект
    easy_questions = questions_data["easy"]
    normal_questions = questions_data["normal"]
    hard_questions = questions_data["hard"]

# Загружаем список студентов
with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
    students = json.load(f)[0]

# Создаём папку для сохранения файлов, если её нет
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Для каждого студента формируем уникальный файл с вопросами
for student in students:
    # Выбираем 5 случайных вопросов из каждой категории
    selected_easy = random.sample(easy_questions, 5)
    selected_normal = random.sample(normal_questions, 5)
    selected_hard = random.sample(hard_questions, 5)

    # Объединяем всё в один список
    all_questions = (
        ["\n--- EASY ---\n"] + selected_easy +
        ["\n--- NORMAL ---\n"] + selected_normal +
        ["\n--- HARD ---\n"] + selected_hard
    )

    # Формируем имя файла
    last_name = student.split()[0]
    first_name = student.split()[1]
    file_name = f"{last_name+first_name}.txt"
    file_path = os.path.join(OUTPUT_DIR, file_name)

    print(all_questions)
    # Записываем в файл
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Студент: {student}\n")
        f.write("=" * 50 + "\n")
        i = 1
        for q in all_questions:
            if not q.startswith("\n---"):
                f.write(f"{i}. {q}\n")
                i += 1
            else:
                f.write(q + "\n")

print(f"✅ Сгенерировано {len(students)} файлов в папке '{OUTPUT_DIR}'.")
