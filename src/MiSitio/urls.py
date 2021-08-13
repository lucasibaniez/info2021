from django.contrib import admin
from django.urls import path, include
from .views import inicio
from .view import ini

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('', ini),
    path('Amigos/', include('apps.amigos.urls'))


]
