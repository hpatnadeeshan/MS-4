from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.
def view_cart(request):
    """ A view to show cart content page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    print(cart)

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    # print(request.session['cart'])
    return redirect(redirect_url)
    
def update_cart(request, item_id):
    """Change the quantity of a product to the certain amount"""

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove a product from the shopping cart"""

    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))