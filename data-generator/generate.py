import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ['Mobile', 'Laptop', 'Tablet', 'Monitor']
actions = ['click', 'view', 'purchase']

while True:
    event = {
        'user_id': random.randint(1, 1000),
        'product': random.choice(products),
        'action': random.choice(actions),
        'timestamp': datetime.now().isoformat()
    }

    producer.send('customer-events', value=event)
    print(f"✅ Sent: {event}")
    time.sleep(2)

