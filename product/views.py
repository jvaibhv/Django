from django.shortcuts import render
from product.models import Product, Review
from product.review import ReviewForm


def product_index(request):
    products = Product.objects.all().order_by('-created_on')
    context = {
        'products': products,
    }
    return render(request, 'product_index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                name=form.cleaned_data["name"],
                review_body=form.cleaned_data["form_body"],
                product=product
            )
            review.save()
    reviews = Review.objects.filter(product=product)
    context = {
                "product": product,
                "reviews": reviews,
                "form": form,
            }
    return render(request, 'product_detail.html', context)
