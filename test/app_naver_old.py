# from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
# app.py
import os
import sys
import urllib.request
import json
# from controller.test import User

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록


@api.route('/hello')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def get(self):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환

        print("검색값을 입력하세요(NAVER) : ", end='')
        userInput = input()
        client_id = "BJB5s0rh1K_g5tFivcbG"
        client_secret = "03o308peGT"
        encText = urllib.parse.quote(userInput)
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)

        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()

            print("서버로 부터 정상적으로 정보를 수신 하였습니다. \n")

            recieveData = response_body.decode('utf-8')
            print(type(response_body.decode('utf-8')))

            json_data = json.loads(recieveData)
            print(type(json_data))
            
            print(json_data.get("title"))

            # for x in recieveData :
            #     testX = x
            #     testY = x[recieveData]

        else:
            print("Error Code:" + rescode)
            # request.get_json()
            # return jsonify(recieveData)
            
            # get_data = data.get('args')
            # print('name = ', get_data.get('name'))
            # print('say = ', get_data.get('say'))

        return recieveData

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)