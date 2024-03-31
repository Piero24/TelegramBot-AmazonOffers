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
import holidays
from datetime import date, datetime

# Importing internal modules
from configs import settings
from utils.log_manager import setup_logger

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

def is_active() -> bool:
    """Checks if the current time falls within a specified range.

    Returns:
        bool: True if the current time falls within the specified range 
            defined by MIN_HOUR, MIN_MINUTE, MAX_HOUR, and MAX_MINUTE 
            parameters, otherwise False.
    """
    now = datetime.now().time()
    current_hour = now.hour
    current_minute = now.minute

    MIN_HOUR = settings.MIN_HOUR
    MIN_MINUTE = settings.MIN_MINUTE

    MAX_HOUR = settings.MAX_HOUR
    MAX_MINUTE = settings.MAX_MINUTE

    # Check if the current time is within the specified range
    if ((MIN_HOUR < current_hour < MAX_HOUR) or 
        (current_hour == MIN_HOUR and current_minute >= MIN_MINUTE) or 
        (current_hour == MAX_HOUR and current_minute <= MAX_MINUTE)):
        return True
    else:
        return False

def is_not_sunday() -> bool:
    """Checks if the current day is not Sunday.

    Returns:
        bool: True if the current day is not Sunday, otherwise False.
    """
    now = datetime.now()
    return not now.weekday() == 6

def is_during_holidays(country: str) -> bool:
    """Checks if the current date is a holiday in the specified country.

    Args:
        country (str): The name of the country for which holidays 
            are being checked.

    Returns:
        bool: True if the current date is a holiday in the specified country, 
            otherwise False.
    """
    now = datetime.now()
    holiday_day = holidays.CountryHoliday(country)
    return date(now.year, now.month, now.day) in holiday_day

def waiting_next_iteration() -> None:
    """Waits for a random amount of time before starting the next iteration.

    The function selects a random waiting time from a list of predefined options 
    with corresponding probabilities and then sleeps for that duration.
    """
    waiting_time_list = [20, 40, 60, 80, 100, 120, 140, 160]
    weights = [0.12, 0.13, 0.125, 0.125, 0.12, 0.13, 0.12, 0.13]

    random_n = random.choices(waiting_time_list, weights=weights, k=1)[0]
    random_split = [random_n, random_n + 10]

    random_range = random.choices(random_split, weights=[0.3, 0.7], k=1)[0]
    random_time = random.randint(random_range, (random_range + 10))

    logging.info(f"Waiting {random_time} minutes before next iteration.")
    time.sleep(random_time * 60)

def static_waiting_time() -> None:
    """Waits for a static amount of time before retrying the bot iteration.

    The function waits for a randomly chosen duration between 1500 and 2100 
    seconds before retrying the bot iteration.
    """
    time_to_wait = random.randint(1500, 2100)
    logging.info(f"Not the right time to iterate the bot. Waiting for "
                 f"{int(time_to_wait / 60)} minutes before the next iteration.")
    time.sleep(time_to_wait)
    logging.info("Waiting completed. Retrying.")

def amz_wait_time() -> None:
    """Waits for a random amount of time before retrying the bot iteration.

    The function waits for a randomly chosen duration between 2 and 3 minutes
    before retrying the bot iteration.
    """
    time_to_wait = random.randint(2, 3)
    logging.debug(f"Waiting {time_to_wait} minutes for Status Code: 429.")
    time.sleep(time_to_wait*60)