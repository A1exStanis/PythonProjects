import pandas as pd
import telebot
from telebot.types import Message
from utils import (
    build_reply_markup,
    phone_request,
    get_df_from_sheet
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
        markup = build_reply_markup(constant.CHOICE_BUTTONS)
        bot.send_message(message.chat.id,
                         constant.ORDER_3_7_DAYS_MESSAGE,
                         reply_markup=markup)
        bot.register_next_step_handler(message, order_3_7_handler)
    elif message.text == constant.ORDER_12_15_DAYS:
        markup = build_reply_markup(constant.CHOICE_BUTTONS)
        bot.send_message(message.chat.id,
                         constant.ORDER_12_15_DAYS_MESSAGE,
                         reply_markup=markup)
        bot.register_next_step_handler(message, order_12_15_handler)
    elif message.text == constant.SPECIAL_OFFERS:
        markup = phone_request()
        bot.send_message(message.chat.id,
                         constant.SPECIAL_OFFERS_MESSAGE,
                         reply_markup=markup)
        bot.register_next_step_handler(message, receive_call_handler)
    elif message.text == constant.ABOUT_US:
        markup = build_reply_markup([constant.BACK])
        bot.send_message(message.chat.id,
                         constant.ABOUT_US_MESSAGE,
                         reply_markup=markup)
        bot.register_next_step_handler(message, receive_call_handler)
    else:
        markup = markup = build_reply_markup(constant.WELCOME_BUTTONS)
        bot.send_message(message.chat.id,
                         constant.USE_BUTTONS_MESSAGE,
                         reply_markup=markup)
        bot.register_next_step_handler(message, next_step)


def receive_call_handler(message: Message) -> None:
    if message.contact:
        markup = build_reply_markup([constant.BACK])
        bot.send_contact(message.chat.id,   #constant.VLAD_CHAT_ID,
                         phone_number=message.contact.phone_number,
                         first_name=message.contact.first_name,
                         last_name=message.contact.last_name)
        bot.send_message(message.chat.id,
                         constant.ANSWER_FOR_CALL_REQUEST,
                         reply_markup=markup)
    elif message.text == constant.BACK:
        start(message)
    else:
        markup = phone_request()
        bot.send_message(message.chat.id,
                         constant.USE_NUMBER_BELOW,
                         reply_markup=markup)
        bot.register_next_step_handler(message, receive_call_handler)


def order_3_7_handler(message: Message) -> None:
    df = get_df_from_sheet(sheet_url=constant.SPREDSHEET_URL, sheet_id=constant.SHEET_ID_3_7)
    if message.text == constant.BACK:
        start(message)
    elif message.text == constant.SNEAKERS:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.SNEAKERS]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler)
    elif message.text == constant.SWEATSHIRT:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.SWEATSHIRT]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler)
    elif message.text == constant.SHORTS:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.SHORTS]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler)
    elif message.text == constant.T_SHIRT:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.T_SHIRT]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler)
    elif message.text == constant.ACCESSORIES:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.ACCESSORIES]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler)
    else:
        markup = phone_request()
        bot.send_message(message.chat.id,
                         constant.USE_NUMBER_BELOW,
                         reply_markup=markup)
        bot.register_next_step_handler(message, order_3_7_handler)


def order_12_15_handler(message: Message) -> None:
    df = get_df_from_sheet(sheet_url=constant.SPREDSHEET_URL, sheet_id=constant.SHEET_ID_12_15)
    if message.text == constant.BACK:
        start(message)
    elif message.text == constant.SNEAKERS:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.SNEAKERS]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler_12_15)
    elif message.text == constant.SWEATSHIRT:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.SWEATSHIRT]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler_12_15)
    elif message.text == constant.SHORTS:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.SHORTS]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler_12_15)
    elif message.text == constant.T_SHIRT:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.T_SHIRT]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler_12_15)
    elif message.text == constant.ACCESSORIES:
        goods = list(str(df.loc[constant.SPREADSHEET_LOC_BY_TEXT[constant.ACCESSORIES]]).split(','))
        markup = build_reply_markup(constant.ORDER_BUTTONS)
        for position in goods:
            bot.send_message(message.chat.id,
                             position,
                             reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler_12_15)
    else:
        markup = phone_request()
        bot.send_message(message.chat.id,
                         constant.USE_NUMBER_BELOW,
                         reply_markup=markup)
        bot.register_next_step_handler(message, order_12_15_handler)


def call_or_back_handler(message: Message) -> None:
    if message.text == constant.BACK:
        markup = build_reply_markup(constant.CHOICE_BUTTONS)
        bot.send_message(message.chat.id,
                         constant.ORDER_3_7_DAYS_MESSAGE,
                         reply_markup=markup)
        bot.register_next_step_handler(message, order_3_7_handler)
    elif message.text == constant.CALL:
        receive_call_handler(message)
    else:
        markup = phone_request()
        bot.send_message(message.chat.id,
                         constant.USE_NUMBER_BELOW,
                         reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler)


def call_or_back_handler_12_15(message: Message) -> None:
    if message.text == constant.BACK:
        markup = build_reply_markup(constant.CHOICE_BUTTONS)
        bot.send_message(message.chat.id,
                         constant.ORDER_3_7_DAYS_MESSAGE,
                         reply_markup=markup)
        bot.register_next_step_handler(message, order_12_15_handler)
    elif message.text == constant.CALL:
        receive_call_handler(message)
    else:
        markup = phone_request()
        bot.send_message(message.chat.id,
                         constant.USE_NUMBER_BELOW,
                         reply_markup=markup)
        bot.register_next_step_handler(message, call_or_back_handler_12_15)


bot.polling(non_stop=True)
