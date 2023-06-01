from django.shortcuts import render
from django.shortcuts import HttpResponse
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('cadastrar_tarefas')
def cadastrar_tarefas(request):
    return HttpResponse('Ola tarefas')