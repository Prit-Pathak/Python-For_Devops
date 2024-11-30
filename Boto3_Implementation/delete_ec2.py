"""Function to terminate the ec2 instances"""

import boto3
import boto3.session
import time


def get_session():
    """created session with aws (aws consle login programetically)"""
    session = boto3.Session(profile_name="default")
    return session


def ec2_instance_id_list():
    """function to get list of all instance id"""
    session = get_session()
    ec2 = session.client("ec2")
    res = ec2.describe_instances()
    ins = res["Reservations"]
    ins_id_list = []
    for item in ins:
        for each_item in item["Instances"]:
            str_item = str(each_item["InstanceId"])
            ins_id_list.append(str_item)
    return ins_id_list


def del_ec2(ins_id_list):
    """function to delete the ec2 instances"""
    session = boto3.Session(profile_name="default")
    ec2 = session.client("ec2")
    # res = ec2.terminate_instances(InstanceIds=['string'])
    res = ec2.terminate_instances(InstanceIds=ins_id_list)


def main():
    """main function to call the above defined function in the script"""
    ins_id = ec2_instance_id_list()
    print(ins_id)
    print(type(ins_id))
    for i in ins_id:
        print(f"Deleting instance: {i}")
        rm = del_ec2([i])
        print(rm)
        time.sleep(50)


if __name__ == "__main__":
    main()
