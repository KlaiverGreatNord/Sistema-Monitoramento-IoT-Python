import sqlite3
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# 1. Configuração do Banco de Dados
def init_db():
    conn = sqlite3.connect('industria.db')
    cursor = conn.cursor()
    # Cria uma tabela para guardar histórico dos sensores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperatura REAL,
            vibracao REAL,
            status TEXT,
            data_hora TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Inicializa o banco ao ligar o programa
init_db()

# 2. Rota para o Dashboard (Visualização)
@app.route('/')
def index():
    conn = sqlite3.connect('industria.db')
    cursor = conn.cursor()
    # Pega a última leitura para mostrar no topo
    cursor.execute('SELECT * FROM leituras ORDER BY id DESC LIMIT 1')
    ultima = cursor.fetchone()
    conn.close()
    return render_template('index.html', leitura=ultima)

# 3. Rota para receber dados do Sensor (API)
@app.route('/api/dados', methods=['POST'])
def receber_dados():
    dados = request.json
    temp = dados.get('temperatura')
    vib = dados.get('vibracao')
    
    # Regra de Negócio: Detecção de Anomalias
    status = "NORMAL"
    if temp > 90 or vib > 80:
        status = "PERIGO"
    elif temp > 70:
        status = "ALERTA"

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Salva no banco
    conn = sqlite3.connect('industria.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO leituras (temperatura, vibracao, status, data_hora) VALUES (?, ?, ?, ?)', 
                   (temp, vib, status, data_hora))
    conn.commit()
    conn.close()

    print(f"Recebido: Temp={temp}°C, Vib={vib}Hz -> Status: {status}")
    return jsonify({"mensagem": "Dados recebidos com sucesso!", "status_calculado": status})

# 4. Rota para o gráfico (atualização automática)
@app.route('/api/historico')
def historico():
    conn = sqlite3.connect('industria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT temperatura, vibracao, data_hora FROM leituras ORDER BY id DESC LIMIT 20')
    dados = cursor.fetchall()
    conn.close()
    return jsonify(dados)

if __name__ == '__main__':
    # Roda o servidor na porta 5000
    app.run(debug=True, port=5000)