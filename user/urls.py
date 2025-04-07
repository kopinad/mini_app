from django.urls import path
from user.views import svyaz

app_name = 'user'

urlpatterns = [
    path('svyaz/', svyaz, name='svyaz'),
]