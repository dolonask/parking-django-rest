from django.urls import path
from . import views


urlpatterns = [
    path('tariff/', views.tariff),
    path('close-oper/', views.close_operation)
]