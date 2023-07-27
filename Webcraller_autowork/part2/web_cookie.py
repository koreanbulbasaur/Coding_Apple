import requests
from bs4 import BeautifulSoup

steam_url = 'https://steamdb.info/'
amazon_url = 'https://www.amazon.com/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
cookies = {'cf_clearance':'GJgV4HSx53YH6Q.qGk68RhVJNt5ci0WGhKDNSKY3rmc-1690265685-0-160.0.0',
            '__cf_bm':'ZX7Vt998lBx6FckKcwVMkAU3WU1rOQOMTNDjsPGd0WM-1690351297-0-AZaKCle7xO+95YLdx0NhEF47+PlkCRVYQXT60c5zdOa1e0mtBR4oxe5qWbksWacvJ2KuKJlaAE6OuoiWkk8r5is='
}

r = requests.get(steam_url, headers=headers, cookies=cookies)

soup = BeautifulSoup(r.content, 'lxml')
if r.status_code == 200:
    print(soup.select('.text-center')[10])
else:
    print('error')

# print(r.content)
# print(r.status_code)