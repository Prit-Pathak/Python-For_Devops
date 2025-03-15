"""
Automation Script to list all the IAM Users in your Account.
"""

import boto3
import boto3.session


def iam_users() -> list:
    """function to get list of users"""
    aws_console = boto3.Session(profile_name="default")
    users = aws_console.client("iam")
    print(users)
    res = users.list_users()
    print(res)
    user_list = []
    for item in res["Users"]:
        user_list.append(item["UserName"])
    return user_list


def main():
    """main function to call the above defined function in the script"""
    res = iam_users()
    print(res)


if __name__ == "__main__":
    main()
