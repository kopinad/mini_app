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


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")
        return False

@csrf_exempt
def form_submit(request):
    if request.method == "POST":
        form = SiteUserForm(request.POST)
        if form.is_valid():
            message = (
                "<b>Новая заявка!</b>\n"
                f"<b>Имя:</b> {form.cleaned_data['full_name']}\n"
                f"<b>Телефон:</b> {form.cleaned_data['phone']}\n"
                f"<b>Услуга:</b> {form.cleaned_data['service']}\n"
                "<b>Способ связи:</b> "
            )
            form.save()

            if form.cleaned_data.get('contact_whatsapp'):
                message += "WhatsApp "
            if form.cleaned_data.get('contact_telegram'):
                message += "Telegram"

            if send_telegram_message(message):
                return JsonResponse({'status': 'success'})

        return JsonResponse({'status': 'error', 'message': 'Ошибка валидации формы'})
    return JsonResponse({'status': 'invalid', 'message': 'Неверный метод запроса'})
