from asgiref.sync import sync_to_async

from store.models import Product


@sync_to_async
def persist_product_event(event):
    Product.objects.create(
        name=event.name,
        description=event.description,
        price=event.price
    )
