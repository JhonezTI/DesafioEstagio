from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage, name='manage'),
    path('newKitnet/', views.newKitnet, name='new-kitnet'),
    path('edit/<int:id>', views.editKitnet, name='Editar' ),
    path('delete/<int:id>', views.deleteKitnet, name='Deletar'),
    
]
