from django.shortcuts import render
from .models import Category, Review


def works(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return render(request, 'custom_error.html', status=404)

    products = category.services.all()
    categories = Category.objects.all()
    return render(request, 'works.html', {
        'category': category,
        'products': products,
        'categories': categories
    })


def show_info_services(request):
    categories = Category.objects.all()
    reviews = Review.objects.all()
    return render(request, 'glav.html', {'categories': categories, 'reviews': reviews})
