from dataclasses import fields
from django import forms
from .models import kitnet

class kitnetForms(forms.ModelForm):
    class Meta:
        model = kitnet
        fields = ('NumKitnet','nome', 'cpf', 'Tam_Kitnet', 'Valor_Imovel')