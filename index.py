from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from main import scraper


# добавить запись в ексель 
# запись в csv
# многопоточность
# получение данных о группах
# получение твитов
# 


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
links = []
mi.people_finder('anime')
links = mi.get_links()



for i in range(len(links)):
    mi.openWebsite(links[i])
    time.sleep(1)
    print('https://twitter.com/'+mi.get_id())
    print(mi.get_id())
    print(mi.get_name())
    print(mi.get_twits_num())
    print(mi.get_following())
    print(mi.get_followers())
    
    
mi.close()
# r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l
# css-901oao css-16my406 r-1n1174f r-1loqt21 r-poiln3 r-bcqeeo r-qvutc0