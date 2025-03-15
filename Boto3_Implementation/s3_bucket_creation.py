import boto3
import boto3.session


def get_session():
    session = boto3.Session(profile_name="default")
    return session


def create_s3():
    session = get_session()
    buk = session.client("s3", region_name="ap-south-1")
    res = buk.create_bucket(
        Bucket="pritbucket1366556666556677",
        CreateBucketConfiguration={"LocationConstraint": "ap-south-1"},
    )

    return res["ResponseMetadata"]["HTTPStatusCode"]


def list_bucket():
    session = get_session()
    bucket = session.client("s3", region_name="ap-south-1")
    res = bucket.list_buckets()
    # print(res)
    return res["Buckets"][0]["Name"]


# res = create_s3()
res = list_bucket()
print(res)
