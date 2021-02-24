from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://twitter.com/George_McD'

options = webdriver.ChromeOptions()
options.add_argument("window-size=1,1")
options.add_argument('ignore-certificate-errors')

win = webdriver.Chrome('./chromedriver.exe',chrome_options=options) 
win.get(url)
# html = BeautifulSoup(r.text,'html.parser')

# print(html)
