from django.urls import path, include
from .import views
urlpatterns = [
    path('cadastrar_tarefas/',views.cadastrar_tarefas, name="cadastar_tarefas")
]
