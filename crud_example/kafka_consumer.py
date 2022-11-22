import os
import faust
import django

# eventlet is used as a bridge to communicate with asyncio
os.environ.setdefault("FAUST_LOOP", "eventlet")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crud_example.settings")
django.setup()

# Django logic models only imported after django setup is called

from consumer.models import Product
from consumer.service import persist_product_event

from django.conf import settings

app = faust.App("store", broker=f"kafka://{settings.KAFKA_URL}")


topic = app.topic(settings.KAFKA_STREAM_TOPIC, value_type=Product)


@app.agent(topic)
async def process_topic(stream):
    async for event in stream:
        print("received event %s", event)
        await persist_product_event(event)
