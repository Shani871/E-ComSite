from django.shortcuts import render
from Ecomsite.models import Product
from django.core.paginator import Paginator


def index(request):
    product_object = Product.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_object = product_object.filter(title__icontains=item_name)

    # paginator code
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_object': product_object})


def detail(request,id):
    product_object = Product.objects.get(id=id)
    return  render(request,'shop/deatil.html',{'product_object':product_object})
