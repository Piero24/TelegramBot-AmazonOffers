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
import random
import shutil
import logging
import os
from datetime import datetime

# Importing internal modules
from utils.log_manager import setup_logger

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

def choose_max_offers_number() -> int:
    """Choose a random number of maximum offers based on predefined 
        probabilities.

    The function uses a predefined dictionary of numbers and their associated
    probabilities to randomly select a number of maximum offers.

    Args:
        None

    Returns:
        int: The chosen number of maximum offers.
    """
    numbers_probabilities = {2:0.1, 3: 0.12, 4: 0.2, 5: 0.3, 6: 0.28}
    chosen_number = random.choices(list(numbers_probabilities.keys()), 
                                   list(numbers_probabilities.values()))[0]
    return chosen_number

def delete_folder(folder_path: str) -> bool:
    """Deletes a folder and all its contents.

    Args:
        folder_path (str): The path to the folder to be deleted.

    Returns:
        bool: True if the folder and its contents were successfully deleted, 
            False otherwise.

    """
    try:
        shutil.rmtree(folder_path)
        logging.debug(f"The folder {folder_path} and all its "
                      f"contents were successfully deleted.")
        return True
    
    except FileNotFoundError:
        logging.debug(f"The folder {folder_path} does not exist.")

    except Exception as e:
        logging.error(f"There is an error when try to delete "
                      f"the folder {folder_path}: {e}.")
    return False

def split_number(num_min: int, num_max: int) -> list:
    """Split a number randomly into three parts such that:
    - The first part (A) constitutes 60% of the number
    - The second part (B) constitutes 25% of the number
    - The third part (C) constitutes the remaining 25% of the number

    Args:
        num_min (int): The minimum value for the random number generation.
        num_max (int): The maximum value for the random number generation.

    Returns:
        list: A list containing three integers representing the split numbers 
            [num_A, num_B, num_C].
    """
    # 8 - 50%, 25%, 25%
    num = random.randint(num_min, num_max)

    num_A, num_B = int(num * 0.6), int(num * 0.25)
    num_C = num - num_A - num_B
    remaining = num - 8

    while remaining > 0:
        weights=[0.3, 0.4, 0.3]
        # Choose the split for the remaining part
        split_choice = random.choices(['A', 'B', 'C'], weights=weights)[0]
        
        if split_choice == 'A': num_A += 1
        elif split_choice == 'B': num_B += 1
        else: num_C += 1
        
        remaining -= 1
    return [num_A, num_B, num_C]

def count_strings(dictionary: dict) -> tuple:
    """Counts the number of strings in each list within a dictionary and 
        calculates the total count.

    Args:
        dictionary (dict): A dictionary where keys are categories and 
            values are lists of strings.

    Returns:
        tuple: A tuple containing two elements:
               - dict_counts: A dictionary where keys are categories and 
                    values are the counts of strings in each category.
               - total_count (int): The total count of strings 
                    across all categories.
    """
    total_count = 0
    dict_counts = {}

    for key, lst in dictionary.items():
        dict_counts[key] = len(lst)
        total_count += len(lst)

    return dict_counts, total_count

def lists_categories_probability(dict_counts: dict) -> tuple:
    """Extracts keys and their corresponding counts from a dictionary.

    Args:
        dict_counts (dict): A dictionary with keys as categories and 
            values as counts.

    Returns:
        tuple: A tuple containing two lists: key_list and quantity_values_list.
               - key_list: List of keys (categories).
               - quantity_values_list: List of counts corresponding 
                    to each category.
    """
    key_list, quantity_values_list = [], []

    for key, value in dict_counts.items():
        key_list.append(key)
        quantity_values_list.append(value)
    
    return key_list, quantity_values_list

def build_archive() -> None:

    folders_path = [
        "archive", 
        "archive/img", 
        "archive/tmp", 
        ]

    for folder in folders_path:
        os.makedirs(folder, exist_ok=True)

def str_to_datetime(date_string: str) -> datetime.date:
    """Converts a string to a datetime object.

    Args:
        date_string (str): A string representing a date in the format 
            "YYYY-MM-DD".
    
    Returns:
        datetime: A datetime object representing the input date.
    """
    new_date = datetime.strptime(date_string, "%Y-%m-%d")
    return new_date.date()