from django.urls import path
from services.views import show_info_services, works

app_name = 'services'

urlpatterns = [
    path('', show_info_services, name='home'),  # Главная страница
    path('works/<int:category_id>/', works, name='works'),
]