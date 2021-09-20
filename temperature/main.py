from setting import password, from_email
from send_email import send_email

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas
import datetime
import random

# 取得現在時間
now = datetime.datetime.now()
txt = '上次更新時間為：' + str(now)

# 轉成df
df = pandas.DataFrame([txt], index=['UpdateTime'])

# 存出檔案
df.to_csv('log.csv', header=False)

with open('data.txt', 'rt') as dt:
    while True:
        try:
            print('Fill in temperature. . .')
            account, id, to_email= dt.readline().split()
            temperature = str(random.randrange(35, 37)) + '.' + str(random.randrange(0, 9))

            browser = webdriver.Chrome()
            browser.get('http://163.32.67.138/login')

            search = browser.find_element_by_xpath('//*[@id="home-form"]/input[1]')
            search.send_keys(account)

            search = browser.find_element_by_xpath('//*[@id="home-form"]/input[2]')
            search.send_keys(id)
            search.send_keys(Keys.RETURN)

            search = browser.find_element_by_xpath('//*[@id="home-form"]/input[1]')
            search.send_keys(temperature)
            search.send_keys(Keys.RETURN)
            print('Complete!')

            send_email(from_email, password, to_email)

            browser.close()

        except:
            break


