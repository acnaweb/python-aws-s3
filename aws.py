#!/usr/bin/env python
# coding: utf-8

# ### AWS S3 - Management

# AWS SDK
# !pip install boto3

import boto3
from botocore.exceptions import ClientError
import logging


class S3Manager:
    
    
    # construtor
    def __init__(self, access_key, secret):
        self.aws = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret
        )
        # other params
        # region_name
      
    
    # criar bucket
    def create_bucket(self, bucket_name):
        try:
            self.aws.create_bucket(Bucket=bucket_name)
            
        except ClientError as e:
            logging.error(e)
            return False        
        return True
    
    
    # file upload
    def upload_object(self, file_name, bucket, object_name=None):
        if object_name is None:
            object_name = file_name
        try:
            response = self.aws.upload_file(file_name, bucket, object_name)
            
        except ClientError as e:
            logging.error(e)
            return False
    
        return True
    
    
    # list buckets
    def list_buckets(self):
        return self.aws.list_buckets()
    
    
    # listing objects in bucket
    def list_objects(self, bucket_name):
        return self.aws.list_objects(Bucket=bucket_name)
    
    
    # download object
    def download_object(self, bucket, object_name, file_name):
        try:
            self.aws.download_file(bucket, object_name, file_name)
        except ClientError as e:
            logging.error(e)
            return False
    
        return True         
    

