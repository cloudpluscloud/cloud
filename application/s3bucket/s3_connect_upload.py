import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError

#pip install boto3
#pip install python-dotenv


load_dotenv()

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

#local file name, bucket name, name that it will have in s3
uploaded = upload_to_aws('cat.jpg', BUCKET_NAME, 'cat.jpg')