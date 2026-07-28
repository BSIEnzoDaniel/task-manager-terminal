from funcoes_visual import *
from datetime import datetime, date


def validar_entrada_int(text, maximo, minimo=1):
    while True:
        try:
            user = int(input(text))
        except (ValueError, TypeError):
            erro('O valor digitado não é aceito')
        except KeyboardInterrupt:
            erro('\nOperação cancelada pelo usuário\n', False)
            return False
        else:
            if user < minimo or user > maximo:
                erro('O valor digitado não está disponível')
            else:
                return user



def validar_caractere(text, opts):
    while True:
        try:
            resp = str(input(text)).strip().upper()[0]
        except KeyboardInterrupt:
            erro('\nOperação cancelada pelo usuário', False)
            return 'N'
        else:
            if not resp:
                erro('Entrada vazia')
            elif resp.isnumeric():
                erro('Números não são válidos aqui')
            elif resp not in opts:
                erro('Esse caractere é inválido')
            else:
                return resp



def validar_texto(text, caracteres_permitidos):
    while True:
        try:
            texto_usuario = str(input(text))
        except KeyboardInterrupt:
            erro('\nOperação cancelada pelo usuário', False)
            return False
        else:
            if not texto_usuario:
                erro('O nome da tarefa deve ser preenchido', False)
            elif len(texto_usuario) > caracteres_permitidos:
                erro(f'Esse nome é muito longo! ({len(texto_usuario)} de {caracteres_permitidos} caracteres usados)', False)
            else:
                return texto_usuario



