from selenium import webdriver
import random
from fake_useragent import UserAgent

import time




#url='https://юзерагент.рф/'
url='https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
chrome_path='/home/fan/projects/chromedriver' #WINDOWS->   c:\\driver\\selenium.exe
user_agent=UserAgent()




options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument(f'user-agent={user_agent.random}')

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")


browser = webdriver.Chrome(executable_path=chrome_path, options=options)

try:
    browser.get(url=url)
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()



