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
import random

# External libraries
from paapi5_python_sdk.condition import Condition

# Importing internal modules
from utils.product import Product
from utils import amz_paapi_sdk
from configs import category_keywords
from configs import settings
from configs import api_keys
from utils.log_manager import setup_logger
from utils import functions_toolbox
from utils import time_scheduler

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

def sub_of_raw_products(
        categories_1: dict[str, list],
        categories_2: dict[str, list],
        categories_3: dict[str, list]
    ) -> dict[str, list]:
    """Generate a subset of raw products based on given categories.

    Args:
        categories_1 (dict[str, list]): The first set of categories.
        categories_2 (dict[str, list]): The second set of categories.
        categories_3 (dict[str, list]): The third set of categories.

    Returns:
        dict[str, list]: A dictionary containing the subset of raw products, 
                         where keys represent categories and values are lists 
                         of selected products.

    This function selects a subset of raw products from each category provided 
    based on their probability distribution. It calculates the probability 
    distribution of each category, selects a random item from each category 
    according to this distribution, and aggregates them into a dictionary 
    representing the subset of raw products.
    """
    subst_categories = {}
    already_selected = []

    cp_cts_1 = categories_1.copy()
    cp_cts_2 = categories_2.copy()
    cp_cts_3 = categories_3.copy()

    cts_dict_list = [cp_cts_1, cp_cts_2, cp_cts_3]
    len_cts_dict_list = len(cts_dict_list)

    split_number_list = functions_toolbox.split_number(6, 15)

    for j in range(len_cts_dict_list):

        list_counts, total_count = functions_toolbox.count_strings(
            cts_dict_list[j])
        
        k, q = functions_toolbox.lists_categories_probability(list_counts)
        key_list, quantity_values_list = k.copy(), q.copy()
        
        while (split_number_list[j] > 0):
            probability_list = quantity_values_list.copy()

            for i in range(len(probability_list)):
                probability_list[i] = probability_list[i] / total_count

            split_choice = random.choices(key_list, 
                                          weights=probability_list)[0]

            random_kwd = ""
            while ((random_kwd in already_selected) or (random_kwd == "")):
                random_kwd = random.sample(cts_dict_list[j][split_choice], k=1)
            
            if split_choice in subst_categories:
                subst_categories[split_choice].extend(random_kwd)
            else:
                subst_categories[split_choice] = random_kwd

            key_position = key_list.index(split_choice)
            quantity_values_list[key_position] -= 1

            total_count -= 1
            split_number_list[j] -= 1
    
    logging.debug(f"Total number of category selected: {len(subst_categories)}")
    return subst_categories

def saving_percentage(min_saving_percent: int) -> int:
    """Calculate the minimum saving percentage based on a given threshold.

    Args:
        min_saving_percent (int): The minimum saving percentage threshold.

    Returns:
        int: The calculated minimum saving percentage.

    This function calculates the minimum saving percentage based on the 
    given threshold. It randomly selects a value from a list of two values 
    based on a predefined probability distribution.
    """
    split = [0, min_saving_percent]
    min_saving_percent = random.choices(split, weights=[0.7, 0.3], k=1)[0]
    return min_saving_percent

