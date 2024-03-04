from model.data.data_classes import TrafficEntry
from typing import List


class MetricsCalculator:
    @staticmethod
    def calculate_unique_nodes(traffic_data: List[TrafficEntry]) -> int:
        unique_nodes = set(entry.source_node for entry in traffic_data) | set(entry.destination_node for entry in traffic_data)
        return len(unique_nodes)

    @staticmethod
    def calculate_average_speed(traffic_data: List[TrafficEntry]) -> float:
        total_speed = sum(entry.byte_size / entry.duration for entry in traffic_data)
        total_entries = len(traffic_data)
        return total_speed / total_entries
