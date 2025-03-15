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


print(psutil.cpu_percent(1))
print(psutil.cpu_stats())
print(psutil.cpu_count())
print(psutil.cpu_freq(1))
print()
print(psutil.virtual_memory()[2])
print(psutil.virtual_memory()[3] / 1000000000)


# def disk_warn(path):
#     d_usage = psutil.disk_usage(path)
#     per_usage = d_usage.percent
#     return per_usage

# def cpu_warn():
#     cpu_usage = psutil.cpu
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
