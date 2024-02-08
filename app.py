from flask import Flask, request, render_template, jsonify, make_response
from werkzeug.utils import secure_filename
import environment

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        uploaded_file = request.files['file-to-upload']
        filename = secure_filename(uploaded_file.filename)
        environment.upload(uploaded_file)
        response_filepath = environment.getFile(filename)
        if response_filepath:
            return render_template('index.html', filepath=response_filepath)

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