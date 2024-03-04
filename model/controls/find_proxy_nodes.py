class ProxyFinder:
    def __init__(self, traffic_data):
        self.traffic_data = traffic_data

    def find_proxy_nodes(self):
        send_receive_pairs = {}
        proxies = set()

        for record in self.traffic_data:
            key = (record.source_node, record.destination_node, record.udp_or_tcp)

            if key not in send_receive_pairs:
                send_receive_pairs[key] = {'send': set(), 'receive': set()}

            send_receive_pairs[key]['send'].add(record.source_mac)
            send_receive_pairs[key]['receive'].add(record.destination_mac)

        for key, pairs in send_receive_pairs.items():
            if pairs['send'].intersection(pairs['receive']):
                proxies.add(key[0])
                proxies.add(key[1])

        return proxies
