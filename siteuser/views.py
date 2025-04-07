from django.shortcuts import render, redirect
from .forms import SiteUserForm
from services.models import Category


def svyaz(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = SiteUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path + '?submitted=true')
    else:
        form = SiteUserForm()

    return render(request, 'user/formasvyazi.html', {
        'form': form,
        'categories': categories,
        'submitted': request.GET.get('submitted') == 'true'
    })