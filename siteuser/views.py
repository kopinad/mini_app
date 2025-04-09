from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import logging
from .forms import SiteUserForm

logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""


@csrf_exempt
def send_telegram_message(text):
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={
                'chat_id': TELEGRAM_CHAT_ID,
                'text': text,
                'parse_mode': 'HTML'
            },
            timeout=5
        )
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Telegram error: {str(e)}")
        return False


def svyaz(request):
    if request.method == 'POST':
        form = SiteUserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            service_name = cleaned_data['service'].name if cleaned_data['service'] else "Не указано"

            message = (
                "<b>Новая заявка!</b>\n"
                f"<b>Имя:</b> <code>{cleaned_data['full_name']}</code>\n"
                f"<b>Телефон:</b> <code>{cleaned_data['phone']}</code>\n"
                f"<b>Услуга:</b> <code>{service_name}</code>\n"
                f"<b>Способ связи:</b> "
                f"{'WhatsApp' if cleaned_data['contact_whatsapp'] else ''}"
                f"{', ' if cleaned_data['contact_whatsapp'] and cleaned_data['contact_telegram'] else ''}"
                f"{'Telegram' if cleaned_data['contact_telegram'] else ''}"
            )

            if send_telegram_message(message):
                return JsonResponse({'status': 'success'})
            return JsonResponse({'status': 'telegram_error'}, status=500)
        else:
            return JsonResponse({'status': 'form_error', 'errors': form.errors}, status=400)

    form = SiteUserForm()
    return render(request, 'user/formasvyazi.html', {'form': form})