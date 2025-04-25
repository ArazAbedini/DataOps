from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import time

def wait_for_kafka(broker, max_retries=30, delay=1):
    for i in range(max_retries):
        try:
            KafkaProducer(bootstrap_servers=broker)
            print("Kafka is ready!")
            return True
        except NoBrokersAvailable:
            print(f"Waiting for Kafka... (Attempt {i+1}/{max_retries})")
            time.sleep(delay)
    raise Exception("Kafka not ready after maximum retries")



if __name__ == '__main__':
    
   
    
    BROKER = 'kafka:9092'
    TOPIC = 'json_topic'

    PATH = '/app/files/dirty_data_large.json'
    
    wait_for_kafka(BROKER)

    producer = KafkaProducer(
        bootstrap_servers=BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    try: 
        with open(PATH, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                for record in data:
                    producer.send(TOPIC, value=record)
                    print(f'the data {record} were sent!')
        
            
    except FileNotFoundError:
        print(f'File in the address {PATH} not found')
    finally:
        time.sleep(20)
        producer.flush()
        producer.close()
        