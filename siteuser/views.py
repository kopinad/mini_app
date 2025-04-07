from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import requests
from services.models import Category
from siteuser.forms import SiteUserForm
from django.views.decorators.csrf import csrf_exempt

TELEGRAM_TOKEN = "8000922634:AAHg4zWCpme_nQu1aSSKL6mLgF41PFa6aeY"
TELEGRAM_CHAT_ID = "-4761244038"


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

@csrf_exempt
def form_submit(request):
    if request.method == "POST":
        form = SiteUserForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({
            'status': 'error',
            'message': 'Ошибка валидации',
            'errors': form.errors.as_json()
        })
    return JsonResponse({'status': 'invalid'})