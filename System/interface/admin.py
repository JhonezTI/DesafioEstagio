from django.contrib import admin

from .models import kitnet

class conteudo(admin.ModelAdmin):
    list_display = ('NumKitnet', 'nome')

admin.site.register(kitnet, conteudo)
