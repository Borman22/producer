import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--brokers", type=str, default="localhost:9092", help="Bootstrap server URL. Default=localhost:9092")
parser.add_argument("--schema_registry_url", type=str, default="http://localhost:8081", help="Schema registry URL. Default=http://localhost:8081")
parser.add_argument("--topic", type=str, default="test", help="Kafka topic. Default=test")
parser.add_argument("--format", type=str, choices=["avro", "json"], default="avro", help="Data format. avro or json. Default=avro")
parser.add_argument("--interval", type=int, default="60", help="Interval in second between requests to servers with station_info and station_status. Default=60")


def parse():
    return parser.parse_args()