from django.contrib import admin
from .models import Confirmacao

@admin.register(Confirmacao)
class ConfirmacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_responsavel', 'email', 'quantidade_criancas', 'confirmado_em')