import telebot
# TOKEN DEFINITIVO VALIDADO DESDE BOTFATHER
TOKEN = '8507245492:AAHLg6b5EITtnjulhPzlxCjRpQd9RFhuvao' 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "dime... mi caballero supremo. aria_v1 esta despierta. todos los mastercores estan operativos y la masterdata lista para aprender.")

print("aria conectando... portal Aria_v1 abierto y estable.")
bot.polling()
