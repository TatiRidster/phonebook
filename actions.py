
from correctdata import correct_number, correct_text
def edit_person():
    pass


def del_person():
    pass

# first name 
def input_firstname(): 
    first = input( "Введите имя: ")
    correct_text(first) 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
def input_firstname2(): 
    first = input( "Введите отчество: ")
    correct_text(first) 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
# last name 
def input_lastname(): 
    last = input( "Введите фамилию: ") 
    correct_text(last)
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 

def add_person():
    user_surname = input_lastname()
    user_first_name = input_firstname() 
    user_second_name = input_firstname2() 
    user_phone = input( "Введите номер +7 код номер без пробелов: ")
    correct_number(user_phone) 
    user_birthday = input( "Введите день рождения: ")
    user_job = input( "Введите чем человек занимается: ")
    user_address = input( "Введите адрес: ")
    contactDetails =("[" + user_surname +" "+ user_first_name + " " + user_second_name + ", " + user_phone + ", " + user_birthday + ", "+ user_job+", "+user_address +"]\n") 
    #тут реализовать проверку записи в существующем файле по номеру телефона
    #и сказать что запись уже есть, если такого телефона нет- записываем в конец файла
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!") 

    


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
