# app.py
import os
import sys
import urllib.request
import json
from flask import Flask, render_template, redirect, request, url_for, jsonify
# from controller.test import User


 
#Flask 객체 인스턴스 생성
app = Flask(__name__)


# @app.route('/') # 접속하는 url
# def index():
#   return render_template('index.html')
@app.route('/')
def index():
    return render_template('index.html')
    # if request.method == 'GET':
    #     return redirect(url_for('test'))
 
@app.route('/test', methods=['GET','POST'])

def test():

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



if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)

