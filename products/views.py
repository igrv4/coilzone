from django.shortcuts import render
from products.models import *


def products(request):
    products = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'products/products.html', locals())


def product(request, product_id):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print("ss = ", request.session.session_key)
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product.html', locals())

