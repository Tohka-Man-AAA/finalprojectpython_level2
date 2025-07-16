import telebot,time,os,random,requests
bot = telebot.TeleBot("TOKEN")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    time.sleep(1)
    bot.reply_to(message, f"Привет! Я бот {bot.get_me().first_name}!")
    time.sleep(1)
    bot.reply_to(message, "Этот бот направлен на изучение темы глобальноо потепления. Давайте узнаем что это.")
    time.sleep(1)
    bot.reply_to(message, "Глобальное потепление — это длительное повышение средней температуры Земли из-за изменения баланса тепла в атмосфере. Оно связано с усилением парникового эффекта.")


@bot.message_handler(commands=['help'])
def send_help(message):
    time.sleep(2)
    bot.reply_to(message, "Помочь планете с глобальным потеплением можно, сокращая выбросы парниковых газов в разных сферах: промышленности, сельском хозяйстве, транспорте и быту. Важно комплексный подход, так как глобальное решение проблемы требует масштабных действий со стороны правительств и крупных компаний, но вклад каждого человека также имеет значение.")


@bot.message_handler(commands=['hello'])
def send_hello(message):
    time.sleep(1)
    bot.reply_to(message, "Привет! Как дела?")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    time.sleep(1)
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['meme'])
def send_meme(message):
    time.sleep(1)
    a = os.listdir('images')
    img_name = random.choice(a)
    with open(f'images/{img_name}','rb') as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=["ping"])
def on_ping(message):
    time.sleep(1)
    bot.reply_to(message, "Я все еще работаю!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    time.sleep(1)
    bot.reply_to(message, message.text)



bot.polling()
