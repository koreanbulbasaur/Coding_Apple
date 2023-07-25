import requests
import json
import time

def num_view(number):
    number_str = str(number)[::-1]
    chunks = [number_str[i:i + 4][::-1] for i in range(0, len(number_str), 4)]
    num = ','.join(chunks)
    return num

url = "https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/BTC?interval=1H&1690275676127"
data = requests.get(url)

딕셔너리 = json.loads(data.content)
print(딕셔너리['body']['candles'][0]['close'])
print(딕셔너리['body']['candles'][1]['close'])

for i in range(200):
    epochtime = int(딕셔너리['body']['candles'][i]['dt'])
    data_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochtime/1000))
    print(data_time) 
    number = int(float(딕셔너리['body']['candles'][i]['close']))
    n = num_view(number)
    print(n)