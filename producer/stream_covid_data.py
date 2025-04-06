import pandas as pd
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable, KafkaError
import json
import time




df = pd.read_csv('data/worldwide-aggregate.csv')

print(df.head())
messages = df.to_dict(orient='records')

connection_not_successful = True


while connection_not_successful:
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka:29092',  # Connect to the Kafka container
            value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize data to JSON
        )

        print("Connection to Kafka broker successful!")

        connection_not_successful = False
        # Produce some data
        topic = "covid-data"

        print("Starting Kafka producer...")
        for message in messages:
            producer.send(topic, value=message)
            print(f"Sent: {message}")
            time.sleep(5)

        producer.close()
        print("Finished producing messages.")
    
    except (NoBrokersAvailable, KafkaError) as e: 
        print(e)
