from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='principal'),
    path('login/', views.login),

    path('Amigos/', include('apps.amigos.urls'))


]
