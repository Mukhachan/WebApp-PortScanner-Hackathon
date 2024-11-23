def correct_ipe(ip: str) -> bool:
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
    return True

def correct_cidr(ip: str) -> bool:
    oshib = ValueError("Некорректная CIDR-нотация")
    if ip.find('/') == -1:
        raise oshib
    correct = ip.split('/')
    if len(correct) != 2:
        raise oshib
    correct_ipe(correct[0])
    try:
        x = int(correct[1])
        if not isinstance(x, int) and not (0 <= x <= 32):
            raise ValueError
    except:
        raise ValueError("В записи CIDR-нотации содержатся некорректные символы")
    return True
