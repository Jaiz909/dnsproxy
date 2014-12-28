import os
from socket import inet_ntoa, inet_aton
from struct import pack, unpack
INDENT = '  '


def long2ip(ip):
    return inet_ntoa(pack("!L", ip))


def ip2long(ip_addr):
    return unpack("!L", inet_aton(ip_addr))[0]


def config_format(line, do_ident=True):
    if (do_ident):
        return INDENT + line + os.linesep
    return line + os.linesep


def port(protocol):
    if protocol == "http":
        return 80
    elif protocol == "https":
        return 443


def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]
