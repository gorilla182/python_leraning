from random import *



positive_response = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']
hesitantly_positive_response = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
neutral_response = ['Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять']
negative_response = ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
all_responses = positive_response + hesitantly_positive_response + negative_response + neutral_response

def welcome_mes():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('Как тебя зовут? Введи свое имя ниже: ')
    name = input()
    print('Привет, ', name)

def choice(responses):
    n = randint(0, len(all_responses)-1)
    return responses[n]

def question():
    print('Какой у тебя вопрос? Задай его мне, я дам ответ на любые твои вопросы. Но он должен быть закрытого типа.')
    quest = input()
    print('Твой вопрос - ', quest, ' давай подумаем, сбудется ли... И так, мой вердикт:')


def start():
    welcome_mes()
    while True:
        question()
        n = choice(all_responses)
        print(n)
        print('Хочешь ли ты узнать что то еще о своей судьбе? Напиши Д - если да, или Н - если нет.')
        answer = input()
        if answer.lower() == 'д':
            continue
        elif answer.lower() == 'н':
            print('Возвращайся, если возникнут вопросы!')
            break

start()











