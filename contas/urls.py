from django.urls import path

from .views import meu_login

urlpatterns = [
    path('login', meu_login),
]
