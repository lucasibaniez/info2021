from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('login/', views.login),
    path('', views.ini),

    path('Amigos/', include('apps.amigos.urls'))


]
