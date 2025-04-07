from django.shortcuts import render
from services.models import Category


def svyaz(request):
    categories = Category.objects.all()
    return render(request, 'user/formasvyazi.html', {
        'categories': categories
    })
