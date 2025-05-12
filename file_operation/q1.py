""" "
1. Read a text file and count the occurrence of each word
Input (file.txt):
hello world
hello Python
hello world
Expected Output:
hello: 3
world: 2
Python: 1
"""


def read_file(file_name):
    with open(file_name) as file:
        res = file.read()
    print(f"res --->> {res}")
    res = res.strip().split()
    print(f"============={res}")

    # res = res.strip().split(",")
    feq = {}
    for word in res:
        feq[word] = feq.get(word, 0) + 1

    print(feq)
    maxi = float("-inf")
    max_item = None
    for k, v in feq.items():
        if v > maxi:
            maxi = v
            max_item = k
    print(f"1111111111111=> {max_item}")


read_file("C:/Users/rita6/Desktop/Python-For_Devops/file_operation/file1.csv")
