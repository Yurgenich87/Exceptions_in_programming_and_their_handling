import random

int_array = []

for _ in range(5):
    random_number = random.randint(1, 100)
    int_array.append(random_number)

d = 0
try:
    result = int_array[8] / d
    print("Результат =", result)
except ZeroDivisionError as e:
    print("Перехвачено исключение:", e)
except IndexError as e:
    print("Ошибка индекса:", e)

# Задание 3
def print_sum(a, b):
    print(a + b)


try:
    a = 90
    b = 3
    print(a / b)
    print_sum(23, 234)
    abc = [1, 2]
    abc[3] = 9
except Exception as ex:
    print("Что-то пошло не так...")
except ZeroDivisionError as ex:
    print("Указатель не может указывать на null!")
except IndexError as ex:
    print("Массив выходит за пределы своего размера!")
