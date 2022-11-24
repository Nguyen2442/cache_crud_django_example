from django.db import models
from core.models import TimeStampedUUIDModel

class Product(TimeStampedUUIDModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "products"

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.description,
            'price': self.price,
        }