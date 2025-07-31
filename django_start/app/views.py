from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse
from .models import Items, Transactions, TransactionItems
from backend.inventory import find_item_by_id

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

def add_to_cart(request):
    
    item_id = getID(request)
    
    item = find_item_by_id(item_id) #item object


    cart = request.session.get('cart', {})
    
    # Populate the cart in the session
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    else:
        cart[str(item_id)] = {
            'item_id': item_id, 
            'item' : item.name,
            'quantity': 1, 
            'price': item.price
        }
    request.session['cart'] = cart # This updates the session with the new cart data
    print("Item added to cart:", item_id)

    # Prepare the cart data for the response
    # This is a list of dictionaries, each representing an item in the cart with its subtotal calculated
    cart_data = []
    total = 0.0
    for item_data in cart.values():
        subtotal = item_data['quantity'] * item_data['price']
        item_data['subtotal'] = round(subtotal, 2)
        total += subtotal

        cart_data.append(item_data)
    

    return JsonResponse({
        'cart': cart_data, #cart_data is a list of dictionaries contraining item_id, item name, quantity, price, and subtotal
        'total_price': round(total, 2)
    })