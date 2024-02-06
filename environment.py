import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'storage'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload(file):
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return 'No selected file'

    if not allowed_file(file.filename):
        return 'FILE NOT ALLOWED!'

    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))