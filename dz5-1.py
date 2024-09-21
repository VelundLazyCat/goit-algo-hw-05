
"""
Замикання в програмуванні - це функція, яка зберігає посилання на змінні зі свого лексичного контексту, 
тобто з області, де вона була оголошена.
Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання
вже обчислених значень чисел Фібоначчі.
Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., де кожне наступне число послідовності
виходить додаванням двох попередніх членів ряду.
У загальному вигляді для обчислення n-го члена ряду Фібоначчі потрібно вирахувати вираз: 
F(n)=F(n−1) + F(n−2)
Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа послідовності доти,
доки виклик не сягне членів ряду менше n = 1, де послідовність задана.

Вимоги до завдання:
Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
Використання рекурсії для обчислення чисел Фібоначчі
"""

# щоб порахувати скільки раз ми викличемо рекурсію введемо атрибут count та ініціалізуемо лічільник


def caching_fibonacci(start=0) -> int:
    cache = {}
    # миб значно спростили внутрішню функцію якби зразу додали в словник базові випадки cash = {0: 0, 1: 1}
    # булаб тільки первірка в кеші і розрахунок якшо даних не має

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # лічільник рекурсивних викликів
        fibonacci.count += 1
        return cache[n]
    # ініціалізація лічільника
    fibonacci.count = start
    return fibonacci


if __name__ == '__main__':
    # блок автотесту
    b = caching_fibonacci()
    # довжина послідовності
    n = 10
    print(f'сума ряда Фібоначчі для послідовності {
          n} чисел = {b(10)}, обраховано за {b.count} кроків')
