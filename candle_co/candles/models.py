from django.db import models
from datetime import date

# Create your models here.

class Candles(models.Model):
    name = models.CharField(max_length=64)
    scent = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    created_at = models.DateTimeField(default=date.today)

    def __str__(self):
        return f"{self.name} - {self.scent} ${self.price} In Stock:{self.inventory} Created on:{self.created_at}"