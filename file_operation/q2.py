"""
2. Parse a log file and extract error messages with timestamps
Input (log.txt):
[2025-03-10 10:00:00] INFO: System started
[2025-03-10 10:05:30] ERROR: Disk failure
[2025-03-10 10:10:15] ERROR: Network timeout
Expected Output:
2025-03-10 10:05:30 - Disk failure
2025-03-10 10:10:15 - Network timeout

"""

import re


def parse_error(file_name):
    with open(file_name) as file:
        res = file.read()
    res = res.strip()
    pat = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] ERROR: [^\n]+"
    out = re.findall(pat, res)
    print(out)


parse_error("file.txt")
