import os
from flask import Flask, request, render_template, jsonify, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'storage'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        uploaded_file = request.files['file-to-upload']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if uploaded_file.filename == '':
            return 'No selected file'

        if not allowed_file(uploaded_file.filename):
            return 'FILE NOT ALLOWED!'

        filename = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(UPLOAD_FOLDER, filename))

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