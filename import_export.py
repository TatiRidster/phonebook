import csv
import json


def read_all_data(filename: str) -> list[list]:
    """
    Считываем все данные из CSV в список со списками

    @param filename: имя CSV файла
    @return: Список со списками данных по пользователям
    """
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            data.append(row)
        return data


def write_json(database: dict) -> None:
    """
    Сохраняем словарь в JSON файл

    @param database: Словарь с данными
    @return: ничего не возвращаем, сохраняем файл
    """
    with open('phonebook.json', 'w', encoding='utf-8') as file:
        json.dump(database, file, indent=4, ensure_ascii=False)
    print('JSON файл успешно сохранён')


def create_json_data(database: list[list]) -> dict:
    """
    Конвертируем список полученный из CSV в словарь данных о пользователях

    @param database: Список со списками данных
    @return: Словарь для экспорта в JSON
    """
    data = {}
    for user_data in database:  # Формируем словарь
        user_id = user_data[0]
        user_surname = user_data[3]
        user_first_name = user_data[1]
        user_second_name = user_data[2]
        user_phone = user_data[4]
        user_birthday = user_data[5]
        user_job = user_data[6]
        user_address = user_data[7]
        data[user_id] = {
            'Surname': user_surname,
            'Firstname': user_first_name,
            "Second_name": user_second_name,
            'Phone': user_phone,
            'Birthday': user_birthday,
            'Profession': user_job,
            'Address': user_address
        }
    return data


def write_csv(data: list[list]) -> None:
    with open('phonebook.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)
    print('CSV файл успешно сохранён')


def main():
    pass


if __name__ == "__main__":
    main()
