from django.shortcuts import get_object_or_404, render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'min_price':
        phones = phones.order_by('price')
    elif sort_by == 'max_price':
        phones = phones.order_by('-price')
    else:
        phones = phones.order_by('name')
    template = 'catalog.html'
    context = {'phones': phones, 'sort_by': sort_by}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
