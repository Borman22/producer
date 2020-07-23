FROM python:3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

 RUN git clone https://github.com/Borman22/producer.git
 WORKDIR /usr/src/app/producer/
#COPY . /usr/src/app/

RUN pip3 install --upgrade setuptools
RUN pip3 install wheel
RUN pip3 install avro-python3


RUN pip3 install confluent-kafka

RUN pip install requests
ENTRYPOINT ["python", "-u", "main.py"]
