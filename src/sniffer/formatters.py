import json

def mac_address_formatter(hex_string):
    # should consist of 6 bytes
    if len(hex_string) != 12:
        return None
    #
    mac_addr = [ hex_string[i:i + 2] for i in range(0, 12, 2) ]
    mac_addr = ':'.join(mac_addr)
    return mac_addr


def ip_address_formatter(hex_string):
    # should consist of 4 bytes
    if len(hex_string) != 8:
        return None
    #
    ip_addr = [ str(int(hex_string[i:i + 2], 16)) for i in range(0, 8, 2) ]
    ip_addr = '.'.join(ip_addr)
    return ip_addr


def tcp_control_flags_formatter(value):
    flags = []
    #
    if value & 1:
        flags += ["FIN"]
    #
    if value & 2:
        flags += ["SYN"]
    #
    if value & 4:
        flags += ["RST"]
    #
    if value & 8:
        flags += ["PSH"]
    #
    if value & 16:
        flags += ["ACK"]
    #
    flags = " ".join(flags)
    return flags


