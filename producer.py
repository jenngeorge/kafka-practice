import sys
import time
import requests
import json
# import cv2
from kafka import SimpleProducer, KafkaClient
#  connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
# Assign a topic
topic = 'citibike_stations'

# def video_emitter(video):
#     # Open the video
#     video = cv2.VideoCapture(video)
#     print(' emitting.....')
#
#     # read the file
#     while (video.isOpened):
#         # read the image in each frame
#         success, image = video.read()
#         # check if the file has read to the end
#         if not success:
#             break
#         # convert the image png
#         ret, jpeg = cv2.imencode('.png', image)
#         # Convert the image to bytes and send to kafka
#         producer.send_messages(topic, jpeg.tobytes())
#         # To reduce CPU usage create sleep time of 0.2sec
#         time.sleep(0.2)
#     # clear the capture
#     video.release()
#     print('done emitting')

def data_emitter():
    response_data = requests.get('https://proxy.streamdata.io/https://feeds.citibikenyc.com/stations/stations.json', stream=True)

    # citidata streaming api
    for chunk in response_data.iter_content(chunk_size=128):
        print(chunk.decode("utf-8"))
        print('printing!')
        # response_strs = json.dumps(response_data.content)
        # response_bytes = response_str.encode('utf-8')
        producer.send_messages(topic, chunk)


if __name__ == '__main__':
    # video_emitter('SampleVideo_360x240_2mb.mp4')
    data_emitter()
