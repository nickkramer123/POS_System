from django.contrib import admin
from .models import Items, Transactions, TransactionItems


# Register your models here.
admin.site.register(Items)
admin.site.register(Transactions)
admin.site.register(TransactionItems)

