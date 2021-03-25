#
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

'''
 Changes the number of Amazon Kendra Enterprise Edition index capacity units

 Parameters
 ----------
 event : dict
 Lambda event

 Returns
 -------
 The additional capacity action or an error
'''

import json
import boto3
from botocore.exceptions import ClientError
import os

# Variable declaration
KENDRA = boto3.client("kendra")
# Define your Amazon Kendra Enterprise Edition index ID
INDEX_ID = os.environ['INDEX_ID']

# Define your baseline units
DEFAULT_UNITS = os.environ['DEFAULT_UNITS']
# Define your the number of Query Capacity Units needed for increased capacity
ADDITIONAL_UNITS= os.environ['ADDITIONAL_UNITS']


def add_capacity(INDEX_ID,capacity_units):
    try:
        response = KENDRA.update_index(
            Id=INDEX_ID,
            CapacityUnits={
                'QueryCapacityUnits': int(capacity_units),
                'StorageCapacityUnits': 0
                
            })
        return(response)
    except Exception as e:
        raise e

    
def reset_capacity(INDEX_ID,DEFAULT_UNITS):
    try:
        response = KENDRA.update_index(
            Id=INDEX_ID,
            CapacityUnits={
            'QueryCapacityUnits': DEFAULT_UNITS,
            'StorageCapacityUnits': 0
        })
    except Exception as e:
        raise e

  
def current_capacity(INDEX_ID):
    try:
        response = KENDRA.describe_index(
        Id=INDEX_ID)
        return(response)
    except Exception as e:
        raise e  


def lambda_handler(event,context):
    print("Checking for query capacity units......")
    response = current_capacity(INDEX_ID)
    currentunits = response['CapacityUnits']['QueryCapacityUnits']
    print ("Current query capacity units are: "+str(currentunits))
    status = response['Status']
    print ("Current index status is: "+status)
    # If index is stuck in UPDATE state, don't attempt changing the capacity
    if status == "UPDATING":
        return ("Index is currently being updated. No changes have been applied")
    if status == "ACTIVE":
        if currentunits == 0:
            print ("Adding query capacity...")
            response = add_capacity(INDEX_ID,ADDITIONAL_UNITS)    
            print(response)
            return response
        else:
            print ("Removing query capacity....")
            response = reset_capacity(INDEX_ID, DEFAULT_UNITS)
            print(response)
            return response
    else:
         response = "Index is not ready to modify capacity. No changes have been applied."
         return(response)
