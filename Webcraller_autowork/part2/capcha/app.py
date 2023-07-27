from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyperclip
import time

options = webdriver.ChromeOptions()

# 평소에 크롬브라우저로 쓰던 계정정보를 여기에 복붙
options.add_argument(r'user-data-dir=C:\Users\korea\AppData\Local\Google\Chrome\User Data\Default')

driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=https%3A%2F%2Fm.naver.com%2Fna%2F')

time.sleep(1)

# 아이디/비번입력
e = driver.find_element(By.ID, 'id')

pyperclip.copy('ga225')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(1)

e = driver.find_element(By.ID, 'pw')

pyperclip.copy('dhkdrlQma27!')
e.send_keys(Keys.CONTROL, 'v')
e.send_keys(Keys.ENTER)

time.sleep(2)
driver.get('https://m.blog.naver.com/FeedList.naver')
time.sleep(1.5)
driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FGoWriteForm.naver')

time.sleep(1.5)
e = driver.find_element(By.CLASS_NAME, 'documentTitle_blog')
title = e.find_element(By.CLASS_NAME, 'se_textarea')
title.send_keys('블로그 제목')

time.sleep(1.5)
e = driver.find_element(By.CLASS_NAME, 'se_paragraph')
contant = e.find_element(By.CLASS_NAME, 'se_editable')
contant.send_keys('블로그 내용')
contant.send_keys(Keys.ENTER)
contant.send_keys('End')

time.sleep(3)