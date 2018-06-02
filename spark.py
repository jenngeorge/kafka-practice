from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

sc = SparkContext(appName="spark_citibike")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 2)

kafkaStream = KafkaUtils.createDirectStream(
    ssc,
    ['citibike_stations'],
    {"metadata.broker.list": 'localhost:9092'})

def printRDD(rdd):
    print(rdd.collect())

# parsed = kafkaStream.map(lambda x: json.loads(x[1]))
kafkaStream.foreachRDD(printRDD)

ssc.start()
ssc.awaitTermination()


# https://gist.github.com/rmoff/fb033086b285655ffe7f9ff0582dedbf
# https://www.datacamp.com/courses/introduction-to-pyspark?tap_a=5644-dce66f&tap_s=210732-9d6bbf&utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48303643819&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=255798221920&utm_targetid=aud-392016246653:dsa-377762271983&utm_loc_interest_ms=&utm_loc_physical_ms=9004067&gclid=CjwKCAjwur7YBRA_EiwASXqIHBoDFRgrETDPvkc8BNHZvuajiwWGrm9UoMeicIkg9UUfhJFIMmxlUhoCIeUQAvD_BwE
# https://www.rittmanmead.com/blog/2017/01/getting-started-with-spark-streaming-with-python-and-kafka/
