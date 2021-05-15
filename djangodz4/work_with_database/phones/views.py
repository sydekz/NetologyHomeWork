from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    context = {}

    phone_query = Phone.objects.all()

    sorting = request.GET.get('sort')

    if sorting == 'name':
        phone_query = phone_query.order_by('name')

    if sorting == 'min_price':
        phone_query = phone_query.order_by('price')

    if sorting == 'max_price':
        phone_query = phone_query.order_by('-price')

    context['phones'] = phone_query

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}

    phone_query = Phone.objects.filter(slug=slug)

    if phone_query:
        context['phone'] = phone_query[0]
    else:
        print(f'Такого телефона нет в базе - {phone_query}')

    return render(request, template, context)
