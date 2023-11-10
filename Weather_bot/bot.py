import telebot
from telebot.types import Message
import constant, json, requests
import utills

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
                 data['main']['temp'],
                 reply_markup=markup)
        bot.register_next_step_handler(message,message_varification_handler, data)
    elif message.text == constant.WHEATHER:
        pass
    elif message.text == constant.WIND:
        pass
    elif message.text == constant.SUNRISE_SET:
        pass

bot.polling(non_stop=True)