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

# Imported modules
import telebot
import logging

# Imported modules
from utils.product import Product
from configs import api_keys
from messages.message import Message
from utils.log_manager import setup_logger

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

def single_message(bot: telebot.TeleBot, product: Product) -> bool:
    """Sends a single message about a product to a channel.

    Args:
        bot (telebot.TeleBot): The Telegram bot instance.
        product (Product): The product to send a message about.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    PARTNER_TAG = api_keys.PARTNER_TAG
    CHANNEL_ID = api_keys.CHANNEL_ID

    try:
        mess = Message.from_product(product, PARTNER_TAG)

    except Exception as e:
            logging.error(f"An error occurred while extracting the message "
                          f"information from the product for the "
                          f"asin {product.asin}: {e}")
            return False
    
    try:
        html = Message.html_message(mess)

    except Exception as e:
            logging.error(f"An error occurred while creating the html message "
                          f"for the asin {product.asin}: {e}")
            return False
    
    try:
        markup = Message.markup_generator(mess, PARTNER_TAG)

    except Exception as e:
            logging.error(f"An error occurred while creating the markup "
                          f"object for the asin {product.asin}: {e}")
            return False

    try:    
        bot.send_message(CHANNEL_ID, html, parse_mode = 'html',
                         reply_markup=markup)
        
    except Exception as e:
            logging.error(f"Error when sending the message for "
                          f"the asin {product.asin} to the channel: {e}")
            return False
    
    logging.info(f"Message send successfully for the asin {product.asin}")
    return True
