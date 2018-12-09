from telegram.ext import Updater, CommandHandler, RegexHandler
import time

status = 'idle'

#note: this is a mock telegram bot. This bot is used only to show how this bot would work if we had time to code it.

# conversation starting.
def start(bot, update):
	chat_id = update.message.chat_id
	#once the first message is received, wait for a long time so the user can erase messages
	time.sleep(3)
	bot.sendMessage(chat_id=chat_id,text = 'Como identificar a manipulação?')
	time.sleep(2)
	bot.sendMessage(chat_id=chat_id,text = 'Existe uma diferença entre influência social saudável e manipulação psicológica.')
	time.sleep(4)
	bot.sendMessage(chat_id=chat_id,text = 'Influência social saudável é parte do dar e receber de relacionamentos construtivos. Na manipulação psicológica, uma pessoa é usada para o benefício de outra. A pessoa manipuladora deliberadamente cria um desequilíbrio de poder e o explora para servir aos seus próprios interesses.')
	time.sleep(3)
	bot.sendMessage(chat_id=chat_id,text = 'Alguma destas situações soa familiar para você em algum de seus relacionamentos?')
	status = 'waiting'

def getReply(bot, update):
	time.sleep(1)
	update.message.reply_text('Te entendo. Isso acontece com muitas mulheres')
	time.sleep(2)
	update.message.reply_text('Aqui tem algumas dicas para você lidar melhor com isso, e algumas redes que podem te apoiar. www.valentina.com/guia-manipulação')
	time.sleep(3)
	update.message.reply_text('Se precisar de mim, estou sempre aqui!')



updater = Updater('528704631:AAHGVV17f0VujJjxWVhOsrOz2v_6o-NOXTM')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(RegexHandler('sim', getReply))

updater.start_polling()
updater.idle()