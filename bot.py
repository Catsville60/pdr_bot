# -*- coding: utf-8 -*-

import telebot
import json
import traceback
# Токен
bott = telebot.TeleBot('1751046677:AAHnRV2LBt8O4dpI22T-GOeKHuIEOKQHNZI')
bott.remove_webhook()

# Just say Hi!
@bott.message_handler('hi_pidar')
def hi_pidar(message):
    bott.send_message(message.chat.id, "Привет, пидар!")
    bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

# Registration new pidor
@bott.message_handler('reg_pidar')
def reg_pidar(message):
    try:
        Username = message.from_user.username
        Score = 0
        #with open('users.json', 'w') as users_file:
        #    dic = {"Users":Username, "Score":Score}
        #    jsons = json.dump(dic, users_file)
        with open('users.json', 'r') as users_file1:
            deco = json.load(users_file1)
            print (deco['Users'])
        de = deco['Users']
        a = 0
        for d in de:
            if Username == d:
                a = 1
                break
        if a == 1:
            bott.send_message(message.chat.id, f'{d} ты уже в Пидорленде')
            bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

        else:
            bott.send_message(message.chat.id, f'Добро пожаловать в Пидорленд @{Username}!')
            bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')
    except:
        bott.send_message(traceback.format_exc())
# Chouse pidor of day
@bott.message_handler('chouse_pidr')
def chouse_pidr(message):
    print('gay')
# Stat
@bott.message_handler('pidor_score')
def pidor_score(message):
    print('gay')

bott.polling(none_stop=True, interval=0)
