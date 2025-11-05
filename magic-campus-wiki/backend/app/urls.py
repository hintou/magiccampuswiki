from django.urls import path
from app.views import calcular

urlpatterns = [
    path('api/calcular', calcular),
]