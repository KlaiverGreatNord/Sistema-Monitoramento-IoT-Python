# Sistema de Monitoramento Inteligente via IoT (Simulado)

Este projeto implementa um sistema completo de monitoramento industrial simulado, atendendo aos requisitos da disciplina.

## 📋 Funcionalidades
- **Hardware Simulado:** Sensor virtual em Python que gera dados de Temperatura e Vibração.
- **Backend:** Servidor Flask que recebe os dados via HTTP (API REST).
- **Banco de Dados:** Armazenamento histórico em SQLite.
- **Dashboard:** Interface Web para visualização em tempo real com alertas visuais.
- **Regras de Negócio:** Detecção automática de anomalias (Status: Normal, Alerta, Perigo).

## 🚀 Como rodar o projeto

### Pré-requisitos
Instale as dependências:
```bash
pip install flask requests
