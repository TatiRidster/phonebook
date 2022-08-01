from import_export import *
from actions import *
from pprint import pprint
import logging


def main():
    loger.debug('Program start')
    phonebook = read_all_data('phonebook.csv')
    while True:
        print('1 - Просмотр справочника\n'
              '2 - Поиск по справочнику\n'
              '3 - Изменить данные\n'
              '4 - Добавить данные\n'
              '5 - Удалить данные\n'
              '6 - Сохранить данные\n'
              '0 - Выход')
        menu_num = None
        while True:  # Проверка ввода пользователя
            try:
                menu_num = int(input('Для работы со справочником введите цифру: '))
            except ValueError:
                loger.warning('Wrong input!')
            if menu_num or menu_num == 0:
                break
        if menu_num == 0:
            loger.debug('Program exit')
            exit()
        elif menu_num == 1:
            pprint(phonebook)
        elif menu_num == 2:
            find_person(phonebook)
        elif menu_num == 3:
            edit_person(phonebook)  # Наполнить функцию содержимым
        elif menu_num == 4:
            add_person()
        elif menu_num == 5:
            del_person(phonebook)
        elif menu_num == 6:
            data_json = create_json_data(phonebook)
            write_json(data_json)
            write_csv(phonebook)
            loger.info('All data saved')


if __name__ == '__main__':
    logging.basicConfig(filename='phonebook.log',
                        level=logging.DEBUG,
                        datefmt='%Y.%m.%d %H:%M:%S',
                        format='%(asctime)s - %(name)s: %(message)s')
    loger = logging.getLogger('phonebook')
    main()
