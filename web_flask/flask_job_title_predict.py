# -*- coding:utf-8 -*-
from flask import Flask, request, session, render_template, send_file

app = Flask(__name__, static_url_path='/template/')


@app.route('/js/jquery-1.12.4.min.js', methods=["GET"])
def index_js():
    return send_file("./template/js/jquery-1.12.4.min.js")


@app.route('/js/jquery.animate-colors-min.js', methods=["GET"])
def index_js2():
    return send_file("./template/js/jquery.animate-colors-min.js")


@app.route('/', methods=["GET"])
def index():
    return send_file("./template/index.html")


@app.route("/data", methods=["GET"])
def get_data():
    word = request.args.get('word')
    word = word.lower()
    ret = di_pro.get(word, list())
    li = sorted(ret, key=lambda x: x[1], reverse=True)[:10]
    lis = [i[0] for i in li]
    di = 'dothis({q:"a",p:true,s:%s})' % lis
    return str(di)


if __name__ == '__main__':
    with open('../data_out/predict.data', 'r', encoding='utf-8') as f3:
        di_pro = eval(f3.read())
    app.run(host='127.0.0.1', port=8080, debug=True)
