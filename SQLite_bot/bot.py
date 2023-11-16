import telebot
import sqlite3
import constant

bot = telebot.TeleBot(constant.API_KEY)

@bot.message_handler(commands=['start'])

def start(message) -> None:
    connect = sqlite3.connect('testsql.sql')
    typer = connect.cursor()

    typer.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), time varchar(50))')
    connect.commit()
    typer.close()
    connect.close()

    bot.send_message(message.chat.id, 'Done')

bot.polling(none_stop=True)