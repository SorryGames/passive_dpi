import re 



class PayloadWindow():
    """
    """

    WINDOW_SIZE = 5000


    def __init__(self):
        self.window = ""


    def put(self, content):
        self.window = self.window + content
        self._shrink()  # remove extra part from the beginning


    def _shrink(self):
        self.window = self.window[-PayloadWindow.WINDOW_SIZE:]


    def find(self, regex):
        try:
            return re.match(regex, self.window).groups()
        except Exception as e:
            print(e)  # TODO
            return []


    def __str__(self):
        return self.window