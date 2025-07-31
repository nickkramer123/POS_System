from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Items


def index(request):
    return HttpResponse("Hello, world. You're at the xyz.")

def template(request):
    items = Items.objects.all()
    cart = request.session.get('cart', [])
    return render(request, 'app/template.html', {'items': items, 'cart': cart})


def getID(request):
    query = request.GET.get('search_query', '')
    print("user searched for: ", query)
    return query