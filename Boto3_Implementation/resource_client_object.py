"""
Automation Script to list all the IAM Users in your Account.
"""

import boto3
import boto3.session


def iam_users() -> list:
    """function to get list of users usig Resource Object"""
    aws_console = boto3.Session(profile_name="default")
    iam = aws_console.resource("iam")
    print(f"----> {iam}")
    user_list = []
    for user in iam.users.all():
        user_list.append(user.name)
    return user_list


def main():
    """main function to call the above defined function in the script"""
    res = iam_users()
    print(res)


if __name__ == "__main__":
    main()
