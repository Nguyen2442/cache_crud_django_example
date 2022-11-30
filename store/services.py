import json 
from django.conf import settings
from kafka import KafkaProducer, KafkaConsumer
from core.singleton import Singleton

class MessagePublisher:
    def __init__(self, client) -> None:
        self.client = client
    
    def publish(self, topic, data):
        self.client.publish(topic, data)
        

class KafkaPublisher(metaclass=Singleton):
    _producer = None
    
    def __init__(self, url=settings.KAFKA_URL) -> None:
        self._producer = KafkaProducer(bootstrap_servers=url, api_version=(0,11,5))
    
    def publish(self, topic, data):
        self._producer.send(topic, json.dumps(data).encode("utf-8"))
        

class KafkaConsumer(metaclass=Singleton):
    _consumer = None
    
    def __init__(self, url=settings.KAFKA_URL) -> None:
        self._consumer = KafkaConsumer(bootstrap_servers=url)
        
    def subscribe(self, value):
        self._consumer.assign(value)