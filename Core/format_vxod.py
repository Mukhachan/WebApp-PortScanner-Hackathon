from ipaddress import ip_network, ip_address

def format_cidr(cdir_ip : str) -> list:
    network = ip_network(cdir_ip)
    ip_addresses = [network[x] for x in range(network.num_addresses) if x != 0 and x != network.num_addresses - 1]
    return ip_addresses

def format_range(str_range : str) -> list:
    ip_start, ip_end = [x for x in str_range.split('-') if len(x) != 0]
    ip_start = [int(x) for x in ip_start.split('.')]
    ip_end = [int(x) for x in ip_end.split('.')]
    ip_start = ip_start[0] * 256 ** 3 + ip_start[1] * 256 ** 2 + ip_start[2] * 256 + ip_start[3]
    ip_end = ip_end[0] * 256 ** 3 + ip_end[1] * 256 ** 2 + ip_end[2] * 256 + ip_end[3]
    ip_addresses = [str(ip_address(x)) for x in range(ip_start, ip_end + 1)]
    return ip_addresses

print(format_range("192.168.1.1 - 192.168.3.3"))
