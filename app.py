#coding=utf-8
from flask import Flask, jsonify, send_file, send_from_directory,request
import os
from urllib import unquote
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


@app.route('/img/<id>',methods=['GET', "POST"])
def get_img(id):
    myID = unquote(id)
    if request.method == 'POST':
        # 获得车牌号, 在这里写处理函数
        print(myID)
        return 'ok'
    else:
        return send_from_directory(
            os.path.join(os.path.dirname(__file__), 'img'), myID + '.jpg')


if __name__ == '__main__':
    app.run(debug=True)