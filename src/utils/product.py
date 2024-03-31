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
from datetime import datetime, timedelta
from typing import Union

# External libraries
from paapi5_python_sdk.item import Item

# Importing internal modules
from utils.log_manager import setup_logger

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

class Product:
    """Represents a product with various attributes and methods 
        for extracting product information.

    Attributes:
        asin (str): Amazon Standard Identification Number.
        parent_asin (str, optional): Parent ASIN if applicable.
        brand (str, optional): Brand of the product.
        main (str, optional): Main category of the product.
        first_sub (str, optional): First sub-category of the product.
        second_sub (str, optional): Second sub-category of the product.
        third_sub (str, optional): Third sub-category of the product.
        fourth_sub (str, optional): Fourth sub-category of the product.
        coupon (bool, optional): Indicates if the product has a coupon.
        promo_code (str, optional): Promo code associated with the product.
        title (str, optional): Title of the product.
        image_link (str, optional): Link to the product image.
        bullet_points (list of str, optional): Bullet points describing the product.
        marketplace (str, optional): Marketplace where the product is listed.
        price (float, optional): Current price of the product.
        currency (str, optional): Currency of the price.
        old_price (float, optional): Previous price of the product.
        old_currency (str, optional): Currency of the previous price.
        lowest_historical_price (bool, optional): Indicates if the current 
            price is the lowest historical price.
        discount (float, optional): Discount percentage.
        priority (int, optional): Priority of the product.
        rank (int, optional): Rank of the product.
        is_lightning_deals (bool, optional): Indicates if the product 
            is available in lightning deals.
        release_date (datetime, optional): Release date of the product.
        date_added (datetime, optional): Date when the product was added.

    Methods:
        __repr__(self): Return a string representation of the product.
        __str__(self): Return a string representation of the product.
        __eq__(self, other): Check if two products are equal.
        __lt__(self, other): Compare two products.
        __gt__(self, other): Compare two products.
        lists_to_products(cls, items_list: list) -> list['Product']: 
            DEPRECATED: Use the method 'from_items_list' instead.
        list_to_products(cls, items_list: list[Item]) -> list['Product']: 
            Convert a list of items to a list of products.
        from_item(cls, item: Item) -> Union['Product', str, None]: 
            Create a product from an item.
        Various static and class methods for extracting specific 
            attributes from an item.
    """
    def __init__(
            self, 
            asin, 
            parent_asin=None, 
            brand=None, 
            main=None, 
            first_sub=None, 
            second_sub=None, 
            third_sub=None, 
            fourth_sub=None, 
            coupon=False, 
            promo_code=None, 
            title=None, 
            image_link=None, 
            bullet_points=None, 
            marketplace=None, 
            price=0, 
            currency=None, 
            old_price=0, 
            old_currency=None, 
            lowest_historical_price=False, 
            discount=None, 
            priority=0, 
            rank=0, 
            is_lightning_deals=False,
            release_date=None,
            date_added=None
        ) -> None:

        """Initializes a Product object with the given attributes.

        Args:
            asin (str): The ASIN (Amazon Standard Identification Number) 
                of the product.
            parent_asin (str, optional): The parent ASIN of the product, 
                if applicable.
            brand (str, optional): The brand of the product.
            main (str, optional): The main category of the product.
            first_sub (str, optional): The first sub-category of the product.
            second_sub (str, optional): The second sub-category of the product.
            third_sub (str, optional): The third sub-category of the product.
            fourth_sub (str, optional): The fourth sub-category of the product.
            coupon (bool, optional): Indicates if the product 
                has a coupon available.
            promo_code (str, optional): The promo code associated 
                with the product, if applicable.
            title (str, optional): The title of the product.
            image_link (str, optional): The link to the image of the product.
            bullet_points (List[str], optional): The bullet 
                points describing the product.
            marketplace (str, optional): The marketplace where 
                the product is listed.
            price (float, optional): The price of the product.
            currency (str, optional): The currency in which the price is listed.
            old_price (float, optional): The previous price of the product.
            old_currency (str, optional): The currency in which 
                the previous price is listed.
            lowest_historical_price (bool, optional): Indicates if 
                the current price is the lowest in history.
            discount (float, optional): The discount percentage 
                applied to the product.
            priority (int, optional): The priority of the product.
            rank (int, optional): The rank of the product.
            is_lightning_deals (bool, optional): Indicates if the product 
                is part of Lightning Deals.
            release_date (str, optional): The release date of the product.
            date_added (str, optional): The date when the product was added.

        Returns:
            None
        """
        self.asin = asin
        self.parent_asin = parent_asin
        self.brand = brand
        self.main = main
        self.first_sub = first_sub
        self.second_sub = second_sub
        self.third_sub = third_sub
        self.fourth_sub = fourth_sub
        self.coupon = coupon
        self.promo_code = promo_code
        self.title = title
        self.image_link = image_link
        self.bullet_points = bullet_points
        self.marketplace = marketplace
        self.price = price
        self.currency = currency
        self.old_price = old_price
        self.old_currency = old_currency
        self.lowest_historical_price = lowest_historical_price
        self.discount = discount
        self.priority = priority
        self.rank = rank
        self.is_lightning_deals = is_lightning_deals
        self.release_date = release_date
        self.date_added = date_added
    
    def __repr__(self) -> str:
        """Returns a string representation of the Product object.

        Returns:
            str: A string representation of the Product object 
                including its attributes.
        """
        return (
            f"Product(asin={self.asin}, "
            f"parent_asin={self.parent_asin}, "
            f"brand={self.brand}, "
            f"main={self.main}, "
            f"first_sub={self.first_sub}, "
            f"second_sub={self.second_sub}, "
            f"third_sub={self.third_sub}, "
            f"fourth_sub={self.fourth_sub}, "
            f"coupon={self.coupon}, "
            f"promo_code={self.promo_code}, "
            f"title={self.title}, "
            f"image_link={self.image_link}, "
            f"bullet_points={self.bullet_points}, "
            f"marketplace={self.marketplace}, "
            f"price={self.price}, "
            f"currency={self.currency}, "
            f"old_price={self.old_price}, "
            f"old_currency={self.old_currency}, "
            f"lowest_historical_price={self.lowest_historical_price}, "
            f"discount={self.discount}, "
            f"priority={self.priority}, "
            f"rank={self.rank}, "
            f"is_lightning_deals={self.is_lightning_deals}, "
            f"release_date={self.release_date}, "
            f"date_added={self.date_added})"
        )

    def __str__(self) -> str:
        """Returns a human-readable string representation of the Product object.

        The returned string includes the values of all attributes of the 
            Product object, formatted for easy readability.

        Returns:
            str: A human-readable string representation of the Product object.
        """
        return (
            f"ASIN: {self.asin}, "
            f"Parent ASIN: {self.parent_asin}, "
            f"Brand: {self.brand}, "
            f"Main Category: {self.main}, "
            f"First Sub-Category: {self.first_sub}, "
            f"Second Sub-Category: {self.second_sub}, "
            f"Third Sub-Category: {self.third_sub}, "
            f"Fourth Sub-Category: {self.fourth_sub}, "
            f"Coupon: {self.coupon}, "
            f"Promo Code: {self.promo_code}, "
            f"Title: {self.title}, "
            f"Image Link: {self.image_link}, "
            f"Bullet Points: {self.bullet_points}, "
            f"Marketplace: {self.marketplace}, "
            f"Current Price: {self.price}, "
            f"Current Currency: {self.currency}, "
            f"Old Price: {self.old_price}, "
            f"Old Currency: {self.old_currency}, "
            f"Lowest Historical Price: {self.lowest_historical_price}, "
            f"Discounted Percentage: {self.discount}, "
            f"Priority: {self.priority}, "
            f"Rank: {self.rank}, "
            f"Is Lightning Deals: {self.is_lightning_deals}, "
            f"Release Date: {self.release_date}, "
            f"Date Added: {self.date_added}"
        )

    def __eq__(self, other: 'Product') -> bool:
        """Checks if two products are equal based on name and price.

        Args:
            other (Product): Another product to compare.

        Returns:
            bool: True if both products have the same name and price, 
                False otherwise.
        """
        return self.asin == other.asin

    def __lt__(self, other: 'Product') -> bool:
        """Checks if the product's price is less than another product's price.

        Args:
            other (Product): Another product to compare.

        Returns:
            bool: True if the product's price is less than the other 
                product's price, False otherwise.
        """
        return self.price < other.price

    def __gt__(self, other: 'Product') -> bool:
        """Checks if the product's price is greater than another 
            product's price.

        Args:
            other (Product): Another product to compare.

        Returns:
            bool: True if the product's price is greater than the other 
                product's price, False otherwise.
        """
        return self.price > other.price
    
    def __tuple__(self):
        """Returns a tuple representation of the object's attributes.

        Returns:
            tuple: A tuple containing the values of the object's attributes.

        The method constructs and returns a tuple representation of the object 
        containing the values of its attributes in the following order:
        - ASIN, Parent ASIN, Brand, Main Category, Sub-Categories, Coupon, 
          Promo Code, Title, Image Link, Description List, Marketplace, Prices, 
          Historical Prices, Discount Percentage, Priority, Rank, 
          Lightning Deals and Date added.

        Note:
        - The method is used to generate a tuple containing attribute 
            values for the object.
        - It ensures the order of attributes matches the order specified in 
            the return tuple.
        """
        return (
            self.asin, self.parent_asin, self.brand, self.main, self.first_sub, 
            self.second_sub, self.third_sub, self.fourth_sub, self.coupon, 
            self.promo_code, self.title, self.image_link,
            str(self.bullet_points), self.marketplace, self.price, 
            self.currency, self.old_price, self.old_currency,
            self.lowest_historical_price, self.discount, self.priority, 
            self.rank, self.is_lightning_deals, self.release_date, 
            self.date_added)

    def categories_comparator(self, other: 'Product') -> bool:
        """Checks if the product's category is equal to another 
            product's category.

        Args:
            other (Product): Another product to compare.

        Returns:
            bool: True if the product's category is equal to the other 
                product's category, False otherwise.
        """
        return (
            self.main == other.main and 
            self.first_sub == other.first_sub and 
            self.second_sub == other.second_sub and 
            self.third_sub == other.third_sub and 
            self.fourth_sub == other.fourth_sub
        )
    
    def brand_comparator(self, other: 'Product') -> bool:
        """Checks if the product's brand is equal to another product's brand.

        Args:
            other (Product): Another product to compare.

        Returns:
            bool: True if the product's brand is equal to the other 
                product's brand, False otherwise.
        """
        brand_1 = self.brand.lower()
        brand_2 = other.brand.lower()
        
        len_brand_1 = len(brand_1)
        len_brand_2 = len(brand_2)

        if len_brand_1 > 4 and len_brand_2 > 4:
            return (brand_1 == brand_2 or 
                    brand_1 in brand_2 or 
                    brand_2 in brand_1)
        else:
            return (brand_1 == brand_2)
    
    def low_category(self) -> Union[str, None]:
        """Returns the lowest-level category available among
            different levels of subcategories.

        Returns:
            Union[str, None]: The lowest-level category if available, 
                otherwise None.
        """
        if self.fourth_sub is not None:
            return self.fourth_sub
        
        elif self.third_sub is not None:
            return self.third_sub
        
        elif self.second_sub is not None:
            return self.second_sub
        
        elif self.first_sub is not None:
            return self.first_sub
        
        elif self.main is not None:
            return self.main
        
        return None

    @classmethod
    def list_to_products(cls, items_list: list[Item]) -> list['Product']:
        """Convert a list of items into a list of Product instances.

        Args:
            items_list (list[Item]): A list of items to convert into 
                Product instances

        Returns:
            list['Product']: Containing instances of Product 
                derived from the items_list.

        Example:
            product = Product.list_to_products(items_list)
        """
        list_of_products = []
        list_asin_not_ok = []
        if (items_list == []) or (items_list is None):
            return []
        
        for item in items_list:
            product = Product.from_item(item)

            if isinstance(product, str):
                list_asin_not_ok.append(item)
                continue
            
            elif product is not None:
                list_of_products.append(product)
        
        if len(list_asin_not_ok) > 0:
            logging.warning(f"Product not created for: {list_asin_not_ok}.")

        return list_of_products
    
    @classmethod
    def from_item(cls, item: Item) -> Union['Product', str, None]:
        """Create a Product instance from an item string.

        Args:
            item (Item): A string representing an item.

        Returns:
            Union['Product', str, None]: A Product instance if successfully 
                created, otherwise a string representing the ASIN if the 
                product couldn't be created, or None if ASIN couldn't be found.

        Example:
            Consider an item string containing information about a product:

            product = Product.from_item(item)

            If the ASIN couldn't be found in the item string, it returns None. 
            If the creation of the Product instance fails for any reason, 
            it returns the ASIN string as a representation of the failure.
        
        Notes:
            Below are the paths reached by the code. Not everyone has relevant 
                values at the moment but they could be used for future versions. 
                For this reason the paths to the value have already been created 
                that contain. 
                
                Just define the new variable and capture the value you want.
            
                The first element is an example of the job they contain while 
                the second is the path to find it.
                
                ATTENTION: Where None is present it means that for the moment 
                there is no information about it e so it is not known what value 
                one might find. or if maybe there are additional json entries.
            
                The symbol [] indicates that we are in a list. 
                In the first case for example ( items_result.items[] ) it 
                indicates us that we are in the list of various products 
                that we have requested and received from the response to PAAPI.

            B091G3WT74
            items_result.items[].asin

            Elettronica
            items_result.items[].browse_node_info.browse_nodes[0].ancestor.ancestor.ancestor.ancestor.context_free_name

            Elettronica
            items_result.items[].browse_node_info.browse_nodes[0].ancestor.ancestor.ancestor.context_free_name

            Home Audio e Hi-Fi
            items_result.items[].browse_node_info.browse_nodes[0].ancestor.ancestor.context_free_name

            Dispositivi per lo Streaming
            items_result.items[].browse_node_info.browse_nodes[0].ancestor.context_free_name

            None
            items_result.items[].browse_node_info.browse_nodes[0].children

            Server multimediali
            items_result.items[].browse_node_info.browse_nodes[0].context_free_name

            None
            items_result.items[].browse_node_info.browse_nodes[0].sales_rank

            Elettronica
            items_result.items[].browse_node_info.browse_nodes[1].ancestor.ancestor.ancestor.ancestor.context_free_name

            Elettronica
            items_result.items[].browse_node_info.browse_nodes[1].ancestor.ancestor.ancestor.context_free_name

            Home Audio e Hi-Fi
            items_result.items[].browse_node_info.browse_nodes[1].ancestor.ancestor.context_free_name

            Dispositivi per lo Streaming
            items_result.items[].browse_node_info.browse_nodes[1].ancestor.context_free_name

            None
            items_result.items[].browse_node_info.browse_nodes[1].children

            Client Streaming
            items_result.items[].browse_node_info.browse_nodes[1].context_free_name

            1
            items_result.items[].browse_node_info.browse_nodes[1].sales_rank

            Informatica
            items_result.items[].browse_node_info.browse_nodes[2].ancestor.ancestor.context_free_name

            Informatica
            items_result.items[].browse_node_info.browse_nodes[2].ancestor.context_free_name

            None
            items_result.items[].browse_node_info.browse_nodes[2].children

            Accessori per computer
            items_result.items[].browse_node_info.browse_nodes[2].context_free_name

            Dispositivi Amazon & Accessori
            items_result.items[].browse_node_info.browse_nodes[3].ancestor.ancestor.ancestor.ancestor.context_free_name

            Dispositivi Amazon & Accessori
            items_result.items[].browse_node_info.browse_nodes[3].ancestor.ancestor.ancestor.context_free_name

            Dispositivi Amazon
            items_result.items[].browse_node_info.browse_nodes[3].ancestor.ancestor.context_free_name

            Fire
            items_result.items[].browse_node_info.browse_nodes[3].ancestor.context_free_name

            None
            items_result.items[].browse_node_info.browse_nodes[3].children

            Dispositivi per lo Streaming
            items_result.items[].browse_node_info.browse_nodes[3].context_free_name

            1
            items_result.items[].browse_node_info.browse_nodes[3].sales_rank

            Dispositivi Amazon & Accessori
            items_result.items[].browse_node_info.browse_nodes[4].ancestor.ancestor.ancestor.ancestor.ancestor.context_free_name

            Self Service
            items_result.items[].browse_node_info.browse_nodes[4].ancestor.ancestor.ancestor.ancestor.context_free_name

            Special Features Stores
            items_result.items[].browse_node_info.browse_nodes[4].ancestor.ancestor.ancestor.context_free_name

            partition_025
            items_result.items[].browse_node_info.browse_nodes[4].ancestor.ancestor.context_free_name

            partition_000
            items_result.items[].browse_node_info.browse_nodes[4].ancestor.context_free_name

            None
            items_result.items[].browse_node_info.browse_nodes[4].children

            Fire TV Stick Lite, telecomando vocale Alexa | Lite (2ª generazione)
            items_result.items[].browse_node_info.browse_nodes[4].context_free_name

            None
            items_result.items[].browse_node_info.browse_nodes[4].sales_rank

            Dispositivi Amazon & Accessori
            items_result.items[].browse_node_info.website_sales_rank.context_free_name

            1
            items_result.items[].browse_node_info.website_sales_rank.sales_rank

            https://www.amazon.it/dp/B091G3WT74?tag=andrepietr-21&linkCode=ogi&th=1&psc=1
            items_result.items[].detail_page_url

            500
            items_result.items[].images.primary.large.height

            https://m.media-amazon.com/images/I/31H+yPMQGeL._SL500_.jpg
            items_result.items[].images.primary.large.url

            500
            items_result.items[].images.primary.large.width


            500
            items_result.items[].images.primary.medium.height

            https://m.media-amazon.com/images/I/31H+yPMQGeL._SL500_.jpg
            items_result.items[].images.primary.medium.url

            500
            items_result.items[].images.primary.medium.width

            None
            items_result.items[].images.variants

            Amazon
            items_result.items[].item_info.by_line_info.brand.display_value

            it_IT
            items_result.items[].item_info.by_line_info.brand.locale

            Amazon
            items_result.items[].item_info.by_line_info.manufacturer.display_value

            it_IT
            items_result.items[].item_info.by_line_info.manufacturer.locale

            Elettronica
            items_result.items[].item_info.classifications.binding.display_value

            it_IT
            items_result.items[].item_info.classifications.binding.locale

            it_IT
            items_result.items[].item_info.content_info.languages.locale

            La versione più conveniente di Fire ..... riprodurre musica e altro ancora.
            items_result.items[].item_info.features.display_values[]

            BLACK
            items_result.items[].item_info.product_info.color.display_value

            False
            items_result.items[].item_info.product_info.is_adult_product.display_value

            None
            items_result.items[].item_info.product_info.unit_count

            None
            items_result.items[].item_info.technical_info

            Fire TV Stick Lite con telecomando vocale Alexa | Lite 
            (senza comandi per la TV), Streaming in HD
            items_result.items[].item_info.product_info.title.display_value

            2
            items_result.items[].offers.listings[0].availability.max_order_quantity

            Disponibilità immediata.
            items_result.items[].offers.listings[0].availability.message

            1
            items_result.items[].offers.listings[0].availability.min_order_quantity

            Now
            items_result.items[].offers.listings[0].availability.type

            None
            items_result.items[].offers.listings[0].condition.display_value

            None
            items_result.items[].offers.listings[0].acondition.sub_condition.display_value

            New
            items_result.items[].offers.listings[0].condition.sub_condition.value

            New
            items_result.items[].offers.listings[0].condition.value

            True
            items_result.items[].offers.listings[0].delivery_info.is_amazon_fulfilled

            True
            items_result.items[].offers.listings[0].delivery_info.iis_free_shipping_eligible

            True
            items_result.items[].offers.listings[0].delivery_info.is_prime_eligible

            None
            items_result.items[].offers.listings[0].delivery_info.shipping_charges

            True
            items_result.items[].offers.listings[0].is_buy_box_winner

            Amazon.it
            items_result.items[].offers.listings[0].merchant_info.name

            24.99
            items_result.items[].offers.listings[0].price.amount

            EUR
            items_result.items[].offers.listings[0].price.currency

            EUR
            items_result.items[].offers.listings[0].price.price_per_unit

            10.0
            items_result.items[].offers.listings[0].price.savings.amount

            EUR
            items_result.items[].offers.listings[0].price.savings.currency

            29
            items_result.items[].offers.listings[0].price.savings.percentage

            None
            items_result.items[].offers.listings[0].price.savings.price_per_unit

            None
            items_result.items[].offers.listings[0].program_eligibility.is_prime_exclusive

            None
            items_result.items[].offers.listings[0].program_eligibility.is_prime_pantry

            None
            items_result.items[].offers.listings[0].promotions

            34.99
            items_result.items[].offers.listings[0].saving_basis.amount

            EUR
            items_result.items[].offers.listings[0].saving_basis.currency

            None
            items_result.items[].offers.listings[0].saving_basis.price_per_unit

            None
            items_result.items[].offers.summaries[0].condition.display_value

            New
            items_result.items[].offers.summaries[0].condition.value

            24.99
            items_result.items[].offers.summaries[0].highest_price.amount

            EUR
            items_result.items[].offers.summaries[0].highest_price.currency

            None
            items_result.items[].offers.summaries[0].highest_price.price_per_unit

            24.99
            items_result.items[].offers.summaries[0].lowest_price.amount

            EUR
            items_result.items[].offers.summaries[0].lowest_price.currency

            None
            items_result.items[].offers.summaries[0].lowest_price.price_per_unit

            1
            items_result.items[].offers.summaries[0].offer_count

            None
            items_result.items[].parent_asin

            None
            items_result.items[].variation_attributes
            
            2021-01-01
            items_result.items[].product_info.release_date.display_value
        """
        asin = Product.asin_extractor(item)

        if asin is None:
            logging.critical(f"Cant find the asin of the product: {item}.")
            return None
        
        categories = Product.category_extractor(item, asin)

        if categories == []:
            return asin
        
        main, first_sub, second_sub, third_sub, fourth_sub = categories

        # children = Product.children_extractor(item, asin)
        rank = Product.rank_extractor(item, asin)

        # sales_rank_cf_name = Product.sales_rank_cf_name_extractor(item, asin)
        # page_link = Product.page_link_extractor(item, asin)

        # image_sizes = Product.image_size_extractor(item, asin)
        image_link = Product.image_link_extractor(item, asin)

        if image_link is None:
            return asin
        
        # image_variants = Product.image_variants_extractor(item, asin)
        brand = Product.brand_extractor(item, asin)
        
        # locale = Product.locale_extraction(item, asin)
        # classifications = Product.classifications_extractor(item, asin)

        marketplace = Product.marketplace_extractor(item, asin)
        bullet_points = Product.bullet_points_extractor(item, asin)

        # color = Product.product_color_extractor(item, asin)
        # adult_product = Product.adult_product_extractor(item, asin)

        # unit_count = Product.unit_count_extractor(item, asin)
        # technical_info = Product.technical_info_extractor(item, asin)

        title = Product.title_extractor(item, asin)

        if title is None:
            return asin

        # max_quantity = Product.max_quantity_extractor(item, asin)
        # available = Product.available_extractor(item, asin)
        # min_quantity = Product.min_order_quantity_extractor(item, asin)
        # when_available = Product.when_available_extractor(item, asin)

        # condition = Product.condition_extractor(item, asin)
        # condition_value = Product.condition_value_extractor(item, asin)
        # price_per_unit = Product.price_per_unit_extractor(item, asin)

        # is_amazon_fulfilled = Product.is_amazon_fulfilled(item, asin)
        # is_free_shipping_eligible = Product.is_free_shipping_eligible(item, asin)
        # is_prime_eligible = Product.is_prime_eligible(item, asin)
        # shipping_charges = Product.shipping_charges_extractor(item, asin)

        # is_buy_box_winner = Product.is_buy_box_winner(item, asin)

        price = Product.price_extractor(item, asin)
        currency = Product.currency_extractor(item, asin)
        
        # price_per_unit = Product.price_per_unit_extractor(item, asin)
        # savings_price = Product.savings_price_extractor(item, asin)
        # savings_currency = Product.savings_currency_extractor(item, asin)
        discount = Product.discounted_percentage_extractor(item, asin)
        # savings_price_per_unit = Product.savings_price_per_unit_extractor(item, asin)

        # prime_exclusive = Product.is_prime_exclusive(item, asin)
        # prime_pantry = Product.is_prime_pantry(item, asin)
        # promotions = Product.promotions_extractor(item, asin) 

        old_price = Product.old_price_extractor(item, asin)
        old_currency = Product.old_currency_extractor(item, asin)

        # merchant = Product.merchant_brand_extractor(item, asin)

        # hightest_price = Product.hightest_price_extractor(item, asin)
        # hightest_currency = Product.hightest_currency_extractor(item, asin)
        # hightest_price_per_unit = Product.hightest_price_per_unit_extractor(item, asin)

        # lowest_price = Product.lowest_price_extractor(item, asin)
        # lowest_currency = Product.lowest_currency_extractor(item, asin)
        # lowest_price_per_unit = Product.lowest_price_per_unit_extractor(item, asin)

        # offer_count = Product.offer_count_extractor(item, asin)

        parent_asin = Product.parent_asin_extractor(item, asin)
        
        # variant_attribute = Product.variation_attributes_extractor(item, asin)

        release_date = Product.release_date_extractor(item, asin)

        try:
            product = cls(asin, parent_asin, brand, main, first_sub, second_sub, 
                          third_sub, fourth_sub, False, None, title, image_link, 
                          bullet_points, marketplace, price, currency, 
                          old_price, old_currency, False, discount, 0, rank, 
                          False, release_date, None)
        except Exception as e:
            logging.error(f"An error occurred while creating the class "
                          f"product for the asin {asin}: {e}.")
            return asin

        return product
            
    @staticmethod
    def asin_extractor(item: Item) -> Union[str, None]:
        """Extract ASIN from the item.

        Args:
            item (Item): The item from which ASIN needs to be extracted.

        Returns:
            Union[str, None]: ASIN if found, otherwise None.

        Example:
            asin = Product.asin_extractor(item)

            B091G3WT74
            items_result.items[].asin
        """
        asin = None
        try:
            if item.asin is not None:
                asin = item.asin

        except Exception as e:
            logging.critical(f"An error during the extraction of "
                             f"the asin for the item: {item} - {e}.")
        return asin

    @staticmethod
    def category_extractor(item: Item, asin: str) -> list[str]:
        """Extract categories from the item's browse node information.

        Args:
            item (Item): The item from which categories need to be extracted.
            asin (str): ASIN of the product.

        Returns:
            list[str]: A list containing the main category and its subcategories.

        Example:
            categories = Product.category_extractor(item, asin)

            Elettronica
            items_result.items[].browse_node_info.browse_nodes[0].ancestor.ancestor.ancestor.ancestor.context_free_name

            Elettronica
            items_result.items[].browse_node_info.browse_nodes[0].ancestor.ancestor.ancestor.context_free_name

            Home Audio e Hi-Fi
            items_result.items[].browse_node_info.browse_nodes[0].ancestor.ancestor.context_free_name

            Dispositivi per lo Streaming
            items_result.items[].browse_node_info.browse_nodes[0].ancestor.context_free_name
        """
        category_list = [None, None, None, None, None]

        if ((item.browse_node_info is not None) and 
            (item.browse_node_info.browse_nodes is not None)):
            short = item.browse_node_info.browse_nodes[0]

            try:
                if short.ancestor is not None:
                    category_list[3] = Product.third_sub_category(short)

                    if short.ancestor.ancestor is not None:
                        category_list[2] = Product.second_sub_category(short)

                        if short.ancestor.ancestor.ancestor is not None:
                            category_list[1] = Product.first_sub_category(short)

                            short_ancestor_3 = short.ancestor.ancestor.ancestor
                            if short_ancestor_3.ancestor is not None:
                                category_list[0] = Product.main_category(short)

                category_list[4] = Product.fourth_sub_category(short)

            except Exception as e:
                logging.error(f"An error occurred with the "
                              f"category of the ASIN {asin}: {e}.")
                return []  

            while category_list[0] == None:
                first_idx = category_list.pop(0)
                category_list.append(first_idx)

        return category_list
    
    @staticmethod
    def main_category(short: Item) -> Union[str, None]:
        """Extract the main category from the given browse node information.

        Args:
            short (Item): The browse node information for the product.

        Returns:
            Union[str, None]: The main category if found, otherwise None.
        """
        short_ancestor_3 = short.ancestor.ancestor.ancestor

        if (short_ancestor_3.ancestor.context_free_name is not None):
            return short_ancestor_3.ancestor.context_free_name
        return None

    @staticmethod
    def first_sub_category(short: Item) -> Union[str, None]:
        """Extract the first sub-category from the given browse node information

        Args:
            short (Item): The browse node information for the product.

        Returns:
            Union[str, None]: The first sub-category if found, otherwise None.
        """
        short_ancestor_3 = short.ancestor.ancestor.ancestor

        if (short_ancestor_3.context_free_name is not None):
            return short_ancestor_3.context_free_name
        return None

    @staticmethod
    def second_sub_category(short: Item) -> Union[str, None]:
        """Extract the second sub-category from the given browse 
            node information.

        Args:
            short (Item): The browse node information for the product.

        Returns:
            Union[str, None]: The second sub-category if found, otherwise None.
        """
        if (short.ancestor.ancestor.context_free_name is not None):
            return short.ancestor.ancestor.context_free_name
        return None

    @staticmethod
    def third_sub_category(short: Item) -> Union[str, None]:
        """Extract the third sub-category from the given browse node information.

        Args:
            short (Item): The browse node information for the product.

        Returns:
            Union[str, None]: The third sub-category if found, otherwise None.
        """
        if (short.ancestor.context_free_name is not None):
            return short.ancestor.context_free_name
        return None

    @staticmethod
    def fourth_sub_category(short: Item) -> Union[str, None]:
        """Extract the fourth sub-category from the given browse
            node information.

        Args:
            short (Item): The browse node information for the product.

        Returns:
            Union[str, None]: The fourth sub-category if found, otherwise None.
        """
        if (short.context_free_name is not None):
            return short.context_free_name
        return None

    @staticmethod
    def children_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract children nodes from the browse node information of the item.

        Args:
            item (Item): The item from which children nodes need to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Children nodes if found, otherwise None.
        
        Example:
            children = Product.children_extractor(item, asin)

            None
            items_result.items[].browse_node_info.browse_nodes[0].children
        """
        children = None

        if ((item.browse_node_info is not None) and 
            (item.browse_node_info.browse_nodes is not None)):
            short = item.browse_node_info.browse_nodes[0]

            try:
                if (short.children is not None) and (children is None):
                        children = short.children

            except Exception as e:
                logging.error(f"A error occurred while extracting "
                              f"the children of the asin {asin}: {e}.")
        return children

    @staticmethod
    def rank_extractor(item: Item, asin: str) -> int:
        """Extract the sales rank from the browse node information of the item.

        Args:
            item (Item): The item from which sales rank needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            int: Sales rank if found, otherwise -1.

        Example:
            rank = Product.rank_extractor(item, asin)

            None
            items_result.items[].browse_node_info.browse_nodes[0].sales_rank
        """
        rank = -1

        if ((item.browse_node_info is not None) and 
            (item.browse_node_info.browse_nodes is not None)):
            short = item.browse_node_info.browse_nodes[0]

            try:
                if (short.sales_rank is not None) and (rank == -1):
                        rank = int(short.sales_rank)
                
                short = item.browse_node_info

                if (short.website_sales_rank is not None) and (rank == -1):
                    if (short.website_sales_rank.sales_rank is not None):
                        rank = int(short.website_sales_rank.sales_rank)

            except Exception as e:
                logging.error(f"An error occurred while extracting the "
                              f"rank of the asin {asin}: {e}.")
        return rank
    
    @staticmethod
    def sales_rank_cf_name_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the context-free name associated with the sales rank from 
            the browse node information of the item.

        Args:
            item (Item): The item from which the context-free name of the sales 
                rank needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Context-free name if found, otherwise None.
        """
        short = item.browse_node_info
        sales_rank_cf_name = None

        if (short.website_sales_rank is not None):
            if (short.website_sales_rank.context_free_name is not None):
                sales_rank_cf_name = short.website_sales_rank.context_free_name
        return sales_rank_cf_name
    
    @staticmethod
    def page_link_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the detail page URL from the item.

        Args:
            item (Item): The item from which the detail page URL needs 
                to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Detail page URL if found, otherwise None.
        
        Example:
            page_link = Product.page_link_extractor(item, asin)

            https://www.amazon.it/dp/B091G3WT74?tag=andrepietr-21&linkCode=ogi&th=1&psc=1
            items_result.items[].detail_page_url
        """
        page_link = None

        if (item.detail_page_url is not None):
                page_link = item.detail_page_url
        return page_link
    
    @staticmethod
    def image_size_extractor(item: Item, asin: str) -> tuple[int, int]:
        """Extract the image size (height and width) from the item.

        Args:
            item (Item): The item from which the image size needs 
                to be extracted.
            asin (str): ASIN of the product.

        Returns:
            tuple[int, int]: A tuple containing the height and width of the 
                image, or (-1, -1) if not found.
            
        Example:
            img_height, img_width = Product.image_size_extractor(item, asin)

            500
            items_result.items[].images.primary.large.height

            500
            items_result.items[].images.primary.large.width

            500
            items_result.items[].images.primary.medium.height

            500
            items_result.items[].images.primary.medium.width
        """
        img_height, img_width = -1, -1

        if item.images is not None:
            if item.images.primary is not None:

                if item.images.primary.large is not None:
                    large = item.images.primary.large

                    try:
                        if (large.height is not None):
                            img_height = int(large.height)

                        if (large.width is not None):
                            img_width = int(large.width)

                    except Exception as e:
                        img_height, img_width = -1, -1
                        logging.error(f"An error occurred while extracting "
                                      f"the image size for the asin {asin} "
                                      f"Next attempt it will be with "
                                      f"the medium image: {e}.")

                if item.images.primary.medium is not None:
                    medium = item.images.primary.medium

                    try:
                        if ((medium.height is not None) and (img_height == -1)):
                            img_height = int(medium.height)

                        if ((medium.width is not None) and (img_width == -1)):
                            img_width = int(medium.width)

                    except Exception as e:
                        img_height, img_width = -1, -1
                        logging.error(f"An error occurred while extracting "
                                      f"the image size for the asin {asin} "
                                      f"Next attempt it will be with "
                                      f"the small image: {e}.")
        return img_height, img_width

    @staticmethod
    def image_link_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the image link from the item.

        Args:
            item (Item): The item from which the image link 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Image link if found, otherwise None.
        
        Example:
            image_link = Product.image_link_extractor(item, asin)

            https://m.media-amazon.com/images/I/31H+yPMQGeL._SL500_.jpg
            items_result.items[].images.primary.large.url

            https://m.media-amazon.com/images/I/31H+yPMQGeL._SL500_.jpg
            items_result.items[].images.primary.medium.url
        """
        image_link = None

        if item.images is not None:
            if item.images.primary is not None:

                if item.images.primary.large is not None:
                    large = item.images.primary.large

                    try:
                        if ((large.url is not None) and (image_link is None)):
                            image_link = item.images.primary.large.url

                    except Exception as e:
                        logging.error(f"An error occurred while extracting "
                                      f"the image link for the asin {asin} "
                                      f"Next attempt it will be with "
                                      f"the medium image: {e}.")

                if item.images.primary.medium is not None:
                    medium = item.images.primary.medium

                    try:
                        if (medium.url is not None) and (image_link is None):
                            image_link = item.images.primary.medium.url

                    except Exception as e:
                        logging.error(f"An error occurred while extracting "
                                      f"the image link for the asin {asin} "
                                      f"Next attempt it will be with "
                                      f"the small image: {e}.")
        return image_link
    
    @staticmethod
    def image_variants_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract image variants from the item.

        Args:
            item (Item): The item from which image variants need to be extracted
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Image variants if found, otherwise None.
        
        Example:
            image_variants = Product.image_variants_extractor(item, asin)

            None
            items_result.items[].images.variants

        Note:
            # TODO: Need more info 
        """
        if item.images is not None:
            if item.images.variants is not None:
                pass
    
    @staticmethod
    def brand_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the brand name from the item.

        Args:
            item (Item): The item from which the brand name 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Brand name if found, otherwise None.
        
        Example:
            brand = Product.brand_extractor(item, asin)

            Amazon
            items_result.items[].item_info.by_line_info.brand.display_value

            Amazon
            items_result.items[].item_info.by_line_info.manufacturer.display_value
        """
        brand = None

        if item.item_info is not None:
            short = item.item_info

            if short.by_line_info is not None:
                sub_short = short.by_line_info

                try:
                    if sub_short.brand is not None:
                        if sub_short.brand.display_value is not None:
                            brand = sub_short.brand.display_value

                except Exception as e:
                    logging.error(f"An error occurred while extracting "
                                    f"the brand name for the asin {asin} "
                                    f"Next attempt it will be with "
                                    f"the manufacturer name: {e}.")
                if brand is None:

                    try:
                        if sub_short.manufacturer is not None:
                            if sub_short.manufacturer.display_value is not None:
                                brand = sub_short.manufacturer.display_value

                    except Exception as e:
                        logging.error(f"An error occurred while extracting "
                                        f"the manufacturer name for the "
                                        f"asin {asin}: {e}.")
        return brand
    
    def locale_extraction(item: Item, asin: str) -> Union[str, None]:
        """Extract the locale information from the item.

        Args:
            item (Item): The item from which the locale information 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Locale information if found, otherwise None.
        
        Example:
            locale = Product.locale_extraction(item, asin)

            it_IT
            items_result.items[].item_info.by_line_info.brand.locale

            it_IT
            items_result.items[].item_info.by_line_info.manufacturer.locale

            it_IT
            items_result.items[].item_info.classifications.binding.locale
        """
        if item.item_info is None:
            return None
        
        locale = None
        short = item.item_info

        try:
            if short.by_line_info is not None:
                if short.by_line_info.brand is not None:

                    if short.by_line_info.brand.locale is not None:
                        locale = short.by_line_info.brand.locale

                if locale is not None:

                    if short.by_line_info.manufacturer is not None:
                        if short.by_line_info.manufacturer.locale is not None:
                            locale = short.by_line_info.manufacturer.locale

                if locale is not None:
                    
                    if ((short.classifications is not None) and 
                        (short.classifications.binding is not None)): 

                        if short.classifications.binding.locale is not None: 
                            locale = short.classifications.binding.locale

        except Exception as e:
            logging.error(f"An error occurred while extracting "
                            f"the locale for the asin {asin}: {e}.")
        return locale
    
    @staticmethod
    def classifications_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the classifications from the item.

        Args:
            item (Item): The item from which the classifications 
                need to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Classifications if found, otherwise None.
        
        Example:
            classifications = Product.classifications_extractor(item, asin)

            Elettronica
            items_result.items[].item_info.classifications.binding.display_value
        """
        if item.item_info is None:
            return None
        
        classifications = None
        sub_short = item.item_info

        if ((sub_short.classifications is not None) and 
            (sub_short.classifications.binding is not None)): 

            if (sub_short.classifications.binding.display_value is not None): 
                classifications = sub_short.classifications.binding.display_value
        return classifications
    
    @staticmethod
    def marketplace_extractor(item: Item, asin: str) -> Union[str, None]:
        """
        Extract the marketplace from the item.

        Args:
            item (Item): The item from which the marketplace 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Marketplace if found, otherwise None.

        Example:
            marketplace = Product.marketplace_extractor(item, asin)

            it_IT
            items_result.items[].item_info.content_info.languages.locale

            it_IT
            items_result.items[].item_info.features.locale
        """
        if item.item_info is None:
            return None
        
        marketplace = None
        sub_short = item.item_info
        
        try:
            if ((sub_short.content_info is not None) and 
                (sub_short.content_info.languages is not None) and 
                (sub_short.content_info.languages.locale is not None)):
                marketplace = sub_short.content_info.languages.locale
        except Exception as e:
            logging.error(f"An error occurred while extracting "
                            f"the marketplace for the asin {asin}: {e}.")
        
        if marketplace is None:
            try:
                if ((sub_short.features is not None) and 
                    (sub_short.features.locale is not None)):
                        marketplace = sub_short.features.locale

            except Exception as e:
                logging.error(f"An error occurred while extracting "
                            f"the marketplace for the asin {asin}: {e}.")
        return marketplace
    
    @staticmethod
    def bullet_points_extractor(item: Item, asin: str) -> list[str]:
        """Extract the bullet points from the item.

        Args:
            item (Item): The item from which the bullet points 
                need to be extracted.
            asin (str): ASIN of the product.

        Returns:
            list[str]: List of bullet points if found, otherwise an empty list.
        
        Example:
            bullet_points = Product.bullet_points_extractor(item, asin)

            La versione più conveniente di Fire ... musica e altro ancora.
            items_result.items[].item_info.features.display_values
        """
        bullet_points = []

        if item.item_info is not None:
            sub_short = item.item_info

            try:
                if ((sub_short.features is not None) and 
                    (sub_short.features.display_values is not None)):

                    for bullet_point in sub_short.features.display_values:
                        bullet_points.append(bullet_point)

            except Exception as e:
                logging.error(f"An error occurred while extracting "
                              f"the bullet points for the asin {asin}: {e}.")
        return bullet_points
    
    @staticmethod
    def color_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the color from the item.

        Args:
            item (Item): The item from which the color needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Color if found, otherwise None.
        
        Example:
            color = Product.color_extractor(item, asin)

            BLACK
            items_result.items[].item_info.product_info.color.display_value
        """
        if item.item_info is None:
            return None

        sub_short = item.item_info
        product_color = None

        if sub_short.product_info is not None:

            try:
                if ((sub_short.product_info.color is not None) and 
                    (sub_short.product_info.color.display_value is not None)):
                    product_color = sub_short.product_info.color.display_value

            except Exception as e:
                logging.error(f"An error occurred while extracting "
                              f"the product color for the asin {asin}: {e}.")
        return product_color
    
    @staticmethod
    def is_adult_product(item: Item, asin: str) -> Union[bool, None]:
        """Extract whether the item is an adult product.

        Args:
            item (Item): The item to check if it's an adult product.
            asin (str): ASIN of the product.

        Returns:
            Union[bool, None]: True if it's an adult product, 
                False if it's not, or None if information is not available.
        
        Example:
            adult_product = Product.is_adult_product(item, asin)

            False
            items_result.items[].item_info.product_info.is_adult_product.display_value
        """
        if item.item_info is None:
            return None

        short = item.item_info
        is_adult_product = None

        if short.product_info is not None:
            sub_short = short.product_info
        
            try:
                if ((sub_short.is_adult_product is not None) and 
                    (sub_short.is_adult_product.display_value is not None)):
                    adult_product = sub_short.is_adult_product.display_value

                    if adult_product == "True":
                        is_adult_product = True
                    else:
                        is_adult_product = False

            except Exception as e:
                logging.error(f"An error occurred while extracting "
                              f"the adult product for the asin {asin}: {e}.")
        return is_adult_product
    
    @staticmethod
    def unit_count_extractor(item: Item, asin: str) -> int:
        """Extract the unit count from the item.

        Args:
            item (Item): The item from which the unit count 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            int: Unit count if found, otherwise -1.
        
        Example:
            unit_count = Product.unit_count_extractor(item, asin)

            None
            items_result.items[].item_info.product_info.unit_count
        """
        if item.item_info is None:
            return -1

        unit_count = -1
        sub_short = item.item_info
        
        if sub_short.product_info is not None:
            if (sub_short.product_info.unit_count is not None):
                unit_count = int(sub_short.product_info.unit_count)
                
        return unit_count
    
    @staticmethod
    def technical_info_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the technical information from the item.

        Args:
            item (Item): The item from which the technical information 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Technical information if found, otherwise None.
        
        Example:
            technical_info = Product.technical_info_extractor(item, asin)

            None
            items_result.items[].item_info.technical_info
        """
        if item.item_info is None:
            return None

        sub_short = item.item_info
        technical_info = None

        if (sub_short.technical_info is not None):
            technical_info = sub_short.technical_info
        return technical_info
    
    @staticmethod
    def title_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the title from the item.

        Args:
            item (Item): The item from which the title needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Title if found, otherwise None.

        Example:
            title = Product.title_extractor(item, asin)

            Fire TV Stick Lite con telecomando vocale Alexa | Lite .....
            items_result.items[].item_info.product_info.title.display_value
        """
        if item.item_info is None:
            return None

        title = None
        sub_short = item.item_info

        try:
            if (sub_short.product_info.title is not None) and (
                sub_short.product_info.title.display_value is not None):
                title = sub_short.product_info.title.display_value

        except:
            if (sub_short.title is not None) and (
                sub_short.title.display_value is not None):
                title = sub_short.title.display_value
        return title
    
    @staticmethod
    def max_order_quantity_extractor(item: Item, asin: str) -> int:
        """Extract the maximum order quantity from the item.

        Args:
            item (Item): The item from which the maximum order quantity 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            int: Maximum order quantity if found, otherwise -1.

        Example:
            max_quantity = Product.max_order_quantity_extractor(item, asin)

            2
            items_result.items[].offers.listings[0].availability.max_order_quantity
        """
        max_quantity = -1

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.availability is not None:
                    sub_short = short.availability
                    if sub_short.max_order_quantity is not None:
                        max_quantity = int(sub_short.max_order_quantity)
        return max_quantity
    
    @staticmethod
    def availability_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the availability message from the item.

        Args:
            item (Item): The item from which the availability 
                message needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Availability message if found, otherwise None.

        Example:
            available = Product.availability_extractor(item, asin)

            Disponibilità immediata.
            items_result.items[].offers.listings[0].availability.message
        """
        available = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.availability is not None:
                    if short.availability.message is not None:
                        available = short.availability.message
        return available

    @staticmethod
    def min_order_quantity_extractor(item: Item, asin: str) -> int:
        """Extract the minimum order quantity from the item.

        Args:
            item (Item): The item from which the minimum order 
                quantity needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            int: Minimum order quantity if found, otherwise -1.
        
        Example:
            min_quantity = Product.min_order_quantity_extractor(item, asin)

            1
            items_result.items[].offers.listings[0].availability.min_order_quantity
        """
        min_quantity = -1

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.availability is not None:
                    sub_short = short.availability
                    if sub_short.min_order_quantity is not None:
                        min_quantity = int(sub_short.min_order_quantity)
        return min_quantity

    @staticmethod
    def when_available_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract when the item is available.

        Args:
            item (Item): The item from which the availability 
                type needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Availability type if found, otherwise None.

        Example:
            when_available = Product.when_available_extractor(item, asin)

            Now
            items_result.items[].offers.listings[0].availability.type
        """
        when_available = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.availability is not None:
                    if short.availability.type is not None:
                        when_available = short.availability.type
        return when_available
    
    @staticmethod
    def condition_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the condition of the item.

        Args:
            item (Item): The item from which the condition needs to be extracted
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Condition of the item if found, otherwise None.

        Example:
            condition = Product.condition_extractor(item, asin)

            None
            items_result.items[].offers.listings[0].condition.display_value

            None
            items_result.items[].offers.listings[0].acondition.sub_condition.display_value

            New
            items_result.items[].offers.listings[0].condition.sub_condition.value
        """
        condition = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]
                
                if short.condition is not None:
                    if short.condition.display_value is not None:
                        condition = short.condition.display_value

                    if ((short.condition.sub_condition is not None) and 
                        (condition is None)):
                        sub_short = short.condition.sub_condition

                        if sub_short.display_value is not None:
                            condition = sub_short.display_value
        
            if condition is None:
                if item.offers.summaries is not None:
                    short = item.offers.summaries[0]

                    if short.condition is not None:
                        if short.condition.display_value is not None:
                            condition = short.condition.display_value
        return condition

    @staticmethod
    def condition_value_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the condition value of the item.

        Args:
            item (Item): The item from which the condition 
                value needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Condition value of the item if found, 
                otherwise None.

        Example:
            condition_value = Product.condition_value_extractor(item, asin)

            New
            items_result.items[].offers.listings[0].condition.value

            New
            items_result.items[].offers.listings[0].condition.sub_condition.value
        """
        condition_value = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.condition is not None:
                    
                    if short.condition.value is not None:
                        condition_value = short.condition.value

                    if ((short.condition.sub_condition is not None) and 
                        (condition_value is None)):

                        if short.condition.sub_condition.value is not None:
                            condition_value = short.condition.sub_condition.value
        
            if condition_value is None:
                if item.offers.summaries is not None:
                    short = item.offers.summaries[0]

                    if short.condition is not None:
                        if short.condition.value is not None:
                            condition_value = short.condition.value
        return condition_value
            
    @staticmethod
    def is_amazon_fulfilled(item: Item, asin: str) -> Union[bool, None]:
        """Extract whether the item is Amazon fulfilled or not.

        Args:
            item (Item): The item from which the Amazon fulfillment 
                status needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[bool, None]: True if Amazon fulfilled, False if not, 
                otherwise None.

        Example:
            amz_fulfilled = Product.is_amazon_fulfilled(item, asin)

            True
            items_result.items[].offers.listings[0].delivery_info.is_amazon_fulfilled
        """
        is_amazon_fulfilled = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.delivery_info is not None:
                    if short.delivery_info.is_amazon_fulfilled is not None:
                        amz_fulfilled = short.delivery_info.is_amazon_fulfilled
                        if amz_fulfilled == "True":
                            is_amazon_fulfilled = True
                        else:
                            is_amazon_fulfilled = False
        return is_amazon_fulfilled
    
    @staticmethod
    def is_free_shipping_eligible(item: Item, asin: str) -> Union[bool, None]:
        """Extract whether the item is eligible for free shipping.

        Args:
            item (Item): The item from which the free shipping 
                eligibility needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[bool, None]: True if eligible for free shipping, 
                False if not, otherwise None.
        
        Example:
            free_ship_eligible = Product.is_free_shipping_eligible(item, asin)

            True
            items_result.items[].offers.listings[0].delivery_info.iis_free_shipping_eligible
        """
        is_free_shipping_eligible = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.delivery_info is not None:
                    sub_short = short.delivery_info

                    if sub_short.is_free_shipping_eligible is not None:
                        free_ship_eligible = sub_short.is_free_shipping_eligible

                        if free_ship_eligible == "True":
                            is_free_shipping_eligible = True
                        else:
                            is_free_shipping_eligible = False
        return is_free_shipping_eligible
    
    @staticmethod
    def is_prime_eligible(item: Item, asin: str) -> Union[bool, None]:
        """Extract whether the item is eligible for Amazon Prime.

        Args:
            item (Item): The item from which the Prime eligibility 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[bool, None]: True if eligible for Amazon Prime, 
                False if not, otherwise None.
        
        Example:
            prime_eligible = Product.is_prime_eligible(item, asin)

            True
            items_result.items[].offers.listings[0].delivery_info.is_prime_eligible
        """
        is_prime_eligible = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.delivery_info is not None:
                    if short.delivery_info.is_prime_eligible is not None:
                        prime_eligible = short.delivery_info.is_prime_eligible

                        if prime_eligible == "True":
                            is_prime_eligible = True
                        else:
                            is_prime_eligible = False
        return is_prime_eligible
    
    @staticmethod
    def shipping_charges_extractor(item: Item, asin: str) -> float:
        """Extract the shipping charges of the item.

        Args:
            item (Item): The item from which the shipping 
                charges need to be extracted.
            asin (str): ASIN of the product.

        Returns:
            float: The shipping charges of the item. Returns -1.0 
                if shipping charges are not available.
        
        Example:
            shipping_charges = Product.shipping_charges_extractor(item, asin)

            None
            items_result.items[].offers.listings[0].delivery_info.shipping_charges
        """
        shipping_charges = -1.0

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.delivery_info is not None:
                    if short.delivery_info.shipping_charges is not None:
                        shipping_charges = short.delivery_info.shipping_charges
        return shipping_charges
    
    @staticmethod
    def is_buy_box_winner(item: Item, asin: str) -> Union[bool, None]:
        """Extract whether the item is the winner of the Buy Box.

        Args:
            item (Item): The item from which the Buy Box winner status 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[bool, None]: True if the item is the winner of the 
                Buy Box, False if not, otherwise None.
        
        Example:
            buy_box_winner = Product.is_buy_box_winner(item, asin)

            True
            items_result.items[].offers.listings[0].is_buy_box_winner
        """
        is_buy_box_winner = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.is_buy_box_winner is not None:
                    buy_box_winner = short.is_buy_box_winner

                    if buy_box_winner == "True":
                        is_buy_box_winner = True
                    else:
                        is_buy_box_winner = False
        return is_buy_box_winner
    
    @staticmethod
    def price_extractor(item: Item, asin: str) -> float:
        """
        Extract the current price of the item.

        Args:
            item (Item): The item from which the current price 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            float: The current price of the item. Returns -1.0 if 
                price extraction fails.
            
        Raises:
            AttributeError: If there is an attribute error while 
                extracting the price.
            ValueError: If there is a value error while extracting the price.
            Exception: If any other error occurs during the extraction process.
        
        Example:
            current_price = Product.price_extractor(item, asin)

            24.99
            items_result.items[].offers.listings[0].price.amount
        """
        current_price = -1.0

        try:
            if item.offers is not None:
                if item.offers.listings is not None:
                    short = item.offers.listings[0]
                    
                    if short.price is not None:
                        if short.price.amount is not None:
                            current_price = float(short.price.amount)
        except AttributeError as ae:
            logging.error(f"An attribute error occurred while extracting "
                            f"the current price for the asin {asin}: {ae}.")
        except ValueError as ve:
            logging.error(f"A value error occurred while extracting "
                            f"the current price for the asin {asin}: {ve}.")
        except Exception as e:
            logging.error(f"An error occurred while extracting "
                            f"the current price for the asin {asin}: {e}.")
        return current_price
    
    @staticmethod
    def currency_extractor(item: Item, asin: str) -> Union[str, None]:
        """
        Extract the currency of the item's price.

        Args:
            item (Item): The item from which the currency needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The currency of the item's price. Returns 
                None if currency extraction fails.
            
        Raises:
            AttributeError: If there is an attribute error while 
                extracting the currency.
            Exception: If any other error occurs during the extraction process.
        
        Example:
            current_currency = Product.currency_extractor(item, asin)

            EUR
            items_result.items[].offers.listings[0].price.currency
        """
        current_currency = None

        try:
            if item.offers is not None:
                if item.offers.listings is not None:
                    short = item.offers.listings[0]
                    
                    if short.price is not None:
                        if short.price.currency is not None:
                            current_currency = short.price.currency
        except AttributeError as ae:
            logging.error(f"An attribute error occurred while extracting "
                          f"the current currency for the asin {asin}: {ae}.")
        except Exception as e:
            logging.error(f"An error occurred while extracting "
                          f"the current currency for the asin {asin}: {e}.")
        return current_currency
    
    @staticmethod
    def price_per_unit_extractor(item: Item, asin: str) -> Union[str, None]:
        """
        Extract the price per unit of the item.

        Args:
            item (Item): The item from which the price per unit 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The price per unit of the item. 
                Returns None if price per unit extraction fails.
        
        Example:
            price_per_unit = Product.price_per_unit_extractor(item, asin)

            EUR
            items_result.items[].offers.listings[0].price.price_per_unit
        """
        price_per_unit = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.price is not None:
                    if short.price.price_per_unit is not None:
                        price_per_unit = short.price.price_per_unit
        return price_per_unit
    
    @staticmethod
    def savings_price_extractor(item: Item, asin: str) -> float:
        """Extract the savings price of the item.

        Args:
            item (Item): The item from which the savings price 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            float: The savings price of the item. Returns -1.0 
                if extraction fails.
        
        Example:
            savings_price = Product.savings_price_extractor(item, asin)

            10.0
            items_result.items[].offers.listings[0].price.savings.amount
        """
        savings_price = -1.0

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.price is not None:
                    if short.price.savings is not None:

                        if short.price.savings.amount is not None:
                            savings_price = float(short.price.savings.amount)
        return savings_price
    
    @staticmethod
    def savings_currency_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extract the currency of the savings price of the item.

        Args:
            item (Item): The item from which the savings currency 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The currency of the savings price of the item. 
                Returns None if extraction fails.
        
        Example:
            savings_currency = Product.savings_currency_extractor(item, asin)

            EUR
            items_result.items[].offers.listings[0].price.savings.currency
        """
        savings_currency = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]
                
                if short.price is not None:
                    if short.price.savings is not None:

                        if short.price.savings.currency is not None:
                            savings_currency = short.price.savings.currency
        return savings_currency
    
    @staticmethod
    def discounted_percentage_extractor(item: Item, asin: str) -> int:
        """Extract the discounted percentage of the item.

        Args:
            item (Item): The item from which the discounted percentage 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            int: The discounted percentage of the item. Returns 0 if 
                extraction fails.

        Raises:
            Exception: If an error occurs during extraction.
        
        Example:
            percentage = Product.discounted_percentage_extractor(item, asin)

            29
            items_result.items[].offers.listings[0].price.savings.percentage
        """
        disc_percentage = 0

        try:
            if item.offers is not None:
                if item.offers.listings is not None:
                    short = item.offers.listings[0]

                    if short.price is not None:
                        if short.price.savings is not None:
                            sub_short = short.price.savings
                            
                            if sub_short.percentage is not None:
                                disc_percentage = int(sub_short.percentage)
        except Exception as e:
            logging.error(f"An error occurred while extracting "
                          f"the discounted percentage for "
                          f"the asin {asin}: {e}.")
        return disc_percentage
    
    @staticmethod
    def savings_price_per_unit_extractor(
        item: Item, 
        asin: str
    ) -> Union[str, None]:
        """Extracts the savings price per unit of the item.

        Args:
            item (Item): The item from which the savings price per 
                unit needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The savings price per unit of the item. 
                Returns None if extraction fails.
        
        Example:
            svg_price_per_unit = Product.savings_price_per_unit_extractor(item, asin)

            None
            items_result.items[].offers.listings[0].price.savings.price_per_unit
        """
        savings_price_per_unit = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.price is not None:
                    if short.price.savings is not None:
                        sub_short = short.price.savings

                        if sub_short.price_per_unit is not None:
                            savings_price_per_unit = sub_short.price_per_unit

        if savings_price_per_unit is None:

            if item.offers is not None:
                if item.offers.listings is not None:
                    short = item.offers.listings[0]

                    if short.saving_basis is not None:
                        sub_short = short.saving_basis

                        if sub_short.price_per_unit is not None:
                            savings_price_per_unit = sub_short.price_per_unit
        return savings_price_per_unit
    
    @staticmethod
    def is_prime_exclusive(item: Item, asin: str) -> Union[bool, None]:
        """Extracts whether the item is exclusive to Amazon Prime members.

        Args:
            item (Item): The item from which the prime exclusivity 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[bool, None]: True if the item is exclusive to 
                Amazon Prime members, False if not.
            None if extraction fails.
        
        Example:
            prime_exclusive = Product.is_prime_exclusive(item, asin)

            None
            items_result.items[].offers.listings[0].program_eligibility.is_prime_exclusive
        """
        is_prime_exclusive = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.program_eligibility is not None:
                    sub_short = short.program_eligibility

                    if sub_short.is_prime_exclusive is not None:
                        prime_exclusive = sub_short.is_prime_exclusive

                        if prime_exclusive == "True":
                            is_prime_exclusive = True
                        else:
                            is_prime_exclusive = False
        return is_prime_exclusive
    
    @staticmethod
    def is_prime_pantry(item: Item, asin: str) -> Union[bool, None]:
        """Extracts whether the item is available through Amazon Prime Pantry.

        Args:
            item (Item): The item from which the Prime Pantry availability 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[bool, None]: True if the item is available through 
                Amazon Prime Pantry, False if not.
            None if extraction fails.
        
        Example:
            prime_pantry = Product.is_prime_pantry(item, asin)

            None
            items_result.items[].offers.listings[0].program_eligibility.is_prime_pantry
        """
        is_prime_pantry = None

        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.program_eligibility is not None:
                    sub_short = short.program_eligibility

                    if sub_short.is_prime_pantry is not None:
                        prime_pantry = sub_short.is_prime_pantry

                        if prime_pantry == "True":
                            is_prime_pantry = True
                        else:
                            is_prime_pantry = False
        return is_prime_pantry
    
    @staticmethod
    def promotions_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extracts promotions available for the item.

        Args:
            item (Item): The item from which promotions need to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: Promotions available for the item, or 
                None if no promotions are found
            or extraction fails.
        
        Example:
            promotions = Product.promotions_extractor(item, asin)

            None
            items_result.items[].offers.listings[0].promotions
        """
        promotions = None
        if item.offers is not None:
            if item.offers.listings is not None:
                short = item.offers.listings[0]

                if short.promotions is not None:
                    promotions = short.promotions
        return promotions
    
    @staticmethod
    def old_price_extractor(item: Item, asin: str) -> float:
        """
        Extracts the old price of the item.

        Args:
            item (Item): The item from which the old price needs to be extracted
            asin (str): ASIN of the product.

        Returns:
            float: The old price of the item, or -1.0 if extraction fails.

        Raises:
            Exception: If an error occurs during extraction.
        
        Example:
            old_price = Product.old_price_extractor(item, asin)

            34.99
            items_result.items[].offers.listings[0].saving_basis.amount
        """
        old_price = -1.0

        try:
            if item.offers is not None:
                if item.offers.listings is not None:
                    short = item.offers.listings[0]

                    if short.saving_basis is not None:
                        
                        if short.saving_basis.amount is not None:
                            old_price = float(short.saving_basis.amount)
        except Exception as e:
            logging.error(f"An error occurred while extracting "
                          f"the old price for the asin {asin}: {e}.")
        return old_price
    
    @staticmethod
    def old_currency_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extracts the old currency of the item.

        Args:
            item (Item): The item from which the old currency 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The old currency of the item, or 
                None if extraction fails.

        Raises:
            Exception: If an error occurs during extraction.
        
        Example:
            old_currency = Product.old_currency_extractor(item, asin)

            EUR
            items_result.items[].offers.listings[0].saving_basis.currency
        """
        old_currency = None

        try:
            if item.offers is not None:
                if item.offers.listings is not None:
                    short = item.offers.listings[0]

                    if short.saving_basis is not None:
                        
                        if short.saving_basis.currency is not None:
                            old_currency = short.saving_basis.currency
        except Exception as e:
            logging.error(f"An error occurred while extracting "
                          f"the old currency for the asin {asin}: {e}.")
        return old_currency
    
    @staticmethod
    def merchant_brand_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extracts the merchant brand name of the item.

        Args:
            item (Item): The item from which the merchant brand 
                name needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The merchant brand name of the item, 
                or None if extraction fails.

        Raises:
            Exception: If an error occurs during extraction.
        
        Example:
            merchant_brand = Product.merchant_brand_extractor(item, asin)

            Amazon
            items_result.items[].offers.listings[0].merchant_info.brand_name
        """
        merchant = None

        try:
            if item.offers is not None:
                if item.offers.listings is not None:
                    short = item.offers.listings[0]
                    
                    if ((short.merchant_info is not None) and 
                        (short.merchant_info.name is not None)):
                        merchant = short.merchant_info.name

        except Exception as e:
            logging.error(f"An error occurred while extracting "
                            f"the merchant name for the "
                            f"asin {asin}: {e}.")
        return merchant
    
    @staticmethod
    def hightest_price_extractor(item: Item, asin: str) -> float:
        """Extracts the highest price of the item.

        Args:
            item (Item): The item from which the highest price 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            float: The highest price of the item, or -1.0 if extraction fails.
        
        Example:
            hightest_price = Product.hightest_price_extractor(item, asin)

            24.99
            items_result.items[].offers.summaries[0].highest_price.amount
        """
        hightest_price = -1.0

        if item.offers is not None:
            if item.offers.summaries is not None:
                short = item.offers.summaries[0]

                if short.highest_price is not None:
                    if short.highest_price.amount is not None:
                        hightest_price = float(short.highest_price.amount)
        return hightest_price
    
    @staticmethod
    def hightest_currency_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extracts the currency of the highest price of the item.

        Args:
            item (Item): The item from which the currency of the 
                highest price needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The currency of the highest price of 
                the item, or None if extraction fails.
        
        Example:
            hightest_currency = Product.hightest_currency_extractor(item, asin)

            EUR
            items_result.items[].offers.summaries[0].highest_price.currency
        """
        hightest_currency = None

        if item.offers is not None:
            if item.offers.summaries is not None:
                short = item.offers.summaries[0]

                if short.highest_price is not None:
                    if short.highest_price.currency is not None:
                        hightest_currency = short.highest_price.currency
        return hightest_currency
    
    @staticmethod
    def hightest_price_per_unit_extractor(
        item: Item, 
        asin: str
    ) -> Union[str, None]:
        """Extracts the price per unit of the highest price of the item.

        Args:
            item (Item): The item from which the price per unit of the 
                highest price needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The price per unit of the highest price of 
                the item, or None if extraction fails.
        
        Example:
            h_price_per_unit = Product.hightest_price_per_unit_extractor(item, asin)

            None
            items_result.items[].offers.summaries[0].highest_price.price_per_unit
        """
        hightest_price_per_unit = None

        if item.offers is not None:
            if item.offers.summaries is not None:
                short = item.offers.summaries[0]

                if short.highest_price is not None:
                    sub_short = short.highest_price
                    if sub_short.price_per_unit is not None:
                        hightest_price_per_unit = sub_short.price_per_unit
        return hightest_price_per_unit
    
    @staticmethod
    def lowest_price_extractor(item: Item, asin: str) -> float:
        """Extracts the lowest price of the item.

        Args:
            item (Item): The item from which the lowest price needs 
                to be extracted.
            asin (str): ASIN of the product.

        Returns:
            float: The lowest price of the item, or -1.0 if extraction fails.
        
        Example:
            lowest_price = Product.lowest_price_extractor(item, asin)

            24.99
            items_result.items[].offers.summaries[0].lowest_price.amount
        """
        lowest_price = -1.0

        if item.offers is not None:
            if item.offers.summaries is not None:
                short = item.offers.summaries[0]

                if short.lowest_price is not None:
                    if short.lowest_price.amount is not None:
                        lowest_price = float(short.lowest_price.amount)
        return lowest_price
    
    @staticmethod
    def lowest_currency_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extracts the currency of the lowest price of the item.

        Args:
            item (Item): The item from which the currency of the 
                lowest price needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The currency of the lowest price, or 
                None if extraction fails.
        
        Example:
            lowest_currency = Product.lowest_currency_extractor(item, asin)

            EUR
            items_result.items[].offers.summaries[0].lowest_price.currency
        """
        lowest_currency = None

        if item.offers is not None:
            if item.offers.summaries is not None:
                short = item.offers.summaries[0]

                if short.lowest_price is not None:
                    if short.lowest_price.currency is not None:
                        lowest_currency = short.lowest_price.currency
        return lowest_currency
    
    @staticmethod
    def lowest_price_per_unit_extractor(
        item: Item, 
        asin: str
    ) -> Union[str, None]:
        """Extracts the lowest price per unit of the item.

        Args:
            item (Item): The item from which the lowest price per 
                unit needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The lowest price per unit, or 
                None if extraction fails.
        
        Example:
            lowest_price_per_unit = Product.lowest_price_per_unit_extractor(item, asin)

            None
            items_result.items[].offers.summaries[0].lowest_price.price_per_unit
        """
        lowest_price_per_unit = None

        if item.offers is not None:
            if item.offers.summaries is not None:
                short = item.offers.summaries[0]

                if short.lowest_price is not None:
                    sub_short = short.lowest_price
                    if sub_short.price_per_unit is not None:
                        lowest_price_per_unit = sub_short.price_per_unit
        return lowest_price_per_unit
    
    @staticmethod
    def offer_count_extractor(item: Item, asin: str) -> int:
        """Extracts the count of offers available for the item.

        Args:
            item (Item): The item from which the offer count 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            int: The count of offers available, or -1 if extraction fails.
        
        Example:
            offer_count = Product.offer_count_extractor(item, asin)

            1
            items_result.items[].offers.summaries[0].offer_count
        """
        offer_count = -1

        if item.offers is not None:
            if item.offers.summaries is not None:
                short = item.offers.summaries[0]
                
                if short.offer_count is not None:
                    offer_count = short.offer_count
        return offer_count
    
    @staticmethod
    def parent_asin_extractor(item: Item, asin: str) -> Union[str, None]:
        """Extracts the parent ASIN of the item.

        Args:
            item (Item): The item from which the parent ASIN 
                needs to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The parent ASIN if available, otherwise None.
        
        Example:
            parent_asin = Product.parent_asin_extractor(item, asin)

            None
            items_result.items[].parent_asin
        """
        parent_asin = None
        if item.parent_asin is not None:
            parent_asin = item.parent_asin 
        return parent_asin
    
    @staticmethod
    def variation_attributes_extractor(
        item: Item, 
        asin: str
    ) -> Union[str, None]:
        """
        Extracts the variation attributes of the item.

        Args:
            item (Item): The item from which the variation attributes 
                need to be extracted.
            asin (str): ASIN of the product.

        Returns:
            Union[str, None]: The variation attributes if available, 
                otherwise None.
        
        Example:
            var_attributes = Product.variation_attributes_extractor(item, asin)

            None
            items_result.items[].variation_attributes
        Notes:
            # TODO: Need more info 
        """
        if item.parent_asin is not None:
            if item.variation_attributes is not None:
                pass

    @staticmethod
    def release_date_extractor(item: Item, asin: str) -> Union[datetime, None]:
        """Extract the release date of the item.

        Args:
            item (Item): The item from which the release date 
                needs to be extracted.
            asin (str): ASIN of the product.
        
        Returns:
            Union[datetime, None]: The release date of the item if 
                available, otherwise None.

        Example:
            release_date = Product.release_date_extractor(item, asin)

            2021-01-01
            items_result.items[].product_info.release_date.display_value
        
        Notes:
            # TODO: Check if there is always a Z in the date.
            #: Find a way to find the correct release date if not available.
        """
        release, release_date = None, None

        try:
            if item.item_info is not None:
                if item.item_info.product_info is not None:
                    sub_item = item.item_info.product_info
                    
                    if sub_item.release_date is not None:
                        if sub_item.release_date.display_value is not None:
                            release = sub_item.release_date.display_value

        except Exception as e:
            logging.error(f"An error occurred while extracting the "
                        f"release date for the asin {asin}: {e}.")
            
        if release is None:
            current_date = datetime.now()
            one_year_ago_date = current_date - timedelta(days=365)
            return one_year_ago_date.date()
            
        if 'Z' in release:
            release = release.replace('Z', '+00:00')
            release_date = datetime.fromisoformat(release)

        else:
            logging.error(f"Release date does not have a Z for the "
                        f"asin {asin}.")

        return release_date.date()
            
