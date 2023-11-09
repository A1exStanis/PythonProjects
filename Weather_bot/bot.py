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
    markup = utills.build_inline_markup()
    city = message.text.strip().lower()
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={constant.API_weather}&units=metric')
    data = json.loads(result.text)
    bot.send_message(message.chat.id, data['main']['temp'])

bot.polling(non_stop=True)