import csv
from csv import writer
from correctdata import correct_number, correct_text
from random import randint
import logging

logging.basicConfig(filename='phonebook.log',
                    level=logging.DEBUG,
                    datefmt='%Y.%m.%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
loger = logging.getLogger('actions')


def edit_person(lst: list[list]) -> None:
    loger.info('Start edit person')
    find_person(lst)
    person_id = input('Введите ID из показанных выше, для изменения данных или "0" для возврата в главное меню: ')
    if person_id == '0':
        return None
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if person_id in lst[i]:
                temp_lst = lst[i]
                print(f'Меняем данные о пользователе с ID {person_id}')
                temp_lst[0] = person_id
                while True:
                    full_name = input('Введите имя, отчество, фамилию (порядок важен!) через пробел: ').title().split()
                    if len(full_name) == 3:
                        temp_lst[1] = full_name[0]
                        temp_lst[2] = full_name[1]
                        temp_lst[3] = full_name[2]
                        break
                    else:
                        print('ФИО не может быть пустым и должно содержать 3 элемента')
                        print('В случае отсутствия каких либо данных, вместо них введите "None"')
                while True:
                    try:
                        temp_lst[4] = perfect_phone_num(correct_number(input('Введите новый телефон: ')))
                        break
                    except Exception as _:
                        print('Ошибка, попробуйте ещё раз')
                        loger.error(_)
                birthday = input('Введите новую дату рождения: ')
                if not birthday:
                    temp_lst[5] = 'Not specified'
                job = input('Введите новую профессию: ')
                if not job:
                    temp_lst[6] = 'Not specified'
                address = input('Введите новый адрес: ')
                if not address:
                    temp_lst[7] = 'Not specified'
                lst[i] = temp_lst
                break


def del_person(data_list: list[list]) -> None:
    loger.info('Start delete person')
    search_string = input('Введи строку для поиска: ')
    for i in data_list:
        for j in i:
            if search_string.lower() in j.lower():
                print(i)
    search_id = input('Введи id строки для удаления: ')
    for k in data_list:
        for l in k:
            if search_id in l:
                data_list.pop(data_list.index(k))
                print(f'Пользователь с id {search_id} удалён')


def input_firstname():
    first = input("Введите имя: ")
    correct_text(first)
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


def input_firstname2():
    first = input("Введите отчество: ")
    correct_text(first)
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


def input_lastname():
    last = input("Введите фамилию: ")
    correct_text(last)
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


def add_person():
    loger.info('Start add person')
    user_surname = input_lastname()
    find_phone(user_surname)
    user_first_name = input_firstname()
    user_second_name = input_firstname2()
    user_phone = input("Введите номер +7 код номер без пробелов: ")
    user_phone = correct_number(user_phone)
    user_phone = perfect_phone_num(user_phone)
    if find_phone(user_phone) == False:
        user_birthday = input("Введите день рождения: ")
        user_job = input("Введите чем человек занимается: ")
        user_address = input("Введите адрес: ")
    contactDetails = (
                "[" + user_surname + " " + user_first_name + " " + user_second_name + ", " + user_phone + ", " + user_birthday + ", " + user_job + ", " + user_address + "]\n")
    get_ID = randint(100000, 999999)
    if find_phone(get_ID) == False:
        user_id = str(get_ID)
        data = [user_id, user_surname, user_first_name, user_second_name, user_phone, user_birthday, user_job,
                user_address]
        with open('phonebook.csv', 'a', newline='', encoding='utf-8') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
    print("The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!")


def perfect_phone_num(user_phone):
    user_phone_new1 = user_phone[0] + user_phone[1] + " (" + user_phone[2] + user_phone[3] + user_phone[4] + ") "
    user_phone_new2 = user_phone[5] + user_phone[6] + user_phone[7] + "-" + user_phone[8] + user_phone[9] + "-"
    user_phone_new3 = user_phone[10] + user_phone[11]
    user_phone_new = user_phone_new1 + user_phone_new2 + user_phone_new3
    return user_phone_new


def find_phone(user_phone):
    searchname = user_phone
    with open('phonebook.csv', 'r', encoding='utf-8', newline='') as file:
        filecontents = csv.reader(file, delimiter=',')
        found = False
        for line in filecontents:
            if searchname in line:
                print("Your Contact already in phonebook:", end=" ")
                print(line)
                found = True
                break
        if found == False:
            print("This contact really new ", searchname)
    return found


def find_person(data_list: list):
    loger.info('Start search person')
    search_string = input('Введи строку для поиска: ')
    for i in data_list:
        for j in i:
            if search_string.lower() in j.lower():
                print(i)


def main():
    pass


if __name__ == '__main__':
    main()
