import time
import json
import parsers
import threading

from session_id_generator import SessionIDGenerator
from session_classes import TCPSession





class DatabaseEntry():
    """
    """

    TTL = 1000  # seconds

    def __init__(self, session_object):
        self.session_object = session_object 
        #
        self.last_seen = 0
        self.make_online()


    def make_online(self):
        self.last_seen = int(time.time())


    def is_online(self):
        return DatabaseEntry.TTL > (int(time.time()) - self.last_seen)


    def get_session(self):
        return self.session_object


    def get_entry_info(self):
        entry_info = {
            "is_online": self.is_online(),
            "age": int(time.time()) - self.last_seen,
            "ttl": DatabaseEntry.TTL,
            "session_object_type": str(type(self.session_object)),
            "session_object": self.session_object.get_session_info(),
        }
        return entry_info


    def __str__(self):
        return json.dumps(self.get_entry_info(), sort_keys=True, indent=4)




class SessionDatabase():
    """
    """

    def __init__(self):
        self.database = {}
        self._print_database = threading.Thread(target=self._print_database)
        self._print_database.start()


    def update_tcp_session(self, src_ip, src_port, dst_ip, dst_port, payload=""):
        session_id = SessionIDGenerator.get_tcp_session_id(
            src_ip=src_ip,
            dst_ip=dst_ip,
            src_port=src_port,
            dst_port=dst_port,
        )
        if session_id is None:
            return False
        #
        if session_id not in self.database:
            self.database[session_id] = DatabaseEntry(
                session_object = TCPSession(
                    src_ip=src_ip,
                    dst_ip=dst_ip,
                    src_port=src_port,
                    dst_port=dst_port,
                )
            )
        #
        self.database[session_id].make_online()
        self.database[session_id].get_session().update_with_payload(payload=payload)
        #


    def _clear_irrelevant_sessions(self):
        pass

    def get_session(self):
        pass

    def _print_database(self):
        while True:
            keys = list(self.database.keys())
            for key in keys:
                print("#" * 60)
                print(key)
                print(self.database[key])
                # print(json.loads(str(self.database[key]), sort_keys=True, indent=4))
                print("#" * 60)
                print("\n" * 7)

            time.sleep(5)