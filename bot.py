import telebot
from config import *
import sqlite3 
con = sqlite3.connect() 
cur = con.cursor()

con.close()

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"привет ,я бот технической поддержки ты можешь меня спросить 6 следующих вопросов.\nКак оформить заказ?\nКак узнать статус моего заказа?\nКак отменить заказ?\nЧто делать, если товар пришел поврежденным?\nКак связаться с вашей технической поддержкой?\nКак узнать информацию о доставке?")
 
@bot.message_handler(content_types=['text'])
def obrabotka(message):
    print(message.from_user)
    lst_1 = []
    k = 0 
    for i in message.text.split():
        con = sqlite3.connect(database) 
        cur = con.cursor()
        cur.execute("SELECT * FROM answersquestions")
        lst = cur.fetchall() 
        for x in lst:
            if message.text == x[1]:
                bot.reply_to(message, x[0])
                k = 1
                break
           
            if i in x[1]:
                if x[1] not in lst_1:
                    lst_1.append(x[1])
            
                
        con.close()
        if k == 1:
            break
    else:
        if lst_1:
            bot.reply_to(message, '\n'.join(lst_1))
        else:
            bot.send_message(1362499598, message.text+'.'+message.from_user.username)
            



    
bot.infinity_polling()
