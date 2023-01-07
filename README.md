# Tinder-Swiping-Bot

Technologies/Concepts Used: Python, Selenium, Web Automation

1. A Python automated bot that swipes tinder profiles for the user at just a click of the button.
2. Upon execution, the program logs into the tinder profile of the user and begins swiping the profiles.
3. Selenium is used to automate the entire process.
4. Exception handling has been used throughout the program in order to handle different website pop-ups during the execution of the program.

Requirements:
1. This program is designed to run in Google Chrome.
2. User needs to install chrome driver which can be downloaded from the following link:
https://chromedriver.chromium.org/downloads
3. Tinder account should be created using facebook. This facilitates the process of authentication, since then the user's facebook account is used to log into tinder.

In order to run the program, make following changes to the main.py:

1. Variable **CHROME_DRIVER_PATH**: "" #Enter the file path for your chrome driver
2. Variable **EMAIL** = "" #Enter your facebook email.
2. Variable **PASSWORD** = "" #Enter your facebook password.
