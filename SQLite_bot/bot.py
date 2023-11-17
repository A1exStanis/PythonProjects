import telebot
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
    name = get_name(message)
    time = get_time(message)
    print(time)
    bot.send_message(message.chat.id, 'Done')


def get_name(message) -> str:
    name = message.from_user.first_name + " " + message.from_user.last_name
    return name

def get_time(message) -> str:
    time = dt.datetime.fromtimestamp(message.date)
    return time

bot.polling(none_stop=True)