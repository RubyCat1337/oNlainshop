from django.shortcuts import render
from .models import Product, AdditionalOption
from django.shortcuts import get_object_or_404
from cart.models import *


def show_catalog(request):
    context = {"list_products": Product.objects.all()}
    return render(request, "catalog/catalog.html", context)


def show_product(request, product_pk):
    if request.method == 'POST':
        #
        session_key = request.session.session_key
        #
        if not session_key:
            #
            request.session.cycle_key()
            #
            session_key = request.session.session_key
        #
        product_in_cart = ProductInCart.objects.create(
            session_key=session_key, product_id=product_pk)
        #
        additional_options = AdditionalOption.objects.filter(
            pk__in=request.POST.getlist('listCheckedOptions[]'))
        #
        product_in_cart.additional_options.set(additional_options)
        #
        product_in_cart.save()
        
    context = {'product': get_object_or_404(Product, pk=product_pk),
               "additional_options": AdditionalOption.objects.all()}

    full_price = context['product'].price
    for option in context["additional_options"]:
        full_price += option.price

    context["full_price"] = full_price
    return render(request, "catalog/product.html", context=context)
