from flask import Flask, render_template, request
from flask.views import MethodView

# Flaskインスタンスの作成
app = Flask(__name__)

# デコレータ
# @app.route('/hello')
# def hello_world():
#     return 'Welcome to Flask world!'

@app.route('/', methods=['GET'])
def index():
    title = 'Sample App'
    message = 'This is Index Page'
    # templatesディレクトリの中からindex.htmlを検索
    return render_template('index.html', title=title, message=message)

@app.route('/<id>/<password>')
def index2(id, password):
    # msg = f'id: {id}, password: {password}'
    msg = 'id: {}, password: {}'.format(id, password)
    return render_template('index.html', title=msg)

#  formの値受け取り
# @app.route('/', methods=['POST'])
# def form():
#     field = request.form['field']
#     return render_template('index.html', title="Form Sample Display", title2=f'{field}')

@app.route('/next', methods=['GET'])
def next():
    data = ['One', 'Two', 'Three']
    return render_template('next.html', title='Next page', message='This is Next Page', data=data)

class HelloAPI(MethodView):
    send = ''

    def get(self):
        title = 'Next Page GET'
        msg = '何か入力してください'
        return render_template('next.html', title=title, message=msg, send=HelloAPI.send)

    def post(self):
        HelloAPI.send = request.form.get('send')
        title = 'Next Page POST'
        msg = f'You send: {HelloAPI.send}'
        return render_template('next.html', title=title, message=msg, send=HelloAPI.send)


app.add_url_rule('/hello/', view_func=HelloAPI.as_view(('hello')))

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
