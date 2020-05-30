from django.urls import path

from blog.views import index, criar, deletar, detalhes, editar

urlpatterns = [
    path('', index),
    path('criar/', criar),
    path('editar/1/', editar),
    path('detalhes/', detalhes),
    path('deletar/1/', deletar),
]
