from collections import defaultdict
import parsers



class TCPSessionDatabase():

	def __init__(self):
		self.database = []



    def create_session(self, session):
		self.database[srcip]
		pass

	def delete_session(self):
		pass

	def get_session(self):
		pass

	def rst_session(self):
		pass



class Session():

    def __init__(self, raw_packet=None):
        self.session = None
        #
        if raw_packet is not None:
            self.session = self.parse_raw_packet(raw_packet)


    def parse_raw_packet(self, raw_packet):
        parsed_data = parsers.parse_http_packet(data=raw_packet)
        #
        if parsed_data is None:
            return None
        #
        #
        #
        srcip = parsed_data["IP Header"]["Source Address"]
        dstip = parsed_data["IP Header"]["Destination Address"]
        #
        proto = parsed_data["IP Header"]["Protocol"]
        #
        srcport = parsed_data["TCP Header"]["Source Port"]
        dstport = parsed_data["TCP Header"]["Destination Port"]
        #
        seqn = parsed_data["TCP Header"]["Seq number"]
        ackn = parsed_data["TCP Header"]["Ack number"]
        #
        #
        #
        session[srcip] = {}
        session[srcip][dstip] = {}
        session[srcip][dstip][srcport] = {}
        session[srcip][dstip][srcport][dstport] = {}
        session[srcip][dstip][srcport][dstport][proto] = {
            "seqn": seqn,
            "ackn": ackn,
            "application": "",
            "hostname": "",
        }
        #
        return session

    def update(self, session):
        pass