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

def controle_prazo(concluida, data_hoje, data_tarefa):
    if concluida:
        print('[\033[32m✔\033[m]')
    else:
        print('[ ]', end=' ')
        atraso = data_hoje > data_tarefa
        diferenca_datas = data_tarefa - data_hoje
        dias = abs(diferenca_datas.days)
        match dias:
            case 0:
                texto_tempo = 'Hoje'
            case 1:
                texto_tempo = 'Amanhã'
            case _:
                if dias > 7:
                    semanas = dias // 7
                    if semanas > 4:
                        texto_tempo = '1+ mês'
                    else:
                        texto_tempo = f'{semanas} sem.'
                else:
                    texto_tempo = f'{dias} d.'
        if atraso:
            print(f'(\033[31m{texto_tempo}\033[m)')
        else:
            if dias <= 2:
                print(f'(\033[33m{texto_tempo}\033[m)')
            else:
                print(f'({texto_tempo})')