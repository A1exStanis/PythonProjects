import telebot
from telebot import types
import sqlite3
import constant
import datetime as dt

bot = telebot.TeleBot(constant.API_KEY)

@bot.message_handler(commands=['start'])

def start(message) -> None:
    connect = sqlite3.connect('testsql.sql')
    typer = connect.cursor()

    typer.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), time varchar(50))')
    connect.commit()
    typer.close()
    connect.close()
    entering(message)


def get_name(message) -> str:
    name = message.from_user.first_name + " " + message.from_user.last_name
    return name

def get_time(message) -> str:
    time = dt.datetime.fromtimestamp(message.date)
    return time

def entering(message) -> None:
    name = get_name(message)
    time = get_time(message)
    connect = sqlite3.connect('testsql.sql')
    typer = connect.cursor()
    typer.execute("INSERT INTO users (name, time) VALUES ('%s','%s')" % (name, time))
    connect.commit()
    typer.close()
    connect.close()

    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Users list', callback_data = ''))
    markup = build_inline_markup({'UsersList':'',})
    bot.send_message(message.chat.id, 'Done', reply_markup=markup)

def build_inline_markup(
    button_list: dict[str, str],
    row_width: int = 2,
) -> types.InlineKeyboardButton:
    markup = types.InlineKeyboardMarkup(row_width=row_width)

    for button, url in button_list.items():
        markup.add(
            types.InlineKeyboardButton(button, url=url)
        )

    return markup

bot.polling(none_stop=True)