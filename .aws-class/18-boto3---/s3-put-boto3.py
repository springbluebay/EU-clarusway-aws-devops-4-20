import boto3

# Use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open('ryu.jpg', 'rb')
s3.Bucket('spring.broadcast').put_object(Key='ryu.jpg', Body=data)
