from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from main import scraper
import threading


# многопоточность
# получение данных о группах
# получение твитов 

find_name = "geo"
numbers_profiles = 3
email = "n8BDm9EJOucT3C0"
password = '0669309431Kot'
url = 'https://twitter.com/'
mi = scraper(email,password,url)
