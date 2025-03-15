import requests
import json
import logging

url = "http://127.0.0.1:5000/api/check_even/10"

def set_log():
    logging.basicConfig(
        filename="api.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def hit_api(url):
    for i in range(1, 100):
        res = requests.get(url, timeout=2)
        try:
            if res.status_code == 200:
                logging.info(
                    f"request {i} has successfully completed : {res.status_code}"
                )
                logging.info(f"response: {res}")
            else:
                logging.error(
                    f"request {i} has failed due to error : {res.status_code}"
                )
        except requests.exceptions.RequestException as e:
            logging.error("request {i} failed due to error {e}", exec_info=True)


def main():
    set_log()
    logging.info(f"starting the api hitting")
    hit_api(url)
    logging.info("hitting completed ")


if __name__ == "__main__":
    main()
