from art import text2art
from import_export import *
from actions import *
from pprint import pprint


def main():
    print(text2art('PHONEBOOK', font='sub-zero'))  # Welcome 'LOGO'
    phonebook = read_all_data('phonebook.csv')
    while True:
        print('1 - Просмотр справочника\n'
              '2 - Поиск по справочнику\n'
              '3 - Изменить данные\n'
              '4 - Добавить данные\n'
              '5 - Удалить данные\n'
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
            find_person(phonebook)  # Поиск по справочнику
        elif menu_num == 3:
            edit_person()  # Доработать и вставить, где будет редактирование справочника
        elif menu_num == 4:
            add_person()  # Доработать и вставить, где добавляется элемент в справочник
        elif menu_num == 5:
            del_person()  # Доработать и вставить, где надо удалить элемент справочника

    # data_json = create_json_data(phonebook)
    # write_data(data_json)


if __name__ == '__main__':
    main()
