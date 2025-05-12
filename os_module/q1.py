"""
🔹 Problem: Check disk usage and print a warning if it exceeds 80%.

✅ Expected Output -> Disk Usage: 85% (WARNING: Disk space is low!)

"""

import os
import shutil
import psutil

# print(psutil.cpu_times())
# print(psutil.cpu_percent(1))
# print(psutil.disk_usage("/"))


# print(f"0 => {psutil.cpu_percent(1)}")
# print(f"1 => {psutil.cpu_stats()}")
# print(f"2 => {psutil.cpu_count()}")
# print(f"3 => {psutil.cpu_freq()}")
# print()
# print(psutil.virtual_memory())
# print(psutil.virtual_memory().percent)
# print(psutil.virtual_memory().used / 1024**3)


# def disk_warn(path):
#     d_usage = psutil.disk_usage(path)
#     per_usage = d_usage.percent
#     return per_usage


# def cpu_warn():
#     cpu_usage = psutil.cpu_percent(1)  # gives o/p at interval of 1 sec
#     return cpu_usage


# def write2file(filename, per_usage):
#     with open(filename, "w") as file:
#         if per_usage > 80:
#             file.write(f"Disk Usage: {per_usage}% (WARNING: Disk space is low!)")
#             print(f"Disk Usage: {per_usage}% (WARNING: Disk space is low!)")
#         else:
#             file.write(f"Disk_usage: {per_usage}")
#             print(f"Disk_usage: {per_usage}")


# res = disk_warn("/")
# write2file("disk_usage.txt", res)
