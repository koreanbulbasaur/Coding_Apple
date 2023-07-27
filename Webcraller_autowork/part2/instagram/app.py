from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

driver = webdriver.Chrome(r'part2\instagram\chromedriver.exe')
driver.get('https://instagram.com')

time.sleep(2)

# 인스타 로그인
e = driver.find_element(By.NAME,'username')
e.send_keys('ga225@naver.com')
e = driver.find_element(By.NAME, 'password')
e.send_keys('qkekrj0225')
e.send_keys(Keys.ENTER)

time.sleep(4)

# 알림 무시하기
e = driver.find_element(By.CLASS_NAME, '_a9_1').click()

# 페이지 이동
driver.get('https://www.instagram.com/explore/tags/%EC%9D%8C%EC%8B%9D/')

# 첫째 사진
driver.implicitly_wait(10)
e = driver.find_element(By.CLASS_NAME, '_aagw').click()

# 사진저장
img = driver.find_element(By.CLASS_NAME,'_aagv')
img_adress = img.find_element(By.TAG_NAME, 'img').get_attribute('src')
urllib.request.urlretrieve(img_adress, '1.jpg')

for i in range(50):
    pass

time.sleep(100)