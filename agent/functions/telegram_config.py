import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

load_dotenv()

def verifica_texto(mensagem):
    return mensagem.text is not None and not mensagem.text.startswith('/')

async def processa_mensagem(update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = update.message
    chat_id = update.effective_chat.id
    user = update.message.from_user

    if mensagem.text:
        print(f"Mensagem recebida de {user.first_name} ({user.id}): {mensagem.text}")
        msg = mensagem.text
        resposta = responder_mensagem(msg)
        await context.bot.send_message(chat_id=chat_id, text=resposta)

def responder_mensagem(mensagem):
    return mensagem

def main():
    app = ApplicationBuilder().token(os.environ["TELEGRAM_KEY"]).build()
    app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), processa_mensagem))
    app.run_polling()