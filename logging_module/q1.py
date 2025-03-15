"""
write a python script that errors logs to a file usinf exception handling
"""

import logging


def set_log():
    logging.basicConfig(
        filename="program.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def div(a, b):
    logging.info("staring calculation")
    try:
        res = a / b
        # return res
        logging.info(f"division success:  {res}")
    except ZeroDivisionError as e:
        logging.error("zero division error", exc_info=True)


def main():
    set_log()
    logging.debug("program started")
    div(10, 2)
    div(10, 5)
    div(10, 0)
    logging.debug("program executed")


if __name__ == "__main__":
    main()
