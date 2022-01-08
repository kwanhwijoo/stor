from flask import Flask, render_template, redirect, request, url_for
 

def create_app():
    app = Flask(__name__)


    @app.route('/index', methods=['GET','POST'])
    
    def tmp():
        value = 'hello, world'
        return render_template('index.html', value = value)



    @app.route('/post', methods=['GET','POST'])
    def post():
        if request.method == 'POST':
            value = request.form['id_name']
            value = str(value)
            print(value)
        return render_template('post.html', value = value)



    return app



if __name__=="__main__":
  create_app.app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)

