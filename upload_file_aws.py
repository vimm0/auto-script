import boto3
from botocore.client import Config
s3 = boto3.resource(
    's3',
    aws_access_key_id='AKIAIGBYCQLUT7CCVVDA',
    aws_secret_access_key='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',
    config=Config(signature_version='s3v4')
)

# SEND_MEDIA_ROOT = '/home/vimm0/office/media/video/cut_71XwINQ.mp4'
# data = open(SEND_MEDIA_ROOT, 'rb')

# s3.Bucket('jus-backend-static-dev').put_object(Key='/media/video/cut_71XwINQ.mp4', Body=data, ACL='public-read')
