import requests
import json
import pandas as pd
from io import StringIO



url='https://catfact.ninja/fact'
response = requests.get(url)
data=response.json()
df=pd.DataFrame([data])
print(data['fact'])
print(response.text)
print(df)
df.to_csv('output_file.csv', index=False)


#*****************************************************
import boto3
# Set up your credentials
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='YOUR_REGION'
)


#********************************************************
# Create an S3 client
s3 = boto3.client('s3')
# Specify the bucket name and the file key
bucket_name = 'your-bucket-name'
file_key = 'path/to/your/file.txt'  # here we will have key
# Download the file
s3.download_file(bucket_name, file_key, 'local_file.txt')
print("File downloaded successfully")



#***************************************************************
import boto3
# Create an S3 client
s3 = boto3.client('s3')
# Upload a file
s3.upload_file('path/to/your/file', 'your-bucket-name', 'your-file-name')






