import time
import cl_parser
import json_parser
from kafka_avro_producer import KafkaAvroProducer
from kafka_json_producer import KafkaJsonProducer

args = cl_parser.parse()
list_of_stations = json_parser.parse()

if args.format == "avro":
    kafka_producer = KafkaAvroProducer(args.brokers, args.schema_registry_url)
else:
    kafka_producer = KafkaJsonProducer(args.brokers)

while True:
    kafka_producer.send_message_to_kafka(list_of_stations, args.topic)
    time.sleep(args.interval)
