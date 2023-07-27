import os
import sys
import urllib.request
import json

def trans(text):
    client_id = "mti1ISIU3A8Av8BjqtoK" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "kRf_DzYeZQ" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(text)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        딕셔너리 = json.loads(response_body)
        # print( 딕셔너리['message']['result']['translatedText'] )
        return 딕셔너리['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)