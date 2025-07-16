import telebot,time,os,random,requests
bot = telebot.TeleBot("TOKEN")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    time.sleep(1)
    bot.reply_to(message, f"Привет! Я бот {bot.get_me().first_name}!")
    time.sleep(1)
    bot.reply_to(message, "На данный момент у меня есть 10 команд\nВведи /help чтобы узнать о каждой!")


@bot.message_handler(commands=['help'])
def send_help(message):
    time.sleep(2)
    bot.reply_to(message, "/hello - бот поприветствует тебя.\n/bye - бот попрощается с тобой.\n/coin - подбросит монетку.\n/password - сгенерирует случайный пароль.\n/duck - отправляет рандомное милое изображение уток.\n/meme - скинет рандомный мем на любую тематику.\n/ping - проверяет работу бота, если бот не отвечает: он выключен.\n/heh - преумножает любое ваше слово или фразу на то количество,которое вы введете.\nПравильная запись:\n/heh слово количество раз\n/dog - бот отправит тебе милое изображение собачек\n/fox - отправляет рандомную картинку с лисами")


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
