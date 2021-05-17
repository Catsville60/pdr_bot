# -*- coding: utf-8 -*-

import telebot
import json
import random


pidr_names = []
pidr_points = []

# Токен
bott = telebot.TeleBot('1751046677:AAHnRV2LBt8O4dpI22T-GOeKHuIEOKQHNZI')

# Просто поздороваться
@bott.message_handler('hi_pidar')
def hello_pidr(message):
    bott.send_message(message.chat.id, "Привет, пидар!")
    bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

# Регистрация нового игрока
@bott.message_handler('reg_pidar')
def reg_pidr(message):
    f = open('pidr_list.json')
    data = json.load(f)
    da = data['names']
    y = 0
    print(len(da))
    # Проверка был ли зареган игрок
    for i in da:
        if i == message.from_user.username:
            if message.from_user.username != None:
                print('Ты уже зареган!' + i)
                bott.send_message(message.chat.id, 'Ты уже зареган пидар! ' + '@' + message.from_user.username)
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBTEFgn_j6RP8Ec5CyJ3cqmR6oUNFLqwACsgMAAgk7OxNQtIaPmAABfG4fBA')
                y = 1
                break
        elif i == (message.from_user.first_name + ' ' + message.from_user.last_name):
            if message.from_user.username == None:
                bott.send_message(message.chat.id, 'Ты уже зареган пидар! ' + message.from_user.first_name + ' ' + message.from_user.last_name)
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBTEFgn_j6RP8Ec5CyJ3cqmR6oUNFLqwACsgMAAgk7OxNQtIaPmAABfG4fBA')
                y = 1
                break
        else:
            y = 0
            continue
        return y

    # Добавление игрока в JSON
    if y != 1:
        if message.from_user.username != None:
            bott.send_message(message.chat.id, 'Велком пидар! ' + '@' + message.from_user.username)
            bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBSDRgnQxwAVY-NmkrPchTYX9i0XyrBgACsQMAAgk7OxNuaRS5G0Mbjh8E')
            pidr_names.append(message.from_user.username)
            pidr_points.append(0)
            json_pidr = {'names': pidr_names, 'points': pidr_points}
            with open('pidr_list.json', 'w') as f:
                f.write(json.dumps(json_pidr))
            #with open('pidr_list.json') as f:
                #print(f.read())
        elif message.from_user.username == None:
            bott.send_message(message.chat.id, 'Велком пидар! ' +  message.from_user.first_name + ' ' + message.from_user.last_name)
            bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBSDRgnQxwAVY-NmkrPchTYX9i0XyrBgACsQMAAgk7OxNuaRS5G0Mbjh8E')
            pidr_names.append(message.from_user.first_name + ' ' + message.from_user.last_name)
            pidr_points.append(0)
            json_pidr = {'names': pidr_names, 'points': pidr_points}
            with open('pidr_list.json', 'w') as f:
                f.write(json.dumps(json_pidr))
           #with open('pidr_list.json') as f:
                #print(f.read())
# Trash
     #elif message.from_user.username != None:
    #print ('1')
    # bott.send_message(message.chat.id, 'Ты зареган ПИДАР! ' + message.from_user.username)
    # bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBSDRgnQxwAVY-NmkrPchTYX9i0XyrBgACsQMAAgk7OxNuaRS5G0Mbjh8E')
    # pidr_names.append(message.from_user.username)
    # pidr_points.append(0)
    # json_pidr = {'names': pidr_names, 'points': pidr_points}
    # with open('pidr_list.json', 'w') as f:
    #      f.write(json.dumps(json_pidr))
    #  with open('pidr_list.json') as f:
    #      print(f.read())

    # bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBSDRgnQxwAVY-NmkrPchTYX9i0XyrBgACsQMAAgk7OxNuaRS5G0Mbjh8E')
    # pidr_names.append(message.from_user.username)
    # pidr_points.append(0)
    # print(pidr_names)

    # elif message.from_user.username == None and y == 1:
    # pidr_names.append(bott.send_message(message.chat.id, message.from_user.first_name + ' ' + message.from_user.last_name))
    # pidr_points.append(0)
    # pidr_names.append(message.from_user.first_name + ' ' + message.from_user.last_name)
    # pidr_points.append(0)
    # json_pidr = {'names': pidr_names, 'points': pidr_points}
    # with open('pidr_list.json', 'w') as f:
    #   f.write(json.dumps(json_pidr))
    # with open('pidr_list.json') as f:
    #    print(f.read())
    # print(pidr_names[0])
    #  print('2')

# Выбор пидора дня
@bott.message_handler('select_pidar_of_day')
def chouse_pidr(message):
    f = open('pidr_list.json')
    data = json.load(f)
    da = data['names']
    point = data['points']

    for i in da:
        print(i)
    for y in point:
        print(str(y))

    # print('Сегодня пидор дня' + d)
    # bott.send_message(message.chat.id, 'Сегодня пидор дня ' + '@' + str(random.choice(da)))
    # bott.send_message(message.chat.id, "Функция пока не работает пидар!")
    # bott.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBR6xgm5iR1F0mje0LTMTILPF8V6iMiAACvgMAAgk7OxMl-hpfgHaOsh8E")
    # audio = open(r'C:/Users/Catsville/PycharmProjects/pythonProject/ Иди Нахуй.mp3', 'rb')
    # bott.send_audio(message.chat.id, audio)

# Статистика
#@bott.message_handler('pidor_score')
#def score_pidr(message):

bott.polling(none_stop=True, interval=0)
