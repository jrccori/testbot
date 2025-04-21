import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola desde Flask en Railway! 🚂'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa 5000 si no se encuentra PORT
    app.run(host='0.0.0.0', port=port)
