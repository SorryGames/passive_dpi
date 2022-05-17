import socket
import dpkt
import binascii

# custom
import parsers
import session_database
import packet_processing













if __name__ == "__main__":
    #
    #
    # sniffer init
    try:
        s = socket.socket(family=socket.PF_PACKET, type=socket.SOCK_RAW, proto=socket.ntohs(3))
    except Exception as e:
        print(e)
        exit()
    #
    #
    # create PacketProcessing instance
    processing = packet_processing.PacketProcessing()


    # session_database = TCPSessionDatabase
    #
    while True:
        # byte string (ascii)
        raw_data = s.recvfrom(65565)
        processing.push(raw_data[0])

















        # parsed_data = parsers.parse_http_packet(data=raw_data[0])
        # #
        # if parsed_data is None:
        #     continue
        # #
        # # if True:
        # if parsed_data["TCP Header"]["Destination Port"] == 80 or parsed_data["TCP Header"]["Source Port"] == 80:
        #     parsers.formatters.tcp_packet_formatter(parsed_data)
        #     #
        #     session = session_database.TCPSession(raw_packet=raw_data[0])
        #     print(session.get())
        #     #
        #     #
        #     #

