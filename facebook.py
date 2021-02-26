import main
import time

ChromeDriver= './chromedriver.exe'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/88.0.4324.190 Safari/537.36'

# class for job with window
window = main.window()

fake_user_agent = window.fake_user_agent()
window.win_init_user_agent(ChromeDriver,fake_user_agent)
window.openWebsite('https://www.facebook.com/')
time.sleep(10)



