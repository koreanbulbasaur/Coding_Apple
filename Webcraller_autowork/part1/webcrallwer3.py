import requests
from bs4 import BeautifulSoup

def fun(material):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={material}')
    soup = BeautifulSoup(data.content, 'html.parser')
    now_price = soup.find_all('strong', id='_nowVal')[0].text
    print(soup.find_all('span', class_='tah')[5].text)
    print('-'*75)
    return now_price

mater_list = ['005930', '066575', '005380', '035720', '034220', '003490']

f = open('test.txt', 'w')

for m in mater_list:
    price = fun(m)
    f.write(f'{price}\n')

f.close()