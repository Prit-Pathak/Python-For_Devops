"""
3. Reverse the rows in a CSV file while keeping the header intact
Input (data.csv):
id,name,score
1,Alice,85
2,Bob,90
3,Charlie,78
Expected Output:
id,name,score
3,Charlie,78
2,Bob,90
1,Alice,85

"""

import csv


def rev_row(f_name):
    with open(f_name) as file:
        res = file.readlines()
    res = [item.strip().split() for item in res]
    print(f"res-> {res}")
    rev_res = [res[0]] + res[1:][::-1]
    print(f"rev res => {rev_res}")
    return rev_res


def write2csv(filename, res):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(res)


data = rev_row("data.csv")
write2csv("data1.csv", data)
