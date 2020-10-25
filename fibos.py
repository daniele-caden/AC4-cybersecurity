import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def fibonacci ():
    x = 0
    y = 1
    contagem = 1
    limite = 100
    resultado = "0"
    while ( contagem < limite):
        z = x + y
        resultado += "," +str(z)
        y = z 
        x = y
        contagem += 1
    return resultado

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
