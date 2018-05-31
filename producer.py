import time
import requests
import json

from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient('localhost:9092')
station_producer = SimpleProducer(kafka)

topic = 'citibike_stations'

def data_emitter():
    response_data = requests.get('https://proxy.streamdata.io/https://feeds.citibikenyc.com/stations/stations.json', stream=True)

    # citidata streaming api
    for chunk in response_data.iter_content(chunk_size=128):
        station_producer.send_messages(topic, chunk)


if __name__ == '__main__':
    data_emitter()
