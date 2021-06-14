import logging

from telegram.ext import Updater
from components import register

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater('1876415562:AAHc6EqouChhhGSaW5--Ny6JlJeMbvXrzgs')

register(updater.dispatcher)

updater.start_polling()

updater.idle()
