# Copyright (C) by Pietrobon Andrea - All Rights Reserved
#
# This file is part of the project: TelegramBot-AmazonOffers
# It can only be distributed from Andrea Pietrobon's official Github profile
# The use of the project TelegramBot-AmazonOffers or of this file follow
# the rules indicated in the LICENSE file.
# The redistribution or sale of the files without the written consent 
# of the author is not authorized.
#
# Written by Pietrobon Andrea, Jan 2024
# Official website <https://pietrobonandrea.com>
# Github website <https://github.com/Piero24>

# Standard library modules
import time
import logging

# External libraries
import telebot

# Importing internal modules
from utils import bot_starter
from web import activity_inspector
from utils.log_manager import setup_logger
from configs import api_keys

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

# Initialize the Telegram bot
bot = telebot.TeleBot(api_keys.TELEGRAM_TOKEN)

if __name__ == "__main__":

    activity_inspector.run_server_thread()

    while True:
        try:
            bot_starter.start(bot)
            
        except ConnectionError:
            logging.error('Internet connection error. Retry in 20 minutes.')
            time.sleep(1200)
            
        except Exception as e:
            logging.critical(f'Error during bot execution: {type(e)} - {e}')