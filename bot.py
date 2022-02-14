# -*- coding: utf-8 -*-

import random
import telebot
import json
import traceback
import datetime

#TODO Hide the token
#TODO Change stickers

# Token
bott = telebot.TeleBot('1751046677:AAHnRV2LBt8O4dpI22T-GOeKHuIEOKQHNZI')
bott.remove_webhook()

# Just say Hi!
@bott.message_handler(commands=['hi_pidar'])
def hi_pidar(message):
    bott.send_message(message.chat.id, "Привет, пидар!")
    bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

# Registration new pidor
@bott.message_handler(commands=['reg_pidar'])
def reg_pidar(message):
    try:
        Usernic = message.from_user.username
        Username = message.from_user.first_name
        User_chat_id = message.from_user.id
        Score = 0
        trigger = 0

        with open('users.json', 'r') as users_file_r:
            Users_list = json.load(users_file_r)
            Users_list_unparse = Users_list['Users']
            Users_ids = Users_list['id']

        for User_id in Users_ids:
            if User_chat_id == User_id:
                trigger = 1
                break

        for User in Users_list_unparse:
            if Usernic == User:
                trigger = 1
                break

            elif Username == User:
                trigger = 1
                break

        if trigger == 1:
            if Usernic is not None:
                bott.send_message(message.chat.id, f'@{Usernic} ты уже в Пидорленде!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

            else:
                bott.send_message(message.chat.id, f'{Username} ты уже в Пидорленде!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

        else:
            if Usernic is not None:
                bott.send_message(message.chat.id, f'Добро пожаловать в Пидорленд @{Usernic}!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

            else:
                bott.send_message(message.chat.id, f'Добро пожаловать в Пидорленд {Username}!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

            with open('users.json', "r") as users_file_re:
                infor = json.load(users_file_re)

                if Usernic is None:
                    infor["id"] += User_chat_id,
                    infor["Users"] += Username,
                    infor["Score"] += Score,

                    with open('users.json', "w"):

                        with open('users.json', "a") as users_file_a:
                            json.dump(infor, users_file_a)
                            users_file_a.close()

                else:
                    infor["id"] += User_chat_id,
                    infor["Users"] += Usernic,
                    infor["Score"] += Score,

                    with open('users.json', "w"):

                        with open('users.json', "a") as users_file_a:
                            json.dump(infor, users_file_a)
                            users_file_a.close()
    except:
        bott.send_message(traceback.format_exc())
        print("chel tiiii")

# Chouse pidor of day
@bott.message_handler(commands=['choose_pidr'])
def choose_pidr(message):

        with open('users.json', "r") as users_file_re:
            infor = json.load(users_file_re)
            rnd_user = random.choice(infor["Users"])
        pidr_of_day = infor["Pidr_of_day"]
        today = datetime.datetime.now()
        trigger = today.day - (datetime.datetime.strptime(infor["Today"], "%Y/%m/%d")).day
        print(trigger)
        if trigger >= 1:

            Username_index = infor["Users"].index(rnd_user)
            print(f"Username_index {Username_index}")

            infor["Score"][Username_index] = infor["Score"][Username_index] + 1
            print(infor["Score"])

            bott.send_message(message.chat.id, f'Кто-то сын маминой подруги, а ты @{rnd_user} пидор!!!')
            bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')
            infor["Today"] = f"{today.year}/{today.month}/{today.day}"
            infor["Pidr_of_day"] = rnd_user
            with open('users.json', "w"):
                with open('users.json', "a") as users_file_a:
                    json.dump(infor, users_file_a)
                    users_file_a.close()
        else:
            bott.send_message(message.chat.id, f'Пидор дня {pidr_of_day}!')
        print(f'{rnd_user} gay')

#TODO Add xmas pidor of the year
#TODO Add phrases when you choose pidr of the day
#TODO Clear json and create new after New Year

# Stat
@bott.message_handler(commands=['pidor_score'])
def pidor_score(message):
    with open('users.json', "r") as users_file_re:
        infor = json.load(users_file_re)
        tabel = f"Ими гордится пидорленд:\n"
    for username in (infor["Users"]):
        score_index = infor["Users"].index(username)
        score = infor["Score"][score_index]

        tabel += f"{username}: {score} хуй\n"
    bott.send_message(message.chat.id, f'{tabel}')
    print(tabel)
    print('gay')

#TODO Declension of nouns after numeric

bott.polling(none_stop=True, interval=0)
