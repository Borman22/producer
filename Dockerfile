FROM python:3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

RUN git clone https://github.com/Borman22/producer.git
WORKDIR /usr/src/app/producer/

RUN pip3 install --upgrade setuptools
RUN pip3 install wheel
RUN pip3 install avro-python3
RUN pip3 install confluent-kafka
RUN pip install requests


ENV BROKERS=broker:9092
ENV SCHEMA_REGISTRY_URL=http://schema-registry:8081
ENV TOPIC=initial_data_avro
ENV HDP_IP=10.132.0.23
ENV HDP_DOMAIN_NAME sandbox.hortonworks.com

CMD echo "$HDP_IP $HDP_DOMAIN_NAME" >> /etc/hosts && python -u main.py --brokers $BROKERS --schema_registry_url $SCHEMA_REGISTRY_URL --topic $TOPIC --format avro --interval 60
