import os
import json
import logging
import sys
import boto3
from dotenv import load_dotenv

from flask import Flask, request, abort, Response
from botocore.exceptions import ClientError


# Load environment variables
load_dotenv('.env')

# Initialize Flask app
app = Flask(__name__)

app.config.from_object('config.ProductionConfig')

logger = logging.getLogger(__name__)

sqs = boto3.client(
    'sqs',
    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
    region_name=app.config['AWS_DEFAULT_REGION']
)

queue_url = app.config['AWS_SQS_QUEUE_URL']


def send_message(payment_id):
    # Send message to SQS queue

    try:
        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={
                'payment_id': {
                    'DataType': 'String',
                    'StringValue': payment_id
                },
            },
            MessageBody=(
                payment_id
            ),
        )
        return response
    except ClientError as error:
        logger.exception("Send message failed payment_id: {}".format(payment_id))
        return None


@app.route('/notifications', methods=['POST'])
def notifications():

    if not request.args.get('topic') == 'payment' or not request.args.get('id'):

        logger.exception("Missing fields")
        return Response(status=200)

    payment_id = request.args.get('id')
    send_message(payment_id)
    return Response(status=200)
