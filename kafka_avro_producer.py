from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

key_schema = avro.loads(open("key_schema.avsc").read())
value_schema = avro.loads(open("value_schema.avsc").read())


class KafkaAvroProducer:
    def __init__(self, bootstrap_servers, schema_registry_url):
        self.producer = AvroProducer({
            'bootstrap.servers': bootstrap_servers,
            'schema.registry.url': schema_registry_url
        }, default_key_schema=key_schema, default_value_schema=value_schema)

    def send_message_to_kafka(self, list_of_stations, topic_name):
        for station in list_of_stations:
            self.producer.produce(topic=topic_name, value=station, key=station["station_id"])
        self.producer.flush()
