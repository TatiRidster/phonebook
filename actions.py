def edit_person():
    pass


def del_person():
    pass


def add_person():
    pass


def find_person(data_list: list):
    search_string = input('Введите данные для поиска: ')
    for i in data_list:
        for j in i:
            if search_string.lower() in j.lower():
                print(i)


def main():
    pass


if __name__ == '__main__':
    main()
