from django.db import models

# Create your models here.
# first step to getting database in html

class InventoryItem(models.Model):
    # add fields
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed from your inventory database

    def __str__(self):
        return self.name