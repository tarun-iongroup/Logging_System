from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_lambda_destinations as destinations,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3 as s3,
    aws_sns_subscriptions as sub,
    aws_s3_notifications as s3_notify
)

class AwsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self,"ion-bucket")
        queue = sqs.Queue(self,"ion-queue")
        lambda_func = _lambda.Function(self, 'LambdaListener',
                       runtime=_lambda.Runtime.PYTHON_3_8,
                       handler='lambda.handler',
                       code=_lambda.Code.from_asset('lambda'),
                       environment={'BUCKET_NAME':bucket.bucket_name,'QUEUE_NAME':queue.queue_name},
                       # on_success=destinations.SqsDestination(queue)
                       )

        queue.grant_send_messages(lambda_func)

        notification = s3_notify.LambdaDestination(lambda_func)
        notification.bind(self, bucket)
        
        bucket.grant_read(lambda_func)
        bucket.add_object_created_notification(notification)

