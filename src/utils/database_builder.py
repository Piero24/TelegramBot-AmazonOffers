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
import ast
import logging
import sqlite3
from typing import Optional
from datetime import datetime, timedelta

# Importing internal modules
from utils.product import Product
from utils.log_manager import setup_logger
from utils import functions_toolbox

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

def add_to_database(product: Product, name: Optional[str] = '') -> str:
    """Adds a product to the database.

    Args:
        product (Product): The product to add to the database.
        name (str, optional): The name of the database. Defaults to ''.

    Returns:
        str: The ASIN of the added product.
    """
    now = datetime.now()

    if not name :

        name = f"{now.strftime('%m')}"
        db_path = f"./database/{now.strftime('%Y')}/"
        db_name = f"{db_path}/{name}.db"

        table_name = f"day_{now.strftime('%d')}"

    else:
        db_path = f"./database/"
        db_name = f"{db_path}/{name}.db"

        table_name = "waiting_list"

    os.makedirs(db_path, exist_ok=True)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    conn.execute(
        f'''CREATE TABLE IF NOT EXISTS {table_name} (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            ASIN TEXT,
            "DATE ADDED" DATE
        );'''
    )

    try:

        if product.date_added is None:
            # Get the current date in the format YYYY-MM-DD
            current_date = datetime.now().strftime('%Y-%m-%d')

        else :
            current_date = product.date_added

        cursor.execute(f"INSERT INTO {table_name} "
                       "(ASIN, 'DATE ADDED') "
                       "VALUES (?, ?)",
                       (product.asin, current_date,))
        
        conn.commit()

    except sqlite3.IntegrityError:
        logging.error(f"Error when try to insert the product: "
                      f"{product.asin} to the database {name}.")
        return ''

    conn.close()
    return product.asin

def correctly_added(asin_list: list[str]) -> None:
    """Log the correct addition of products with ASINs to the database.

    The function logs a debug message indicating that products with the 
    specified ASINs have been correctly added to the database.

    Args:
        asin_list (list[str]): A list of ASINs for products that have been 
            added to the database.

    Example:
        correctly_added(['ASIN1', 'ASIN2', 'ASIN3'])
    """
    logging.debug(f"Products with ASINs: {asin_list} "
                  f"correctly added to the database.")

def is_valid_for_resend(product: Product, max_days: int) -> bool:
    """Check if this product has already been sent in the latest messages.

    If not enough products have already been shipped on the same day,
        check the number of products remaining in the previous days.

    Args:
        product (Product): Product object with all its characteristics.
        number_msg_to_check (int): Number of products you want to check.

    Returns:
        Return 1 if this product has already been sent. 0 otherwise.
    """
    for day_index in range(0, max_days):
        now = datetime.now()
        new_date = now - timedelta(days=day_index)

        try:
            db_path = f"./database/{new_date.strftime('%Y')}/"
            db_name = f"{db_path}/{new_date.strftime('%m')}.db"
            os.makedirs(db_path, exist_ok=True)

            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
        
        except sqlite3.Error as e:
            logging.error("SQLite error:", e)
        
        try:
            cursor.execute(f'''
                            SELECT *
                            FROM day_{new_date.strftime("%d")}
                            WHERE ASIN = ?''', (product.asin,))
            
        except sqlite3.OperationalError as e:
            error_message = str(e)
            err_msg = f"no such table: day_{new_date.strftime('%d')}"

            if error_message != err_msg: 
                logging.warning(f"SQLite error: {error_message} - Can't "
                                f"connect to the table "
                                f"day_{new_date.strftime('%d')}.")
            continue

        try:
            # Fetch all ASINs from the database for the specific day
            rows = cursor.fetchall()

            if len(rows) < 1:
                conn.close()
                continue

            else:
                conn.close()
                logging.debug(f"Asin: {product.asin} already sent on "
                              f"{new_date.strftime('%d-%m-%Y')}.")
                return False

        except Exception as e:
            logging.error(f"Error during the ferch of the price "
                            f"for the asin:{product.asin} - {e}")
    return True

def check_products_in_list(
        product_list: list[Product], 
        max_days: int
    ) -> list[Product]:
    """Check products in a list for validity based on the maximum number of days

    The function iterates through a list of product objects and filters out 
    products that are valid for resend based on the maximum number 
    of days specified.

    Args:
        product_list (List[Product]): A list of Product objects to be checked.
        max_days (int): Maximum number of days considered for product validity.

    Returns:
        List[Product]: List of valid products based on the max number of days.

    Example:
        valid_products = check_products_in_list(products_list, 7)
    """
    products_valid_to_send = []

    for product in product_list:
        if is_valid_for_resend(product, max_days):
            products_valid_to_send.append(product)
    
    return products_valid_to_send