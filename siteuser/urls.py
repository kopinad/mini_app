from django.urls import path
from siteuser.views import svyaz, form_submit

app_name = 'user'

urlpatterns = [
    path('svyaz/', svyaz, name='svyaz'),
]
