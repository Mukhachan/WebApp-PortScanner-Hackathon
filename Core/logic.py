import socket
from datetime import datetime
import sys
from data_ports import ports
def scan_all_ports(api_to_scan : str) -> dict:
    all_ports = dict()
    ip = socket.gethostbyname(api_to_scan)
    for port in ports:
        cont = socket.socket()
        cont.settimeout(1)
        try:
            cont.connect((ip, port))
        except socket.error:
            all_ports[port] = "Закрыт"
        else:
            all_ports[port] = "Открыт"
            # print(f"{socket.gethostbyname(ip)}:{str(port)} is open/{ports[port]}")
            cont.close()
    all_ports_sorted = {x[0]: x[1] for x in sorted(all_ports.items(), key = lambda item: item[1] == "Закрыт")}
    return all_ports_sorted
    # input("Press Enter to the exit....")

print(scan_all_ports("192.168.161.191"))




