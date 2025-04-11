import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample products and actions
products = ['Laptop', 'Phone', 'Shoes', 'Watch', 'Backpack']
actions = ['viewed', 'added_to_cart', 'clicked_checkout']

# Generate and send fake customer events
while True:
    event = {
        'user_id': random.randint(1000, 9999),
        'product': random.choice(products),
        'action': random.choice(actions),
        'timestamp': datetime.now().isoformat()
    }
    producer.send('customer-events', value=event)
    print(f"✅ Sent: {event}")
    time.sleep(2)
