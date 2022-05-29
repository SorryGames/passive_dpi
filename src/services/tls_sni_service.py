from database.session_classes import TCPSession


class TLSService():
    """
    the task to export TLS SNI (server name indication) value from the TCP payload
    """


    TLS_SNI_REGEX = '.*Host:\\s*([\\w\\.]*).*'

    def __init__(self):
        pass


    def run(self, session):
        """
        suppose to work with DatabaseEntry class
        """

        # check if we are working with TCP session class
        if not isinstance(session.get_session(), TCPSession):
            return False
        #
        result = session.get_session().get_payload().find(TLSService.TLS_SNI_REGEX)
        if not len(result):
            return False
        #
        # export tls_sni and save it to TCPSession instance 
        tls_sni = result[-1]
        session.get_session().update_with_attribute(key="tls_sni", value=tls_sni)
        #
        return True
