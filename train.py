from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
user_agent = userAgent
opts = Options()
opts.add_argument(f'user-agent={user_agent}')
win = webdriver.Chrome(chrome_options=opts, executable_path='./chromedriver.exe')
win.get('https://www.facebook.com/')