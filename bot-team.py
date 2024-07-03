#from config import *
pip install -r requirements.txt
import telebot
#instanciamos el bot de telegram
TELEGRAM_TOKEN = "7396093828:AAGnVl82-lG7hBlkbuSJpXRayEy_pJJbY8A"
bot = telebot.TeleBot(TELEGRAM_TOKEN)



#responde al comando / start
#@bot.message_handler(commands=["start", "ayuda", "help"])
#def cmd_start(message):
    #bot.reply_to(message, "Hola, como estas?")

#responde a los mensajes de texto que no son comandos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    #formatos HTML
    #texto_html = '<b><u>Formatos HTML</u>:</b>' + '\n' #negrita en HTML
    #texto_html += '<b>Hello handsome</b>' + '\n' #negrita en HTML
    #texto_html += '<i>how are you</i>' + '\n' #cursiva en HTML
    texto_html = '<b>PEPE DJEN TEAM</b>' 
    texto_html += ' ' + '\n' #cursiva en HTML
    texto_html += 'Project Owner: @stephadvisor' + '\n' 
    texto_html += 'Project Lead: @hipworth' + '\n' 
    texto_html += 'Bot Dev: @crypto_LDyz' + '\n' #cursiva en HTML
    texto_html += 'CM: @AnDj' + '\n' #cursiva en HTML
    texto_html += ' ' + '\n' #cursiva en HTML
    texto_html += 'A subsidiary of The Klub S.A.S' + '\n' #cursiva en HTML
    #bot.send_photo(message.chat.id, foto)
    #texto_html += '<s>some</s>' + '\n' #tachado en HTML
    #texto_html += '<code>decaff</code>' + '\n' #monoespaciado en HTML
    #texto_html += '<span class="tg-spoiler">SPOILER</span>' + '\n' #spoiler en HTML
    #texto_html += '<a href="https://pepedjen.djenerates.com/">PEPE DJEN Web Page</a>' + '\n' #enlace en HTML
    #formatos MarkdownV2
    #texto_markdown = '*__Formatos Markdown__:*' + '\n'
    #texto_markdown += '*NEGRITA*' + '\n'
    #texto_markdown += '_CURSIVA_' + '\n'
    #texto_markdown += '__SUBRAYADO__' + '\n'
    #texto_markdown += '~TACHADO~' + '\n'
    #texto_markdown += '```MONOESPACIADO```' + '\n'
    #texto_markdown += '||SPOILER||' + '\n'
    #texto_markdown += '[ENLACE](https://pepedjen.djenerates.com/)' + '\n'
    
    image_path = 'C:/Python/PythScripts/pepedjen.jpg'
    #foto += open(image_path, "rb")

    if message.text.startswith("/team"):
        #bot.send_message(message.chat.id, texto_html, parse_mode="html", disable_web_page_preview=False) 
        foto = open(image_path, "rb")
        bot.send_photo(message.chat.id, foto, caption=texto_html, parse_mode ="html") 
         
    else:
        bot.send_message(message.chat.id)
        


if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
