import json
import requests
import string
import random

base_url = "https://gorest.co.in"
auth_token = "Bearer d6ed757f96c934fa20e2157c95ecae0276a9d4a279b36c2a0078ac4cd3479121"


def ran_email():
    email_length = 10
    domain_name = "gmail.com"
    email_str = "".join(
        random.choice(string.ascii_lowercase) for _ in range(email_length)
    )
    email = email_str + "@" + domain_name
    return email


def POST(base_url):
    url = base_url + "/public/v2/users"
    print("get url: ", url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "P2p",
        # "email": "p2@etfertz-hermann.example",
        "email": ran_email(),
        "gender": "male",
        "status": "inactive",
    }
    response = requests.post(url, data=data, headers=headers)
    res_json = response.json()
    print("-->", res_json)
    json_str = json.dumps(res_json, indent=4)
    print("json POST response body: ", json_str)
    user_id = res_json["id"]
    print("user id ===>", user_id)
    assert response.status_code == 201
    assert res_json["name"] == "P2p"
    return user_id


def PUT(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("get url: ", url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "P12p",
        # "email": "p12@etfertz-hermann.example",
        "email": ran_email(),
        "gender": "male",
        "status": "active",
    }
    response = requests.put(url, data=data, headers=headers)
    res_json = response.json()
    print("-->", res_json)
    json_str = json.dumps(res_json, indent=4)
    print("json PUT response body: ", json_str)
    print("user id ===>", user_id)
    assert response.status_code == 201
    assert res_json["name"] == "P12p"
    assert res_json["id"] == user_id


def main():
    try:
        user_id = POST(base_url)
        PUT(user_id)

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
