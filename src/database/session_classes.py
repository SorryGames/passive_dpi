import time
import json


from structures.payload_window import PayloadWindow



class TCPSession():
    """
    structure of class is the following:
    {
        src_ip: x.x.x.x
        src_port: XXXXX

        dst_ip: y.y.y.y
        dst_port: YYYYY
        
        payload: PayloadWindow()
        custom: {
            **custom key-value pairs**
        }
    }

    """

    def __init__(self, src_ip, src_port, dst_ip, dst_port, payload=""):
        self.src_ip = src_ip
        self.src_port = src_port
        #
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        #
        self.payload = PayloadWindow()
        self.update_with_payload(payload=payload)
        #
        self.attributes = {}


    def update_with_payload(self, payload):
        self.payload.put(content=payload)
        return True


    def update_with_attribute(self, key, value=None):
        self.attributes[key] = value
        return True


    def get_source(self):
        return (self.src_ip, self.src_port)


    def get_destination(self):
        return (self.dst_ip, self.dst_port)


    def get_payload(self):
        return self.payload


    def get_attributes(self):
        return self.attributes


    def get_session_info(self):
        session_info = {
            "Src IP/Port": "{}:{}".format(*self.get_source()),
            "Dst IP/Port": "{}:{}".format(*self.get_destination()),
            "TCP Payload": str(self.get_payload()),
            "Attributes": self.get_attributes(),
        }
        return session_info


    def __str__(self):        
        return json.dumps(self.get_session_info(), sort_keys=True, indent=4)
