from flask import Flask, render_template, request

# Flaskインスタンスの作成
app = Flask(__name__)

# デコレータ
@app.route('/hello')
def hello_world():
    return 'Welcome to Flask world!'

@app.route('/', methods=['GET'])
def index():
    title = 'Form Sample'
    # templatesディレクトリの中からindex.htmlを検索
    return render_template('index.html', title=title)

@app.route('/<id>/<password>')
def index2(id, password):
    # msg = f'id: {id}, password: {password}'
    msg = 'id: {}, password: {}'.format(id, password)
    return render_template('index.html', title=msg)

#  formの値受け取り
@app.route('/', methods=['POST'])
def form():
    field = request.form['field']
    return render_template('index.html', title="Form Sample Display", title2=f'{field}')


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
