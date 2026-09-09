import uuid
import os
import boto3
from flask import current_app
from werkzeug.utils import secure_filename

def get_s3_client():
    """Returns a boto3 client configured for local RustFS/S3."""
    return boto3.client(
        's3',
        endpoint_url=current_app.config['S3_ENDPOINT_URL'],
        aws_access_key_id=current_app.config['S3_ACCESS_KEY'],
        aws_secret_access_key=current_app.config['S3_SECRET_KEY']
    )

def upload_file_to_s3(file_obj) -> str:
    """
    Uploads a Flask FileStorage object to S3/RustFS.
    Returns the unique object key/filename.
    """
    s3 = get_s3_client()
    
    # 1. Sanitize filename and make it unique using UUID
    filename = secure_filename(file_obj.filename)
    ext = os.path.splitext(filename)[1].lower()
    unique_filename = f"recipes/{uuid.uuid4().hex}{ext}"
    
    # 2. Upload to RustFS bucket
    s3.upload_fileobj(
        file_obj,
        current_app.config['S3_BUCKET_NAME'],
        unique_filename,
        ExtraArgs={
            "ContentType": file_obj.content_type
        }
    )
    
    return unique_filename

def get_s3_image_url(image_filename: str) -> str:
    """Generates the accessible URL for an image stored in RustFS."""
    if not image_filename:
        return ""
    endpoint = current_app.config['S3_ENDPOINT_URL']
    bucket = current_app.config['S3_BUCKET_NAME']
    return f"{endpoint}/{bucket}/{image_filename}"