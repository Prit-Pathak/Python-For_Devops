"""
Read a CSV file without using any libraries and fix the mapping between name and email
name,email
abhishek,soham@e.com
shubham,abhishek@gmail.com
soham,shubham@outlook.com
Read CSV file without libraries
"""


def correct_mapping(file_name):
    """
    time complexity -> O(Nlogn) + O(N**2) --> O(N)
    space complexity -> O(n)
    """
    with open(file_name) as file:
        lines = file.readlines()
    header = lines[0].strip().split(",")
    data = [line.strip().split(",") for line in lines[1:]]

    names = sorted(set(item[0] for item in data))  # O(nlogn)
    cor_mapp = {}
    for name in names:  # O(n)
        for per, email in data:  # O(n)
            if name in email:
                cor_mapp[name] = email
    return cor_mapp


file_name = "details.csv"
res = correct_mapping(file_name)
print(res)
