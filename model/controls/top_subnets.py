from collections import Counter


class TopSubnetsAnalyzer:
    def __init__(self, traffic_data):
        self.traffic_data = traffic_data

    def top_subnets_by_sessions(self, num_subnets=10):
        subnet_sessions = Counter()

        for entry in self.traffic_data:
            source_subnet = '.'.join(entry.source_node.split('.')[:-1])
            destination_subnet = '.'.join(entry.destination_node.split('.')[:-1])
            subnet_sessions[source_subnet] += 1
            subnet_sessions[destination_subnet] += 1

        sorted_subnets = subnet_sessions.most_common(num_subnets)
        return sorted_subnets
