import telebot
from telebot.types import Message
import constant
import json
import requests
import utills
import datetime as dt

bot = telebot.TeleBot(constant.API_KEY)


@bot.message_handler(commands=["start"])
def start(message: Message) -> None:
    bot.send_message(message.chat.id, constant.HI_COMAND)


@bot.message_handler(content_types=['text'])
def get_weather(message: Message) -> None:
    markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
    city = message.text.strip().lower()
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={
                          city}&appid={constant.API_weather}&units=metric')
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
                         f'{constant.TEMP_MES}{data['main']['temp']}\n{constant.MIN_MES}{data['main']['temp_min']}\n{
                             constant.MAX_MES}{data['main']['temp_max']}\n{
                             constant.FEELS_MES}{data['main']['feels_like']}',
                         reply_markup=markup)
        bot.register_next_step_handler(
            message, message_varification_handler, data)
    elif message.text == constant.WHEATHER:
        markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
        bot.send_message(message.chat.id,
                         f'{constant.WHETHER_MES}{data['weather'][0]['main']}\n{constant.DESCRIPTION_MES}{
                             data['weather'][0]['description']}',
                         reply_markup=markup)
        bot.register_next_step_handler(
            message, message_varification_handler, data)
    elif message.text == constant.WIND:
        markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
        if 'gust' in data['wind']:
            bot.send_message(message.chat.id,
                             f'{constant.WIND_MES}{data["wind"]["speed"]} {constant.MS_MES}\n{
                                 constant.GUST_MES}{data["wind"]["gust"]} {constant.MS_MES}',
                             reply_markup=markup)
            bot.register_next_step_handler(
                message, message_varification_handler, data)
        else:
            bot.send_message(message.chat.id,
                             f'{constant.WIND_MES}{
                                 data['wind']['speed']} {constant.MS_MES}',
                             reply_markup=markup)
            bot.register_next_step_handler(
                message, message_varification_handler, data)
    elif message.text == constant.SUNRISE_SET:
        markup = utills.build_reply_markup(constant.MAIN_SCREEN_BUTTONS)
        sun_set = dt.datetime.fromtimestamp(data['sys']['sunset'])
        sun_rise = dt.datetime.fromtimestamp(data['sys']['sunrise'])
        bot.send_message(message.chat.id,
                         f'{constant.SUNRISE_MES} {sun_rise}\n{
                             constant.SUNSET_MES}{sun_set}',
                         reply_markup=markup)
        bot.register_next_step_handler(
            message, message_varification_handler, data)
    else:



bot.polling(non_stop=True)
