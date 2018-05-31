from kafka import KafkaConsumer

station_consumer = KafkaConsumer('citibike_stations', group_id='view', bootstrap_servers=['0.0.0.0:9092'])
