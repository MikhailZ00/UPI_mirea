import csv


def get_teachers():
    teachers = set() # создаем множество для хранения уникальных ФИО преподавателей
    with open('classes.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            teachers.add(row[' ФИО преподавателя']) # добавляем ФИО преподавателя в множество
    return teachers


# Пример использования
teachers = get_teachers()
print("ФИО преподавателей:")
for teacher in teachers:
    print(teacher)
