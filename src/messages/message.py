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
import re
import os
import random
import logging
from typing import Union

# External libraries
import flag 

# Imported modules
from media import image_generator as image_gen
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.product import Product
from messages.phrase_library import mix_phrase_list
from messages.phrase_library import discount_65_more
from messages.phrase_library import discount_35_more
from utils.log_manager import setup_logger

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

class Message:
    """Represents a message containing information about a product.

    Attributes:
        asin (str): The unique identifier for the product.
        brand (str): The brand name of the product.
        title (str): The title or name of the product.
        bullet_points (list[str]): A list of bullet points describing 
            the product features.
        url (str): The URL of the product page.
        marketplace (tuple[str, str]): A tuple containing the name and 
            flag of the nationality of the marketplace. Example: ('US', '🇺🇸').
        price (Union[int, float]): The current price of the product.
        currency (tuple[Union[str, None], Union[str, None]]): The location 
            and currency code for the current price. Example: ("USD", "$").
        old_price (Union[int, float]): The previous price of the product.
        old_currency (tuple[Union[str, None], Union[str, None]]): The location 
            and currency code for the previous price.
        discount_percentage (Union[int, float]): The discount percentage 
            of the product.
        image_url (str): The URL of the product image.

    Methods:
        __init__: Initializes a Message object with provided information.
        __repr__: Returns a string representation of the Message object.
        __str__: Returns a human-readable string representation 
            of the Message object.
        __dict__: Returns a dictionary representation of the Message object.
        invisible_image_url: Returns an HTML anchor tag for an invisible image 
            linked to the image URL.
        markup_generator: Generates an InlineKeyboardMarkup for sending a 
            markdown message with Amazon links.
        html_message: Generates an HTML message with product information.
        from_product: Creates a Message instance from a Product instance.
        process_price: Processes the price for a given ASIN.
        process_currency: Processes the currency for a given ASIN.
        process_discount_percentage: Processes the discount percentage 
            for a given ASIN.
        process_discount: Processes the discount amount for a given ASIN.
        title_generator: Generates bullet points from a product title.
        bp_generator: Generates bullet points for a Message from the 
            title and description list.
        image_url_generator: Generates a more visually appealing product image.
        marketplace_emoji: Generates an emoji representation for a marketplace.
        marketplace_location: Extracts the country flag for a given marketplace.
        coupon_generator: Placeholder method for future coupon generation.
    """
    def __init__(
            self,
            asin: str,
            brand: str,
            title: str,
            bullet_points: list[str],
            url: str,
            marketplace: tuple[str, str],
            price: Union[int, float],
            currency: tuple[Union[str, None], Union[str, None]],
            old_price: Union[int, float],
            old_currency: tuple[Union[str, None], Union[str, None]],
            discount_percentage: Union[int, float],
            image_url: str,
        ) -> None:
        """Initializes a Message object with the provided information.

        Args:
            asin (str): The unique identifier for the product.
            brand (str): The brand name of the product.
            title (str): The title or name of the product.
            bullet_points (list[str]): A list of bullet points describing 
                the product features.
            url (str): The URL of the product page.
            marketplace (tuple[str, str]): A tuple containing the name and 
                flag of the nationality of the marketplace. 
                Example: ('US', '🇺🇸').
            price (Union[int, float]): The current price of the product.
            currency (tuple[Union[str, None], Union[str, None]]): The location 
                and currency code for the current price. 
                Example: ("USD", "$").
            old_price (Union[int, float]): The previous price of the product.
            old_currency (tuple[Union[str, None], Union[str, None]]): The 
                location and currency code for the previous price.
            discount_percentage (Union[int, float]): The discount percentage 
                of the product.
            image_url (str): The URL of the product image.

        Returns:
            None: This method does not return anything.

        Raises:
            Any exceptions raised during object initialization are propagated.

        Example:
            product = Message(
                asin="B07WDCJ8VH",
                brand="ExampleBrand",
                title="Example Product",
                bullet_points=["Feature 1", "Feature 2", "Feature 3"],
                url="https://example.com/product",
                marketplace=('US', '🇺🇸'),
                price=99.99,
                currency=("$", "USD"),
                old_price=129.99,
                old_currency=("$", "USD"),
                discount_percentage=10,
                image_url="https://example.com/image.jpg"
            )
        """
        self.asin = asin
        self.brand = brand
        self.title = title
        self.bullet_points = bullet_points
        self.url = url
        self.marketplace = marketplace
        self.price = price
        self.currency = currency
        self.old_price = old_price
        self.old_currency = old_currency
        self.discount_percentage = discount_percentage
        self.image_url = image_url
    
    def __repr__(self) -> str:
        """Returns a string representation of the Message object that can 
            be evaluated to recreate the object.

        Returns:
            str: A string representation of the Message object.

        Example:
            repr_message = repr(message)
            # Output: 'Message(asin=example_asin, brand=example_brand, 
                title=example_title, ...)'
        """
        return (
            f"Message(asin={self.asin}, "
            f"brand={self.brand}, "
            f"title={self.title}, "
            f"bullet_points={self.bullet_points}, "
            f"url={self.url}, "
            f"marketplace={self.marketplace}, "
            f"price={self.price}, "
            f"currency={self.currency}, "
            f"old_price={self.old_price}, "
            f"old_currency={self.old_currency}, "
            f"discount_percentage={self.discount_percentage}, "
            f"image_url={self.image_url})"
        )

    def __str__(self) -> str:
        """Returns a human-readable string representation of the Message object.

        Returns:
            str: A human-readable string representation of the Message object.

        Example:
            str_message = str(message)
            # Output: 'Asin: example_asin, Brand: example_brand, 
                Title: example_title, ...'
        """
        return (
            f"Asin: {self.asin}, "
            f"Brand: {self.brand}, "
            f"Title: {self.title}, "
            f"Bullet Points: {self.bullet_points}, "
            f"Url: {self.url}, "
            f"Marketplace: {self.marketplace}, "
            f"Price: {self.price}, "
            f"Currency: {self.currency}, "
            f"Old Price: {self.old_price}, "
            f"Old Currency: {self.old_currency}, "
            f"Discount Percentage: {self.discount_percentage}%, "
            f"Image Url: {self.image_url}"
        )
    
    def __dict__(self) -> dict:
        """Returns a dictionary representation of the Message object.

        Returns:
            dict: A dictionary containing the attributes of the Message object.

        Example:
            message_dict = message.__dict__()
            # Output: {'asin': 'example_asin', 'brand': 'example_brand', 
                'title': 'example_title', ...}
        """
        return {
            "asin": self.asin,
            "brand": self.brand,
            "title": self.title,
            "bullet_points": self.bullet_points,
            "url": self.url,
            "marketplace": self.marketplace,
            "price": self.price,
            "currency": self.currency,
            "old_price": self.old_price,
            "old_currency": self.old_currency,
            "discount_percentage": self.discount_percentage,
            "image_url": self.image_url
        }
    
    @property
    def invisible_image_url(self) -> str:
        """Returns an HTML anchor tag for an invisible image 
            linked to the image URL.

        Returns:
            str: An HTML anchor tag for an invisible image.

        Example:
            invisible_image = message.invisible_image_url
            # Output: "<a href='example_image_url'>&#8205</a>"
        """
        return f"<a href='{self.image_url}'>&#8205</a>"

    def markup_generator(self, partner_tag: str) -> InlineKeyboardMarkup:
        """Generates an InlineKeyboardMarkup for sending a markdown 
            message with Amazon links.

        Args:
            partner_tag (str): The partner tag used for affiliate linking.

        Returns:
            InlineKeyboardMarkup: An InlineKeyboardMarkup object 
                containing the generated markup.

        Example:
            markup = message.markup_generator("example_partner_tag")
            # Output: An InlineKeyboardMarkup object containing 
                buttons for Amazon links.
        """
        url=f"http://www.amazon.it/provaprime?tag={partner_tag}"

        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(
            InlineKeyboardButton("👑 Prime GRATIS", 
                                callback_data="free prime",
                                url=url),

            InlineKeyboardButton("📲 APRI IN APP", 
                                callback_data="apri app", 
                                url=self.url),)
        return markup
    
    def html_message(self) -> str:
        """Generate an HTML-formatted message for displaying product information

        The HTML message includes the product title, an optional emoji title 
            based on the discount percentage, an invisible image URL, 
            bullet points of product features, marketplace emoji, price 
            information, and a link to open the product page on Amazon.

        Returns:
            str: HTML-formatted message.
        """
        if ((self.discount_percentage < 35)):
            emj_title = ""

        elif self.discount_percentage < 50:
            emj_title = random.choice(["💣", "🧨", "⚠️"])

        else:
            emj_title = random.choice(["🆘", "🔥"])

        html = f"{emj_title} <b>{self.title}</b> {emj_title}\n\n" \
                f"{self.invisible_image_url}"
        
        for index in self.bullet_points:
            if index is not None:
                # '●' '🔹' '▫️' '🔘'
                html += f"{'▫️'}️ {remove_emj(index)}\n"
        
        html += Message.marketplace_emoji(self.marketplace[1])

        if self.discount_percentage != 0:
            discount_price = Message.process_discount(self.asin, self.price, 
                                                      self.old_price)
            
            discount_price_str = format(discount_price,'.2f').replace('.', ',')
            price_str = format(self.price,'.2f').replace('.', ',')
            old_price_str = format(self.old_price,'.2f').replace('.', ',')
            
            html += f"💶 <b>{price_str}" \
            f"{self.currency[1]}</b> invece di " \
            f"{old_price_str}{self.currency[1]}\n" \
            f"📈 <b>Risparmi {discount_price_str}" \
            f"{self.old_currency[1]} ({self.discount_percentage}%) </b>"

        else:
            html += f"💶 Il prezzo è di: <b>{price_str}" \
            f"{self.currency[1]}</b>"

        html += f"\n\n\n➡️ <a href='{self.url}'>" \
        "<b>Apri su Amazon</b></a>\n\n"

        return html
    
    @classmethod
    def from_product(cls, product: Product, partner_tag: str) -> "Message":
        """Creates a Message instance from a Product instance.

        Args:
            cls: The class itself.
            product (Product): The product object containing information about 
                the product.
            partner_tag (str): The partner tag for affiliate linking.

        Returns:
            Message: A Message instance created from the provided 
                Product instance.

        Example:
            message = Message.from_product(example_product, "example_partner_tag")
        """
        asin = product.asin
        brand = product.brand

        title_tuple = Message.title_generator(product.title, product.brand, 
                                              product.asin)
        title = title_tuple[0]
        
        url = f"https://www.amazon.it/dp/{product.asin}?&tag={partner_tag}"

        marketplace = Message.marketplace_location(product.asin, 
                                                   product.marketplace)
        
        price = Message.process_price(product.asin, product.price)
        currency = Message.process_currency(product.asin, 
                                            product.currency, 
                                            product.old_currency)

        old_price = Message.process_price(product.asin, product.old_price)
        old_currency = Message.process_currency(product.asin, 
                                                product.old_currency, 
                                                product.currency)
        
        discount_percentage = product.discount

        bullet_points = Message.bp_generator(
            product.bullet_points, 
            title_tuple[1],
            product.asin,
            product.brand, 
            discount_percentage)
        
        image_url = Message.image_url_generator(
            product.asin,
            product.image_link,
            product.brand,
            price,
            currency[1],
            old_price,
            old_currency[1],
            discount_percentage)
        
        return cls(asin, brand, title, bullet_points, url, marketplace, price, 
                   currency, old_price, old_currency, discount_percentage, 
                   image_url)
    
    @staticmethod
    def process_price(
        asin: str, 
        price: Union[int, float], 
    ) -> Union[int, float]:
        """Processes the price for a given ASIN.

        Args:
            asin (str): The ASIN of the product.
            price (Union[int, float]): The price of the product.

        Returns:
            Union[int, float]: The processed price.

        Example:
            processed_price = Message.process_price("example_asin", 99.00)
            # Output: 99
        """
        try:
            price = float(price)
            if price.is_integer():
                price = int(price)
        except Exception as e:
            logging.error(f"An error occurred while generating "
                          f"the prices for asin {asin}: {e}")
            return -1
        return price
    
    @staticmethod
    def process_currency(
        asin: str, 
        currency: str, 
        other_currency: str
    ) -> tuple[Union[str, None], Union[str, None]]:
        """Processes the currency for a given ASIN.

        Args:
            asin (str): The ASIN of the product.
            currency (str): The currency of the product.
            other_currency (str): The fallback currency.

        Returns:
            tuple[Union[str, None], Union[str, None]]: A tuple containing 
                the processed currency and its symbol, or None for both 
                if an error occurs.

        Example:
            processed_currency, currency_symbol = Message.process_currency(
                "example_asin", "USD", "USD")
            processed_currency, currency_symbol = Message.process_currency(
                "example_asin", None, "USD")
            # Output: ("USD", "$")
        """
        try:
            if not currency:
                currency = other_currency
            
            currency_symbol = currency_code_to_symbol(currency)

        except Exception as e:
            logging.error(f"An error occurred while generating "
                          f"the currency for asin {asin}: {e}")
            return None
        return currency, currency_symbol
    
    @staticmethod
    def process_discount_percentage(asin: str, discount_percentage: int) -> int:
        """Processes the discount percentage for a given ASIN.

        Args:
            asin (str): The ASIN of the product.
            discount_percentage (int): The discount percentage of the product.

        Returns:
            int: The processed discount percentage.

        Example:
            processed_discount_percentage = 
                Message.process_discount_percentage("example_asin", 20)
            # Output: 20
        """
        try:
            discount_percentage = int(discount_percentage)
        except Exception as e:
            logging.error(f"An error occurred while generating "
                          f"the discount percentage for asin {asin}: {e}")
            return -1
        return discount_percentage
    
    @staticmethod
    def process_discount(
        asin: str, 
        price: Union[int, float], 
        old_price: Union[int, float]
    ) -> Union[int, float]:
        """Processes the discount amount for a given ASIN.

        Args:
            asin (str): The ASIN of the product.
            price (Union[int, float]): The current price of the product.
            old_price (Union[int, float]): The previous price of the product.

        Returns:
            Union[int, float]: The processed discount amount.

        Example:
            processed_discount = 
                Message.process_discount("example_asin", 100.00, 120.00)
            # Output: 20
        """
        try:
            discount = old_price - price
            if (discount % 1) == 0:
                discount = int(discount)
        except Exception as e:
            logging.error(f"An error occurred while generating "
                          f"the discount for asin {asin}: {e}")
            return -1
        return discount

    @staticmethod
    def title_generator(
        title: str, 
        brand: str = "",
        asin: str = ""
    ) -> tuple[str, list[str]]:
        """Generates bullet points from a product title.

        Args:
            title (str): The title of the product.
            brand (str): The brand of the product.
            asin (str): The ASIN of the product.

        Returns:
            tuple[str, list[str]]: A tuple containing the processed 
                product title and a list of bullet points extracted 
                from the title.
        """
        ##
        ## As is mentioned in the readme file, the code in this function can be really
        ## different based on your preference.
        ##
        ## You must personalize this function based on your needs.
        ##
        ## If you don't modify this function it automatically selects a short
        ## sub string as title and return the rest so you can use it for bullet points.
        ##
        ##

        title_list = title.replace("(", "")
        title_list = title_list.replace(")", "")
        title_list = title_list.replace("[", "")
        title_list = title_list.replace("]", "")

        title_list = title_list.split(", ")
        new_title = title_list[0]

        while (len(new_title) < 25) and (len(title_list) > 1):
            new_title = new_title + " - " + title_list[1]
            title_list.pop(1)

        bullets_from_title = title_list[1:]
        return new_title, bullets_from_title
    
    @staticmethod
    def bp_generator(
        description_list: list, 
        from_title: list[str],
        asin: str = "",
        brand: str = "",
        discount_percentage: int = 0
    ) -> list[str]:
        """Generates bullet points for a Message from the residual part of 
            the title and from the description list that is a list of phrase 
            that explain the product.

        Args:
            asin (str): The ASIN of the product.
            description_list (list): A list of product descriptions.
            brand (str): The brand of the product.
            discount_percentage (int): The discount percentage of the product.
            bullets_from_title (list[str]): A list of bullet points extracted 
                from the product title.

        Returns:
            list[str]: A list of generated bullet points.
        """
        ##
        ## As is mentioned in the readme file, the code in this function can be really
        ## different based on your preference.
        ##
        ## You must personalize this function based on your needs.
        ##
        ## If you don't modify this function it automatically selects some
        ## bullet points from the description list and the title list.
        ##
        ##

        MAX_BULLET_POINTS = 3
        returned_list = []

        # Clean and preprocess bullet points
        no_emj_list = []
        for bullet_point in description_list:
            bullet_point = bullet_point.capitalize()

            bullet_point = bullet_point.replace('(', '').replace(')', '')
            bullet_point = bullet_point.replace('[', '').replace(']', '')
            bullet_point = bullet_point.replace(' – ', ' - ')

            no_emoji_text = remove_emj(bullet_point)
            no_emj_list.append(no_emoji_text)

        # Extract relevant bullet points
        tmp_list = []
        for bullet_point in no_emj_list:
            if bullet_point.strip() and 10 < len(bullet_point) < 40:
                tmp_list.append(bullet_point)

            elif len(bullet_point) > 40:
                bullet_point_list = bullet_point.split('. ')

                if len(bullet_point_list[0]) > 40:
                    bullet_point_list = bullet_point.split(', ')

                if len(bullet_point_list[0]) > 40:
                    bullet_point_list = bullet_point.split(';')
                    
                tmp_list.append(bullet_point_list[0])

        # Process and filter bullet points from titles and descriptions
        for txt in tmp_list + from_title:
            brand_c = brand.capitalize()
            txt = txt.strip()

            if txt and txt != brand_c and len(txt) > 10 and len(txt) < 40:
                txt = remove_start_end_space(txt)
                returned_list.append(txt)

        # Additional processing if generated bullet points are insufficient
        if len(returned_list) < 2:

            for i in description_list:
                split_list = i.split(',')
                
                if len(split_list[0]) < 75:
                    returned_list.extend(split_list[0].capitalize())

        # Capitalize and filter final bullet points
        final_list = [i.capitalize() for i in returned_list if len(i) >= 15]

        extra_phrase = add_extra_phrase(asin, brand, discount_percentage)
        
        if extra_phrase is not None:
            final_list.append(extra_phrase)

        return final_list[:MAX_BULLET_POINTS]

    @staticmethod
    def image_url_generator(
        asin: str, 
        url: str, 
        brand: str,
        new_price: float, 
        new_currency: str, 
        old_price: float, 
        old_currency: str, 
        discount_percentage: int
    ) -> str:
        """Generates an a more pretty image of the product for a better 
            background and some price information. When the image it's 
            generated it upload the image on a cloud website and return
            the link of the image.

        Args:
            asin (str): The ASIN of the product.
            url (str): The URL of the product image.
            brand (str): The brand of the product.
            new_price (float): The current price of the product.
            new_currency (str): The currency of the current price.
            old_price (float): The previous price of the product.
            old_currency (str): The currency of the previous price.
            discount_percentage (int): The discount percentage of the product.

        Returns:
            str: The URL of the generated image.

        Example:
            image_url = Message.image_url_generator("AW21ZX34QD", 
                "https://example.com/image.jpg", "Example Brand", 
                20.00, "USD", 25.00, "USD", 20)
            # Output: "https://example.com/generated_image.jpg"
        Note:
            # TODO: Add exception
        """
        image_gen.original_img_download(asin, url)

        if (discount_percentage != 0) and (discount_percentage > 55):
            backg_img = 3
        else:
            backg_img = 2

        image_gen.gen_img(asin, new_price, new_currency, old_price, 
                          old_currency, discount_percentage, backg_img)  

        new_img_upload_response = image_gen.upload_img(asin, url)
        if new_img_upload_response[0] != 200:
            new_img_upload_response = image_gen.upload_img(asin, url)
            
        os.remove(f"archive/tmp/{asin}.jpg")
        os.remove(f"archive/img/{asin}-1.jpg")
        return new_img_upload_response[1]

    @staticmethod
    def marketplace_emoji(marketplace_flag: str) -> str:
        """Generates an emoji representation for a marketplace.

        Args:
            marketplace_flag (str): The flag representing the marketplace.

        Returns:
            str: An emoji representation of the marketplace.

        Example:
            emoji_representation = Message.marketplace_emoji("🇺🇸")
            # Output: "🛒 Amazon <b>🇺🇸</b>"
        """
        emj_marketplace = random.choice(["🛒", "🚚", "📦"])
        if marketplace_flag is None:
            return f"\n{emj_marketplace} Amazon\n"
        return  f"\n{emj_marketplace} Amazon <b>{marketplace_flag}</b>\n"

    @staticmethod
    def marketplace_location(
        asin: str,
        marketplace: str
    ) -> tuple[Union[str, None], Union[str, None]]:
        """Extracts the country flag for a given marketplace.

        Args:
            asin (str): The ASIN of the product.
            marketplace (str): The name of the marketplace EX: 'en:US'.

        Returns:
            tuple[Union[str, None], Union[str, None]]: A tuple containing the 
                country name and its flag emoji if available, or None for 
                both if an error occurs.

        Example:
            country, country_flag = 
            Message.marketplace_location("example_asin", "en:US")
            # Output: ("US", "🇺🇸")
        """
        try:
            country = extract_capitalized_letters(marketplace)
            country_flag = flag.flag(country)

        except Exception as e:
            logging.error(f"Error occurred when extracting"
                        f" the country flag for asin: {asin}: {e}")
            return None, None
        
        return country, country_flag

    @staticmethod
    def coupon_generator():
        """
        # 🎟 emoji to use in the future for coupons
        """
        pass

