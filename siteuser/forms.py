from django import forms
from .models import SiteUser
from services.models import Category


class SiteUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Category.objects.all()

    class Meta:
        model = SiteUser
        fields = ['full_name', 'phone', 'service', 'contact_whatsapp', 'contact_telegram']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'id': 'fio',
                'placeholder': 'Введите ФИО',
                'class': 'form-input'
            }),
            'phone': forms.TextInput(attrs={
                'id': 'phone',
                'placeholder': 'Введите Ваш номер телефона',
                'type': 'tel',
                'class': 'form-input'
            }),
            'service': forms.Select(attrs={
                'id': 'work',
                'class': 'form-select'
            }),
            'contact_whatsapp': forms.CheckboxInput(attrs={
                'id': 'inp-1',
                'class': 'form-checkbox'
            }),
            'contact_telegram': forms.CheckboxInput(attrs={
                'id': 'inp-2',
                'class': 'form-checkbox'
            }),
        }
        labels = {
            'full_name': 'ФИО',
            'phone': 'Номер телефона',
            'service': 'Какую услугу Вы бы хотели приобрести?',
            'contact_whatsapp': 'WhatsApp',
            'contact_telegram': 'Telegram',
        }
