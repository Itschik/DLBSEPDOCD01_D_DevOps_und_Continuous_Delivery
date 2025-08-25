from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import CartItem

@login_required
def add_to_cart(request, product_id):
    if request.method != 'POST':
        return redirect('product_detail', product_id=product_id)
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(i.product.price * i.quantity for i in items)
    return render(request, 'cart/cart_view.html', {'items': items, 'total': total})

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.filter(user=request.user, product=product).delete()
    return redirect('cart_view')

@login_required
def checkout(request):
    # Dummy-Seite: keine Zahlung/Orderanlage – nur Confirmation
    items = CartItem.objects.filter(user=request.user)
    total = sum(i.product.price * i.quantity for i in items)
    return render(request, 'cart/checkout.html', {'items': items, 'total': total})
