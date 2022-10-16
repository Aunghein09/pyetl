from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

###### Deprecated ######
# options = ChromeOptions()
# options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# print(options.binary_location)
# driver = Chrome('./chromedriver', options=options)
# driver = Chrome('./chromedriver')
########################

service = Service("./chromedriver")
driver = Chrome(service=service)

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)
# driver.find_element_by_class_name('board-name').click() # Deprecated
driver.find_element(by=By.CLASS_NAME, value='board-name').click()
# driver.find_element_by_class_name('btn-big').click() # Deprecated
driver.find_element(by=By.CLASS_NAME, value='btn-big').click()


cookie = driver.get_cookies()
# [{'domain': 'www.ptt.cc', 'httpOnly': False, 'name': 'over18', 'path': '/', 'secure': False, 'value': '1'},
#  {'domain': '.ptt.cc', 'expiry': 1665907282, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},
#  {'domain': '.ptt.cc', 'expiry': 1665993623, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1651547368.1665907222'}, 
# {'domain': '.ptt.cc', 'expiry': 1700467223, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.694564142.1665907222'}]
print(cookie)

driver.close()

ss = requests.session()

# 設定cookies
for c in cookie:
    ss.cookies.set(c['name'], c['value'])

res = ss.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())