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

    typer.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), time varchar(50))')
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
    typer.execute(
        "INSERT INTO users (name, time) VALUES ('%s','%s')" % (name, time))
    connect.commit()
    typer.close()
    connect.close()

    markup = build_inline_markup(
        {'UsersList': 'https://send.monobank.ua/jar/5F27ncLLf3'})
    bot.send_message(message.chat.id, 'Done', reply_markup=markup)


def build_inline_markup(
    button_list: dict[str, str],
    row_width: int = 2,
) -> types.InlineKeyboardButton:
    markup = types.InlineKeyboardMarkup(row_width=row_width)

    for button, calldata in button_list.items():
        markup.add(
            types.InlineKeyboardButton(button, callback_data=calldata)
        )

    return markup


@bot.callback_query_handler(func=lambda call: True)

def callback(call) -> None:
    connect = sqlite3.connect('testsql.sql')
    typer = connect.cursor()
    typer.execute('SELECT * FROM users')
    notes = typer.fetchall()

    info = ''
    for number, el in enumerate(notes):
        info += f'ID:{number+1}, Name: {el[1]}, Time: {el[2]}.\n'

    typer.close()
    connect.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
