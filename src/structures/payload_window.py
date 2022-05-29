import re 



class PayloadWindow():
    """
    """

    WINDOW_SIZE = 500


    def __init__(self):
        self.window = bytes()


    def put(self, content):
        self.window = self.window + content
        self._shrink()  # remove extra part from the beginning


    def _shrink(self):
        self.window = self.window[-PayloadWindow.WINDOW_SIZE:]


    def find(self, regex):
        try:
            matches = re.match(regex, self.window, re.IGNORECASE)
            if matches is None:
                return ()
            #
            return matches.groups()
        except Exception as e:
            print(e)  # TODO
            return ()


    def __str__(self):
        return str(self.window)