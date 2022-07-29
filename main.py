from art import text2art
from import_export import *


def main():
    print(text2art('PHONEBOOK', font='sub-zero'))  # Welcome 'LOGO'
    phonebook = read_all_data('phonebook.csv')
    data_json = create_json_data(phonebook)
    write_data(data_json)


if __name__ == '__main__':
    main()
