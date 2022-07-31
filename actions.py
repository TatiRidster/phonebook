import csv
from csv import writer
from correctdata import correct_number, correct_text


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
    #по хорошему тут надо реализовать поиск по фамилии в файле, 
    # но справиться с написанной find_person(data_list: list) я не могу - выводит пустоту
    # Если такая фамилия есть - то вывести все записи с фамилией 
    # и спросить продолжаем ли мы вносить контакт
    user_first_name = input_firstname() 
    user_second_name = input_firstname2() 
    user_phone =input( "Введите номер +7 код номер без пробелов: ")
    user_phone = correct_number(user_phone)
    user_phone = perfect_phone_num(user_phone)
    #тут я пытаюсь реализовать проверку записи в существующем файле по номеру телефона
    if find_phone(user_phone)==False:
        user_birthday = input( "Введите день рождения: ")
        user_job = input( "Введите чем человек занимается: ")
        user_address = input( "Введите адрес: ")
    contactDetails =("[" + user_surname +" "+ user_first_name + " " + user_second_name + ", " + user_phone + ", " + user_birthday + ", "+ user_job+", "+user_address +"]\n") 
    #если такого телефона нет- записываем в конец файла, сам csv фаил надо закрыть вручную
    with open('phonebook.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(contactDetails)  
        f_object.close() 
    print( "The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!") 

def perfect_phone_num(user_phone):
    user_phone_new =""
    user_phone_new1 =user_phone[0]+user_phone[1]+" ("+user_phone[2]+user_phone[3]+user_phone[4]+") "
    user_phone_new2 = user_phone[5]+user_phone[6]+user_phone[7]+"-"+user_phone[8]+user_phone[9]+"-"
    user_phone_new3 =user_phone[10]+user_phone[11]
    user_phone_new =user_phone_new1+user_phone_new2+user_phone_new3
    return user_phone_new

def find_phone(user_phone):
    searchname = user_phone 
    remname = searchname[1:] 
    firstchar = "+" 
    searchname = firstchar + remname
    #searchname = '+7 (486) 572-60-60'
    #тут падает с ошибкой и не может справиться с чтением файла
    with open('phonebook.csv','rb') as csvfile:
        filecontents = csv.DictReader(csvfile, delimiter=',')
                  
        found = False 
        for line in filecontents: 
            if searchname in line: 
                print( "Your Contact already in phonebook:", end = " ") 
                print( line) 
                found = True 
                break 
        if found == False: 
            print( "This contact really new ", searchname)
    csvfile.close()
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
