from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#this is used to press keys such as enter after filling web form
from selenium.webdriver.common.keys import Keys
from time import sleep


CHROME_DRIVER_PATH: "" #Enter the file path for your chrome driver
EMAIL = "" #Enter your facebook email.
PASSWORD = "" #Enter your facebook password.

#setting up basic selenium
chrome_driver_path = CHROME_DRIVER_PATH
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/")


sleep(2)
#clicking log in
login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()


#clicking on facebook login window
sleep(2)
fb_login = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login.click()


#switching to fb login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

#filling the facebook login form
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(EMAIL)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
sleep(5)

#switching back to tinder window
driver.switch_to.window(base_window)


#allowing the location
try:
    allow_location = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
    allow_location.click()
    sleep(2)
except:
    pass



#aceepting the alert
try:
    driver.switch_to.alert.accept()
except:
    pass



#disallowing the notifications
try:
    allow_notifications = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
    allow_notifications.click()
    sleep(2)
except:
    pass

#accepting cookies
try:
    allow_cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
    allow_cookies.click()
    sleep(2)
except:
    pass


#not allowing the dark mode
try:
    dark_mode = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button')
    dark_mode.click()
    sleep(2)
except:
    pass


#dismissing other requests
try:
    likes = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[3]/button[1]')
    likes.click()
    sleep(2)
except:
    pass


try:
    likes = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/button')
    likes.click()
    sleep(2)
except:
    pass


have_likes = True
#start liking
while(have_likes):
    try:
        like_button = driver.find_element(By.CSS_SELECTOR, 'body')
        like_button.send_keys(Keys.RIGHT)
        sleep(2)
    except NoSuchElementException:
        sleep(3)


    try:
        driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[2]/button[2]').click()
        sleep(1)
    except:
        pass


    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[3]/button[2]').click()
        have_likes = False
    except:
        pass
    else:
        print("You've reached the end of your daily likes!") 
