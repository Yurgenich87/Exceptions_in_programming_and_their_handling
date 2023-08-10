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
