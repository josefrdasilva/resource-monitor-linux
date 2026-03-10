import psutil
import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    while True:
        limpar_tela()
        print(f"--- Monitor em Tempo Real ---")
        print(f"CPU: {psutil.cpu_percent()}%")
        print(f"RAM Usada: {psutil.virtual_memory().percent}%")
        print(f"Freq CPU: {psutil.cpu_freq().current} MHz")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nMonitoramento parado.")