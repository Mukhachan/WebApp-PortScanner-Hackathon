from ipaddress import ip_network, ip_address
import re
from sys import stdin
class Read_vxod:
    def __init__(self):
        vxod = [x for x in re.split(r"[;,\s+]", str(stdin.readlines())) if len(x) != 0]
        self.__ip_address = []
        for i in range(len(vxod) - 1):
            if "/" in vxod[i]:
                self.format_cidr(vxod[i])
            if "-" in vxod[i]:
                try:
                    self.format_range(vxod[i - 1], vxod[i + 1])
                except IndexError:
                    raise IndexError("Некорректные входные данные")
                except:
                    raise
            self.format_ip(vxod[i])
    def format_cidr(self, cdir_ip: str) -> None:
        self.correct_cidr(cdir_ip)
        network = ip_network(cdir_ip)
        ip_addresses = [network[x] for x in range(network.num_addresses) if x != 0 and x != network.num_addresses - 1]
        self.__ip_address.extend(ip_addresses)

    def format_range(self, ip_start: str, ip_end: str) -> None:
        self.correct_ipe(ip_start, ip_end)
        ip_start = [int(x) for x in ip_start.split('.')]
        ip_end = [int(x) for x in ip_end.split('.')]
        ip_start = ip_start[0] * 256 ** 3 + ip_start[1] * 256 ** 2 + ip_start[2] * 256 + ip_start[3]
        ip_end = ip_end[0] * 256 ** 3 + ip_end[1] * 256 ** 2 + ip_end[2] * 256 + ip_end[3]
        ip_addresses = [str(ip_address(x)) for x in range(ip_start, ip_end + 1)]
        self.__ip_address.extend(ip_addresses)
    def format_ip(self, ip: str) -> None:
        self.correct_ipe(ip)
        self.__ip_address.append(ip)
    def correct_ipe(self, *ip_adreses: list[str]) -> None:
        for ip in ip_adreses:
            oshib = ValueError("Некорректный айпиадрес")
            if ip.count('.') != 3:
                raise oshib
            correct = ip.split('.')
            try:
                for x in correct:
                    x = int(x)
                    if not (0 <= x <= 254):
                        raise ValueError
            except:
                raise ValueError("В айпиадресе содержатся некорретные символы")

    def correct_cidr(self, ip: str) -> None:
        oshib = ValueError("Некорректная CIDR-нотация")
        if ip.find('/') == -1:
            raise oshib
        correct = ip.split('/')
        if len(correct) != 2:
            raise oshib
        self.correct_ipe(correct[0])
        try:
            x = int(correct[1])
            if not isinstance(x, int) and not (0 <= x <= 32):
                raise ValueError
        except:
            raise ValueError("В записи CIDR-нотации содержатся некорректные символы")
    @property
    def ip_address(self) -> list:
        return self.__ip_address



