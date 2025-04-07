from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import requests
from services.models import Category

TELEGRAM_TOKEN = "8000922634:AAHg4zWCpme_nQu1aSSKL6mLgF41PFa6aeY"
TELEGRAM_CHAT_ID = "-4761244038"


def svyaz(request):
    categories = Category.objects.all()
    return render(request, 'user/formasvyazi.html', {
        'categories': categories
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


def form_submit(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        service = request.POST.get('service', '').strip()
        contact_whatsapp = request.POST.get('contact_whatsapp') == 'on'
        contact_telegram = request.POST.get('contact_telegram') == 'on'

        message = (
            "<b>Новая заявка!</b>\n"
            f"<b>Имя:</b> {full_name}\n"
            f"<b>Телефон:</b> {phone}\n"
            f"<b>Услуга:</b> {service}\n"
            "<b>Предпочитаемый способ связи:</b> "
        )

        if contact_whatsapp:
            message += "WhatsApp "
        if contact_telegram:
            message += "Telegram"

        if send_telegram_message(message):
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Ошибка отправки в Telegram'})

    return JsonResponse({'status': 'invalid', 'message': 'Неверный метод запроса'})