import time
import parsers
from session_id_generator import SessionIDGenerator
from session_classes import TCPSession





class SessionTTL():
    """
    """

    TTL = 1000  # seconds

    def __init__(self, TTL):
        self.last_seen = 0
        self.make_online()


    def make_online(self):
        self.last_seen = int(time.time())


    def is_online(self):
        pass


class SessionDatabase():
    """
    """

    def __init__(self):
        self.database = {}
        self.ttl = {}



    def push_tcp_packet(self, src_ip, src_port, dst_ip, dst_port):
        session_id = SessionIDGenerator.get_tcp_session_id(
            src_ip=src_ip,
            dst_ip=dst_ip,
            src_port=src_port,
            dst_port=dst_port,
        )
        if session_id is None: 
            return False
        #
        #
        self.database[session_id] = TCPSession(
            src_ip=src_ip,
            dst_ip=dst_ip,
            src_port=src_port,
            dst_port=dst_port,
        )



    def _clear_irrelevant_sessions(self):
        pass

    def get_session(self):
        pass

    def rst_session(self):
        pass


