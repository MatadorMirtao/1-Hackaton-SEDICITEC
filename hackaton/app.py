from flask import Flask
from models.cientista_models import inicializar_banco
from controllers.cientistas_controllers import registrar_rotas

app = Flask(__name__)

# Inicializa o Banco de Dados SQL puro
inicializar_banco(app)

# Registra as rotas
registrar_rotas(app)

if __name__ == '__main__':
    app.run(debug=True)