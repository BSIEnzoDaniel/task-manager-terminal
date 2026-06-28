from funcoes_menu import *
from funcoes_tratamento import validar_entrada_int
from funcoes_arquivo import carregar_tarefas
from funcoes_visual import topo

acoes = {
    1: 'ADIOCIONAR TAREFAS',
    2: 'LISTAR TAREFAS',
    3: 'ATUALIZAR TAREFA',
    4: 'REMOVER TAREFAS',
    0: 'SAIR'
}

lista_tarefas = carregar_tarefas()
while True:
    topo('Gerenciador de Tarefas')
    total, pendentes, concluidas = contagem_dinamica_tarefas(lista_tarefas)
    print(f'\033[33mTotal\033[m: {total} | \033[31mPendentes\033[m: {pendentes} | \033[32mConcluídas\033[m: {concluidas}')
    for numero, acao in acoes.items():
        print(f'[\033[34m{numero}\033[m] \033[36m{acao.capitalize()}\033[m')
    usuario = validar_entrada_int('\nO que deseja fazer? ', max(acoes.keys()), 0)
    match usuario:
        case 1:
            add_tarefa(lista_tarefas)
        case 2:
            listagem(lista_tarefas)
        case 3:
            status(lista_tarefas)
        case 4:
            remocao(lista_tarefas)
        case 0:
            topo('Aplicação encerrada!')
            break
#Gerenciador de tarefas usando arquivo .json para salvamento