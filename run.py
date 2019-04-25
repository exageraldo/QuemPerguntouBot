import sys
import logging
import telegram
from random import randint
from telegram.ext.dispatcher import run_async
from loguru import logger
from telegram.ext import (Updater, StringCommandHandler, StringRegexHandler,
						  MessageHandler, CommandHandler, RegexHandler, Filters)


token = sys.argv[1]
updater = Updater(token)
dp = updater.dispatcher


def start(bot, update):
	texto = "Olá.\nEsse bot foi desenvolvido para fins que não importam a você."
	bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=texto)


def lista(bot, update):
	mensagem = update.message.text
	mensagem = mensagem.replace("/lista","")
	if(not(mensagem)):
		texto = "Lista de quem perguntou:\n1.\n2.\n3.\n4.\n5.\nTotal: ZERO!"
		bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=texto)
	else:
		mensagem = mensagem.replace(" ","")
		texto = "Lista de quem perguntou a opinião de " + str(mensagem) + ":\n1.\n2.\n3.\n4.\n5.\nTotal: <b>ZERO</b>!"
		bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=texto, parse_mode=telegram.ParseMode.HTML)


def add(bot, update):
	mensagem = update.message.text
	mensagem = mensagem.replace("/add","")
	frases = ["Sinceramente, ninguem quer saber da sua opinião ", "Acho melhor você ficar calad@ e se recolher na sua insignificância ",
			"Não adianta inisistir, você nunca será ouvid@ (nem lid@) "]
	if(not(mensagem)):
		texto = "De quem você quis adicionar a opinião?!\n<b>Foda-se</b>. Não é importante de qualquer maneira."
		bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=texto, parse_mode=telegram.ParseMode.HTML)
	else:
		mensagem = mensagem.replace(" ","")
		frase = frases[randint(0,len(frases)-1)]
		texto = str(frase) + str(mensagem) + "."
		bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=texto)


def help(bot, update):
	texto = "<b>Comandos</b>:\n\
			/start - Iniciar o chat com o bot.\n\
			/add - Adicionar a opinião de alguem à lista de pessoas que perguntaram.\n\
			/lista - Listar as pessoas que perguntaram alguma coisa.\n\
			/info - Informação sobre o bot e o desenvolvedor.\n\
			/help - Você está nele, coisa linda da mãe!"
	bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=texto, parse_mode=telegram.ParseMode.HTML)


def info(bot, update):
	texto = "Bot desenvolvido por <b>Geraldo</b> (@exaGeraldo).\nMas ninguem liga pra isso também."
	bot.sendMessage(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=texto, parse_mode=telegram.ParseMode.HTML)


def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))


if __name__ == '__main__':
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("lista", lista))
	dp.add_handler(CommandHandler("add", add))
	dp.add_handler(CommandHandler("info", info))
	dp.add_handler(CommandHandler("help", help))

	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()
