from funcoes_visual import erro
from datetime import date, datetime
def validar_data():
    data_atual = date.today()
    while True:
        try:
            data = input('Data de conclusão (DD/MM/AAAA): ')
            teste_data = datetime.strptime(data, "%d/%m/%Y")
        except KeyboardInterrupt:
            erro('\nOperação cancelada pelo usuário', False)
            break
        except ValueError:
            erro('Formato de data incorreto')
        else:
            data_validada = teste_data.date()
            if data_validada < data_atual:
                erro('Data de conclusão inválida')
            else:
                return data

def controle_prazo(concluida, data_tarefa):
    data_hoje = date.today()
    if concluida:
        print('[\033[32m✔\033[m]')
    else:
        atraso = data_hoje > data_tarefa
        diferenca_datas = data_tarefa - data_hoje
        dias = abs(diferenca_datas.days)
        if dias > 7:
            semanas = dias // 7
            if semanas > 4:
                msg_prazo = '1+ mês'
            else:
                msg_prazo = f'{semanas} sem.'
        elif dias > 2:
            msg_prazo = f'{dias} d.'
        elif dias > 0:
            msg_prazo = f'\033[33m{dias} d.\033[m'
        else:
            msg_prazo = '\033[33mHoje\033[m'
        if atraso:
            msg_prazo = f'\033[31m{msg_prazo}\033[m'
        print(f'[ ] ({msg_prazo})')