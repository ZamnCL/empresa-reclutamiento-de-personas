from django.urls import path
from . import views

urlpatterns = [
    # Mapea la URL raíz de la aplicación a la vista 'index'
    path('', views.index, name='index'),
    
    # Mapea 'personal' a su vista correspondiente
    path('personal/', views.personal, name='personal'),
    
    # Mapea 'clientes' a su vista correspondiente
    path('clientes/', views.clientes, name='clientes'),
    
    # Mapea 'egresados/' a su vista correspondiente
    path('egresados/', views.egresados, name='egresados'),
]
