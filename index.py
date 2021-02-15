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

# mi.people_finder(input('write please what you want find: '))
mi.people_finder('anime')
mi.close()

# r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l
# css-901oao css-16my406 r-1n1174f r-1loqt21 r-poiln3 r-bcqeeo r-qvutc0