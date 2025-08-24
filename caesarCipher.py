exceptions = [" ", ",", ".", "!", "?"]
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def cypher_valid():
    while True:
        text = input()
        if text.lower() == 'д' or text.lower() == 'ш':
            return text
        else:
            print('Неверный формат ввода!! Попробуйте еще раз')


def language_valid():
    while True:
        text = input()
        if text.lower() == 'eng' or text.lower() == 'rus':
            return text
        else:
            print('Неверный формат ввода!! Попробуйте еще раз')


def key_valid():
    while True:
        text = input()
        if text.isdigit():
            return int(text)  # Преобразуем в число сразу
        else:
            print('Неверный формат ввода!! Попробуйте еще раз')


def cypher(x, n, k):
    return (x + k) % n


def decypher(y, n, k):
    return (y - k) % n


def start():
    print('Вы хотите шифровать текст или дешифровать? (д/ш)')
    func = cypher_valid()

    print('На каком языке ваше сообщение? (rus/eng)')
    language = language_valid()

    print('Введите ключ шифрования: ')
    key = key_valid()

    print('Введите ваше сообщение:')
    msg = input()
    msg_symbols = list(msg)
    result_msg = ''

    if func.lower() == 'д':  # Дешифрование
        if language.lower() == 'eng':
            for i in range(len(msg_symbols)):
                if msg_symbols[i] not in exceptions:
                    if msg_symbols[i].isupper() and msg_symbols[i] in eng_upper_alphabet:
                        idx = eng_upper_alphabet.index(msg_symbols[i])
                        new_idx = decypher(idx, 26, key)
                        msg_symbols[i] = eng_upper_alphabet[new_idx]
                    elif msg_symbols[i].islower() and msg_symbols[i] in eng_lower_alphabet:
                        idx = eng_lower_alphabet.index(msg_symbols[i])
                        new_idx = decypher(idx, 26, key)
                        msg_symbols[i] = eng_lower_alphabet[new_idx]

        elif language.lower() == 'rus':
            for i in range(len(msg_symbols)):
                if msg_symbols[i] not in exceptions:
                    if msg_symbols[i].isupper() and msg_symbols[i] in rus_upper_alphabet:
                        idx = rus_upper_alphabet.index(msg_symbols[i])
                        new_idx = decypher(idx, 33, key)
                        msg_symbols[i] = rus_upper_alphabet[new_idx]
                    elif msg_symbols[i].islower() and msg_symbols[i] in rus_lower_alphabet:
                        idx = rus_lower_alphabet.index(msg_symbols[i])
                        new_idx = decypher(idx, 33, key)
                        msg_symbols[i] = rus_lower_alphabet[new_idx]

    elif func.lower() == 'ш':  # Шифрование
        if language.lower() == 'eng':
            for i in range(len(msg_symbols)):
                if msg_symbols[i] not in exceptions:
                    if msg_symbols[i].isupper() and msg_symbols[i] in eng_upper_alphabet:
                        idx = eng_upper_alphabet.index(msg_symbols[i])
                        new_idx = cypher(idx, 26, key)
                        msg_symbols[i] = eng_upper_alphabet[new_idx]
                    elif msg_symbols[i].islower() and msg_symbols[i] in eng_lower_alphabet:
                        idx = eng_lower_alphabet.index(msg_symbols[i])
                        new_idx = cypher(idx, 26, key)
                        msg_symbols[i] = eng_lower_alphabet[new_idx]

        elif language.lower() == 'rus':
            for i in range(len(msg_symbols)):
                if msg_symbols[i] not in exceptions:
                    if msg_symbols[i].isupper() and msg_symbols[i] in rus_upper_alphabet:
                        idx = rus_upper_alphabet.index(msg_symbols[i])
                        new_idx = cypher(idx, 33, key)
                        msg_symbols[i] = rus_upper_alphabet[new_idx]
                    elif msg_symbols[i].islower() and msg_symbols[i] in rus_lower_alphabet:
                        idx = rus_lower_alphabet.index(msg_symbols[i])
                        new_idx = cypher(idx, 33, key)
                        msg_symbols[i] = rus_lower_alphabet[new_idx]

    result_msg = ''.join(msg_symbols)
    print(f"Результат: {result_msg}")
    return result_msg


start()