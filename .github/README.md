<!--TelegramBot-AmazonOffers-->
<!--TelegramBot AmazonOffers-->
<!--Jan 2024-->

<div id="top"></div>
<br/>
<br/>


<p align="center">
  <img src="logo.png" width="180" height=auto>
</p>
<h1 align="center">
    <a href="https://github.com/Piero24/TelegramBot-AmazonOffers">TelegramBot AmazonOffers</a>
</h1>
<p align="center">
    <!-- BADGE -->
    <!--
        *** You can make other badges here
        *** [shields.io](https://shields.io/)
        *** or here
        *** [CircleCI](https://circleci.com/)
    -->
    <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/commits/master">
    <img src="https://img.shields.io/github/last-commit/piero24/TelegramBot-AmazonOffers">
    </a>
    <a href="https://github.com/Piero24/TelegramBot-AmazonOffers">
    <img src="https://img.shields.io/badge/Maintained-yes-green.svg">
    </a>
    <!--<a href="https://github.com/Piero24/TelegramBot-AmazonOffers">
    <img src="https://img.shields.io/badge/Maintained%3F-no-red.svg">
    </a> -->
    <a href="https://github.com/Piero24/twitch-stream-viewer/issues">
    <img src="https://img.shields.io/github/issues/piero24/TelegramBot-AmazonOffers">
    </a>
    <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/piero24/TelegramBot-AmazonOffers">
    </a>
</p>
<p align="center">
    A Telegram bot that send offers from Amazon.
    <br/>
    <!-- <a href="documentation.md"><strong>Explore the docs »</strong></a>
    <br/> -->
    <br/>
    <a href="https://linktr.ee/webofferte">View Demo</a>
    •
    <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/issues">Report Bug</a>
    •
    <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/issues">Request Feature</a>
</p>


---

> [!NOTE]  
> The images in this readme are the result of further customization of this bot. In fact, as explained below, it is possible to customize various aspects of the product such as the image or title but this depends a lot on the result you want to obtain. For example, to personalize images, the use of an image storage system is required. However, the default version is more than sufficient to use the bot fully.

> [!IMPORTANT]  
> Your support is essential for the success of this project. If you find it valuable, please consider showing your appreciation by starring ⭐️ the project on GitHub ↗️. Thank you!


<br/><br/>
<h2 id="introduction">📔  Introduction</h2>
<p>
    This bot is designed to send offers from Amazon to a Telegram channel. By providing different keywords, the bot will search for the best offers and return a series of products with the relative information. Then the information are parsed for extract only relevant information like:
    <ul>
        <li>Title</li>
        <li>Bullet Points</li>
        <li>Current Price</li>
        <li>Original Price</li>
        <li>Image</li>
    </ul>
    By using some basic algorithm the bot will select the best offers and send them to the channel. The diffent parameters are hihgly customizable and can be changed by the user. For Exaple you can change the number of products to send and when send it. The quantity of product to require through the <a href="https://programma-affiliazione.amazon.it/assoc_credentials/home"><strong>Amazon Product Advertising API (PAAPI)</strong></a> and the working time. Also the image sended to the channel as a preview of the product can be changed.
</p>
<br/>
<img src="cover.png">
<br/>
<br/>
<p>
    The bot provide also a web page that show if the bot is still online and that provide a direct link to al the channels connected to the bot. You can find the web page <a href="https://localhost:8000"><strong>localhost:8000</strong></a> By default.
</p>
<p>
    The background image of the product instead is highly costumazible. Also the font and the color of the text can be changed.
</p>
<br/>
<table>
  <tr  align="center">
    <th><strong>Web Page</strong></th>
    <th><strong>Personalized image example</strong></th> 
  </tr>
  <tr  align="center">
    <th><img src="Localhost.png" alt="Web Page"></th>
    <th><img src="example_img.jpeg" alt="Example Image"></th> 
  </tr>
</table>
<br/>
<br/>

> [!IMPORTANT]  
> 1. Since I haven't an account from another country I didn't test the bot in the different regions like UK, US, ESP, FR and so on. So I can't guarantee the bot will work in all the regions. But You can fix the problem in a couple of steps. Or you can report the problem here: [**Report Bug**](https://github.com/Piero24/TelegramBot-AmazonOffers/issues) And I will fix it as soon as I wind an API Key for the tests.
> 2. No responsibility is assumed for the use of the bot and the data it provides. The use of it at your own risk. To check the Amazon regulation about the PAAPI see the [PAAPI Documentation](https://webservices.amazon.com/paapi5/documentation/best-programming-practices.html) section.
> 3. To use this bot you need to have an Amazon account and an API key. You can require your API key [here](https://programma-affiliazione.amazon.it/home).
> 4. The storage of any information returned by the PAAPI is **NOT PERMITTED**. To this reason it's difficult to know the difference between price of a product already send and the same product in the queue or other comparison. As mentioned here basically all the information returned by the PAAPI must be cancelled in a couple of hours (see [here](https://webservices.amazon.com/paapi5/documentation/best-programming-practices.html#how-to-cache) for more information). But the only data that is not mentioned so can assume it is possible to store is the product ASIN. This is used **ONLY** for preventing to send the same product more times in a certain period.
> 5. If you want to support the project subscribe to one of the channel at this link: [WebOfferte](https://linktr.ee/webofferte)


<h2 id="made-in"><br/>🛠  Built in</h2>
<p>
    This project is entirely written in <strong>Python</strong> and uses the <strong>Amazon Product Advertising API</strong> for the search of the products and the <strong>Telegram API</strong> to send the message. It use <strong>SQLite</strong> only for the part of the ASIN storage. There is also a part written in <strong>html</strong> and <strong>css</strong> for a web page to advice if the bot is still online and that provide a direct link to al the channels connected to the bot.
</p>
<br/>
<p align="center">
    <a href="https://www.python.org">Python</a> • <a href="https://www.sqlite.org">SQLite</a> • <a href="">HTML</a> • <a href="">CSS</a> • <a href="https://getbootstrap.com">BootStrap</a> • <a href="https://webservices.amazon.com/paapi5">Amazon PAAPI</a> • <a href="https://github.com/eternnoir/pyTelegramBotAPI">Telegram API</a>
</p>

<p align="right"><a href="#top">⇧</a></p>

<h2 id="index"><br/>📋  Index</h2>
<ul>
    <!-- <li><h4><a href="#documentation">Documentation</a></h4></li> -->
    <li><h4><a href="#prerequisites">Prerequisites</a></h4></li>
    <li><h4><a href="#how-to-start">How to Start</a></h4></li>
    <li><h4><a href="#responsible-disclosure">Responsible Disclosure</a></h4></li>
    <li><h4><a href="#report-a-bug">Report a Bug</a></h4></li>
    <li><h4><a href="#license">License</a></h4></li>
    <li><h4><a href="#third-party-licenses">Third Party Licenses</a></h4></li>
</ul>

<p align="right"><a href="#top">⇧</a></p>

<!-- <h2 id="documentation"><br/><br/>📚  Documentation</h2>
<p>
    Here you can find a more detailed documentation about the project. The documentation is divided into different sections to make it easier to find the information you need.
</p>
<p>
    For a broader view it is better to refer the user to the documentation via links: <a href="https://github.com/Piero24/.github/documentation.md">Documentation »</a>
</p>


<p align="right"><a href="#top">⇧</a></p> -->

<h2 id="prerequisites"><br/>🧰  Prerequisites</h2>
There is two way to run the project:

1. With <a href="https://www.docker.com">Docker</a>
2. With the classic environment 

If you want to use Docker you can skip this part and go to the next section. For the classic installation instead you need to install the required package. Start by creating the enviroment `env`.
```sh
    python3 -m venv env
```
You can Install all the requirement in one shot by using the following command:

```sh
    pip install -r requirements.txt
```
Alternatively you can install it one by one the package in the requirements.txt file.

<p align="right"><a href="#top">⇧</a></p>


<h2 id="how-to-start"><br/>⚙️  How to Start</h2>
<p>
    Now we must set up the bot. There are different steps to follow to set up the bot. The steps must be followed in both cases, whether you are using Docker or the classic environment.
</p>

1. Clone the repo
  
    ```sh
    git clone https://github.com/Piero24/TelegramBot-AmazonOffers.git
    ```

2. Setup the `api_Keys.py` file with all the required from Amazon and Telegram.
    You can find an example <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/blob/main/.github/api_Keys_Setup.md">here</a>.

3. Setup the `settings.py` file with all the required for running the bot.
    You can find an example <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/blob/main/.github/settings.md">here</a>.

4. Setup the `category_keywords.py` file with the categories and the keywords for the search. More information <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/blob/main/.github/categories_list.md">here</a>.

5. <strong>Facultative</strong>: There are many other parameters that can be changed. <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/blob/main/.github/other_parameters.md">Here</a> you can find more information about what you can do and where you can find it.

<br/>
<h4 align="center">
     ⚠️ ATTENTION ⚠️ 
</h4>
<p align="center">
    Read the point 5 for more information for the personalized image.
</p>
<br/>

<p>
    At this moment all the parameters are set and the bot is ready to run. And the operations are different depending on whether you are using Docker or the classic environment. 
</p>
<h3 id="how-to-start">
    <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/97_Docker_logo_logos-512.png" width="30" height="30" align="center"> Docker
</h3>
<p>
    Whit docker it's very easy to run the bot. You can run the bot with the following command:
</p>

1. Open docker on your system (different for any platform) and run the following command via ssh or terminal:
  
    ```sh
    docker build -t REPO-NAME .
    ```
    Where `REPO-NAME` is the name of the repository. For example `amazon-offers-bot`. (Remember the dot at the end of the command).

2. Run the bot with the following command:

    ```sh
    docker run -p 8000:8000 REPO-NAME
    ```
    Where `REPO-NAME` is the name of the repository. For example `amazon-offers-bot`. 

<h3 id="how-to-start">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="30" height="30" align="center"> Python Environment
</h3>

1. Open the terminal and go to the directory `TelegramBot-AmazonOffers` downloaded from the repository.

2. Run the bot with the following command:

    ```sh
    python main.py
    ```

For any problem you can check the log file in the `log` folder.

<p align="right"><a href="#top">⇧</a></p>

---

<h3 id="responsible-disclosure"><br/>📮  Responsible Disclosure</h3>
<p>
    We assume no responsibility for an improper use of this code and everything related to it. We do not assume any responsibility for damage caused to people and / or objects in the use of the code.
</p>
<strong>
    By using this code even in a small part, the developers are declined from any responsibility.
</strong>
<br/>
<br/>
<p>
    It is possible to have more information by viewing the following links: 
    <a href="#code-of-conduct"><strong>Code of conduct</strong></a>
     • 
    <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/blob/main/LICENSE"><strong>License</strong></a>
</p>

<p align="right"><a href="#top">⇧</a></p>


<h3 id="report-a-bug"><br/>🐛  Bug and Feature</h3>
<p>
    To <strong>report a bug</strong> or to request the implementation of <strong>new features</strong>, it is strongly recommended to use the <a href="https://github.com/Piero24/TelegramBot-AmazonOffers/issues"><strong>ISSUES tool from Github »</strong></a>
</p>
<br/>
<p>
    Here you may already find the answer to the problem you have encountered, in case it has already happened to other people. Otherwise you can report the bugs found.
</p>
<br/>
<strong>
    ATTENTION: To speed up the resolution of problems, it is recommended to answer all the questions present in the request phase in an exhaustive manner.
</strong>
<br/>
<br/>
<p>
    (Even in the phase of requests for the implementation of new functions, we ask you to better specify the reasons for the request and what final result you want to obtain).
</p>
<br/>

<p align="right"><a href="#top">⇧</a></p>
  
 --- 

<h2 id="license"><br/>🔍  License</h2>
<strong>APACHE LICENSE</strong>
<br/>
<i>Version 2.0, Jan 2004</i>
<br/>
<br/>
<i>"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.
<br/>
<br/>
"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License... </i>
<br/>
<a href="https://github.com/Piero24/TelegramBot-AmazonOffers/blob/main/LICENSE"><strong>License Documentation »</strong></a>
<br/>
<br/>


<h3 id="third-party-licenses"><br/>📌  Third Party Licenses</h3>

In the event that the software uses third-party components for its operation, 
<br/>
the individual licenses are indicated in the following section.
<br/>
<br/>
<strong>Software list:</strong>
<br/>
<table>
  <tr  align="center">
    <th>Software</th>
    <th>License owner</th> 
    <th>License type</th> 
    <th>Link</th>
  </tr>
  <tr  align="center">
    <td>pyTelegramBotAPI</td>
    <td>eternnoir</td> 
    <td>GPL-2.0 license</td>
    <td><a href="https://github.com/eternnoir/pyTelegramBotAPI">here</a></td>
  </tr>
  <tr  align="center">
    <td>flag</td>
    <td>cvzi</td> 
    <td>MIT License</td>
    <td><a href="https://github.com/cvzi/flag?tab=MIT-1-ov-file">here</a></td>
  </tr>
  <tr  align="center">
    <td>python-holidays</td>
    <td>vacanza</td> 
    <td>MIT License</td>
    <td><a href="https://github.com/vacanza/python-holidays/">here</a></td>
  </tr>
</table>

<p align="right"><a href="#top">⇧</a></p>


---
> *<p align="center"> Copyrright (C) by Pietrobon Andrea <br/> Released date: Jan 2024*
