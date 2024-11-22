import sys
from logic import scan_all_ports
from format_vxod import format_cidr, format_range
from datetime import datetime
from correct_input import correct_ipe, correct_cidr
import re

vxod = [x for x in re.split(r"[;,\s]", input()) if len(x) != 0]
format_vxod = []

for i in range(len(vxod) - 1):
    if "/" in vxod[i]:
        correct_cidr(vxod[i])
        format_vxod.extend(format_cidr(vxod[i]))
    if "-" in vxod[i]:
        try:
            correct_ipe(vxod[i - 1])
            correct_ipe(vxod[i + 1])
            format_vxod.extend(format_range(vxod[i - 1], vxod[i + 1]))
        except IndexError:
            raise IndexError("Некорректные входные данные")
    correct_ipe(vxod[i])
    format_vxod.append(vxod[i])
    



