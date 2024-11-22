from ipaddress import ip_network

def format_cidr(cdir_ip : str) -> list:
    network = ip_network(cdir_ip)
    ip_addresses = [network[x] for x in range(network.num_addresses) if x != 0 and x != network.num_addresses - 1]
    return ip_addresses

