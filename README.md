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
- pip install doesnt actually include everything
- go to http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22spark-streaming-kafka-0-8-assembly_2.11%22 and download the jar


submitting applications: https://spark.apache.org/docs/2.1.1/submitting-applications.html

'if your application uses advanced sources (e.g. Kafka, Flume), then you will have to package the extra artifact they link to, along with their dependencies, in the JAR that is used to deploy the application. For example, an application using KafkaUtils will have to include spark-streaming-kafka-0-10_2.11 and all its transitive dependencies in the application JAR'
https://spark.apache.org/docs/2.3.0/streaming-programming-guide.html#deploying-applications


run spark application with `env/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 spark.py`
