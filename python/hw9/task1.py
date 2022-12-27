import telebot
from random import randint
from random import choice

bot = telebot.TeleBot("5966875273:AAFYBa0eBrZli_2b_oJl503fUBSWF7eyCkc")
candy = dict()
game_mode = dict()
choose = dict()


def game_check(message):
    global game_mode
    try:
        if game_mode(message.chat.id) and 1 <= int(message.text) <= 28:
            return True
        else:
            return False
    except KeyError:
        game_mode(message.chat.id) == False
        if game_mode(message.chat.id) and 1 <= int(message.text) <= 28:
            return True
        else:
            return False


@bot.message_handler(commands=['start'])
def greeting_msg(message):
    global candy, game_mode, choose
    bot.reply_to(message, 'Начнем')
    candy[message.chat.id] = 117
    choose[message.chat.id] = choice[('Бот', 'Пользователь')]
    bot.send_message(
        message.chat.id, f'Первый ходит {choose[message.chat.id]}')
    game_mode[message.chat.id] = True
    if choose(message.chat.id) == 'Бот':
        get = randint(1, candy[message.chat.id] % 29)
        candy[message.chat.id] -= get
        bot.send_message(message.chat.id, f'Бот взял {get} конфет')
        bot.send_message(
            message.chat.id, f'Осталось {candy(message.chat.id)} конфет')
        choose(message.chat.id) == 'Пользователь'


@bot.message_handler(func=game_check)
def game_process(message):
    global candy, game_mode, choose
    if choose(message.chat.id) == 'Пользователь':
        if candy[message.chat.id] > 28:
            candy[message.chat.id] -= int(message.text)
            bot.send_message(
                message.chat.id, f'Осталось {candy(message.chat.id)} конфет')
            if candy[message.chat.id] > 28:
                get = randint(1, candy[message.chat.id] % 29)
                bot.send_message(message.chat.id, f'Бот взял {get} конфет')
                bot.send_message(
                    message.chat.id, f'Осталось {candy(message.chat.id)}шт')
                if candy[message.chat.id] <= 28:
                    bot.send_message(message.chat.id, 'Победил Пользователь')
                    game_mode[message.chat.id] = False
            else:
                bot.send_message(message.chat.id, 'Победил Бот')
                game_mode[message.chat.id] = False
        else:
            bot.send_message(message.chat.id, 'Победил Бот')
            game_mode[message.chat.id] = False


bot.infinity_polling()