def extraction_raw_products() -> list[list]:
    """Extracts raw product data from the Amazon PA-API 5.0.

    This function retrieves raw product data by iterating through categories 
    and associated keywords from a predefined list. It uses the 
    Amazon PA-API 5.0 to search for items based on categories and keywords, 
    and gathers the resulting items' data.

    Args:
        None

    Returns:
        list[list]: A list containing raw product data in the form of sublists.

    The function operates as follows:
    - Iterates through categories and associated keywords to search 
        for items on Amazon.
    - Collects item data for each keyword and category, appending it 
        to 'raw_products_list'.
    - Retrieves items using the PA-API 5.0 search_items_by_kw function 
        with specific parameters.
    - Checks for valid responses and extends 'raw_products_list' with item data.
    - Handles cases where the response from the PA-API 5.0 is None, 
        logging an error.
    - If 'raw_products_list' is empty, logs a warning and returns an empty list.
    - If the 'MAX_PAGE' parameter is less than 2, logs a debug message 
        indicating the requirement.

    Note:
    - The function assumes 'parameters.MAX_PAGE' for the maximum number of 
        pages to search.
    - It uses the 'amz_paapi_sdk' to interact with the Amazon PA-API 5.0.
    - Ensure 'secretKeys' and 'parameters' modules are appropriately 
        defined and accessible.
    - Proper handling is implemented for None responses from the 
        PA-API 5.0 and empty result lists.
    """
    raw_products_list = []
    raw_asins_list = []
    MIN_SAVING = api_keys.MIN_SAVING_PERCENT

    functions_toolbox.build_archive()
    # ONLY FOR TESTING smoller dict so the program can loop only the same 
    # products to check. (To use it set parameters.SUBSET_MODE to 0)
    categories = category_keywords.categories
    
    if settings.SUBSET_MODE:
        categories = sub_of_raw_products(category_keywords.categories_1,
                                         category_keywords.categories_2,
                                         category_keywords.categories_3)
    for category in categories:
        for keyword in categories[category]:
            MAX_PAGE = settings.MAX_PAGE

            for item_page in range(1, MAX_PAGE + 1):
                MIN_SAVING_PERCENT = saving_percentage(MIN_SAVING)

                response = amz_paapi_sdk.search_items_by_kw(
                    api_keys.ACCESS_KEY, 
                    api_keys.SECRET_KEY, 
                    api_keys.PARTNER_TAG, 
                    api_keys.HOST, 
                    api_keys.REGION,
                    keyword, 
                    Condition.NEW,
                    settings.ITEM_COUNT,
                    item_page,
                    category,
                    MIN_SAVING_PERCENT)
                
                if response == 429:
                    time_scheduler.amz_wait_time()
                    continue

                elif response is not None:

                    # Be carful with the words returned from the paapi. 
                    # If you make a request through the asin the returned 
                    # response contain items_result but if you use the keyword 
                    # the response contain search_result.
                    if ((response.search_result is not None) and 
                        (response.search_result.items is not None)):
                        items_list = response.search_result.items

                        for item in items_list:
                            if ((item.asin is not None) and 
                                (item.asin not in raw_asins_list)):
                                    
                                    raw_asins_list.append(item.asin)
                                    raw_products_list.append(item)
                    time.sleep(2)
                else:
                    logging.error(f"None Response from the PA-API 5.0 for the "
                                  f"keyword: {keyword} on category: {category}")
                    time.sleep(10)

    if not raw_products_list:
        logging.warning(f"Empty list of products from the PA-API 5.0!")
        return raw_products_list

    available_products_list = offers_checker(raw_products_list)
    return available_products_list

def print_no_discount(products_list_no_offers: list) -> None:
    """Prints a warning message for each batch of products without discounts.

    Args:
        products_list_no_offers (list): A list of products without discounts.

    Returns:
        None
    """
    while len(products_list_no_offers) > 0:
        i = 0
        tmp_list_no_offers = []

        while i < 10:
            try: 
                tmp_offer = products_list_no_offers.pop(0)
                tmp_list_no_offers.append(tmp_offer)
            except: pass
            i += 1

        logging.warning(f"No discount found for he asins: {tmp_list_no_offers}")

def offers_checker(raw_products_list: list[dict]) -> list[dict]:
    """Checks for offers in a list of raw products based on discount thresholds.

    Args:
        raw_products_list (list[dict]): A list of raw products.

    Returns:
        list[dict]: A list of products with offers.
    """
    MIN_DISCOUNT = api_keys.MIN_SAVING_PERCENT
    MIN_DISCOUNT_VALUE = api_keys.MIN_SAVING_VALUE
    products_list_with_offers = []
    products_list_no_offers = []

    for product in raw_products_list:

        try: short = product.offers.listings[0]
        except Exception as e:
            products_list_no_offers.append(product.asin)
            continue

        try:
            discounted_percentage = int(short.price.savings.percentage)

            old_price = short.saving_basis.amount
            current_price = short.price.amount
            numerator = old_price - current_price
            percentage = (numerator / old_price) * 100

            if (((discounted_percentage >= MIN_DISCOUNT) or 
                 (percentage >= MIN_DISCOUNT)) and 
                 ((numerator > MIN_DISCOUNT_VALUE) or 
                  (MIN_DISCOUNT_VALUE == -1))):
                
                products_list_with_offers.append(product)
                continue
            
        except:
            products_list_no_offers.append(product.asin)

    print_no_discount(products_list_no_offers)
    return products_list_with_offers

def offers_extractor(products: list[Product], max_offers: int) -> list[Product]:
    """
    """
    ##
    ## As is mentioned in the readme file, the code in this function can be really
    ## different based on which products you prefer to send.
    ##
    ## You must personalize this function based on your needs.
    ##
    ## If you don't modify this function it automatically selects n random products
    ## where n is the max number of offers you want to send that take in input.
    ##
    ##
    ##

    logging.info(f"There are {len(products)} offers in the list but the "
                 f"max is {max_offers}. Start Swap offers.")
    
    random.shuffle(products)
    returned_list = products[:max_offers]
    return returned_list