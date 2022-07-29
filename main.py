from art import text2art
from import_export import *
from actions import *


def main():
    print(text2art('PHONEBOOK', font='sub-zero'))  # Welcome 'LOGO'
    phonebook = read_all_data('phonebook.csv')
    data_json = create_json_data(phonebook)
    write_data(data_json)
    add_person()  # Доработать и вставить, где добавляется элемент в справочник
    edit_person()  # Доработать и вставить, где будет редактирование справочника
    del_person()  # Доработать и вставить, где надо удалить элемент справочника


if __name__ == '__main__':
    main()
