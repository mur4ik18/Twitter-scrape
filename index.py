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

try:
    # log in
    mi.win_init()
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

def scrape_info(x,y):
    """
    we scrape info and save in the ram
    """
    info = []
    mi.win_init()
    for i in range(x,y):
        time.sleep(1)
        mi.openWebsite(links[i])
        time.sleep(0.5)
        local_info = []
        local_info.extend(
            (mi.get_id(),
            mi.get_name(),
            mi.get_twits_num(),
            mi.get_following(),
            mi.get_followers(),
            'https://twitter.com/'+ mi.get_id()
            )
        )
        info.append(local_info)

    return info
        
x = len(links)//2
if __name__ == '__main__':
    p2 = threading.Thread(target=scrape_info,name="Thread1", args=(0,x))
    p2.start()
p1 = scrape_info(x,len(links))
info = []
info.extend(p1)
info.extend(p2)



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



def save_to_excel(arr):
    for i in range(len(arr)):        
        # num
        mi.write_col('A',i+2,i+1,workSheet)
        # id
        mi.write_col('B',i+2,arr[i][0],workSheet)
        # name
        mi.write_col('C',i+2,arr[i][1],workSheet)
        # tweets number
        mi.write_col('D',i+2,arr[i][2],workSheet)
        # following numb
        mi.write_col('E',i+2,arr[i][3],workSheet)
        # followers numb
        mi.write_col('F',i+2,arr[i][4],workSheet)
        # link
        mi.write_col('G',i+2,arr[i][5],workSheet)
    mi.save_excel(find_name)
save_to_excel(info)

mi.close()