def remove_start_end_space(phrase: str) -> str:
    """Removes leading and trailing spaces from a string.

    Args:
        phrase (str): The input string.

    Returns:
        str: The input string with leading and trailing spaces removed.

    Example:
        cleaned_phrase = remove_start_end_space("  Example Phrase  ")
        # Output: "Example Phrase"
    """
    if phrase[0] == ' ': phrase = phrase[1:]
    if phrase[-1] == ' ': phrase = phrase[:-1]
    return phrase

def extract_capitalized_letters(text: str) -> Union[str, None]:
    """Extracts capitalized letters from a string.

    Args:
        text (str): The input string.

    Returns:
        Union[str, None]: The extracted capitalized letters, or 
            None if no match is found.

    Example:
        extracted_letters = 
            extract_capitalized_letters("some_text_WITH_CAPITALS")
        # Output: "WITH"
    """
    match = re.search(r'(?<=_)[A-Z]+', text)

    if match:
        # Extract and return the found letters
        return match.group(0)
    else:
        return None

def remove_emj(text: str) -> str:
    """Removes emojis from a given text.

    Args:
        text (str): The input text containing emojis.

    Returns:
        str: The input text with emojis removed.

    Example:
        cleaned_text = remove_emj("Hello 😀 World 🌍")
        # Output: "Hello  World "
    """
    emoji_pattern = re.compile("["
                               # emoticons
                               u"\U0001F600-\U0001F64F"
                               # symbols & pictographs
                               u"\U0001F300-\U0001F5FF"
                               # transport & map symbols
                               u"\U0001F680-\U0001F6FF"
                               # flags (iOS)
                               u"\U0001F1E0-\U0001F1FF"
                               # chinese char
                               u"\U00002500-\U00002BEF"
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642" 
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               # dingbats
                               u"\ufe0f"
                               u"\u3030"
                               # Custom characters
                               "¹²³⁴⁵⁶⁷⁸⁹⁰"
                               "]+",
                               flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)

