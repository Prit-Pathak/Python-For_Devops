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
    res = res.strip().split()

    # res = res.strip().split(",")
    feq = {}
    for word in res:
        feq[word] = feq.get(word, 0) + 1

    print(feq)


read_file("file.txt")
