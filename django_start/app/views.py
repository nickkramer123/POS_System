from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Items


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def template(request):
    items = Items.objects.all()
    return render(request, 'app/template.html', {'items': items})