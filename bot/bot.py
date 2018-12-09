from telegram.ext import Updater, CommandHandler, RegexHandler
import time

status = 'idle'

#note: this is a mock telegram bot. This bot is used only to show how this bot would work if we had time to code it.

# conversation starting.
def start(bot, update):
	chat_id = update.message.chat_id
	#once the first message is received, wait for a long time so the user can erase messages
	time.sleep(7)
	bot.sendMessage(chat_id=chat_id,text = 'Sete coisas importantes para um relacionamento saudável:')
	time.sleep(2)
	bot.sendMessage(chat_id=chat_id,text = '1.	Sentir-se confortável e segura perto da outra pessoa\n2.Estar em um relacionamento em que a liberdade de escolha seja a base da relação\n3.	Ter o diálogo como elemento fundamental para resolver as discordâncias')
	time.sleep(4)
	bot.sendMessage(chat_id=chat_id,text = '4.	Estar com alguém que valorize quem você é\n 5.	Ser uma pessoa melhor primeiro para você mesma\n6.	Ter um(a) companheiro(a) que vibre com as suas conquistas')
	time.sleep(3)
	bot.sendMessage(chat_id=chat_id,text = 'Você sente falta dessas coisas no seu relacionamento?')

def getReply(bot, update):
	time.sleep(1)
	update.message.reply_text('Te entendo. Isso acontece com muitas mulheres')
	time.sleep(2)
	update.message.reply_text('Aqui tem algumas dicas para você lidar melhor com isso, e algumas redes que podem te apoiar. www.valentina.com/guia-relacionamento-saudavel')
	time.sleep(3)
	update.message.reply_text('Se precisar de mim, estou sempre aqui!')



updater = Updater('528704631:AAHGVV17f0VujJjxWVhOsrOz2v_6o-NOXTM')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(RegexHandler('sim', getReply))

updater.start_polling()
updater.idle()