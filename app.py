from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola desde Flask en Render!"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Hola, {nombre}! Bienvenido a Flask en Render."


