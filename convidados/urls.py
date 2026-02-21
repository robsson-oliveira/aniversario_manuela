from django.urls import path
from .views import home, confirmar_presenca, obrigado

urlpatterns = [
    path('', home, name='home'),
    path('confirmar/', confirmar_presenca, name='confirmar'),
    path('obrigado/', obrigado, name='obrigado'),
]