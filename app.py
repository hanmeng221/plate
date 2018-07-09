#coding=utf-8
from flask import Flask, jsonify, send_file, send_from_directory
import os
from urllib import unquote
# 实例化
app = Flask(__name__)


@app.route('/')
def index():
    return send_file(
        os.path.join(os.path.dirname(__file__), 'static', 'index.html'))


@app.route('/img', methods=['GET', "POST"])
def img():

    img_list = []
    for dirpath, dirnames, filenames in os.walk(
            os.path.join(os.path.dirname(__file__), 'img')):
        for file in filenames:
            img_list.append(os.path.splitext(file)[0])
    return jsonify(img_list)


@app.route('/img/<id>')
def get_img(id):
    # 获得车牌号, 在这里写处理函数
    myID = unquote(id)
    print(myID)

    return send_from_directory(
        os.path.join(os.path.dirname(__file__), 'img'), myID + '.jpg')


if __name__ == '__main__':
    app.run(debug=True)