from funcoes_tratamento import *
from funcoes_arquivo import salvar_tarefas
from funcoes_data import *
from datetime import date, datetime

def contagem_dinamica_tarefas(lista): #Conta dinamicamente as tarefas
    total = concluidas = 0
    for item in lista:
        total += 1
        if item["status"]:
            concluidas += 1
    pendentes = total - concluidas
    return total, pendentes, concluidas


def add_tarefa(lista): #Menu: 1
    topo('ADICIONANDO TAREFAS...')
    while True:
        nome_tarefa = validar_texto('Nome da tarefa: ', 20)
        if not nome_tarefa:
            break
        data_tarefa = validar_data()
        if not data_tarefa:
            break
        tarefa = {
            'nome': nome_tarefa.upper(),
            'data': data_tarefa,
            'status': False
        }
        lista.append(tarefa)
        print('\033[32mTarefa adiconada!\033[m')
        resposta = validar_caractere('Deseja continuar? (S/N) ', 'SN')
        print()
        if resposta == 'N':
            break
        print()
    salvar_tarefas(lista)



def listagem(lista, texto='LISTA DE TAREFAS'): #Menu: 2
    data_hoje = date.today()
    if lista:
        topo(texto)
        for indice, task in enumerate(lista):
            data_tarefa = datetime.strptime(task['data'], "%d/%m/%Y").date()
            print(f'{indice + 1}. {task['nome']}' , end=' - ')
            print(f'{task['data'][:5]}', end=' ')
            controle_prazo(task['status'], data_hoje, data_tarefa)
    else:
        msg_listavazia()
    print()


def status(lista): #Menu: 3
    if lista:
        listagem(lista, 'MARCAR / DESMARCAR TAREFAS')
        opcao = validar_entrada_int('Qual tarefa deseja alterar? ', len(lista))
        if not opcao:
            return
        else:
            indice = opcao - 1
            concluida = lista[indice]['status']
            if concluida:
                lista[indice]['status'] = False
                print(f'Tarefa {opcao} desmarcada.\n')
            else:
                lista[indice]['status'] = True
                print(f'Tarefa {opcao} concluída!\n')
            salvar_tarefas(lista)
            return
    else:
        msg_listavazia()
        return



def remocao(lista): #Menu: 4
    if lista:
        while True:
            listagem(lista, 'REMOVER TAREFAS')
            opcao = validar_entrada_int('Qual tarefa deseja excluir? ', len(lista))
            indice = opcao - 1
            del lista[indice]
            print(f'\033[31mTarefa {opcao} removida!\033[m')
            listagem(lista, 'LISTA ATUAL')
            salvar_tarefas(lista)
            if len(lista) == 0:
                break
            resposta = validar_caractere('Deseja continuar? (S/N) ', 'SN')
            print()
            if resposta == 'N':
                break
    else:
        msg_listavazia()

