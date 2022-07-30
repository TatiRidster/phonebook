def correct_text(text):
    name = text
    while True:
        if name.isalpha():
            return name.capitalize()
        print('не корректный ввод')
        name = input(f'Введите снова: ')


def correct_number(user_phone):
    number = user_phone
    while True:
        if number[0] == '+' and number[1:].isdigit() and len(number) == 12:
            return number
        print('не корректный ввод')
        number = input('номер +7 код номер без пробелов -> ')
