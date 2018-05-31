from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

sc = SparkContext(appName="spark_citibike")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 2)

kafkaStream = KafkaUtils.createDirectStream(
    ssc,
    ['citibike-stations'],
    {"metadata.broker.list": ['localhost:9092']})


parsed = kafkaStream.map(lambda x: json.loads(x[1]))
print(parsed)

ssc.start()
ssc.awaitTermination()
