# Kafka producer (Python)

This program periodically takes data from files [station_information.json](https://gbfs.fordgobike.com/gbfs/es/station_information.json) and [station_status.json](https://gbfs.fordgobike.com/gbfs/es/station_status.json), leaves only the necessary fields and publishes them in a Kafka topic in JSON or Avro format.

JSON structure:
```
{
  "last_reported": 1593694561,
  "station_id": "3",
  "num_ebikes_available": 0,
  "num_bikes_available": 21,
  "num_docks_available": 13,
  "station_status": "active",
  "capacity": 35
}
```

Kafka message has KEY (string) equals "station_id" and VALUE (json or avro) which stores all data

## Installation

Download the Dockerfile in a certain folder. Run the command in this folder:

```bash
docker build -t producer .
```
And then:

```bash
docker run --rm producer
```

## Parameters

All parameters are written in the Dockerfile. 

Default parameters (if you delete all parameters from the Dockerfile):

```
--brokers localhost:9092
--schema_registry_url http://localhost:8081
--topic test
--format avro (possible values json, avro)
--interval 60 (in seconds)
```