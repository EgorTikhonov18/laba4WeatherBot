import telebot
from telebot import types
import config
import geo
import weather_api

bot = telebot.TeleBot(config.bot_key)
global text_reading_flag
text_reading_flag = False

@bot.message_handler(commands=['help','start'])
def commands(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/weather")
    markup.add(btn1)
    bot.send_message(message.from_user.id,"<b>Список команд</b>\n"
                                          "<i>/help</i> или <i>/start</i> - Вывод этого сообщения.\n"
                                          "<i>/weather</i> - работа с погодой\n",
                                            parse_mode='html',reply_markup=markup)

@bot.message_handler(commands=['weather'])
def weather(message):
    global text_reading_flag
    bot.send_message(message.from_user.id, "Введите название города на английском")
    text_reading_flag = True


@bot.message_handler(content_types=['text'])
def get_weather(message):
    global text_reading_flag
    if text_reading_flag:
        try:
            coords = geo.get_coordinates(message.text)
            weather = weather_api.get_weather(coords)
            bot.send_message(message.from_user.id, f"Погода в городе {message.text}: \n{weather.weather}\nТемпература: {weather.temperature} градусов Цельсия\nСкорость ветра {weather.wind} м/c")
            text_reading_flag = False
        except Exception:
            bot.send_message(message.from_user.id, "Город либо введен неверно, либо его нету в базе данных")


bot.polling(none_stop=True)