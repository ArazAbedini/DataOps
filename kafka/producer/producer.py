from kafka import KafkaProducer
import json
import time



if __name__ == '__main__':
    
    
    time.sleep(15)
    
    BROKER = 'kafka:9092'
    TOPIC = 'json_topic'

    PATH = '/app/files/dirty_data_large.json'

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
        input("hello:")
    finally:
        producer.flush()
        producer.close()
        