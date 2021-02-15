from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from colorama import Fore,Back,Style
import os

class scraper:

    # consctructor
    def __init__(self,email,password,link):
        self.login = email
        self.password = password
        self.link = link
        self.win = webdriver.Chrome('./chromedriver')
    
    # methods
    
    # open twitter or link
    def openWebsite(self):
        self.win.get(self.link)
        time.sleep(1)

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
        self.openWebsite()
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
        self.get_links()
    
    # get links
    def get_links(self):
        print(Fore.GREEN + 'Try to get links')
        glob_links = []
        for i in range(20):
            links = self.win.find_element_by_xpath('//*[@id="react-root"]/div\
                /div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/\
                section/div/div')
            tink = links.find_elements_by_xpath('//*[@id="react-root"]/div/div\
                /div[2]/main/div/div/div/div/div/div[2]/div/div/\
                section/div/div/div/div/div/div/div[2]/div[1]/div[1]')
            link = tink.find_elements_by_tag_name('a')
            for i in range(len(link)):
                glob_links.append(link[i].get_attribute('href'))
                print(link[i].get_attribute('href'))
            self.win.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
        # .get_attribute('href')
        
        
    # function for close window
    def close(self):
        print(Fore.YELLOW + "Close window...")
        self.win.close()
        print(Fore.GREEN + "Done!")
    
    # clear console
    def clear_console(self):
        os.system('clear')
        print(Fore.GREEN + "Errors : 0")
        print(Fore.GREEN + "We are logged")