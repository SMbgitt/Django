from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from stepshop.views import links_menu
from basketapp.models import Basket
from mainapp.models import Product

def basket(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        title = "корзина"

        context = {
            'title': title,
            'links_menu': links_menu,
        }

        return render(request, 'basket/basket.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))