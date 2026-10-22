from flask import render_template, request, redirect, url_for, jsonify
from models import cientista_models

def registrar_rotas(app):

    @app.route('/')
    def home():
        cientistas = cientista_models.obter_todas()
        return render_template('index.html', cientistas=cientistas)

    @app.route('/adicionar', methods=['POST'])
    def adicionar():
        nome = request.form.get('nome')
        area = request.form.get('area')
        feito = request.form.get('feito')
        if nome and area and feito:
            cientista_models.adicionar(nome, area, feito)
        return redirect(url_for('home'))

    @app.route('/editar/<int:id>', methods=['GET'])
    def carregar_edicao(id):
        cientista = cientista_models.obter_por_id(id)
        if not cientista:
            return redirect(url_for('home'))
        return render_template('editar.html', cientista=cientista)

    @app.route('/atualizar/<int:id>', methods=['POST'])
    def atualizar(id):
        nome = request.form.get('nome')
        area = request.form.get('area')
        feito = request.form.get('feito')
        if nome and area and feito:
            cientista_models.atualizar(id, nome, area, feito)
        return redirect(url_for('home'))

    @app.route('/deletar/<int:id>', methods=['POST'])
    def deletar(id):
        cientista_models.deletar(id)
        return redirect(url_for('home'))

    @app.route('/api/cientistas')
    def api_cientistas():
        return jsonify(cientista_models.obter_todas())