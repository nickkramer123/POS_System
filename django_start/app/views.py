from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Items, Transactions, TransactionItems


def index(request):
    return HttpResponse("Hello, world. You're at the xyz.")

def template(request):
    # get value from searchbar



    items = Items.objects.all()
    transactions = Transactions.objects.all()
    transactionsItems = TransactionItems.objects.all()
    return render(request, 'app/template.html', {'items': items, 'transactions': transactions, 'transactionItems': transactionsItems})


def getID(request):
    query = request.GET.get('search_query', '')
    print("user searched for: ", query)
    return query
