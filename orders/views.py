from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
from .models import *


def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    veins = data.get("veins")
    winding = data.get("winding")
    coil = data.get("coil")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")
    print(is_delete)
    if is_delete == 'true':
        print("is delete true")
        ProductInCart.objects.filter(id=product_id).update(is_active=False)
        print(product_id)
    else:
        print("is delete false")
        new_product, created = ProductInCart.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                   is_active=True, defaults=
                                                                   {"nmb": nmb, "veins": veins, "winding": winding,
                                                                    "coil": coil})
        print(product_id)
        if not created:
            print("not created")
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_cart.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict['id'] = item.id
        product_dict['name'] = item.product.name
        product_dict['nmb'] = item.nmb
        product_dict['price'] = item.product.price
        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_cart.count()
    products_in_cart_id = list(products_in_cart)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        data = request.POST
        # if form.is_valid():
        #     print("yes")
        # else:
        #     print("no")
        customer_phone = data.get("phone", 1234)
        customer_name = data.get("name", 1234)
        comments = data.get("comment", 1234)
        user, created = User.objects.get_or_create(username=customer_phone, defaults={"first_name": customer_name})
        order = Order.objects.create(user=user, customer_name=customer_name, customer_phone=customer_phone,
                                     comments=comments)
        for item in products_in_cart_id:
            id = str(item)
            product_id = ProductInCart.objects.get(id=id)
            print(product_id.veins, product_id.id)
            ProductInOrder.objects.create(product=product_id.product, nmb=product_id.nmb, winding=product_id.winding,
                                          veins=product_id.veins, coil=product_id.coil,
                                          price_per_item=product_id.price_per_item,
                                           total_price=product_id.total_price, order=order)
        print(request.POST)

    return render(request, 'orders/checkout.html', locals())
