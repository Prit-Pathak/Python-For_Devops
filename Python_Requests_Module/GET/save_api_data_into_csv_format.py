import requests
import json
import csv

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"


def fetch_random_user(url):
    res = requests.get(url)
    print(res)
    data = res.json()
    print(data)
    user_data = data["data"]
    # if data["success"] and "data" in data:
    # u_name = user_data["login"]["username"]
    # country = user_data["location"]["country"]

    # else:
    #     raise Exception("Failed to fetch the user data")
    return {
        "u_name": user_data["login"]["username"],
        "password": user_data["login"]["password"],
        "dob": user_data["dob"]["date"],
    }


def save2csv(user_details, filename="details.csv"):
    f_name = user_details.keys()
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=f_name)
        writer.writeheader()
        writer.writerow(user_details)
    print(f"User details saved successfully in {filename}")


def main():
    try:
        user_details = fetch_random_user(url)
        print(user_details)
        save2csv(user_details)  # Save to CSV
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
