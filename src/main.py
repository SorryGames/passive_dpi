import socket
import dpkt
import binascii

# custom
import database.session_database
import sniffer.packet_processing
import services.http_host_service













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
    processing = sniffer.packet_processing.PacketProcessing()
    session_db = database.session_database.SessionDatabase()
    http_service = services.http_host_service.HTTPService()
    #
    # session_db.subscribe_service_for_updates(method_to_execute=http_service.run)
    processing.set_destination_database(database=session_db)
    #
    while True:
        # byte string (ascii)
        raw_data = s.recvfrom(65565)
        processing.push(raw_data[0])









