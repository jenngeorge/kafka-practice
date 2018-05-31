work through and extend tutorial at https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python

about kafka
- https://www.tutorialspoint.com/apache_kafka/apache_kafka_cluster_architecture.htm

## Setup

running the app locally (post-setup):
- start zookeeper: `brew services start zookeeper`
- start kafka: `brew services start kafka`
- `source env/bin/activate`
- one terminal: `python producer.py`
- 2nd terminal: `python consumer.py`


notes:
- also  pip install requests

pyspark notes:
- pip install pyspark
- run interactive pyspark with `env/bin/pyspark`
