import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/good'
API_KEY = '5340785299:AAHcd8pUsViKK2-NYjV5rf_j36fC2yQqMEI'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Hello. Here you can find some stupid jokes. Input 1-9 digit and enjoy:')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Input 1-9 digit:')
bot.polling()