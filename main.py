from utils.file_operations import read_traffic_data
from model.controls.calculate_metrics import MetricsCalculator
from model.controls.analyze_traffic import TrafficAnalyzer
from model.controls.top_nodes import TopNodesAnalyzer
from model.controls.top_subnets import TopSubnetsAnalyzer
from model.controls.find_proxy_nodes import ProxyFinder

if __name__ == "__main__":
    file_path = "traf.txt"
    traffic_data = read_traffic_data(file_path)

    # Создаем объекты классов
    analyzer = TrafficAnalyzer(traffic_data)
    metrics_calculator = MetricsCalculator()
    proxy_finder = ProxyFinder(traffic_data)
    top_nodes_analyzer = TopNodesAnalyzer(traffic_data)
    top_subnets_analyzer = TopSubnetsAnalyzer(traffic_data)

    # Ответы на вопросы
    print(
        f"Q1. Количество уникальных узлов в наблюдаемой сети: {metrics_calculator.calculate_unique_nodes(traffic_data)}")
    print(
        f"Q2. Средняя скорость передачи данных в наблюдаемой сети: {metrics_calculator.calculate_average_speed(traffic_data)} байт/сек")

    avg_udp_speed = analyzer.udp_speed()
    avg_tcp_speed = analyzer.tcp_speed()
    print(f"Q3. Средняя скорость передачи данных по UDP: {avg_udp_speed} байт/сек")
    print(f"    Средняя скорость передачи данных по TCP: {avg_tcp_speed} байт/сек")
    print((lambda: "    Верно, UDP используется для передачи данных с максимальной пиковой скоростью."
    if avg_udp_speed > avg_tcp_speed
    else "    Неверно, TCP используется для передачи данных с максимальной пиковой скоростью.")())

    print("Q4. Топ 10 узлов с самой высокой средней скоростью передачи данных:")
    for node, speed in top_nodes_analyzer.top_nodes_by_speed():
        print(f"   {node}: {speed} байт/сек")

    print("Q5. Топ 10 подсетей с самым большим количеством сессий передачи данных:")
    for a, b in top_subnets_analyzer.top_subnets_by_sessions():
        print(f"   {a}: {b} сессий")

    print("Q6. Узлы, которые могут являться посредниками (PROXY) в сети:")
    proxy_nodes = proxy_finder.find_proxy_nodes()
    print(", ".join(proxy_nodes) if proxy_nodes else "   Нет таких узлов")
