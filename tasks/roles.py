from rolepermissions.roles import AbstractUserRole

class Gerente (AbstractUserRole):
    availe_permissions = {
        'cadastar_tarefas': True,
        'modificar_tarefas': True,
        'apagar_tarefas': True,
        'criar_clientes': True,     
    }

class Cliente (AbstractUserRole):
    avaible_permissions = {
        'ver_tarefas': True,
    }