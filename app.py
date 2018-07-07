#coding=utf-8
from flask import Flask, jsonify, send_file, send_from_directory
import os
# 实例化
app = Flask(__name__)


@app.route('/')
def index():
    return send_file(
        os.path.join(os.path.dirname(__file__), 'static', 'index.html'))


@app.route('/img')
def img():
    img_list = []
    for dirpath, dirnames, filenames in os.walk(
            os.path.join(os.path.dirname(__file__), 'img')):
        for file in filenames:
            img_list.append(os.path.splitext(file)[0])
    return jsonify(img_list)


@app.route('/img/<id>')
def get_img(id):
    return send_from_directory(
        os.path.join(os.path.dirname(__file__), 'img'), id + '.jpg')


if __name__ == '__main__':
    app.run(debug=True)