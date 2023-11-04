# TODO Напишите функцию calculate_average_age для расчета среднего возраста студентов

def calculate_average_age(students_dict):
    # print(students_dict)
    length = len(students_dict.values())
    sum_age = sum(students_dict.values())
    average = sum_age / length
    return average

students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

print(f"Средний возраст студентов: {calculate_average_age(students_dict)}")  # TODO Распечатайте средний возраст студентов
