from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse
from .models import Items, Transactions, TransactionItems
from backend.inventory import find_item_by_id

def home(request):
    # get value from searchbar



    items = Items.objects.all()
    transactions = Transactions.objects.all()
    transactionsItems = TransactionItems.objects.all()

    cart_dict = request.session.get('cart', {})
    

    cart = list(cart_dict.values())  # Convert the cart dictionary to a list of items
    total = request.session.get('total', 0.0)


    return render(request, 'app/home.html', {'items': items, 'transactions': transactions, 'transactionItems': transactionsItems, 'cart': cart, 'total': total})


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
    
    request.session['total'] = round(total, 2)  # save total in session


    return redirect('home')  # Redirect to the template view after adding to cart