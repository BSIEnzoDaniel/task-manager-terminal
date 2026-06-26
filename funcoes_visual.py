def topo(texto):
    print('=' * 44)
    print(f'\033[34m{texto:^44}\033[m')
    print('=' * 44)



def erro(msg, titulo_erro = True):
    if titulo_erro:
        print(f'\033[31mErro: ({msg})\033[m')
    else:
        print(f'\033[31m{msg}\033[m')



def msg_listavazia():
    topo(f'\033[33m{"A lista de tarefas está vazia":^44}\033[m')
#TODAS REVISADAS