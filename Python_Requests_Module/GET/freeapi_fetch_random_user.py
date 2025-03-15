import requests
import json

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"


def fetch_random_user(url):
    res = requests.get(url)
    print(res)
    data = res.json()
    print(data)
    user_data = data["data"]
    if data["success"] and "data" in data:
        u_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
    else:
        raise Exception("Failed to fetch the user data")
    return {u_name: country}


def main():
    try:
        user_details = fetch_random_user(url)
        print(user_details)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
