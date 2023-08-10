def get_float_input():
    while True:
        try:
            user_input = float(input("Введите дробное число: "))
            if user_input.is_integer():
                print("Ошибка! Введите дробное число, а не целое.")
            else:
                return user_input
        except ValueError:
            print("Ошибка! Введите корректное дробное число.")

# Пример использования
user_float = get_float_input()
print(f"Вы ввели: {user_float}")
