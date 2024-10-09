import boto3
import botocore

BUCKET_NAME = 'my-bucket' 
KEY = 'my_image_in_s3.jpg' 

s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
