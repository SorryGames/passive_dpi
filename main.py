import socket
import dpkt
import binascii
import re

# custom
import parsers














if __name__ == "__main__":
    #
    #
    #
    try:
        s = socket.socket(family=socket.PF_PACKET, type=socket.SOCK_RAW, proto=socket.ntohs(3))
    except Exception as e:
        print(e)
        exit()
    #
    # session_database = TCPSessionDatabase
    #
    while True:
        # byte string (ascii)
        raw_data = s.recvfrom(65565)
        parsed_data = parsers.parse_http_packet(data=raw_data[0])
        #
        if parsed_data is None:
            continue
        #
        if True:
            parsers.formatters.tcp_packet_formatter(parsed_data)
            #
            #
            #
            #

