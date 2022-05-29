import time
import json
import threading

from database.session_id_generator import SessionIDGenerator
from database.session_classes import TCPSession





class DatabaseEntry():
    """
    """

    TTL = 300  # seconds

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

    PRINT_TABLE_FREQ = 10
    CLEAR_TABLE_FREQ = 60


    def __init__(self):
        self.database = {}
        self.services = []
        #
        self._print_database = threading.Thread(target=self._print_database)
        self._print_database.start()
        #
        self._database_clear_process = threading.Thread(target=self._remove_irrelevant_sessions)
        self._database_clear_process.start()
        #


    def subscribe_service_for_updates(self, method_to_execute):
        self.services.append(method_to_execute)


    def update_tcp_session(self, src_ip, src_port, dst_ip, dst_port, payload="", **kwargs):
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
        for key, value in kwargs.items():
            self.database[session_id].get_session().update_with_attribute(key=key, value=value)
        #
        #
        # execute subscribed services 
        for service in self.services:
            try:
                # execute service
                service(session=self.database[session_id])
            except Exception as e: 
                print(e)  # TODO
        #
        return True


    def _remove_irrelevant_sessions(self):
        assert SessionDatabase.CLEAR_TABLE_FREQ >= 0, "CLEAR_TABLE_FREQ should have a positive value"
        while True:
            removed_sessions = 0
            for session_id in self.database.keys():
                if self.database[session_id].is_online == False:
                    self.database.pop(session_id)
                    removed_sessions += 1
            #
            #
            print("SessionDatabase._remove_irrelevant_sessions: {} sessions were cleared (age > TTL)".format(
                                                                                            removed_sessions))
            time.sleep(SessionDatabase.CLEAR_TABLE_FREQ)


    def get_session(self):
        pass


    def _print_database(self):
        while SessionDatabase.PRINT_TABLE_FREQ >= 0:
            keys = list(self.database.keys())
            for key in keys:
                print("#" * 60)
                print(key)
                print(self.database[key])
                print("#" * 60)
                print("\n" * 7)
            #
            time.sleep(SessionDatabase.PRINT_TABLE_FREQ)