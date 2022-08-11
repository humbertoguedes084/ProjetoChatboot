import telebot


CHAVE_API = "5527586461:AAECrXP4ol1UWYw4UB-y91tEiX751ku4sQA"


bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Toddynho"])
def toddynho(mensagem):
    bot.send_message(mensagem.chat.id, "Otima escolha, caixa com {10} por apenas 15.00")
    bot.send_message(mensagem.chat.id, "Deseja algo mais? Se sim clique em uma ação")


@bot.message_handler(commands=["Fandangos"])
def fandangos(mensagem):
    bot.send_message(mensagem.chat.id, "Otima escolha, caixa com 10 por apenas 15.00")
    bot.send_message(mensagem.chat.id, "Deseja algo mais? Se sim clique em uma ação")
@bot.message_handler(commands=["Sneaker"])
def sneaker(mensagem):
    bot.send_message(mensagem.chat.id,"Otima escolha, caixa com 10 por apenas 20.00")
    bot.send_message(mensagem.chat.id, "Deseja algo mais? Se sim clique em uma ação")
@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):

    texto = """
    O que você quer? (Clique em uma opção)
    /Toddynho 
    /Fandangos 
    /Sneaker"""
    print(toddynho,fandangos,sneaker)
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Seu ultimo pedido foi...")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Seu valor total é...")

@bot.message_handler(commands=["opcao4"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Para falar com um entendente atravez do numero 84 3232-3232")

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá seja bem vindo(a):D é uma enorme satisfação ter voce conosco. Como posso te ajudar? (Clique no item):
     /opcao1 Fazer um pedido
     /opcao2 Ultimo pedido
     /opcao3 Valor total
     /opcao4 Falar com um atendente
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()