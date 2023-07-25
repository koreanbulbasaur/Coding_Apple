import requests
from bs4 import BeautifulSoup as bs

url = 'https://finance.naver.com/item/sise.nhn?code=005930'

get_url = requests.get(url)

soup = bs(get_url.content, 'html.parser')

# print(soup.find_all('em')[0].text)

'''
<CSS selector>
class : .
id : #
'''

# class='gray' 안에 class = 'f_down'을 찾은 뒤 그 안에 있는 em을 찾아라
output = soup.select('.gray .f_down em')[0].text
# print(output)

# 이미지 뽑기
img = soup.select('#img_chart_area')[0]
print(img['src'])