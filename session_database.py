import parsers



class SessionDatabase():
    """
    
    """

    def __init__(self):
        self.database = {}


    def create_session(self, session):
        pass

    def _generate_session_id(self, session_object):
        session_string = " ".join([
            session_object["client_info"]["ip"],
            session_object["client_info"]["port"],
            session_object["server_info"]["ip"],
            session_object["server_info"]["port"],
        ])
        #
        return hashlib.sha1(session_string)

    def delete_session(self):
        pass

    def get_session(self):
        pass

    def rst_session(self):
        pass


