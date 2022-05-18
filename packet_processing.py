import time
import json
import parsers
import threading
from session_database import SessionDatabase





class PacketProcessing():
    """
    """

    PRINT_QUEUE_INFO_FREQ = 60

    def __init__(self):
        self.queue = []

        # run threads
        self._print_queue_info_thread = threading.Thread(target=self._print_queue_info)
        self._print_queue_info_thread.start()
        #
        self._process_packets_thread = threading.Thread(target=self._process_packets)
        self._process_packets_thread.start()



    def push(self, packet):
        # push packet to queue
        self.queue.append(packet)


    def _process(self):
        if len(self.queue) == 0:
            return None
        #
        return self.queue.pop(0)


    def _print_queue_info(self):
        while True:
            print("Raw packet queue info: Len={}".format(len(self.queue)))
            time.sleep(PacketProcessing.PRINT_QUEUE_INFO_FREQ)


    def _process_packets(self):
        while True:
            if len(self.queue):
                packet = self._process()
                #
                # parsing packet
                parsed_tcp = parsers.parse_tcp_packet(data=packet)
                if parsed_tcp is None:
                    continue
                #
                #
                #
            # src_ip=parsed_tcp["IP Header"]["Source Address"],
            # dst_ip=parsed_tcp["IP Header"]["Destination Address"],
            # src_port=parsed_tcp["TCP Header"]["Source Port"],
            # dst_port=parsed_tcp["TCP Header"]["Destination Port"],

                #
                #
                #



    def _print_packet(self, packet):
        print("New packet arrived:")
        print("#" * 60)
        print(json.dumps(packet, sort_keys=True, indent=4))
        print("#" * 60)
        print("\n" * 7)



