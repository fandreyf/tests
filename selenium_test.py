from selenium import webdriver
import random
from fake_useragent import UserAgent

import time




url='https://юзерагент.рф/'
chrome_path='/home/fan/projects/chromedriver' #WINDOWS->   c:\\driver\\selenium.exe
user_agent=UserAgent()


options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument(f'user-agent={user_agent.random}')



browser = webdriver.Chrome(executable_path=chrome_path, options=options)

try:
    browser.get(url=url)
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()



