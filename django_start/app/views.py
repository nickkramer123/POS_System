from django.shortcuts import render
from backend.inventory import Cart, find_item_by_id

# Create your views here.
from django.http import HttpResponse
from .models import Items


def index(request):
    return HttpResponse("Hello, world. You're at the xyz.")

def template(request):
    items = Items.objects.all()
    print("Items exist?", bool(items))  # FALSE
    return render(request, 'app/template.html', {'items': items})

def search_item(request):
    query = request.GET.get('query')

# When cart is stored in a session, it looks like this:
# request.session['cart'] = [
#           {'item_id': 1, 'quantity': 2},
        #   {'item_id': 2, 'quantity': 1},
#           ...]

# To use cart in views, you get data from the session, then reconstruct the Cart object

