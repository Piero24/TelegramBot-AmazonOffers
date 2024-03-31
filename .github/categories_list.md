# Categories list for the search
There are three categories for the search. Every category have a different priority in the search. The bot will search for products in the first category first and more frequently. The second category will be searched less frequently and so on.

You can find more information on the category name that you can use in your country at this page: [Amazon locale reference](https://webservices.amazon.com/paapi5/documentation/locale-reference.html#topics).

**NOTE:** The categories mast be written in english and must be taken only from the Amazon locale reference page. The keywords istead can be written in your language like if you are searching it from the Amazon website.

## Category 1
The category that have hightest priority in the search. The bot will search for products in this category first and more frequently. Put inside it less keyword respect to the others categories.

```python
categories_1 = {
    "Electronics": [
        "Televisions",
        "OLED TVs",
        "Smartphones",
        "Smartwatches",
        "Headphones",
        "Tablets",
    ],
    "Computers": [
        "Laptops",
        "Gaming Monitors",
    ],
    "Lighting": [],
    "Software": [],
    "VideoGames": [
        "PlayStation 5",
        "Xbox Series X",
    ],
}
```
## Category 2
The category that have medium priority in the search.
```python
categories_2 = {
    "Electronics": [
        "Portable Power Banks",
        "Smartphones",
        "Keyboards",
        "Keyboard and Mouse Sets",
        "In-ear Headphones",
        "Over-ear Headphones",
    ],
    "Computers": [
        "Desktop Computers",
        "Laptops",
        "Personal Computers",
    ],
    "Lighting": [],
    "Software": [],
    "VideoGames": [
        "PlayStation",
        "Xbox",
        "Nintendo",
    ],
}
```
## Category 3
The category that have less priority in the search.
```python
categories_3 = {
    "Electronics": [
        "Screen Protectors",
        "Chargers",
        "Cover Sets and Accessories",
        "External Microphones",
        "PC Speakers",
        "Microphones for PC",
        "Printers",
        "Batteries, Chargers, and Accessories",
        "Ring Lights",
        "Tripods",
        "Microphones",
    ],
    "Computers": [
        "CPU Fans",
        "Case Fans",
        "Processors",
    ],
    "Lighting": [
        "Wi-Fi Bulbs",
        "RGB Lamp",
    ],
    "Software": [
        "Antivirus and Security Software",
    ],
    "VideoGames": [
        "Controllers",
    ],
}
```