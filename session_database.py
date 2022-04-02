import parsers



class SessionDatabase():

    def __init__(self):
        self.database = []



    def create_session(self, session):
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
                "should_be_blocked": None,  # does session should be blocked according to policies
                "category_id": None,  # does session should be blocked according to policies
                "seqn": 0,  # sequence number
                "ackn": 0,  # acknowledge number
            },
        }
        #
        self.update(**kwargs)


    def update(self, **kwargs):
        if "raw_packet" in kwargs.keys():
            update_with = self.update_with_raw_packet(raw_packet=kwargs["raw_packet"])
        else:
            update_with = kwargs
        #
        try:
            for key in self.session.keys():
                self.session[key].update(update_with[key])
        except Exception as e:
            print(e)  # TODO 
            return False
        #
        return True


    def update_with_raw_packet(self, raw_packet):
        parsed_data = parsers.parse_http_packet(data=raw_packet)
        #
        if parsed_data is None:
            return None
        #
        session_update = {
            "server_info": {},
            "client_info": {},
            "session_info": {},
        }
        #
        #
        if parsed_data["TCP Header"]["Control Flags"] == "SYN":
            # write server_info & client_info
            session_update["client_info"] = {
                "ip": parsed_data["IP Header"]["Source Address"],
                "port": parsed_data["TCP Header"]["Source Port"],
            }
            session_update["server_info"] = {
                "ip": parsed_data["IP Header"]["Destination Address"],
                "port": parsed_data["TCP Header"]["Destination Port"],
            }
        if parsed_data.get("HTTP Host") is not None:
            session_update["session_info"] = {
                "http_host": parsed_data["HTTP Host"]
            }
        #
        if parsed_data.get("Application") is not None:
            session_update["session_info"] = {
                "application": parsed_data["Application"]
            }
        #
        if parsed_data.get("Application") is not None:
            session_update["session_info"] = {
                "application": parsed_data["Application"]
            }
        #
        session_update["session_info"]["seqn"] = parsed_data["TCP Header"]["Seq number"]
        session_update["session_info"]["ackn"] = parsed_data["TCP Header"]["Ack number"]
        #
        return session_update


    def get(self):
        return self.session