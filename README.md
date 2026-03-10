# Resource Monitor: Dashboard de Monitoramento com Docker, Prometheus e Grafana

Este projeto é uma ferramenta de monitoramento de infraestrutura em tempo real. Ele coleta métricas de hardware (CPU, RAM, Disco) via script Python e as apresenta através de uma arquitetura baseada em containers.

## Funcionalidades
- **Coleta de Métricas:** Script em Python utilizando `psutil` para monitoramento de recursos.
- **Armazenamento de Séries Temporais:** Prometheus para ingestão e persistência de dados.
- **Visualização de Dados:** Grafana para dashboards interativos e alertas.
- **Orquestração:** Todo o ambiente é gerenciado via `Docker Compose`, garantindo portabilidade e fácil deploy.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.12
- **Monitoramento:** Prometheus e `prometheus_client`
- **Visualização:** Grafana
- **Containerização:** Docker & Docker Compose

## Como rodar
1. Clone o repositório.
2. Certifique-se de ter o Docker e o Docker Compose instalados.
3. Suba o ambiente: `sudo docker compose up -d`
4. Acesse o Grafana na porta 3000 e o Prometheus na porta 9090.
5. Edite sua Dashboard usando o Grafana
