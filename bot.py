import telebot
from config import *



bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,"привет")




    
bot.infinity_polling()
