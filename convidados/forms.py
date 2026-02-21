from django import forms
from .models import Confirmacao

class ConfirmacaoForm(forms.ModelForm):
    class Meta:
        model = Confirmacao
        fields = ['nome_responsavel', 'email', 'quantidade_criancas']