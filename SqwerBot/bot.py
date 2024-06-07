import telebot
from telebot.types import Message
from utils import (
    build_reply_markup,
    build_inline_markup,
    phone_request
)
import constant

bot = telebot.TeleBot(constant.API_KEY)


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    markup = build_reply_markup(constant.WELCOME_BUTTONS)
    bot.send_message(message.chat.id,
                     constant.WELCOME_MESSAGE,
                     reply_markup=markup,
                     parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def next_step(message: Message) -> None:
    if message.text == constant.FEEDBACK:
        markup = phone_request()
        bot.send_message(message.chat.id,
                         constant.NUMBERS,
                         reply_markup=markup)
        bot.register_next_step_handler(message, receive_call_handler)
    elif message.text == constant.ORDER_3_7_DAYS:
        pass
    elif message.text == constant.ORDER_12_15_DAYS:
        pass
    elif message.text == constant.SPECIAL_OFFERS:
        pass


def receive_call_handler(message: Message) -> None:
    if message.contact:
        markup = build_reply_markup([constant.BACK])
        bot.send_contact(message.chat.id,
                         phone_number=message.contact.phone_number,
                         first_name=message.contact.first_name,
                         last_name=message.contact.last_name)
        bot.send_message(message.chat.id,
                         constant.ANSWER_FOR_CALL_REQUEST,
                         reply_markup=markup)
        bot.register_next_step_handler(message, message_verification_handler)
    elif message.text == constant.BACK:
        start(message)
    else:
        markup = phone_request()
        bot.send_message(message.chat.id,
                         constant.USE_NUMBER_BELOW,
                         reply_markup=markup)
        bot.register_next_step_handler(message, receive_call_handler)


def message_verification_handler(message: Message) -> None:
    if message.text == constant.BACK:
        start(message)


bot.polling(non_stop=True)
