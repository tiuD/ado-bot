import logging

from telegram.ext import Updater

import config
from components import register

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=config.telegram_token)

register(updater.dispatcher)

updater.start_polling()

updater.idle()
