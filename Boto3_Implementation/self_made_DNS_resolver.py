"""
Designing a DNS System using Amazon DynamoDB
We can design a simple DNS Resolver using DynamoDB as a key-value store.

Architecture Overview:
    DynamoDB: Stores domain-to-IP mappings as key-value pairs.
    Lambda Functions (or Python Script): Acts as a resolver to fetch IPs from DynamoDB.
    API Gateway / Flask Web App: Provides an API interface for DNS lookups.
"""

import boto3
import boto3.session


import boto3

# Initialize DynamoDB Client
dynamodb = boto3.client("dynamodb", region_name="us-east-1")


def resolve_dns(domain_name):
    response = dynamodb.get_item(
        TableName="DNSRecords", Key={"DomainName": {"S": domain_name}}
    )
    if "Item" in response:
        return response["Item"]["IPAddress"]["S"]
    else:
        return "Domain not found"


# Test Lookup
domain = "example.com"
ip = resolve_dns(domain)
print(f"Resolved {domain} -> {ip}")
