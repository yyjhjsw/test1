"""
create by yin
"""
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return '你好，flask'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
