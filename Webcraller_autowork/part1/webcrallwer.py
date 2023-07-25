import requests
from bs4 import BeautifulSoup as bs

url = 'https://finance.naver.com/item/sise.nhn?code=005930'

get_url = requests.get(url)

# 그 웹페이지의 html을 출력
# print(get_url.content)

# 그 웹페이지 접속 제대로 되고 있나 확인가능
# print(get_url.status_code)

# 예쁜 html 출력
soup = bs(get_url.content, 'html.parser')
# print(soup)

find_data1 = soup.find_all('strong', id='_nowVal')[0].text
print(find_data1)

# class 로 찾을 경우 class_ <- 이렇게 쳐야함
find_data2 = soup.find_all('span', class_='p11')[5].text
print(find_data2)