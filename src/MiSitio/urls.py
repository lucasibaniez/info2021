from django.contrib import admin
from django.urls import path, include

from .views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),

    path('Amigos/', include('apps.amigos.urls'))


]
