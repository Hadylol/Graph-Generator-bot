from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler,ContextTypes, ConversationHandler

import os
import logging

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)



WAITING_FOR_GRAPH_TYPE=1
WAITING_FOR_DATA_TYPE=2
WAITING_FOR_FILE=3

graph_type="a_graph_type"
file_type="file_type"

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user =update.effective_user
    if update.message and user:
        await update.message.reply_text(f"Welcome {user.first_name} ! to Graph Generator Bot \n /help for More Commands")
async def help(update:Update , context:ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("/graph -to create a new graph ! ")


async def create_graph(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print("hey")
    return CHOSSING_TYPE

async def choose_type(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print("hey")


async def cancel(update:Update,context:ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("Graph Generation canceled, \n /help for more Commands!")
    return ConversationHandler.END

def main()-> None:
    BOT_KEY=os.getenv("BOT_KEY")
    if BOT_KEY is None:
        raise ValueError("Couldnt access BOT KEY")
    bot =Application.builder().token(BOT_KEY).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("graph",create_graph)],
        states={
            CHOSSING_TYPE :[
                CallbackQueryHandler(choose_type)
            ]
        },
            fallbacks=[CommandHandler("cancel",cancel)]
    )





    bot.add_handler(CommandHandler("start",start))
    bot.add_handler(CommandHandler("help",help))
    bot.add_handler(conv_handler)

    bot.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
