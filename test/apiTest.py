# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request

client_id = "BJB5s0rh1K_g5tFivcbG"
client_secret = "03o308peGT"

encText = urllib.parse.quote("파이썬")
print(type(encText))
# url = "https://billingapi.apigw.ntruss.com/billing/v1/"
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# https://openapi.naver.com/v1/search/blog.json	

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()

    print("서버로 부터 정상적으로 정보를 수신 하였습니다. 파일로 저장합니다.\n")
    print(response_body.decode('utf-8'))

    # f = open("새파일.txt", 'w')

    # recieveData = response_body.decode('utf-8')
    # f.write(recieveData)
    # f.close()
    



else:
    print("Error Code:" + rescode)



