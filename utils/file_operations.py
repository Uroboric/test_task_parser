from model.data.data_classes import TrafficEntry


def read_traffic_data(file_path):
    traffic_data = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(';')
            if len(data) == 7:
                traffic_entry = TrafficEntry(
                    source_node=data[0],
                    source_mac=data[1],
                    destination_node=data[2],
                    destination_mac=data[3],
                    udp_or_tcp=data[4] == 'true',
                    byte_size=int(data[5]),
                    duration=float(data[6])
                )
                traffic_data.append(traffic_entry)
    return traffic_data
