from collections import Counter


class TopNodesAnalyzer:
    def __init__(self, traffic_data):
        self.traffic_data = traffic_data

    def top_nodes_by_speed(self, num_nodes=10):
        node_speeds = Counter()

        for entry in self.traffic_data:
            node_speeds[entry.source_node] += entry.byte_size / entry.duration
            node_speeds[entry.destination_node] += entry.byte_size / entry.duration

        avg_speeds = {node: speed / 2 for node, speed in node_speeds.items()}
        sorted_nodes = sorted(avg_speeds.items(), key=lambda x: x[1], reverse=True)[:num_nodes]
        return sorted_nodes
