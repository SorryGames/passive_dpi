import re
import struct
import formatters

def parse_ethernet_header(data):
    try:
        header_parts = struct.unpack("!6s6s2s", data)
        parsed_data = {
            "Destination Mac": formatters.mac_address_formatter(header_parts[0].hex()),
            "Source Mac": formatters.mac_address_formatter(header_parts[1].hex()),
            "Ethertype": "0x" + header_parts[2].hex()
        }
    except:
        parsed_data = {}
    #
    return parsed_data



def parse_ip_header(data):
    try:
        header_parts = struct.unpack("!BBHHHBBH4s4s", data)
        parsed_data = {
            "Version": int(header_parts[0]) >> 4, # 1 byte = version (4 bits) + header length (4 bits)
            "Header Length": (header_parts[0] & 15) * 4,
            "TTL": header_parts[5],
            "Protocol": header_parts[6],
            "Source Address": formatters.ip_address_formatter(header_parts[8].hex()),
            "Destination Address": formatters.ip_address_formatter(header_parts[9].hex())
        }
    except: 
        parsed_data = {}
    #
    return parsed_data


def parse_tcp_header(data):
    try:
        header_parts = struct.unpack("!HHLLHHHH", data)
        parsed_data = {
            "Source Port": header_parts[0],
            "Destination Port": header_parts[1],
            "Seq number": header_parts[2],
            "Ack number": header_parts[3],
            "Header Length": (header_parts[4] >> 12) * 4,
            "Control Flags": formatters.tcp_control_flags_formatter(int(header_parts[4]) & 31),
            "Window Size": header_parts[5],
            "Checksum": header_parts[6],
            "Urgent pointer": header_parts[7],
        }
    except Exception as e: 
        print(e)
        parsed_data = {}
    #
    return parsed_data











def parse_http_packet(data):
    data_to_process = data
    parsed_data = {}
    #
    #
    header = parse_ethernet_header(data=data_to_process[:14])
    if header.get("Ethertype") == "0x0800":
        data_to_process = data_to_process[14:]
        parsed_data["Ethernet Header"] = header
    else:
        return None
    #
    #
    header = parse_ip_header(data=data_to_process[:20])
    if header.get("Protocol") == 6:
        data_to_process = data_to_process[header["Header Length"]:]
        parsed_data["IP Header"] = header
    else:
        return None
    #
    #
    header = parse_tcp_header(data=data_to_process[:20])
    data_to_process = data_to_process[header["Header Length"]:]
    parsed_data["TCP Header"] = header
    #
    #
    parsed_data["TCP Payload"] = ""
    try:
        parsed_data["TCP Payload"] = data_to_process.decode("utf-8").replace("\r\n", " ")
    except Exception as e:
        pass
    #
    #
    regex_match = re.match(".*Host:\\W*([\\w\\.]*).*", parsed_data["TCP Payload"])
    if regex_match is not None:
        parsed_data["Application"], parsed_data["HTTP Host"] = ('http', regex_match.group(1))
    #
    #
    return parsed_data