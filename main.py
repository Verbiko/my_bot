from bs4 import BeautifulSoup as b #
import random
import requests
import telebot
bot = telebot.TeleBot('5139733032:AAGQwLS5Ri4gjoHLPmsKSC-VTUyn549Zx5Y')
@bot.message_handler(commands=['start']) #/start
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
url = 'https://nekdo.ru/short/2/'   #cссылка на страницу с анекдотами
r = requests.get(url) #получаем текст страницы
#print(r.status_code)  проверка
#print(r.text)
soup = b(r.text, 'html.parser') #применяем парсер
#print(soup)
anekdots = soup.find_all('div', class_='text') #получаем все дивы класса текст #'div.class_name h3'
#print(anekdots)
clear_anekdots =[]
for i in anekdots:
    clear_anekdots.append(i.text)
#print(clear_anekdots)
#print(random.choice(clear_anekdots))
@bot.message_handler()
def get_jokes(message):
    if message.text == 'анекдот' or message.text == 'Анекдот':
        bot.send_message(message.chat.id, random.choice(clear_anekdots))
bot.polling(none_stop=True)