from django.db import models

# Create your models here.
# first step to getting database in html

class InventoryItem(models.Model):
    # add fields
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        managed = False  # Tell Django not to manage this table's creation
        db_table = 'items'  # The real table name in your DB

    def __str__(self):
        return self.name