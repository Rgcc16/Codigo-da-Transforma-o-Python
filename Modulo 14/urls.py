from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name="listar"),
    path('cadastrar/', views.cadastrar_produto, name="cadastrar"),
    path('editar/<int:id>/', views.editar_produto, name="editar"),
    path('excluir/<int:id>/', views.excluir_produto, name="excluir"),
]

