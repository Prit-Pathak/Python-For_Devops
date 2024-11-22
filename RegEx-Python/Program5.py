import re

text = "CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:"


def match(text):
    pat = r"CVSS:\d{1,9}.\d{1,9}(?:/[\w]+:[\w])*"
    mat = re.findall(pat, text)
    if mat:
        return True
    return False


if match(text):
    print("pattern is matched, lets move to next execution")
else:
    print("pattern not found")
