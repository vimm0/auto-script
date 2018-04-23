import boto3
from botocore.client import Config
s3 = boto3.resource(
    's3',
    aws_access_key_id='XXX',
    aws_secret_access_key='XXX',
    config=Config(signature_version='s3v4')
)

# SEND_MEDIA_ROOT = '/home/vimm0/office/media/video/cut_71XwINQ.mp4'
# data = open(SEND_MEDIA_ROOT, 'rb')

# s3.Bucket('XXX-backend-static-dev').put_object(Key='/media/video/cut_71XwINQ.mp4', Body=data, ACL='public-read')
