from database.session_classes import TCPSession


class HTTPService():
    """
    the task to export HTTP Host value from the TCP payload
    """


    HTTP_HOST_REGEX = '.*Host:\\s*([\\w\\.]*).*'

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
        result = session.get_session().get_payload().find(HTTPService.HTTP_HOST_REGEX)
        if not len(result):
            return False
        #
        # export http_host and save it to TCPSession instance 
        http_host = result[-1]
        session.get_session().update_with_attribute(key="http_host", value=http_host)
        #
        return True
