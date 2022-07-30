from import_export import *
from actions import *
from pprint import pprint


def main():
    phonebook = read_all_data('phonebook.csv')
    while True:
        print('1 - Просмотр справочника\n'
              '2 - Поиск по справочнику\n'
              '3 - Изменить данные\n'
              '4 - Добавить данные\n'
              '5 - Удалить данные\n'
              '6 - Сохранить данные\n'
              '9 - Выход')
        menu_num = None
        while True:  # Проверка ввода пользователя
            try:
                menu_num = int(input('Для работы со справочником введите цифру: '))
            except ValueError:
                print('Wrong input...')
            if menu_num:
                break
        if menu_num == 9:
            exit()
        elif menu_num == 1:
            pprint(phonebook)
        elif menu_num == 2:
            find_person(phonebook)
        elif menu_num == 3:
            edit_person()  # Наполнить функцию содержимым
        elif menu_num == 4:
            add_person()  # Выдаёт ошибку - исправить
        elif menu_num == 5:
            del_person(phonebook)
        elif menu_num == 6:
            data_json = create_json_data(phonebook)
            write_json(data_json)
            write_csv(phonebook)


if __name__ == '__main__':
    main()
