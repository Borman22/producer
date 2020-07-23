from confluent_kafka import Producer
import json


class KafkaJsonProducer:

    def __init__(self, bootstrap_servers):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})

    def send_message_to_kafka(self, list_of_stations, topic_name):
        for station in list_of_stations:
            self.producer.produce(topic_name, key=bytes(station["station_id"], 'UTF-8'),
                                  value=bytes(json.dumps(station), 'UTF-8'))
        self.producer.poll(1)
