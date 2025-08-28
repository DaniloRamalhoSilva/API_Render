import os
from flask import Flask, request, jsonify  # Corrigido: 'Flask' para 'flask'

app = Flask(__name__)

@app.route('/teste', methods=['GET'])
def teste():
    return jsonify({"mensagem": "API funcionando!"})

if __name__ == '__main__':
    app.run(debug=True)