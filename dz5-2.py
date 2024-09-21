'''
Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, 
що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, 
чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, 
яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

Вимоги до завдання:
Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, 
що ітерує по всіх дійсних числах у тексті. Дійсні числа у тексті вважаються записаними без помилок
і чітко відокремлені пробілами з обох боків.

Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers для обчислення
загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.

Рекомендації для виконання:
Використовуйте регулярні вирази для ідентифікації дійсних чисел у тексті, з урахуванням,
що числа чітко відокремлені пробілами.
Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
Переконайтеся, що sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа.

Критерії оцінювання:
Правильність визначення та повернення дійсних чисел функцією generator_numbers.
Коректність обчислення загальної суми в sum_profit.
Чистота коду, наявність коментарів та відповідність стилю кодування PEP8.
'''
import re
from typing import Callable, Generator

# оскільки в умові дз зьявились аннотації. використаємо їх для покращення сприйняття коду третіми особами


def generator_numbers(text: str) -> Generator:
    # знайдемо всі дійсні числа в тексті
    incomes = re.findall(' \d+.\d+ ', text)
    # створимо генератор з отриманого списку
    for come in incomes:
        yield come.strip()


def sum_profit(text: str, func: Callable) -> float:
    sum = 0.0
    # порахуємо всі числа що нам видасть генератор по наданому тексту
    for i in func(text):
        sum += float(i)
    return sum


if __name__ == "__main__":
    # тестова перевірка
    text = """Загальний дохід працівника складається з декількох
              частин: 1000.01 як основний дохід, доповнений додатковими
              надходженнями 27.45 і 324.00 доларів."""

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    # Очікуване виведення: Загальний дохід: 1351.46
