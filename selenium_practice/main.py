# from messger import 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas, numpy
import datetime
import random


# 取得現在時間
now = datetime.datetime.now()
txt = '上次更新時間為：' + str(now)

# 轉成df
df = pandas.DataFrame([txt], index=['UpdateTime'])

# 存出檔案
df.to_csv('log.csv', header=False)

# #寄件資料
# from_emil = 'henry934629@gmail.com'
# password = 'gyipecqaymbguakt'

with open('C:/Users/henry/Desktop/selenium/data.txt', 'rt') as dt:
    while True:
        try:
            account, password= dt.readline().split()
            temperature = str(random.randrange(35, 37)) + '.' + str(random.randrange(0, 9))

            chromedriver = 'chromediver.exe'

            browser = webdriver.Chrome('C:/Users/henry/Desktop/selenium/chromedriver')
            browser.get('http://163.32.67.138/login')

            search = browser.find_element_by_xpath('//*[@id="home-form"]/input[1]')
            search.send_keys(account)

            search = browser.find_element_by_xpath('//*[@id="home-form"]/input[2]')
            search.send_keys(password)
            search.send_keys(Keys.RETURN)

            search = browser.find_element_by_xpath('//*[@id="home-form"]/input[1]')
            search.send_keys(temperature)
            search.send_keys(Keys.RETURN)

            # browser.close()
            # send_email(from_emil, password, to_email)
        except:
            break


