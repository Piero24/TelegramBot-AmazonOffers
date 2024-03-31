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
import os
import logging
from datetime import datetime

def setup_logger() -> logging.Logger:
    """
    Set up and configure a logger for logging messages.

    The function creates a logger that outputs messages to a file in the 'log' 
    directory. The log file is named based on the current year and month.

    Returns:
        logging.Logger: The configured logger.

    Example:
        Add the following code to the top of a file to configure a 
            logger for that file.
        setup_logger()
        logger = logging.getLogger(__name__)

        Add one of the following code to log a message.
        logger.info("This is an info message.")
        logger.warning("This is a warning message.")
        logger.error("This is an error message.")
        logger.debug("This is a debug message.")
        logging.critical("This is a critical message.")
    """
    now = datetime.now()
    log_directory = f"./log/{now.strftime('%Y')}"
    log_file = f"{log_directory}/{now.strftime('%m')}.log"

    # Create directories if they don't exist
    os.makedirs(log_directory, exist_ok=True)

    pre_format = '%(asctime)s :: [%(filename)-25s] - [%(funcName)-23s]'
    post_format = '[%(levelname)-8s] - %(message)s'

    format = pre_format + ' - ' + post_format
    # Configure logging to output messages to a file
    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format=format,
                        datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger()
    return logger