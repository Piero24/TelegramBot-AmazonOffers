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
import random
import logging

# External libraries
import telebot

# Importing internal modules
from utils import time_scheduler
from utils import list_manager
from utils.product import Product
from utils import database_builder
from messages import communication_handler
from configs import settings
from utils.log_manager import setup_logger
from utils import functions_toolbox

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

def start(bot: telebot.TeleBot) -> None:
    """Initiates the process of sending product offers to users.

    This function checks if it's an appropriate time to send offers, 
    then extracts valid offers from a list, checks their validity, 
    shuffles them, selects a number of offers to send, sends each offer 
    individually to users, updates the database with sent offers, and logs 
    the completion of the iteration.

    Args:
        bot (telebot.TeleBot): The Telegram bot object.
    """
    # if ((time_scheduler.is_active()) and (time_scheduler.is_not_sunday()) and 
    #     (not time_scheduler.is_during_holidays(settings.COUNTRY))):
    if True:
        valid_offers_list = list_manager.extraction_raw_products()
        products_list = []

        if valid_offers_list:
            
            products_list_raw = Product.list_to_products(valid_offers_list)
            products_list = database_builder.check_products_in_list(
                products_list_raw, 
                settings.MAX_DAYS_TO_CHECK)

        # Take from the db the products and discard if already in the list.
        # If not check if the offer is still valid. If so add it to the list.
        random.shuffle(products_list)

        if products_list:
            MAX_OFFERS = functions_toolbox.choose_max_offers_number()
            selected_products = list_manager.offers_extractor(products_list, 
                                                              MAX_OFFERS)  
            asin_sended_list = []
            for product in selected_products:
                result = communication_handler.single_message(bot, product)

                if result:
                    asin = database_builder.add_to_database(product)
                    asin_sended_list.append(asin)
            
            database_builder.correctly_added(asin_sended_list)

            # time_scheduler.waiting_next_iteration()
            time.sleep(60*15)
        logging.info("Iteration completed.")
    
    else:
        time_scheduler.static_waiting_time()
