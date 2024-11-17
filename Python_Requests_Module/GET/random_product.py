import requests
import json

url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"


def get_rand_product(url, nums):
    res = requests.get(url)
    data = res.json()
    product_data = data["data"]
    dct = dict()
    if data["success"] and "data" in data:
        for i in range(nums):
            title = product_data["data"][i]["title"]
            price = product_data["data"][i]["price"]
            dct[title] = price

    else:
        raise Exception("failed to fetch the data")
    return dct


def main():
    try:
        res = get_rand_product(url, 8)
        print(f"{res}")
        total = 0
        count = 0
        for k, v in res.items():
            total += v
            count += 1
        avg = total / count
        print(f"avg Price is : {avg}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
