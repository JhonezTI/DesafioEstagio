from asyncio.windows_events import NULL
from operator import not_
from pickle import TRUE
from django.db import models
from django.contrib.auth import get_user_model

class kitnet(models.Model):

    TAMANHO = (
        ('Pequeno', 'Pequeno'),
        ('Medio', 'Medio'),
        ('Grande', 'Grande')
    )

    NumKitnet = models.IntegerField(unique=TRUE, verbose_name="Numero do Kitnet")
    nome = models.CharField(max_length=50, verbose_name="Nome do Titular")
    cpf = models.CharField(max_length=14, unique=TRUE, verbose_name="CPF do Titular")
    Tam_Kitnet = models.CharField(max_length=7,choices=TAMANHO, verbose_name="Tamanho do Kitnet")

    Valor_Imovel = models.CharField(max_length=50, verbose_name="Valor Mensal do Imovel")

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('NumKitnet', 'nome', 'cpf')
