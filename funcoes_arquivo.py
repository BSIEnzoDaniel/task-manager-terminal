from json import load,dump

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            lista = load(arquivo)
    except FileNotFoundError:
        return []
    else:
        return lista
#Função que carrega o arquivo .json e transforma em lista Python. Se o arquivo não existir, ele cria um vazio


def salvar_tarefas(lista):
    with open('tarefas.json', 'w') as listagem_salva:
        dump(lista, listagem_salva, indent=4)
#Função que pega as tarefas (uma lista de dicioonários), trasnforma em .json e deixa salvas no arquivo