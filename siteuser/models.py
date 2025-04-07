from django.db import models
from services.models import Category


class SiteUser(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон'
    )
    service = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Услуга'
    )
    contact_whatsapp = models.BooleanField(
        default=False,
        verbose_name='WhatsApp'
    )
    contact_telegram = models.BooleanField(
        default=False,
        verbose_name='Telegram'
    )

    def __str__(self):
        return f"{self.full_name}"

