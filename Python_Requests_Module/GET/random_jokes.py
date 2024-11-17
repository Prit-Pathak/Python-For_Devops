import requests
import random
import string

url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
# response = requests.get(url)
# print(response.text)


def getJokes(url):
    response = requests.get(url)
    res = response.json()
    data = res["data"]
    if res["success"] and "data" in res:
        cat = data["data"][0]["categories"]
        content = data["data"][0]["content"]
    else:
        raise Exception("failed to fetch the jokes data")

    return cat, content


def ran_email():
    email_length = 10
    domain_name = "gmail.com"
    email_str = "".join(
        random.choice(string.ascii_lowercase) for _ in range(email_length)
    )
    email = email_str + "@" + domain_name
    return email


def main():
    try:
        cat, con = getJokes(url)
        print(f"category : {cat} \ncontent : {con}")
    except Exception as e:
        print(str(e))

    print(ran_email())


if __name__ == "__main__":
    main()
