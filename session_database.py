import parsers



class SessionDatabase():

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



class TCPSession():
    """
    STRUCTURE = {
        server_info = {ip, port, http_host, ssl_servername, ...}
        client_info = {ip, port, ...}
        session_info = {
            application = (http, ssl, ftp, ...)
            seqn, ackn = 0, 0
            should_be_blocked = (True, False)
        }
    }
    """

    def __init__(self, **kwargs):
        """
        PURPOSE
        + create a session using raw network packet (from ethernet header to application payload)
        + or create an empty session and update it with another dict object

        ARGS 
        +   (1) pass any dict object which will be used to update self.session
        +   (2) pass { "raw_packet": <bytes object> } to update self.session

        """

        self.session = {
            "server_info": {  
                "ip": None,
                "port": None,  # new attributes can be added dynamically (for example http_host)
            },
            "client_info": {
                "ip": None,
                "port": None,  # new attributes can be added dynamically (for example mac_address)
            },
            "session_info": {
                "application": None,  # http, ftp, ssh, telnet, ...
                "should_be_blocked": False,  # does session should be blocked according to policies
                "seqn": 0,  # sequence number
                "ackn": 0,  # acknowledge number
            },
        }
        #
        self.update(**kwargs)
    

    def update(self, **kwargs):
        if "raw_packet" in kwargs.keys():
            pass
        else:
            pass


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
        return session

    def update(self, session):
        pass

