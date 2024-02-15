import os
import logging

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'upload'
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

    if os.environ.get('FLASK_ENV')=='development':
        file.save(os.path.join('static', UPLOAD_FOLDER, filename))

    if os.environ.get('FLASK_ENV')=='production':
        import boto3

        bucket_name = os.environ['BUCKET']
        s3 = boto3.resource('s3')

        s3.Bucket(bucket_name).upload_fileobj(file, filename)

def getFile(filename):
    if os.environ.get('FLASK_ENV')=='development':
        from flask import url_for

        filepath = url_for('static', filename = os.path.join(UPLOAD_FOLDER, filename))
        return filepath

    if os.environ.get('FLASK_ENV')=='production':
        import boto3
        from botocore.exceptions import ClientError

        s3_client = boto3.client('s3')
        bucket_name = os.environ['BUCKET']
        try:
            filepath = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': bucket_name,
                                                                'Key': filename},
                                                        ExpiresIn=3600)
            return filepath
        except ClientError as e:
            logging.error(e)
            return None
