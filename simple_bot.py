from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


updater = Updater("TOKEN", use_context=True)


def location(update: Update, context: CallbackContext):
    print(update.message.location)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello. I'm V-001. Please write /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the YouTube URL
    /github - To get the GitHub profile URL
    /gmail - To get the Gmail URL
    /vk - To get the VK URL
    /map - To get the Yandex Maps URL""")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("Gmail Link => https://mail.google.com/")


def maps_url(update: Update, context: CallbackContext):
    update.message.reply_text("Yandex Maps link => https://yandex.ru/maps/")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link => https://www.youtube.com/")


def github_url(update: Update, context: CallbackContext):
    update.message.reply_text("GitHub URL => https://github.com/Krupshark/")


def vk_url(update: Update, context: CallbackContext):
    update.message.reply_text("VK URL => https://vk.com/")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('vk', vk_url))
updater.dispatcher.add_handler(CommandHandler('map', maps_url))
updater.dispatcher.add_handler(CommandHandler('location', location))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

# Filters out unknown commands
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

print("Bot started!")

updater.start_polling()
