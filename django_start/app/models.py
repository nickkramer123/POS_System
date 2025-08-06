from django.db import models

# Create your models here.
# first step to getting database in html

class Items(models.Model):
    # add fields
    item_id = models.IntegerField(primary_key=True)
    item = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()


    class Meta:
        db_table = 'items'  # The real table name in your DB

    def __str__(self):
        return self.name
    
class Transactions(models.Model):
    # add fields
    id = models.IntegerField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.TextField()

    class Meta:
        db_table = 'transactions'  # The real table name in your DB

    def __str__(self):
        return self.name
    


class TransactionItems(models.Model):
    # add fields
    transaction_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'transaction_items'  # The real table name in your DB

    def __str__(self):
        return self.name