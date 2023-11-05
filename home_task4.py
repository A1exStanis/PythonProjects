import json
from urllib import parse, request

key = "doIX6GNX4FmoDRBZbZ8kPy1AHlF7C8pR"
url = "http://api.giphy.com/v1/gifs/search"
number_of_links = "5"



def giphy_gif(name:str) ->list:
  links = []
  # name = input("Input a name: ")
  params = parse.urlencode({
    "q": f"{name}",
    "api_key": key,
    "limit": number_of_links
  })
  with request.urlopen("".join((url, "?", params))) as response:
    data = (json.loads(response.read()))["data"]
  links = [item["url"] for item  in data]
  return links


import telebot
from project1 import giphy_gif

api_key = "6206705730:AAGDucqSW0Nh5vAlYvZi6N4auxvRa6TT46Q"
bot = telebot.TeleBot(api_key)

@bot.message_handler()
def answering(message: list) -> str:
    name = message.text
    links = giphy_gif(name)
    for link in links:
        bot.send_message(message.chat.id, f"{link}")



bot.polling(non_stop=True)