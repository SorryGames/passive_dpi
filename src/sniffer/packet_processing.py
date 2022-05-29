import time
import json
import threading

import sniffer.parsers


class PacketProcessing():
    """
    """

    PRINT_QUEUE_INFO_FREQ = 10
    PRINT_PACKET_STRUCTURE = 1

    def __init__(self):
        self.queue = []
        self.dst_db = None

        # run threads
        self._print_queue_info_thread = threading.Thread(target=self._print_queue_info)
        self._print_queue_info_thread.start()
        #
        self._process_packets_thread = threading.Thread(target=self._process_packets)
        self._process_packets_thread.start()


    def set_destination_database(self, database):
        self.dst_db = database


    def push(self, packet):
        # push packet to queue
        self.queue.append(packet)


    def _process(self):
        if len(self.queue) == 0:
            return None
        #
        return self.queue.pop(0)


    def _print_queue_info(self):
        while PacketProcessing.PRINT_QUEUE_INFO_FREQ >= 0:
            print("Raw packet queue info: Len={}".format(len(self.queue)))
            time.sleep(PacketProcessing.PRINT_QUEUE_INFO_FREQ)


    def _process_packets(self):
        while True:
            if len(self.queue) and self.dst_db is not None:
                packet = self._process()
                #
                # parsing packet
                if self._process_tcp_packet(packet=packet):
                    continue
                #


    def _process_tcp_packet(self, packet):
        #
        parsed_tcp = sniffer.parsers.parse_tcp_packet(data=packet)
        if parsed_tcp is None:
            return False
        #
        # DEBUG
        if PacketProcessing.PRINT_PACKET_STRUCTURE >= 0:
            self._print_packet(packet=parsed_tcp)
        #
        self.dst_db.update_tcp_session(
            src_ip=parsed_tcp["IP Header"]["Source Address"],
            dst_ip=parsed_tcp["IP Header"]["Destination Address"],
            src_port=parsed_tcp["TCP Header"]["Source Port"],
            dst_port=parsed_tcp["TCP Header"]["Destination Port"],                    
            payload=parsed_tcp["TCP Payload"],

            # custom attributes
            seqn=parsed_tcp["TCP Header"]["Seq number"],
            ackn=parsed_tcp["TCP Header"]["Ack number"],
        )
        #
        return True


    def _print_packet(self, packet):
        # 
        output_format = {}
        for key in packet.keys():
            if key in ["IP Header", "TCP Header", "Ethernet Header"]:
                output_format[key] = packet[key]
        #
        print("New packet arrived:")
        print("#" * 60)
        print(json.dumps(output_format, sort_keys=True, indent=4))
        print("#" * 60)
        print("\n" * 7)



