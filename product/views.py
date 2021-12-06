from django.shortcuts import render
from product.models import Product


def product_index(request):
    productss = Product.objects.all().order_by('-created_on')
    context = {
        'productss': productss,
    }
    return render(request, 'product_index.html', context)





