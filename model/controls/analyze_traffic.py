class TrafficAnalyzer:
    def __init__(self, traffic_data):
        self.traffic_data = traffic_data

    def tcp_speed(self):
        tcp_entries = [entry for entry in self.traffic_data if not entry.udp_or_tcp]
        total_tcp_speed = sum(entry.byte_size / entry.duration for entry in tcp_entries)
        avg_tcp_speed = total_tcp_speed / len(tcp_entries)

        return avg_tcp_speed

    def udp_speed(self):
        udp_entries = [entry for entry in self.traffic_data if entry.udp_or_tcp]
        total_udp_speed = sum(entry.byte_size / entry.duration for entry in udp_entries)
        avg_udp_speed = total_udp_speed / len(udp_entries)

        return avg_udp_speed
