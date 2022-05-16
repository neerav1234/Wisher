from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
 
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome("chromedriver.exe")
print("initiated test browser")

browser.get("https://www.facebook.com/")
print("opened facebook.com")

username = "9001388975"

with open('.env', 'r') as source:
    password = source.read().replace('\n', '')

print("Entering")

usrnm = browser.find_element(by=By.XPATH, value="//input[@id='email']")
usrnm.send_keys(username)
print("Username Entered")

pw = browser.find_element(by=By.XPATH, value="//input[@id='pass']")
pw.send_keys(password)
print("Password Entered")

login = browser.find_element(by=By.XPATH, value="//button[@name='login']")
login.click()
print("Logged in")

time.sleep(1)
# try:
#     alert = browser.switch_to_alert()
#     alert.accept()
#     print("alert accepted")
# except:
#     print("no alert")
    
browser.get('https://www.facebook.com/events/birthdays/')

time.sleep(1)
# try:
#     alert = browser.switch_to_alert()
#     alert.accept()
#     print("alert accepted")
# except:
#     print("no alert")
    
print("Hey! Just There")

bdaylist = browser.find_elements(by=By.XPATH, value="//*[@class='_1mf _1mj']")
time.sleep(1)
print("got bdaylist")
print(str(bdaylist))

cnt = 0
feed = "Happy Birthday!!"
for bday in bdaylist:

        cnt += 1
        time.sleep(1)
        element_id = str(bday.get_attribute('data-offset-key'))
        print(element_id)
        XPATH = '//*[@data-offset-key ="' + element_id + '"]'
        post_field = browser.find_elements(by=By.XPATH, value=XPATH)
        time.sleep(1)
        post_field[0].send_keys(feed)
        post_field[0].send_keys(Keys.RETURN)
        print("Birthday Wish posted for friend" + str(cnt))

 
browser.close()