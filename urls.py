from django.contrib import admin
from django.urls import path
from perpustakaan.views import Buku

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Buku/', Buku),
]
