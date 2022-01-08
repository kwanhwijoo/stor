import hashlib
import hmac
import base64
import time
import requests
import sys
import json
import xmltodict #xml to json
from collections import OrderedDict
import xml.etree.ElementTree as elemTree


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
    # uri = "/server/v2/getServerImageProductList"  #요청 URI
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
    response = requests.get("https://ncloud.apigw.ntruss.com/server/v2/getServerInstanceList", headers=custom_headers)



    # 응답결과
    print("####서버 응답결과####") 
    # print(response.text)     

    cc = xmltodict.parse(response.text) # return collections.OrderedDict    
    dd = json.loads(json.dumps(cc)) # return dict

    # print(dd) 
    # print(type(dd.values())) #json 포맷
    print(dd.keys())
    # print(dd['getServerInstanceListResponse']['requestId'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['serverInstanceNo'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['serverName'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['cpuCount'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['memorySize'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['baseBlockStorageSize'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['serverImageName'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['privateIp'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['portForwardingPublicIp'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['baseBlockStorageSize'])
    print(dd['getServerInstanceListResponse']['serverInstanceList']['serverInstance']['createDate'])
    


    
if __name__ == '__main__':
    main(None)

