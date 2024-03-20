import telebot

token = '6802722884:AAFlj2XUHzv8a03kqpIrbEc_0gBjWPARU8Q'
bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Как твои дела? Чем я могу помочь?')

@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'Текст содержит слово "плохой"!')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)

bot.polling()