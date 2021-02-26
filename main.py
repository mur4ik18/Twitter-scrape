from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent

import time
from colorama import Fore,Back,Style
import os

# excel
from openpyxl import Workbook
# csv
import  csv

class scraper:
    # consctructor
    def __init__(self,email,password,link):
        self.login = email
        self.password = password
        self.link = link
    
    # methods
    # click function
    def click(self,xpath,sleep):
        self.win.find_element_by_xpath(xpath).click()
        time.sleep(sleep)
    
    # send key in input 
    def key_send(self,xpath,key,sleep):
        self.win.find_element_by_xpath(xpath).send_keys(key)
        time.sleep(sleep)
        
    # log in in the website
    def log_in(self):
        # open log in website
        print(Fore.MAGENTA + 'open website...')
        self.openWebsite(self.link)
        print(Fore.GREEN + 'Done!')
        
        # click "login"
        self.click('//*[@id="react-root"]/div/div/div/main/div/div/div/'+\
            'div[1]/div/div[3]/a[2]/div',1)
        
        # write email
        print(Fore.YELLOW + 'Trying write email..')
        self.key_send('//*[@id="react-root"]/div/div/div[2]/main/div/div\
            /div[2]/form/div/div[1]/label',self.login,0.5)
        print(Fore.GREEN + 'Done!')  
        
        # write pass 
        print(Fore.YELLOW + 'Trying write password..')
        self.click('//*[@id="react-root"]/div/div/div[2]/main/div/div\
            /div[2]/form/div/div[2]/label',0.5)
        self.key_send('//*[@id="react-root"]/div/div/div[2]/main/div/div\
            /div[2]/form/div/div[2]/label',self.password,0.5)
        print(Fore.GREEN + 'Done!')
        
        # click 'login'
        self.click('//*[@id="react-root"]/div/div/div[2]/main/div/div\
            /div[2]/form/div/div[3]/div',0.5)
    
    
    # search method
    def search(self, x):
        print(Fore.BLUE + "you want find : " + x)
        # click search in the twitter
        self.click('//*[@id="react-root"]/div/div/div[2]/header/div/\
            div/div/div[1]/div[2]/nav/a[2]',0.5)
        self.click('//*[@id="react-root"]/div/div/div[2]/main/div/div/\
            div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div\
                /div/div/form/div[1]/div/div/div[2]/input',0.5)
        self.key_send('//*[@id="react-root"]/div/div/div[2]/main/div/\
            div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]\
                /div/div/div/form/div[1]/div/div/div[2]/input',x,1)
        self.key_send('//*[@id="react-root"]/div/div/div[2]/main/div/\
            div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]\
                /div/div/div/form/div[1]/div/div/div[2]/input',Keys.ENTER,1)
    
    # if we need find people 
    def people_finder(self,x):
        self.search(x)
        self.click('//*[@id="react-root"]/div/div/div[2]/main/div/div/\
            div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a',1)
        print(Fore.GREEN + 'we has opened people search!')
    
    # get links
    def get_links(self, num):
        print(Fore.GREEN + 'Try to get links')
        glob_links = []
        for i in range(num):
            links = self.win.find_element_by_xpath('//*[@id="react-root"]/div\
                /div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/\
                section/div/div')
            link = links.find_elements_by_css_selector("a.r-1wbh5a2")
            for i in range(len(link)):
                glob_links.append(link[i].get_attribute('href'))
                print(link[i].get_attribute('href'))
            self.win.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
        self.clear_console()
        print(Fore.GREEN + 'links getted is done')
        return glob_links
        
    
    # clear console
    def clear_console(self):
        os.system('clear')
        print(Fore.GREEN + "Errors : 0")
        print(Fore.GREEN + "We are logged")
        
    # get @name
    def get_id(self):
        ide = self.win.find_element_by_xpath('//*[@id="react-root"]\
            /div/div/div[2]/main/div/div/div/div/div/div[2]/div/div\
                /div[1]/div/div[2]/div/div/div[2]/div/span').text
        return ide
    
    # get name
    def get_name(self):
        name = self.win.find_element_by_xpath('//*[@id="react-root"]\
            /div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]\
                /div/div/div/div/div[2]/div/h2/div/div/div/span[1]/span/span')
        return name.text
    
    # get twits number
    def get_twits_num(self):
        twits_num = self.win.find_element_by_xpath('//*[@id="react-root"]\
            /div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]\
                /div/div/div/div/div[2]/div/div').text
        twits_num = twits_num.split(' Tweets')        
        return twits_num[0]  
    
    # get following 
    def get_following(self):
        following_nums = self.win.find_element_by_xpath('//*[@id="react-root"]/\
            div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/\
                div[5]/div[1]/a/span[1]/span').text
        return following_nums
    
    # get followers numb
    def get_followers(self):
        followers_num = self.win.find_element_by_xpath('//*[@id="react-root"]/\
            div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/\
                div[5]/div[2]/a/span[1]/span').text
        return followers_num

class window:
    def __init__(self):
        self.win = None
    
    # methods
    # win init
    def win_init(self,location):
        self.win = webdriver.Chrome(location) 
        print(Fore.GREEN + "Initial chrome driver is done!")
    
    def win_init_user_agent(self,location,user_agent):
        opts = Options()
        opts.add_argument(f'user-agent={user_agent}')
        self.win = webdriver.Chrome(chrome_options=opts, executable_path=location) 
        print(Fore.GREEN + "Initial chrome driver with custom UserAgent is done!")

    # open twitter or link
    def openWebsite(self, url):
        self.win.get(url)
        time.sleep(1)
        print(Fore.GREEN + "URL was opened!")

    # function for close window
    def close(self):
        print(Fore.YELLOW + "Close window...")
        self.win.close()
        print(Fore.GREEN + "Done!")

    # created fake user agent
    def fake_user_agent(self):
        options = Options()
        ua = UserAgent()
        userAgent = ua.random
        print(userAgent)
        return userAgent


class scrape:
    """
    universal scrape class
    """
    def __init__(self):
        pass

    def click(self, window, ):
        """
        get window
        """
        pass
        
class facebook:
    def __init__(self):
        pass


    def click(self):
        """

        """
        pass


class excel():
    def __init__(self,):
        """
        intializating  datas
        """
        self.wb = None
    
    
    # methods
    # open excel file 
    def сreate_wb(self):
        """
        here we create excel file
        Make workbook
        return worksheet
        """
        self.wb = Workbook()
        print(Fore.GREEN + 'Workbook has created')
        ws = self.wb.active
        print(Fore.GREEN + 'Workbook has be activeted')
        return ws
    
    # this function save data in excel
    def save_excel(self, name):
        """
        save active workbook in excel file
        """
        self.wb.save(name+'.xlsx')
        print(Fore.MAGENTA + f'{name}.xls has saved')
    
    # write info in column
    def write_col(self, column,row,info,worksheet):
        """
        save info into excel
        use with loop
        use worksheet
        """
        worksheet[str(column)+str(row)] = info
        
        
        
class work_with_csv:
    def __init__(self):
        self.main_file = None
    
    # methods
    def create_csv(self,name):
        """
        create csv for write
        """
        f = open(name+'.csv', 'w')
        self.main_file = csv.writer(f)
    
    def wite_csv(self,argument):
        """
        write row in csv
        """
        self.main_file.writerow(argument)