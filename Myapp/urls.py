from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('services.urls')),  # для home и works
    path('user/', include('siteuser.urls')),  # для svyaz
]
