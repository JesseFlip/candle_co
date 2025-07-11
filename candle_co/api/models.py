from django.db import models

# Create your models here.
class CandlePost(models.Model):
    name = models.CharField(max_length=64)
    scent = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name