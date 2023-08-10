def get_input():
    while True:
        try:
            user_input = float(input("Введите сообщение: "))
            return user_input

        except ValueError:
            print("Ошибка! Вы ничего не ввели.")


# Пример использования
user_float = get_input()
print(f"Вы ввели: {user_float}")
