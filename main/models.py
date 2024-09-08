from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)

    @property
    def __str__(self):
        return self.name
    @property
    def is_in_stock(self):
        return self.quantity > 0