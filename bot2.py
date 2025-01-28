import telebot, time
from telebot import types

token = "6882087021:AAHXp13Zx-agdX3eJ6j0XzD2j18K1feLpzw"
bot = telebot.TeleBot(token)

white_list = ["not_for_ya"]
users_ids = {"not_for_ya": 1455972771, "PeLMeN_Ogurchik": 1652859368, "hidirdede": 6814317456}

with open("E:/docs/log2.txt", "a") as file:
    file.write(str(time.ctime(time.time())) + " | " + "DEV" + " | " + "Executed" + "\n")


@bot.message_handler(commands=["start"])
def start_bot(message):
    #log(message)
    print(message.chat.id, message.from_user.username, message.text)
    bot.send_message(message.chat.id, """Приветик!
Я бот, который не для тебя.
Работаю только по белому списку.""")
    if message.from_user.username in white_list:
        bot.send_message(message.chat.id, """Вы в белом списке.
Пользуйтесь!""")
    else:
        bot.send_message(message.chat.id, """Вы НЕ в белом списке.
Можете оставить заявку.
Пишите сразу сюда.
Я гляну в логах.
*Заявка*""")


@bot.message_handler(commands=["send"])
def send_message(message):
    #log(message)
    if message.from_user.username in white_list:
        print(message.chat.id, message.from_user.username, message.text)
        mesg = bot.send_message(message.chat.id, """Напишите имя пользователя(username), получаещего сообщение.
#Username/@/'Сообщение'#""")
        bot.register_next_step_handler(mesg, function_send_message)
    else:
        bot.send_message(message.chat.id, "Нет доступа!")


def function_send_message(message):
    #log(message)
    print(message.chat.id, message.from_user.username, message.text)
    msg = message.text.split("/@/")
    if len(msg) == 2:
        if msg[0] in users_ids:
            bot.send_message(users_ids[msg[0]], msg[1])
        else:
            bot.send_message(message.chat.id, "Пользователя нет в белом списке.")
    else:
        bot.send_message(message.chat.id, "Неправильный ввод!")


@bot.message_handler(commands=["log"])
def receive_log(message):
    if message.from_user.username in white_list:
        bot.send_document(message.chat.id, open(r"E:/docs/log2.txt", 'rb'))
    else:
        bot.send_message(message.chat.id, "Нет доступа!")


@bot.message_handler(content_types="text")
def log(message):
    with open("E:/docs/log2.txt", "a", encoding='utf-8', errors='ignore') as file:
        file.write(str(time.ctime(time.time())) + " | " + str(message.chat.id) + " | " + str(
            message.from_user.username) + " | " + "USER" + " | " + str(message.text) + "\n")
    print(message.chat.id, message.from_user.username, message.text)


bot.infinity_polling()