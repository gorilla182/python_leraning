from random import choice, randint

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = 'il1Lo0O?'


def is_valid():
    while True:
        text = input()
        if text == 'y' or text == 'n':
            return text
        else:
            print('Ввод некорректен! Попробуйте еще раз!')


def is_valid_cnt():
    while True:
        cnt = input()
        if cnt.isdigit() and int(cnt) > 0:
            return cnt
        else:
            print('Ввод некорректен! Попробуйте еще раз!')


def password_info():
    print('Укажите количество паролей для генерации:')
    passw_cnt = is_valid_cnt()

    print('Укажите длину одного пароля:')
    passw_len = is_valid_cnt()

    print('Включать ли цифры 0123456789? (y/n)')
    digit_in = is_valid()

    print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
    upper_in = is_valid()

    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
    lower_in = is_valid()

    print('Включать ли символы !#$%&*+-=?@^_? (y/n)')
    chars_in = is_valid()

    print('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
    exclude_ambiguous = is_valid()

    return passw_cnt, passw_len, digit_in, upper_in, lower_in, chars_in, exclude_ambiguous


def generate():
    passwords_numbers = list(password_info())
    password_cnt = int(passwords_numbers[0])
    password_len = int(passwords_numbers[1])
    password_chars = ''

    # Формируем строку допустимых символов
    if passwords_numbers[2] == 'y':
        password_chars += digits

    if passwords_numbers[3] == 'y':
        password_chars += uppercase_letters

    if passwords_numbers[4] == 'y':
        password_chars += lowercase_letters

    if passwords_numbers[5] == 'y':
        password_chars += punctuation

    # Исключаем неоднозначные символы, если нужно
    if passwords_numbers[6] == 'y':
        for char in exceptions:
            password_chars = password_chars.replace(char, '')

    # Проверяем, что есть хотя бы один тип символов
    if not password_chars:
        print('Ошибка: не выбран ни один тип символов для пароля!')
        return

    all_passwords = []

    for i in range(password_cnt):
        password = ''
        for j in range(password_len):
            # Выбираем случайный символ из доступных
            password += choice(password_chars)
        all_passwords.append(password)

    print('Сгенерированные пароли:')
    for password in all_passwords:
        print(password)


generate()