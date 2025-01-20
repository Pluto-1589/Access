# An IPv4 address is a string in the form a.b.c.d where a, b, c, and d are integers ("octets") between 0 and 255. For example, 127.0.0.1 is a valid IP address, but 300.0.0.1 is not and 123 is a valid octet but hello is not. The IPv4 address is split into four octets by three . (dots).

def is_valid_IPv4_octet(octet):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""

    if not octet:
        return False

    if not octet.isdigit():
        return False

    octet = int(octet)

    if octet > 255:
        return False
    elif octet < 0:
        return False
    return True


def is_valid_IPv4(ip):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    import re

    if not ip:
        return False

    p = r"(\d+\.){3}"

    if not re.match(p, ip):
        return False
    else:
        octets = ip.split(".")
        for octet in octets:
            if not is_valid_IPv4_octet(octet):
                return False

        return True


# An IPv6 address is a string in the form a:b:c:d:e:f:g:h where a, b, c, d, e, f, g, and h are hexadecimal numbers ("hextets") between 0 and FFFF. For example, 2001:0db8:85a3:0:0000:8a2e:0370:7334 is a valid IP address, but 2001:0db8:85a3:0:0000:8a2e:0370:7334:1234 is not (because it has one too many hextets) and ff3 is a valid hextet, but hello!!! is not. The IPv6 address is split into eight hextets by seven : (colons). Note that for this task, you can assume that IPv6 addresses always contain all eight hextets (ignoring the official specification, which allows trailing 0000 to be omitted). On the other hand, you must assume that individual hextets could be shorter than four characters (e.g.: 'FFF' is a valid hextet equivalent to '0FFF', just like 7 is a valid IPv4 octet equivalent to 007). Character casing should also be ignored.

def is_valid_IPv6_hextet(hextet):
    from string import punctuation
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""

    if not hextet:
        return False

    if len(hextet) > 4:
        return False

    if not all(c in "0123456789abcdefABCDEF" for c in hextet):
        return False

    return True


def is_valid_IPv6(ip):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    import re

    if not ip:
        return False

    p = r"(\d+?|\w+:){7}"

    if not re.match(p, ip):
        return False
    else:
        hextets = ip.split(":")

        for hextet in hextets:
            if not is_valid_IPv6_hextet(hextet):
                return False

        return True


def is_valid_IP(ip):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if "." in ip:
        return is_valid_IPv4(ip)
    elif ":" in ip:
        return is_valid_IPv6(ip)


# print(is_valid_IPv4_octet("123"))
# print(is_valid_IPv4("127.0.0.1"))
# print(is_valid_IPv4(" . . ."))


print(is_valid_IPv6_hextet("2f01"))
print(is_valid_IPv6("2001:0db8:85a3:0:0000:8a2e:0370:7334"))
print(is_valid_IPv6(":::::::"))
