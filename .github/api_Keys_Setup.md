# Secret Keys Setup

The first step is to rename the file `api_keys_template.py` into `api_keys.py`. Then insert in the file all the required keys.
The required paramenters are:

### 1) The PAAPI Credentials
You can generate your own here: <a href="https://programma-affiliazione.amazon.it/assoc_credentials/home">Amazon PAAPI</a>

```python
ACCESS_KEY = "AMAZON ACCESS KEY"

SECRET_KEY = "AMAZON SECRET KEY"
```

### 2) The partner tag and the sub partner tag

```python
PARTNER_TAG = "PARTNER TAG"

SUB_PARTNER_TAG = "SUB PARTNER TAG (OPTIONAL)"
```

### 3) The Host and the Region
PAAPI host and region to which you want to send request. For more details: <a href="https://webservices.amazon.com/paapi5/documentation/common-request-parameters.html#host-and-region">Amazon Regions</a>
```python
HOST = "HOST"

REGION = "REGION"
```

### 4) The Saving Percentage and Value
To avoid that the paapi call return product with no discount you must put the percentage of minimum discount you want here (0 for product with and without discount). The `MIN_SAVING_VALUE` instead is for prevent to send product that have a discount with an hight pergentage but a low value in currency. If you want to disable it put -1.

For example you can have a product with a value of 10$ and with a discount of 10 so it could be send. But this implies tha on the channel you receive a message for a product that pass from 10$ to 9$ and this is not a good thing. So you can set the MIN_SAVING_VALUE to a value like 5$ or more to prevent this.

<h3 align="center">
     ⚠️ WARNING ⚠️ 
</h3>
<p align="center">
    After numerous tests I discovered that using this parameter the bees do not work correctly as they do not return all the products. For example, using this parameter with the keyword `iPhone` only returned some models among the discounted ones. And for example the iPhone 15 models (the most recent ones at the time of this publication) even if they had a considerable discount were not returned. For this reason I have inserted an additional function that randomly disables this function. So you don't miss out on relevant offers. However, it is possible to customize or deactivate this function simply to make the bot operate as you wish.
    <br/><br/>I recommend testing the possible results on the Amazon scratchpad first.
</p>

```python
# MIN_SAVING_PERCENT:
MIN_SAVING_PERCENT = 5
# MIN_SAVING_VAUE (-1 to disable):
MIN_SAVING_VALUE = 5
```

### 5) The Telegram Bot Credentials
```python
TELEGRAM_TOKEN = "TELEGRAM TOKEN FROM BOT FHATER"

CHANNEL_ID = -0000000000000
```

### 6) Example of the secretKeys.py file
Here you can find an example of the `api_keys.py` file:
```python
# ACCESS_KEY:
ACCESS_KEY = "GHIJKLMNOPQRSTUVWXY012"
# SECRET_KEY:
SECRET_KEY = "LMNOPQRSTUVWXYZ1234567890-AbCdEfGhIjKlMnOpQr"
# PARTNER_TAG:
PARTNER_TAG = "example-21"
# SUB_PARTNER_TAG:
SUB_PARTNER_TAG = "sub-example--21"
# PAAPI host and region to which you want to send request
# For more details: 
# https://webservices.amazon.com/paapi5/documentation/common-request-parameters.html#host-and-region
# HOST:
HOST = "webservices.amazon.it"
# REGION:
REGION = "eu-west-1"

# MIN_SAVING_PERCENT:
MIN_SAVING_PERCENT = 15
# MIN_SAVING_VAUE (-1 to disable):
MIN_SAVING_VALUE = 3

### TELEGRAM BOT CREDENTIALS ###
TELEGRAM_TOKEN = "1576349202:ABCDE12fGhIjKlmnopA123456789-AbCdEfGhIjKlMnOpQr"
# Channel ID
CHANNEL_ID = -0000000000000

```