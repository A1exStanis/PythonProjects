import telebot
from telebot.types import Message
import constant, json, requests
import utills
import datetime as dt

bot = telebot.TeleBot(constant.API_KEY)


@bot.message_handler(commands=["start"])
def start(message:Message) -> None:
    bot.send_message(message.chat.id, constant.HI_COMAND)

@bot.message_handler(content_types=['text'])
def get_weather(message: Message) -> None:
    markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
    city = message.text.strip().lower()
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={constant.API_weather}&units=metric')
    data = json.loads(result.text)
    bot.send_message(message.chat.id, 
                     constant.GUIDE,
                     reply_markup=markup)
    bot.register_next_step_handler(message, message_varification_handler, data)

def message_varification_handler(message: Message, data: dict) -> None:
    if message.text == constant.BACK:
        bot.send_message(message.chat.id, constant.HI_COMAND)
    elif message.text == constant.TEMPERATURE:
        markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
        bot.send_message(message.chat.id, 
                 f'Temperature now: {data['main']['temp']}\nMinimum: {data['main']['temp_min']}\nMaximum {data['main']['temp_max']}\nFeels like: {data['main']['feels_like']}',
                 reply_markup=markup)
        bot.register_next_step_handler(message,message_varification_handler, data)
    elif message.text == constant.WHEATHER:
        markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
        bot.send_message(message.chat.id, 
                 f'The weater is: {data['weather'][0]['main']}\nDescription: {data['weather'][0]['description']}',
                 reply_markup=markup)
        bot.register_next_step_handler(message,message_varification_handler, data)     
    elif message.text == constant.WIND:
        markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
        if 'gust' in data['wind']:
            bot.send_message(message.chat.id, 
                 f'Wind speed: {data['wind']['speed']} m/s\nGust: {data['wind']['gust']} m/s',
                 reply_markup=markup)
            bot.register_next_step_handler(message,message_varification_handler, data)
        else:
            bot.send_message(message.chat.id, 
                 f'Wind speed: {data['wind']['speed']} m/s',
                 reply_markup=markup)
            bot.register_next_step_handler(message,message_varification_handler, data)
    elif message.text == constant.SUNRISE_SET:
        markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
        sun_set = dt.datetime.fromtimestamp(data['sys']['sunset'])
        sun_rise = dt.datetime.fromtimestamp(data['sys']['sunrise'])
        bot.send_message(message.chat.id, 
                 f'Sunrise: {sun_rise}\nSunset: {sun_set}',
                 reply_markup=markup)
        bot.register_next_step_handler(message,message_varification_handler, data)  

bot.polling(non_stop=True)