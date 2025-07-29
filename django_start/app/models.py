from django.db import models

# Create your models here.
# first step to getting database in html

class Items(models.Model):
    # add fields
    item_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        db_table = 'items'  # The real table name in your DB

    def __str__(self):
        return self.name