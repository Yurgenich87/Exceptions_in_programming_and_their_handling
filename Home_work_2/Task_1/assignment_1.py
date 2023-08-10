def get_float_input():
    """Ввод дробного числа пользователем"""
    while True:
        try:
            user_input = float(input("Введите дробное число: "))
            if user_input.is_integer():
                print("Ошибка! Введите дробное число, а не целое.")
            else:
                return print(f"Вы ввели дробное число: {user_input}")
        except ValueError:
            print("Ошибка! Введите корректное дробное число.")


if __name__ == '__main__':
    get_float_input()
