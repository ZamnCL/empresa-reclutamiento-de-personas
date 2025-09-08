from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('personal/', views.personal, name='personal'),
    path('clientes/', views.clientes, name='clientes'),
    path('egresados/', views.egresados, name='egresados'),
]
