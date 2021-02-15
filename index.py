from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from main import scraper

email = "n8BDm9EJOucT3C0"
password = '0669309431Kot'
url = 'https://twitter.com/'
mi = scraper(email,password,url)

try:
    # log in
    mi.log_in()
    # clear console
    mi.clear_console()
except:
    mi.close()

mi.people_finder(input('write please what you want find: '))
    
mi.close()