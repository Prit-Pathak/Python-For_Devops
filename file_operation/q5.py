"""
8. Monitor a log file for changes and print new entries in real-time
Input (log.txt, updated over time):
[2025-03-10 12:00:00] INFO: System started
[2025-03-10 12:05:00] WARNING: High CPU usage detected
New Log Entry (after a few minutes):
[2025-03-10 12:10:00] ERROR: Out of memory
"""

import time


def monitor_log(file_path):
    with open(file_path) as file:
        file.seek(0, 2)

        while True:
            pos = file.tell()
            line = file.readline()
            if line:
                print(line.strip())
            else:
                file.seek(pos)
                time.sleep(1)


monitor_log("file.txt")
C:\Users\rita6\Desktop\Python-For_Devops\file_operation\q5.py