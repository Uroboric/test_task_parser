from dataclasses import dataclass


@dataclass
class TrafficEntry:
    source_node: str
    source_mac: str
    destination_node: str
    destination_mac: str
    udp_or_tcp: bool
    byte_size: int
    duration: float
