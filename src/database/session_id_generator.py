import hashlib


class SessionIDGenerator:
    """
    """



    def get_tcp_session_id(src_ip, src_port, dst_ip, dst_port):
        src, dst = str(src_ip) + ":" + str(src_port), str(dst_ip) + ":" + str(dst_port)
        #    
        string_to_hash = "TCP[" + min(src, dst) + "][" + max(src, dst) + "]"
        try:
            hash_result = hashlib.sha1(bytes(string_to_hash, encoding="ascii")).hexdigest()
        except Exception as e: 
            print(e)  # TODO
            return None
        #
        return hash_result
