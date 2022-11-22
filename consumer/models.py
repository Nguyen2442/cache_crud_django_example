import faust


class Product(faust.Record, serializer="json"):
    name: str
    description: str
    price: int
