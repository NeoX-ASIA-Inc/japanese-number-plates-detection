from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/processing")
def processing():
    return "<p>Processing</p>"

@app.route("/result")
def result():
    return "<p>配色:</p><p>地名:</p><p>分類番号:</p><p>ひらがな:</p><p>ナンバー:</p>"