def currency_code_to_symbol(currency_code: str) -> str:
    """Converts a currency code to its corresponding symbol.

    Args:
        currency_code (str): The currency code to convert.

    Returns:
        str: The symbol corresponding to the currency code, or 
            the original currency code if no symbol is found.
    Note:
        Supported country by Amazon are: 'AU': 'A$','BE': '€','BR': 'R$',
            'CA': 'CA$','FR': '€','DE': '€','IN': '₹','IT': '€','JP': '¥',
            'MX': 'MX$','NL': '€','PL': 'zł','SG': 'S$','SA': '﷼','ES': '€',
            'SE': 'kr','TR': '₺','AE': 'د.إ','UK': '£','US': '$'
    """
    symbols = {
        'AUD': 'A$',
        'BRL': 'R$',
        'CAD': 'CA$',
        'EGP': 'E£',
        'EUR': '€',
        'GBP': '£',
        'INR': '₹',
        'JPY': '¥',
        'MXN': 'MX$',
        'PLN': 'zł',
        'SGD': 'S$',
        'SAR': '﷼',
        'SEK': 'kr',
        'TRY': '₺',
        'AED': 'د.إ',
        'USD': '$'
        # Add more currency code to symbol mappings as needed
        }
    return symbols.get(currency_code, currency_code)

def add_extra_phrase(
        asin: str, 
        brand: str, 
        discount_percentage: int
    ) -> Union[str, None]:
    """
    """
    if discount_percentage is None:
        return None

    mix_list = mix_phrase_list.copy()

    try: 
        if discount_percentage > 65:
            mix_list.extend(discount_65_more)

        elif discount_percentage > 35:
            mix_list.extend(discount_35_more)

        gen_bullet = random.choice(mix_list)

        if "*BRAND*" in gen_bullet:
            gen_bullet = gen_bullet.replace("*BRAND*", brand)
            
        if "*PERCENTAGE*" in gen_bullet:
            str_discount_percentage = str(discount_percentage)
            gen_bullet = gen_bullet.replace("*PERCENTAGE*", 
                                            str_discount_percentage)
    
    except Exception as e:
        logging.error(f"An error occurred while generating the extra phrase "
                      f"for the product with asin {asin}: {e}")
        return None
    
    return gen_bullet