import telebot
import random
import re
bot = telebot.TeleBot("5501158943:AAFdsjXKRPrlY8Xx_tmG2VbEpmSQzhT1pe8")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, этот бот сделан для вывода рандомных чисел в вашем заданном диапазоне.\n"
                                      "Введите два числа через пробел:")


@bot.message_handler(content_types=["text"])
def randomizer(message):
    r = re.findall(r"\d+", message.text)
    if len(r) < 2:
        return bot.send_message(message.chat.id, "Вы ввели меньше двух чисел!")
    if len(r) > 2: #обрезание до 2-х
        r = r[:2]
        bot.send_message(message.chat.id, "Вы ввели больше чем два числа!\n Я убрал лишнее!")
    r_min = min([int(i) for i in r]) #если вдруг числа введены в порядке убывания
    r_max = max([int(i) for i in r])
    bot.send_message(message.chat.id, 'Ваше случайное число: {}'.format(random.randint(r_min, r_max)))


bot.infinity_polling()