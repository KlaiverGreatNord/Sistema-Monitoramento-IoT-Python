import requests
import time
import random

# URL do nosso servidor (onde o app.py está rodando)
URL_SERVIDOR = "http://127.0.0.1:5000/api/dados"

print("--- INICIANDO SENSOR VIRTUAL IOT ---")
print("Pressione Ctrl+C para parar.")

maquina_ligada = True

try:
    while maquina_ligada:
        # 1. Simulação dos Sensores (Gerando números aleatórios)
        # Temperatura normal entre 50-70, mas as vezes dá picos
        temperatura = round(random.uniform(50.0, 95.0), 2) 
        
        # Vibração normal até 50, acima disso é problema
        vibracao = round(random.uniform(20.0, 85.0), 2)

        # Pacote de dados (JSON)
        payload = {
            "temperatura": temperatura,
            "vibracao": vibracao
        }

        # 2. Transmissão via HTTP (POST)
        try:
            resposta = requests.post(URL_SERVIDOR, json=payload)
            if resposta.status_code == 200:
                print(f"📡 Enviado: Temp={temperatura}°C | Vib={vibracao}Hz -> Servidor respondeu: OK")
            else:
                print("❌ Erro ao enviar dados.")
        except:
            print("⚠️ Servidor desconectado. Tentando novamente...")

        # Espera 2 segundos antes da próxima leitura
        time.sleep(2)

except KeyboardInterrupt:
    print("\nSensor desligado.")