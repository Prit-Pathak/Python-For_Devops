import boto3
import time


def get_session():
    """created session with aws (aws consle login programetically)"""
    session = boto3.Session(profile_name="default")
    return session


def ec2_create():
    "function to create ec2 instance"
    session = get_session()
    ec2_run = session.client("ec2")
    res = ec2_run.run_instances(
        ImageId="ami-0614680123427b75e",
        InstanceType="t2.micro",
        MaxCount=1,
        MinCount=1,
    )
    return res


def instance_id_list():
    """function to get list of all instance id"""
    session = get_session()
    ec2 = session.client("ec2")
    res = ec2.describe_instances()
    ins = res["Reservations"]
    ins_list = []
    for item in ins:
        for each_item in item["Instances"]:
            ins_list.append(each_item["InstanceId"])
    return ins_list


def ec2_stop(ins_id_list):
    """function to stop ec2 instance"""
    session = get_session()
    ec2 = session.client("ec2")
    response = ec2.stop_instances(InstanceIds=ins_id_list)
    res = response["ResponseMetadata"]["HTTPStatusCode"]
    return res


def ec2_start(ins_id_list):
    """function to start ec2 instance"""
    session = get_session()
    ec2 = session.client("ec2")
    response = ec2.start_instances(InstanceIds=ins_id_list)
    res = response["ResponseMetadata"]["HTTPStatusCode"]
    return res


def ec2_status(ins_id_list):
    "function to check status of ec2 instance"
    session = get_session()
    ec2_run = session.client("ec2")
    # res = ec2_run.describe_instance_status(InstanceIds=["i-0f98d971d2d43fa6a"])
    response = ec2_run.describe_instance_status(InstanceIds=ins_id_list)
    status = response["InstanceStatuses"]
    status_list = []
    for item in status:
        status_list.append(item["InstanceState"]["Name"])
    return status_list


def main():
    """main function to call the above defined function in the script"""
    # ec2_create()
    # print("Instance creation Started....")
    # time.sleep(20)
    ins_id = instance_id_list()
    for i in ins_id:
        status = ec2_status([i])  # Pass a list with the single ID
        # for sta in statuses:
        print(f"Instance {i} status: {status}")
        time.sleep(10)  # Sleep to avoid hitting API rate limits
        stop = ec2_stop([i])
        print(f"Stopping the instance: {i}")
        time.sleep(100)
        if stop == 200:
            print(f"Instance {i} stopped sucessfully")
        start = ec2_start([i])
        print(f"Starting the instance : {i}")
        if start == 200:
            print(f"Instance {i} started sucessfully")
        time.sleep(20)
        # status = ec2_status([i])
        # for sta in statuses:
        print(f"Instance {i} status: {status}")


if __name__ == "__main__":
    main()
