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
import requests

# External libraries
from PIL import Image, ImageDraw, ImageFont

# Importing internal modules
from utils.log_manager import setup_logger

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

def original_img_download(asin: str, url: str) -> None:
    """Download an image from a URL and save it as '{asin}.jpg'.

    Args:
        asin (str): The ASIN of the product.
        url (str): The URL of the image to download.
    """
    with open(f'archive/tmp/{asin}.jpg', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            logger.warning(f'Error downloading image for ASIN {asin}.')

        for block in response.iter_content(1024):
            if not block: break
            handle.write(block)

def gen_img(
        asin: str, 
        price: float, 
        currency: str, 
        old_price: float, 
        old_currency: str, 
        discount: int,
        img_number: int
    ) -> None:
    """Generates an image with product details overlaid 
        on a background template.

    Args:
        asin (str): The ASIN of the product.
        price (float): The current price of the product.
        currency (str): The currency of the price.
        old_price (float): The previous price of the product, if available.
        old_currency (str): The currency of the previous price.
        discount (int): The discount percentage, if available.
        img_number (int): The number identifying the background template image.
    """
    new_price = format(price, '.2f').replace('.', ',')
    old_price = format(old_price, '.2f').replace('.', ',')

    # Open the product image
    im1 = Image.open(f'archive/tmp/{asin}.jpg')

    # Take the size of the image
    width, height = im1.size

    # Calculate the scaling factor based on the desired 
    # increase in width or height
    if width < 315 and height > 490:
        scale_factor = 110

    elif width < 360 and height > 490:
        scale_factor = 140

    elif width < 450 and height > 490:
        scale_factor = 140

    elif width > 490 and height < 495:
        scale_factor = 150

    else: 
        scale_factor = 200

    aspect_ratio = width / height
    new_width = width + scale_factor
    new_height = int(new_width / aspect_ratio)

    # Resize the image maintaining the aspect ratio
    im1_resized = im1.resize((new_width, new_height), Image.ANTIALIAS)

    # Apre l'immagine di background
    im3 = Image.open(f'src/media/template/backg-{img_number}.jpg')
    # Open the background image
    back_im = im3.copy()

    # Paste the resized product image over the copy of the background image
    # Past position is almost central (x axis, y axis)
    back_im.paste(im1_resized, (int((im3.size[0] - new_width) / 2), 
                                int((im3.size[1] - new_height) / 2) - 20))
    
    font_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                             'media', 
                             'font', 
                             'Poppins', 
                             'Poppins-Bold.ttf')

    #! Windows compatibility Fix as soon as possible
    import platform
    # Check if the platform is Windows
    if platform.system() == "Windows":
        font_path = "src/media/font/Poppins/Poppins-Bold.ttf"
        currency = "E"
        old_currency = "E"

    # Attempt to draw text sizes
    w1, h1 = draw.textsize(f"{old_price}{old_currency}", font=font1)
    w2, h2 = draw.textsize(f"{new_price}{currency}", font=font2)

    # Choose the font and size for the 2 texts
    font1 = ImageFont.truetype(font_path, 70)
    font2 = ImageFont.truetype(font_path, 180)
    
    # For drawings and writing on pictures
    draw = ImageDraw.Draw(back_im)
    # Get the size of the writings to be inserted in the files
    w1, h1 = draw.textsize(f"{old_price}{old_currency}", font=font1)
    w2, h2 = draw.textsize(f"{new_price}{currency}", font=font2)

    if old_price is not None:

        # Write the old price with the relative font in the image and the slash
        wh_2, ht_2 = int((im3.size[0] - w1) / 2), int((im3.size[1] - h1) / 2)
        draw.text((wh_2, ht_2 + 365), 
                  text=f"{old_price}{old_currency}", 
                  fill=(50, 50, 50), 
                  font=font1)
        
        draw.line((wh_2 - (w1/14), ht_2 + 365 + ((h1+6)/2), 
                   wh_2 + w1 + (w1/14), 
                   ht_2 + 365 + (h1+6)/2), 
                   fill=(255, 56, 101), 
                   width=13)

        # Write the new price with the relative font in the image
        wh_3, ht_3 = int((im3.size[0] - w2) / 2), int((im3.size[1] - h2) / 2)
        draw.text((wh_3, ht_3 + 480), 
                  text=f"{new_price}{currency}", 
                  fill=(50, 50, 50), 
                  font=font2)

    else:

        # Write the new price with the relative font in the image
        wh_2, ht_2 = int((im3.size[0] - w2) / 2), int((im3.size[1] - h2) / 2)
        draw.text((wh_2, ht_2 + 440), 
                  text=f"{new_price}{currency}", 
                  fill=(50, 50, 50), 
                  font=font2)

    # Save the new image asin-1.jpg
    back_im.save(f'archive/img/{asin}-1.jpg', quality=95)

def upload_img(asin: str, original_img_url: str, storage_key: str = "") -> list:
    """Uploads an image to the website for the storage and 
        returns the link for viewing.

    Args:
        asin (str): The ASIN of the product.
        original_img_url (str): The URL of the original image.
        storage_key (str): The storage key required for image upload.

    Returns:
        list: Containing the status code and the URL of the uploaded image.
    """
    
    ##
    ## As is mentioned in the readme file, the code in this function can be really
    ## different based on which is your "storage provider".
    ##
    ## You must personalize this function based on your needs For upload the
    ## personalized image.
    ##
    ## If you don't modify this function it automatically use the original url
    ## provided by the Amazon API.
    ##
    ##
    ##
    ##
    return [200, original_img_url]

