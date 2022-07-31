import csv
from csv import writer
from correctdata import correct_number, correct_text
from import_export import write_csv
from random import randint
def edit_person():
    pass


def del_person(data_list: list[list]) -> None:
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


# first name
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


# last name 
def input_lastname():
    last = input("Введите фамилию: ")
    correct_text(last)
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


def add_person():
    user_surname = input_lastname()
    find_phone(user_surname)
    user_first_name = input_firstname() 
    user_second_name = input_firstname2() 
    user_phone =input( "Введите номер +7 код номер без пробелов: ")
    user_phone = correct_number(user_phone)
    user_phone = perfect_phone_num(user_phone)
    if find_phone(user_phone)==False:
        user_birthday = input( "Введите день рождения: ")
        user_job = input( "Введите чем человек занимается: ")
        user_address = input( "Введите адрес: ")
    contactDetails =("[" + user_surname +" "+ user_first_name + " " + user_second_name + ", " + user_phone + ", " + user_birthday + ", "+ user_job+", "+user_address +"]\n") 
    get_ID = randint(100000,999999)
    if find_phone(get_ID)==False:
        user_id = str(get_ID)
        data = [user_id,user_surname,user_first_name,user_second_name,user_phone,user_birthday,user_job,user_address]
        with open('phonebook.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow(data)  
            f_object.close()  
    print( "The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!") 


def perfect_phone_num(user_phone):
    user_phone_new = ""
    user_phone_new1 = user_phone[0] + user_phone[1] + " (" + user_phone[2] + user_phone[3] + user_phone[4] + ") "
    user_phone_new2 = user_phone[5] + user_phone[6] + user_phone[7] + "-" + user_phone[8] + user_phone[9] + "-"
    user_phone_new3 = user_phone[10] + user_phone[11]
    user_phone_new = user_phone_new1 + user_phone_new2 + user_phone_new3
    return user_phone_new


def find_phone(user_phone):
    searchname = user_phone 
    #remname = searchname[1:] 
    #firstchar = "+" 
    #searchname = firstchar + remname
    with open('phonebook.csv', 'r', encoding='utf-8', newline='') as file:
        filecontents = csv.reader(csvfile, delimiter=',')
        found = False 
        for line in filecontents: 
            if searchname in line: 
                print( "Your Contact already in phonebook:", end = " ") 
                print( line) 
                found = True 
                break 
        if found == False: 
            print( "This contact really new ", searchname)
    return found  


def find_person(data_list: list):
    search_string = input('Введи строку для поиска: ')
    for i in data_list:
        for j in i:
            if search_string.lower() in j.lower():
                print(i)


def main():
    pass


if __name__ == '__main__':
    main()
