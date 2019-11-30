import json
import os
import boto3
from os import path
from botocore.vendored import requests
import sys
import subprocess
import logging
import uuid
import time
import socket
from datetime import datetime
import random

maxretry = 5
logger = logging.getLogger(__name__)


# post metric to s3 bucket,for integration with wavefront
def put_in_s3(data):
    print("putting data in s3")
    print("data = " + data)

    s3_client_boto = boto3.client('s3')

    random_uuid = str(uuid.uuid4())
    bucketName = os.environ['BucketName']

    response = s3_client_boto.put_object(
        ACL='bucket-owner-full-control',
        Body=data,
        Bucket=bucketName,
        Key=random_uuid,
    )
    print("Data put in s3 bucket")
    return response


def altstatus():
    util = random.randint(10, 91)
    print(util)
    return util


def lambda_handler(event, context):
    util = altstatus()
    _today = datetime.now().strftime('%Y-%m-%d %H:%M')
    _epoch_time = int(time.mktime(time.strptime(_today, '%Y-%m-%d %H:%M')))
    _prefix = "custom.api.simpleml.utilization"
    app = "SimpleMLService"
    location = "lambda"
    print(os.environ)
    env = os.environ['tag_env']
    source = os.environ['tag_source']
    platform = "aws"

    # printing metrics to be sent to Wavefront
    metric = "%s %s %s source='%s' app='%s' location='%s' environment='%s' platform='%s' bu='pire' " % (
    _prefix, util, _epoch_time, source, app, location, env, platform)
    print(metric)

    response = put_in_s3(metric)

    return {
        'statusCode': 200,
        'body': response
    }