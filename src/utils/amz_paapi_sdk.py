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
import logging
from typing import Union

from paapi5_python_sdk.rest import ApiException
from paapi5_python_sdk.condition import Condition
from paapi5_python_sdk.partner_type import PartnerType
from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.get_items_request import GetItemsRequest
from paapi5_python_sdk.get_items_resource import GetItemsResource
from paapi5_python_sdk.search_items_request import SearchItemsRequest
from paapi5_python_sdk.search_items_resource import SearchItemsResource

# Imported modules
from utils.log_manager import setup_logger

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

def search_items_by_kw(
        access_key: str, 
        secret_key: str, 
        partner_tag: str, 
        host: str, 
        region: str,
        keywords, 
        condition: Condition,
        item_count: int,
        item_page: int = 1,
        search_index: str = "All",
        min_saving_percent: int = 0
    ) -> Union[SearchItemsResource, int, None]:
    """Searches items using the Amazon PA-API 5.0 based on specified 
        parameters and keywords.

    Args:
        access_key (str): Access key for Amazon PA-API.
        secret_key (str): Secret key for Amazon PA-API.
        partner_tag (str): Partner tag for Amazon PA-API.
        host (str): Host for the Amazon PA-API endpoint.
        region (str): Region for the Amazon PA-API endpoint.
        keywords (str): Keywords for the item search.
        condition (Condition): Condition of the items to be searched.
        item_count (int): Number of items to be fetched in the response.
        item_page (int): Page number for paginated results.
        search_index (str, optional): The category in which the search request 
            is made. Defaults to "All".

    Returns:
        SearchItemsResource: The response object containing search 
            results if successful.

    The function initiates a search request for items using the 
        Amazon PA-API 5.0 based on provided parameters:
    - Forms a request using specified credentials, keywords, search index, 
        and resources required.
    - Sends the request to the Amazon PA-API and retrieves the search results.
    - Collects ASINs (Amazon Standard Identification Numbers) from 
        the search result items.
    - Logs any errors encountered during the search process.

    Note:
        - The function utilizes the Amazon PA-API 5.0 'DefaultApi' for 
            sending requests.
        - It handles different types of errors such as 'ValueError', 
            'ApiException', 'TypeError', and general 'Exception'.
        - Properly logs details related to API errors, request ID, status codes, 
            and messages.
        - Requires valid access keys, partner tags, and appropriate permissions 
            for the Amazon PA-API.
    
        #! WARNING: min_saving_percent is deactivated since if active it block 
        #!  also product with an hightest discount percentage. For example if 
        #!  activated it doesn't show iPhone 15 for the keyword "iPhone" but 
        #!  show older iphone models. Viceversa if deactivated it shows 
        #! iPhone 15 but doesn't show some of ald model. Need more 
        #! investigation to fix this problem.
    """
    # Specify the category in which search request is to be made
    # For more details, refer: https://webservices.amazon.com/paapi5/documentation/use-cases/organization-of-items-on-amazon/search-index.html

    # API declaration
    default_api = DefaultApi(access_key=access_key, 
                             secret_key=secret_key, 
                             host=host, 
                             region=region)

    # Choose resources you want from SearchItemsResource enum
    # For more details, refer: https://webservices.amazon.com/paapi5/documentation/search-items.html#resources-parameter
    search_items_resource = [
        SearchItemsResource.ITEMINFO_TITLE,
        SearchItemsResource.OFFERS_LISTINGS_PRICE,
        SearchItemsResource.IMAGES_PRIMARY_LARGE,
        SearchItemsResource.OFFERS_LISTINGS_SAVINGBASIS,
        SearchItemsResource.ITEMINFO_FEATURES,
        SearchItemsResource.OFFERS_LISTINGS_PROMOTIONS,
        SearchItemsResource.OFFERS_LISTINGS_CONDITION,
        SearchItemsResource.OFFERS_LISTINGS_ISBUYBOXWINNER,
        SearchItemsResource.OFFERS_SUMMARIES_LOWESTPRICE,
        SearchItemsResource.OFFERS_SUMMARIES_HIGHESTPRICE,
        SearchItemsResource.BROWSENODEINFO_BROWSENODES,
        SearchItemsResource.BROWSENODEINFO_BROWSENODES_ANCESTOR,
        SearchItemsResource.BROWSENODEINFO_BROWSENODES_SALESRANK,
        SearchItemsResource.BROWSENODEINFO_WEBSITESALESRANK,
        SearchItemsResource.ITEMINFO_BYLINEINFO,
        SearchItemsResource.ITEMINFO_CLASSIFICATIONS,
        SearchItemsResource.ITEMINFO_CONTENTINFO,
        SearchItemsResource.ITEMINFO_CONTENTRATING,
        SearchItemsResource.ITEMINFO_EXTERNALIDS,
        SearchItemsResource.ITEMINFO_FEATURES,
        SearchItemsResource.ITEMINFO_MANUFACTUREINFO,
        SearchItemsResource.ITEMINFO_PRODUCTINFO,
        SearchItemsResource.ITEMINFO_TECHNICALINFO,
        SearchItemsResource.ITEMINFO_TRADEININFO,
        SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
        SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_MESSAGE,
        SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_TYPE,
        SearchItemsResource.OFFERS_LISTINGS_CONDITION,
        SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_MINORDERQUANTITY,
        SearchItemsResource.OFFERS_LISTINGS_CONDITION_SUBCONDITION,
        SearchItemsResource.OFFERS_LISTINGS_DELIVERYINFO_ISAMAZONFULFILLED,
        SearchItemsResource.OFFERS_LISTINGS_DELIVERYINFO_ISFREESHIPPINGELIGIBLE,
        SearchItemsResource.OFFERS_LISTINGS_DELIVERYINFO_ISPRIMEELIGIBLE,
        SearchItemsResource.OFFERS_LISTINGS_DELIVERYINFO_SHIPPINGCHARGES,
        SearchItemsResource.OFFERS_LISTINGS_ISBUYBOXWINNER,
        SearchItemsResource.OFFERS_LISTINGS_LOYALTYPOINTS_POINTS,
        SearchItemsResource.OFFERS_LISTINGS_MERCHANTINFO,
        SearchItemsResource.OFFERS_LISTINGS_PROGRAMELIGIBILITY_ISPRIMEEXCLUSIVE,
        SearchItemsResource.OFFERS_LISTINGS_PROGRAMELIGIBILITY_ISPRIMEPANTRY,
        SearchItemsResource.OFFERS_SUMMARIES_OFFERCOUNT,
        SearchItemsResource.PARENTASIN,
        SearchItemsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
        SearchItemsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MESSAGE,
        SearchItemsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MINORDERQUANTITY,
        SearchItemsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_TYPE,
        SearchItemsResource.RENTALOFFERS_LISTINGS_BASEPRICE,
        SearchItemsResource.RENTALOFFERS_LISTINGS_CONDITION,
        SearchItemsResource.RENTALOFFERS_LISTINGS_CONDITION_SUBCONDITION,
        SearchItemsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISAMAZONFULFILLED,
        SearchItemsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISFREESHIPPINGELIGIBLE,
        SearchItemsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISPRIMEELIGIBLE,
        SearchItemsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_SHIPPINGCHARGES,
        SearchItemsResource.RENTALOFFERS_LISTINGS_MERCHANTINFO,
        SearchItemsResource.SEARCHREFINEMENTS,
    ]

    # Forming request
    try:
        search_items_request = SearchItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            keywords=keywords,
            condition=condition,
            search_index=search_index,
            item_count=item_count,
            resources=search_items_resource,
            item_page=item_page,
            #! WARNING: see the comment in the description of the function
            # min_saving_percent=min_saving_percent,
        )

        #! TO TEMPORARY FIX THE PROBLEM OF min_saving_percent
        min_percent_active = "Deactivated"
        if min_saving_percent > 0:
            search_items_request.min_saving_percent = min_saving_percent
            min_percent_active = "Activated"

    except ValueError as exception:
        logging.error(f"Error in forming SearchItemsRequest: {exception}")
        return

    try:
        # Sending request
        response = default_api.search_items(search_items_request)
        # logging.debug("API called Successfully")

        if response.search_result is None:
            return None

        asin_list = []
        for item in response.search_result.items:
            asin_list.append(item.asin)

        logging.info(f"API called Successfully. Category: {search_index} - "
                     f"Keyword: {keywords} - Page: {item_page} - Min Saving "
                     f"Percent: {min_percent_active}")
        
        logging.debug(f"Products Found ({len(asin_list)}/{item_count}):"
                      f" {asin_list}")

        if response.errors is not None:
            logging.error("\nPrinting Errors:"
                  "\nPrinting First Error Object from list of Errors")
            logging.error(f"Error code: {response.errors[0].code}")
            logging.error(f"Error message: {response.errors[0].message}")

        return response

    except ApiException as exception:
        # logging.error("Error calling PA-API 5.0!")
        # logging.error(f"Status code: {exception.status}")
        # logging.error(f"Errors : {exception.body}")
        # logging.error(f'Request ID: {exception.headers["x-amzn-RequestId"]}')
        logging.error(f"Error calling PA-API 5.0! - Status code: "
                      f"{exception.status} - Request ID: "
                      f"{exception.headers['x-amzn-RequestId']}")
        logging.error(f"Errors : {exception.body}")
        return exception.status

    except TypeError as exception:
        logging.error(f"TypeError : {exception}")

    except ValueError as exception:
        logging.error(f"ValueError : {exception}")

    except Exception as exception:
        logging.error(f"Exception : {exception}")