from boto3.session import Session

ACCESS_KEY='AKIAT5VK242JHG3NO7EP'
SECRET_KEY='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'

session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
your_bucket = s3.Bucket('fd-l-test')

for s3_file in your_bucket.objects.all():
    print(s3_file.key)