import boto3
BUCKET = 'fd-l-test'
FILE_TO_READ = 'export_04-05_05-05.json'
s3 = boto3.client('s3',aws_access_key_id='AKIAT5VK242JHG3NO7EP',aws_secret_access_key='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')
s3.put_object(Bucket=BUCKET, Key=FILE_TO_READ)

for s3_file in BUCKET.objects.all():
    print(s3_file.key)