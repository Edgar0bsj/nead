import time
import sys

from colorama import Fore

def animacao_carregamento(msg:str = 'Carregando...'):
    simbolos = ["|", "/", "-", "\\"]
    for i in range(30):  # número de ciclos
        simbolo = simbolos[i % len(simbolos)]
        sys.stdout.write(f"\r{msg} {simbolo}")
        sys.stdout.flush()
        time.sleep(0.1)