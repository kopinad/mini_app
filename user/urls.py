from django.urls import path
from user.views import svyaz, form_submit

app_name = 'user'

urlpatterns = [
    path('svyaz/', svyaz, name='svyaz'),
    path('submit-form/', form_submit, name='form_submit'),
]
