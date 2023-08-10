def print_sum(a, b):
    """Функция сложения двух чисел"""
    print(a + b)


try:
    a = 90
    b = 3
    print(a / b)
    print_sum(23, 234)
    abc = [1, 2]
    abc[3] = 9
except Exception as ex:
    print(f"Ошибка: {ex}")
except ZeroDivisionError as ex:
    print("Указатель не может указывать на null!")
except IndexError as ex:
    print("Массив выходит за пределы своего размера!")
