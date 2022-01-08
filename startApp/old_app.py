# app.py
# from flask import Flask, render_template
from flask import Flask, render_template, redirect, request, url_for
 
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
 





@app.route('/test')
def test():
    return '반갑습니다'








if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)

