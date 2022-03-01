# -*- coding: utf-8 -*-
"""Bot just for fun and trash
and of course choose who's the faggot of the day!"""

import random
import telebot
import json
import traceback
import datetime

# Token
with open("token.txt") as token_file:
    token = token_file.read().strip()
    bott = telebot.TeleBot(f'{token}')
    bott.remove_webhook()

# Just say Hi!
@bott.message_handler(commands=['hi_pidar'])
def hi_pidar(message):
    bott.send_message(message.chat.id, "Привет, пидар!")
    bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAED9WxiDllenmvORyM3NDb_duPmI7E6rgACtwMAAgk7OxO9QpPr5PZ-ciME')

# Registration new pidor
@bott.message_handler(commands=['reg_pidar'])
def reg_pidar(message):
    try:
        usernick = message.from_user.username
        username = message.from_user.first_name
        user_chat_id = message.from_user.id
        score = 0
        trigger = 0

        with open('users.json', 'r') as users_file_r:
            users_list = json.load(users_file_r)
            users_list_unparse = users_list['Users']
            users_ids = users_list['id']

        for user_id in users_ids:
            if user_chat_id == user_id:
                trigger = 1
                break

        for user in users_list_unparse:
            if usernick == user:
                trigger = 1
                break

            elif username == user:
                trigger = 1
                break

        if trigger == 1:
            if usernick is not None:
                bott.send_message(message.chat.id, f'@{usernick} ты уже в Пидорленде!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBTEFgn_j6RP8Ec5CyJ3cqmR6oUNFLqwACsgMAAgk7OxNQtIaPmAABfG4fBA')

            else:
                bott.send_message(message.chat.id, f'{username} ты уже в Пидорленде!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBTEFgn_j6RP8Ec5CyJ3cqmR6oUNFLqwACsgMAAgk7OxNQtIaPmAABfG4fBA')

        else:
            if usernick is not None:
                bott.send_message(message.chat.id, f'Добро пожаловать в Пидорленд @{usernick}!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBSDRgnQxwAVY-NmkrPchTYX9i0XyrBgACsQMAAgk7OxNuaRS5G0Mbjh8E')

            else:
                bott.send_message(message.chat.id, f'Добро пожаловать в Пидорленд {username}!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBSDRgnQxwAVY-NmkrPchTYX9i0XyrBgACsQMAAgk7OxNuaRS5G0Mbjh8E')

            with open('users.json', "r") as users_file_re:
                infor = json.load(users_file_re)

                if usernick is None:
                    infor["id"] += user_chat_id,
                    infor["Users"] += username,
                    infor["Score"] += score,

                    with open('users.json', "w"):
                        with open('users.json', "a") as users_file_a:
                            json.dump(infor, users_file_a)
                            users_file_a.close()
                else:
                    infor["id"] += user_chat_id,
                    infor["Users"] += usernick,
                    infor["Score"] += score,

                    with open('users.json', "w"):

                        with open('users.json', "a") as users_file_a:
                            json.dump(infor, users_file_a)
                            users_file_a.close()
    except:
        bott.send_message(traceback.format_exc())

# Choose pidor of day
@bott.message_handler(commands=['choose_pidr'])
def choose_pidr(message):

        with open('users.json', "r") as users_file_re:
            infor = json.load(users_file_re)
            rnd_user = random.choice(infor["Users"])
        pidr_of_day = infor["Pidr_of_day"]
        today = datetime.datetime.now()
        trigger_day = today.day - (datetime.datetime.strptime(infor["Today"], "%Y/%m/%d")).day
        if trigger_day < 0:
            trigger_day = trigger_day * -1
        if "01-01" in f"{today}":
            with open('users.json', "r") as users_file_re:
                infor = json.load(users_file_re)
                tabel = f"Ими гордится пидорленд:\n"
            for username in (infor["Users"]):
                username_index = infor["Users"].index(username)
                infor["Score"][username_index] = 0
                with open('users.json', "w"):
                    with open('users.json', "a") as users_file_a:
                        json.dump(infor, users_file_a)
                        users_file_a.close()
            bott.send_message(message.chat.id, f'{tabel}')
            bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAED9XBiDlmNHt2G-tNHE6pQsgboMKHXIwACtQMAAgk7OxPvqVG89ySCliME')
        print(trigger_day)
        if trigger_day >= 1:

            username_index = infor["Users"].index(rnd_user)
            print(f"Username_index {username_index}")

            infor["Score"][username_index] = infor["Score"][username_index] + 1
            print(infor["Score"])

            if "12-31" in f"{today}":
                bott.send_message(message.chat.id, f'Сектор ОЧКО товарща на барабане, это значит, что пидор годы ты @{rnd_user} !!!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAED9XRiDl0UIIQAAR1qjKZVMBrzd92cAsQAAq8DAAIJOzsTeE1g2lC8hGMjBA')
            else:
                bott.send_message(message.chat.id, f'Кто-то сын маминой подруги, а ты @{rnd_user} пидор!!!')
                bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBOxNgiicHjwSxTeyWXsLcGQtuLzY17QACqQMAAgk7OxNc9U5oe6y0NR8E')

            infor["Today"] = f"{today.year}/{today.month}/{today.day}"
            infor["Pidr_of_day"] = rnd_user

            with open('users.json', "w"):
                with open('users.json', "a") as users_file_a:
                    json.dump(infor, users_file_a)
                    users_file_a.close()
        else:
            if "12-31" in f"{today}":
                bott.send_message(message.chat.id, f'Пидор года {pidr_of_day}!')
            else:
                bott.send_message(message.chat.id, f'Пидор дня {pidr_of_day}!')
        print(f'{rnd_user} gay')

#TODO Add phrases when you choose pidr of the day

# Statistic
@bott.message_handler(commands=['pidor_score'])
def pidor_score(message):

    with open('users.json', "r") as users_file_re:
        infor = json.load(users_file_re)
        tabel = f"Ими гордится пидорленд:\n"
    for username in (infor["Users"]):
        score_index = infor["Users"].index(username)
        score = infor["Score"][score_index]
        if score < 1:
            hyi = "хуёв"
        elif score >= 1 and score < 2:
            hyi = "хуй"
        elif score >= 2 and score <= 4:
            hyi = "хуя"
        elif score > 4 and score < 21:
            hyi = "хуёв"
        elif score == 21 or score == 31 or score == 41 or score == 51 or score == 61:
            hyi = "хуй"
        elif score == 30 or score == 40 or score == 50 or score == 60:
            hyi = "хуёв"
        else:
            hyi = "хуя"

        tabel += f"{username}: {score} {hyi}\n"

    bott.send_message(message.chat.id, f'{tabel}')
    bott.send_sticker(message.chat.id, 'CAACAgIAAxkBAAED9XBiDlmNHt2G-tNHE6pQsgboMKHXIwACtQMAAgk7OxPvqVG89ySCliME')

bott.polling(none_stop=True, interval=0)
