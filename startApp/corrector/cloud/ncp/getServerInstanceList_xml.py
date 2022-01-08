import hashlib
import hmac
import base64
import time
import requests
import sys
import json
# import xmltodict #xml to json

# 테스트 성공

from requests.models import Response

def main(args):   
     # 시그니처 생성
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)

    access_key = 'hFZbWtU1mqxOzO9HRxLH'
    access_secret = 'GXOy5Z6RoYT8iRxeyGMq90eiyccEHSi6zUrHpc7w'
    access_secret_bytes = bytes(access_secret, 'UTF-8')

    method = "GET"
    # uri = "/billing/v1/product/getServerProductList?serverImageProductCode=KR&responseFormatType=json"  #요청 URI
    uri = "/server/v2/getServerImageProductList"  #요청 URI
    uri = "/server/v2/getServerInstanceList"


    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8') #바이트로 변경하고 문자셋 지정
    signing_key = base64.b64encode(hmac.new(access_secret_bytes, message, digestmod=hashlib.sha256).digest())
    print("####시그니처 생성완료####")  

    # 헤더 생성
    custom_headers = {
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': access_key,
        'x-ncp-apigw-signature-v2': signing_key #HMAC알고리즘
    }
    print("####헤더 생성완료, 서버 요청####")      
    print(custom_headers)

    # 서버요청
    # response = requests.get("https://billingapi.apigw.ntruss.com/billing/v1/product/getPriceList?priceNoList.1=14390&responseFormatType=json", headers=custom_headers) #실제 호출
    # response = requests.get("https://ncloud.apigw.ntruss.com/server/v2/getServerImageProductList", headers=custom_headers)
    response = requests.get("https://ncloud.apigw.ntruss.com/server/v2/getServerInstanceList", headers=custom_headers)


    # 응답결과
    print("####서버 응답결과####")      
    print(response.text)
    result = response.text
    






if __name__ == '__main__':
    main(None)

