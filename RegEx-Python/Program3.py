# 3. Companies in europe reports their financial numbers of semi annual basis
# and you can have a document like this.
# To exatract quarterly and semin annual period you can use a regex as shown
# below
import re

text = """
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
"""


def fyperiod(text):
    """function tha returns financial year and quarterly and semin annual period"""
    pat = r"FY(\d{4} .{2})"
    mat = re.findall(pat, text, re.IGNORECASE)
    return mat


def turnOver(text):
    pat = r"\$[0-9\.]+"
    mat = re.findall(pat, text)
    return mat


def main():
    year = fyperiod(text)
    money = turnOver(text)
    report = dict()
    for i in range(len(year)):
        report[year[i]] = money[i]
    print(f"report is : {report}")


if __name__ == "__main__":
    main()
