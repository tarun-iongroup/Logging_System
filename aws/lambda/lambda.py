import os
import boto3
import json

s3 = boto3.resource('s3')
sqs = boto3.resource('sqs')

def handler(event, context):
    bucket_name = (os.environ['BUCKET_NAME'])
    queue_name = (os.environ['QUEUE_NAME'])
    queue = sqs.get_queue_by_name(QueueName = os.environ['QUEUE_NAME'] )
    key = event['Records'][0]['s3']['object']['key']
    try:
        dest = os.path.join("/tmp",key)
        s3.meta.client.download_file(bucket_name,key,dest)
        with open(dest) as f:
            message = json.load(f)

        response = queue.send_message(MessageBody = str(message))

        return response

    except Exception as e:
        print(e)
        print("[Error] :: Error processing file {} from bucket {}.   ".format(key, bucket_name))
        raise e
