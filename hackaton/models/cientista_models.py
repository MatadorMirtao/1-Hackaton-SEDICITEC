import sqlite3

DB_NAME = 'database.db'

def conectar():
    conexao = sqlite3.connect(DB_NAME)
    conexao.row_factory = sqlite3.Row  # Permite acessar as colunas pelo nome
    return conexao

def inicializar_banco(app):
    conexao = conectar()
    cursor = conexao.cursor()
    # Cria a tabela usando SQL puro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cientistas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            area TEXT NOT NULL,
            feito TEXT NOT NULL
        )
    ''')
    # Adiciona dados iniciais se a tabela estiver vazia
    cursor.execute('SELECT COUNT(*) FROM cientistas')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO cientistas (nome, area, feito) VALUES (?, ?, ?)",
                       ("Ada Lovelace", "Computação / Matemática", "Escreveu o primeiro algoritmo da história."))
        cursor.execute("INSERT INTO cientistas (nome, area, feito) VALUES (?, ?, ?)",
                       ("Enedina Alves Marques", "Engenharia Civil", "Primeira engenheira negra do Brasil."))
        conexao.commit()
    conexao.close()

def obter_todas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM cientistas')
    registros = cursor.fetchall()
    conexao.close()
    return [dict(r) for r in registros]

def obter_por_id(id_cientista):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM cientistas WHERE id = ?', (id_cientista,))
    registro = cursor.fetchone()
    conexao.close()
    return dict(registro) if registro else None

def adicionar(nome, area, feito):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO cientistas (nome, area, feito) VALUES (?, ?, ?)', (nome, area, feito))
    conexao.commit()
    conexao.close()

def atualizar(id_cientista, nome, area, feito):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('UPDATE cientistas SET nome = ?, area = ?, feito = ? WHERE id = ?', (nome, area, feito, id_cientista))
    conexao.commit()
    conexao.close()

def deletar(id_cientista):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM cientistas WHERE id = ?', (id_cientista,))
    conexao.commit()
    conexao.close()