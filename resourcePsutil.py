import psutil
import time
from prometheus_client import Gauge, start_http_server

#Medicoes
cpu_percent_gauge = Gauge("monitor_cpu_percent", "Percentual de uso do CPU")
cpu_freq_gauge = Gauge("monitor_cpu_freq", "Frequencia do CPU")
cpu_count_gauge = Gauge("monitor_cpu_count", "Núcleos lógicos do CPU")
ram_used_gauge = Gauge("monitor_ram_used", "Memória RAM usada")
disk_usage_gauge = Gauge("monitor_disk_usage", "Porcentagem de uso de Disco")
disk_free_gauge = Gauge("monitor_disk_free", "Espaço livre no Disco")
disk_used_gauge = Gauge("monitor_disk_used", "Espaço usado no Disco")


## Inicia na porta 8000
start_http_server(8000)

while True:

    ##COLETANDO DADOS
    #CPU
    cpu_count = psutil.cpu_count()

    cpu_freq = psutil.cpu_freq().current

    cpu_percent = psutil.cpu_percent(interval=1)

    #Disk
    disk = psutil.disk_usage("/")
    disk_usage = disk.percent
    disk_free = disk.free / (1024**3)
    disk_used = disk.used / (1024**3)

    #RAM
    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024**3)



    ##SETANDO OS DADOS
    cpu_percent_gauge.set(cpu_percent)
    
    cpu_freq_gauge.set(cpu_freq)

    cpu_count_gauge.set(cpu_count)

    ram_used_gauge.set(ram_used)

    disk_usage_gauge.set(disk_usage)

    disk_free_gauge.set(disk_free)

    disk_used_gauge.set(disk_used)

    ## Tempo que funciona
    time.sleep(0.1)

    ## Sem break?