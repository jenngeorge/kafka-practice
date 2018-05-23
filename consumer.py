import sys
from flask import Flask, Response
from kafka import KafkaConsumer
#connect to Kafka server and pass the topic we want to consume
# consumer = KafkaConsumer('video', group_id='view', bootstrap_servers=['0.0.0.0:9092'])
consumer = KafkaConsumer('citibike_stations', group_id='view', bootstrap_servers=['0.0.0.0:9092'])
#Continuously listen to the connection and print messages as recieved
app = Flask(__name__)

@app.route('/')
def index():
    # return a multipart response
    return Response(kafkastream(),
                    mimetype='text')
def kafkastream():
    for msg in consumer:
        print(msg)
        # yield (b'--frame\r\n'
        #        b'Content-Type: image/png\r\n\r\n' + msg.value + b'\r\n\r\n')
        yield msg.value

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
