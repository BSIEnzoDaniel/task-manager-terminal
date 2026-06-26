import json

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            lista = json.load(arquivo)
    except FileNotFoundError:
        return []
    else:
        return lista
#Função que carrega um arquivo json e transforma em lista python. Se o arquivo não existir, ele cria um vazio


def salvar_tarefas(lista):
    with open('tarefas.json', 'w') as listagem_salva:
        json.dump(lista, listagem_salva, indent=4)
#Função que pega as tarefas (uma lista), trasnforma em .json e deixa salvas no arquivo