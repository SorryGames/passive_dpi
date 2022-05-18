import time
from payload_window import PayloadWindow



class TCPSession():
    """
    structure of class is the following:
    {
        src_ip: x.x.x.x
        src_port: XXXXX

        dst_ip: y.y.y.y
        dst_port: YYYYY
        
        tcp_payload: PayloadWindow()
        custom: {
            **custom key-value pairs**
        }
    }

    """

    TTL = 300  # seconds

    def __init__(self, src_ip, src_port, dst_ip, dst_port, tcp_payload=""):
        self.src_ip = src_ip
        self.src_port = src_port
        #
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        #
        self.tcp_payload = PayloadWindow()
        self.update_with_payload(tcp_payload=tcp_payload)
        #
        self.custom = {}


    def update_with_payload(self, tcp_payload):
        self.tcp_payload.put(content=tcp_payload)
        return True


    def update_with_attribute(self, key, value=None):
        self.custom[key] = value
        return True

