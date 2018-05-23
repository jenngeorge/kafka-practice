work through and extend tutorial at https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python

running the app locally (post-setup):
- start zookeeper: `brew services start zookeeper`
- start kafka: `brew services start kafka`
- `source env/bin/activate`
- one terminal: `python producer.py`
- 2nd terminal: `python consumer.py`


notes:
- also  pip install requests
