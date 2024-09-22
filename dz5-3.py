'''
Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл,
переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад,
INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент
командного рядка, щоб отримати всі записи цього рівня.

Вимоги до завдання:

Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. 
Він відповідає за виведення всіх записи певного рівня логування. І приймає значення відповідно до рівня 
логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування
(INFO, ERROR, DEBUG, WARNING).
Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. 
Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. 
Вона приймає результати виконання функції count_logs_by_level.

Критерії оцінювання:

Скрипт виконує всі зазначені вимоги, правильно аналізуючи лог-файли та виводячи інформацію.
Скрипт коректно обробляє помилки, такі як неправильний формат лог-файлу або відсутність файлу.
При розробці обов'язково було використано один з елементів функціонального програмування: 
лямбда-функція, списковий вираз, функція filter, тощо.
Код добре структурований, зрозумілий і містить коментарі там, де це необхідно.
'''
import os
import sys
from collections import Counter

path = r'C:\PythonProject\PythonCoreCourse\dz4\logs.txt'


def load_logs(file_path: str) -> list:
    if not os.path.exists(path):
        input("Файл не існує або шлях до нього вказан невірно")
        sys.exit()
    logs_line = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = parse_log_line(line)
                logs_line.append(line)
    except:
        input('Нажаль файл пошкоджено, або його формат не підтримується')
        sys.exit()
    return logs_line


def parse_log_line(line: str) -> dict:
    log_keys = ['date', 'time', 'level', 'message']
    log_items = line.split()
    result = dict(zip(log_keys, log_items))
    return result


def filter_logs_by_level(logs: list, level: str) -> list:
    def check_level(logs):
        if logs['level'] == level:
            return True
        return False
    result = list(filter(check_level, logs))
    return result


def count_logs_by_level(logs: list) -> dict:
    level_list = [i['level'] for i in logs]
    result = dict(Counter(level_list))
    return result


def display_log_counts(counts: dict) -> None:
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for key, value in counts.items():
        print(f'{key:<17}' + '|', f'{value:<10}')


def display_logs_by_levels(logs: list, level: str) -> None:
    print(f'\nДеталі логів для рівня {level}')
    for log in logs:
        print(f'{log['date']} {log['time']} - {log['message']}')


def main():
    if len(sys.argv) == 1:
        input("Шлях до файлу логів не вказано. Нажміть Enter для виходу")
        sys.exit()
    elif len(sys.argv) == 2:
        file_path, error_level = sys.argv[1], None
    elif len(sys.argv) == 3:
        file_path, error_level = sys.argv[1], sys.argv[2].upper()

    logs_list = load_logs(file_path)
    count_level = count_logs_by_level(logs_list)
    display_log_counts(count_level)

    if error_level:
        level_logs_list = filter_logs_by_level(logs_list, error_level)
        display_logs_by_levels(level_logs_list, error_level)
    # input()


if __name__ == "__main__":
    main()

'''
Що сі маєм отримати
Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1
'''
