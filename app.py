from flask import Flask, render_template, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/processing")
def processing():
    return "<p>Processing</p>"

# Sau chuyển phần này thành jsonify kết quả
@app.route("/result")
def result():
    return "<p>配色:</p><p>地名:</p><p>分類番号:</p><p>ひらがな:</p><p>ナンバー:</p>"

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)