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

find_name = "tech"
numbers_profiles = 3
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

mi.people_finder(find_name)
links = mi.get_links(numbers_profiles)
links = list(set(links))

workSheet = mi.сreate_wb()
# num
mi.write_col('A',1,"num",workSheet)
# id
mi.write_col('B',1,'id',workSheet)
# name
mi.write_col('C',1,'name',workSheet)
# tweets number
mi.write_col('D',1,'Tweets num',workSheet)
# following numb
mi.write_col('E',1,"following num",workSheet)
# followers numb
mi.write_col('F',1,"followers num",workSheet)
# link
mi.write_col('G',1,"link",workSheet)

for i in range(len(links)):
    mi.openWebsite(links[i])
    time.sleep(0.5)
    
    # num
    mi.write_col('A',i+2,i+1,workSheet)
    # id
    mi.write_col('B',i+2,mi.get_id(),workSheet)
    # name
    mi.write_col('C',i+2,mi.get_name(),workSheet)
    # tweets number
    mi.write_col('D',i+2,mi.get_twits_num(),workSheet)
    # following numb
    try:
        mi.write_col('E',i+2,mi.get_following(),workSheet)
    except:
        print('scip mi.get_following')
    # followers numb
    try:
        mi.write_col('F',i+2,mi.get_followers(),workSheet)
    except:
        print('scip mi.get_followers')
    # link
    mi.write_col('G',i+2,'https://twitter.com/'+mi.get_id(),workSheet)
    
mi.save_excel(find_name)    
mi.close()