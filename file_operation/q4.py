"""
4. Swap columns dynamically in a CSV file
Input (data.csv):
id,name,score
1,Alice,85
2,Bob,90
3,Charlie,78
User Input:
Enter columns to swap (comma-separated, e.g., name,score): name,score
Expected Output:
id,score,name
1,85,Alice
2,90,Bob
3,78,Charlie

"""

import csv


def swap_field(f_name):
    with open(f_name) as file:
        res = file.readlines()
    res = [item.strip().split(",") for item in res]
    print(f"res-> {res}")
    for item in res:
        # print(item[2])
        item[1], item[2] = item[2], item[1]
    print(f"swappp-> {res}")
    return res


def write2csv(file, res):
    with open(file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(res)


res = swap_field("data.csv")

write2csv("data3.csv", res)
