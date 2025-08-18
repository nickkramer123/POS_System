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


    return render(request, 
                  'app/home.html', 
                  {'items': items, 
                   'transactions': transactions, 
                   'transactionItems': transactionsItems, 
                   'cart': cart, 
                   'total': total})

def tender(request):

    cart = request.session.get('cart', {}) # get the cart from the session
    
    if not cart:
        return redirect('home') # There's nothing to sell so do nothing
    
    item_ids = []
    for item in cart.values():
        item_ids.add(item)

    
    return render(request,
                'app/close_report.html', 
                {'transactions': transactions, 
                'transactionItems': transactionsItems, 
                'cart': cart, 
                'total': total})
def getID(request):
    query = request.GET.get('search_query', '')
    print("user searched for: ", query)
    return query

def add_to_cart(request):
    
    item_id = getID(request)
<<<<<<< HEAD
    if not item_id: # for input validation
        return redirect('home')



    item = find_item_by_id(item_id) #item object
    if not item: # for input validation
=======
    
    try:
        item = Items.objects.get(item_id=int(item_id))
    except Items.DoesNotExist:
>>>>>>> origin/sale-db-logic
        return redirect('home')


    cart = request.session.get('cart', {})
    # Populate the cart in the session
    
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    else:
        cart[str(item_id)] = {
            'item_id': item_id, 
<<<<<<< HEAD
            'item' : item.name,
            'price': item.price,
            'quantity': 1
=======
            'name' : item.name,
            'quantity': 1, 
            'price': float(item.price)
>>>>>>> origin/sale-db-logic
        }

    print(cart)
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

def clear_cart(request):
    request.session['cart'] = {}  # Clear the cart in the session
<<<<<<< HEAD
    request.session['total'] = 0

    return redirect('home')  # Redirect to the template view after clearing the cart



def pos_admin(request):  
    return render(request, "app/pos_admin.html")



def add_or_remove(request):   
    items = Items.objects.all()
    return render(request, "app/add_or_remove.html", {'items': items})


def remove_item(request):
    # same logic as add to cart
    item_id = getID(request)
    if not item_id: # for input validation
        return redirect('add_or_remove')


    item = Items.objects.get(item_id=item_id)
    if not item: # for input validation
        return redirect('add_or_remove')
    
    # remove item from database
    item.delete()

    return redirect('add_or_remove')


def add_item(request):

    # Get values from the form submission
    item_id = request.POST.get("item_id")
    item_name = request.POST.get("item")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")


    Items.objects.create(
            item_id=item_id,
            item=item_name,
            price=price,
            quantity=quantity
        )

    return redirect('add_or_remove')






def edit_quantity(request):   
    items = Items.objects.all()
    return render(request, "app/edit_quantity.html", {'items': items})


def update_quantity(request):

    # get item
    item_id = getID(request)
    if not item_id: # for input validation
        return redirect('edit_quantity')

    item = find_item_by_id(item_id) #item object
    if not item: # for input validation
        return redirect('edit_quantity')
    
    # get new quantity
    new_quantity = request.GET.get('search_query_quantity', '')
    if not new_quantity.isdigit():
        return redirect('edit_quantity')


    # add new quantity to item
    item.quantity = int(new_quantity)
    item.save() 

    
    return redirect('edit_quantity')









def edit_price(request):   
    items = Items.objects.all()
    return render(request, "app/edit_price.html", {'items': items})


=======
    request.session['total'] = 0.0  # Reset the total in the session
    return redirect('home')  # Redirect to the template view after clearing the cart
>>>>>>> origin/sale-db-logic
