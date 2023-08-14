def main(data_name=None):
    try:
        input_line = input("Введите данные (Фамилия Имя Отчество Дата_рождения Номер_телефона Пол): ")
        input_data = input_line.split()

        if len(input_data) != 6:
            raise ValueError("Неверный формат данных.")

        last_name, first_name, middle_name, birth_date, phone_number, gender = input_data

        date_parts = birth_date.split(".")
        if len(date_parts) != 3:
            raise ValueError("Неверный формат даты рождения.")

        day, month, year = date_parts

        if gender not in ["m", "f"]:
            raise ValueError("Неверный формат пола.")

        gender_text = "мужской" if gender == "m" else "женский"

        formatted_data = f"{last_name} {first_name} {middle_name} {day}.{month}.{year} {phone_number} {gender}"

        data_name = "Data.txt"

        # Проверка наличия файла с таким именем
        try:
            with open(data_name, "r") as reader:
                existing_data = reader.read()
                if formatted_data in existing_data:
                    print("Данные для данной фамилии уже существуют.")
                else:
                    with open(data_name, "a") as writer:
                        writer.write(formatted_data + "\n")
                        print(f"Данные успешно записаны в файл {data_name}")
        except FileNotFoundError:
            with open(data_name, "a") as writer:
                writer.write(formatted_data + "\n")
                print(f"Данные успешно записаны в файл {data_name}")

    except ValueError as e:
        print("Ошибка:", e)

if __name__ == '__main__':
    main()
