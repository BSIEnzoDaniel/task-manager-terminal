from json import load,dump
from datetime import datetime
def sincronizar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            lista = load(arquivo)
    except FileNotFoundError:
        lista = []
    finally:
        return lista
#Função que carrega o arquivo json e transforma em lista Python. Se o arquivo não existir, ele cria um vazio


def salvar_tarefas(lista):
    with open('tarefas.json', 'w') as listagem_salva:
        dump(lista, listagem_salva, indent=4)
#Função que pega as tarefas (uma lista de dicioonários), trasnforma em json e deixa salvas no arquivo


def limpeza_tarefas(lista, data_hoje):
    lista_limpa = []
    for tarefa in lista:
        data_tarefa = datetime.strptime(tarefa['data'], "%d/%m/%Y").date()
        tempo_limpeza = (data_hoje - data_tarefa).days
        excluir = tarefa['status'] and tempo_limpeza >= 2
        if not excluir:
            lista_limpa.append(tarefa)
    salvar_tarefas(lista_limpa)
    return lista_limpa
#Função que limpas as tarefas concluídas da lista a partir de 2 dias da sua data de conclusão