# Parameters Setup
The first step is to rename the file `settings_template.py` into `settings.py`. Then insert in the file all the required keys.
The required paramenters are:

These are some of the parameters that you can set to customize the bot.


### 1) Working Hours
The minimum and maximum hour in which the bot can send messages. The bot will not send messages outside of these hours.

```python
MIN_HOUR = 8
MIN_MINUTE = 00

MAX_HOUR = 22
MAX_MINUTE = 30
```

### 2) The Country
The country in which you want to search for products. For example, if you want to search for products in Italy, you should set the COUNTRY variable to "IT". (Used also for detect the holidays in the country and not send messages on that days.)
```python
COUNTRY = "IT"
```

### 3) The Maximum Number of Pages to inspect and the Number of Items for each Request
Here you define the maximum number of pages to inspect and the number of items for each request. The maximum number of pages determines how many pages to inspect at each call for a specific keyword. The Item count determines how many product extract from each page.
```python
# Number of pages to scrape
MAX_PAGE = 3

# N of item for request call (max 10)
ITEM_COUNT = 8
```

### 4) The Maximum Days to Check
Is the maximum number of days in the past to check to see if we have already send this product. For example if today we send a message on the channel for the iPhone 12 Pro we want to avoid to send the same message for the same product tomorrow so we use this parameter to check in if we have already send the product in the last 3 days.
```python
MAX_DAYS_TO_CHECK = 3
```

### 5) The Web port
Whe the bot start it open a connection on the `localhost:8000` To let you now that the bot is running. You can change the port if you want.
```python
PORT = 8000
```

### 6) Example of the settings.py file
Here you can find an example of the `settings.py` file:
```python
# Time
MIN_HOUR = 8
MIN_MINUTE = 00

MAX_HOUR = 22
MAX_MINUTE = 30

# Country
COUNTRY = "IT"

# Number of pages to scrape
MAX_PAGE = 3

# N of item for request call (max 10)
ITEM_COUNT = 8

# Max number of days to check for resend
MAX_DAYS_TO_CHECK = 3

# Server port number
PORT = 8000

#################################### DEBUG ####################################
# 0 = Shoert list, 1 = Full random list
SUBSET_MODE = 1
```