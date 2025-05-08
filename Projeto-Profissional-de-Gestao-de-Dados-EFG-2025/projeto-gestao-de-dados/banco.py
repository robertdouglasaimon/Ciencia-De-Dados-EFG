# importando o banco de dados SQLite
import sqlite3 as lite

# criando a conexão com o banco de dados
con = lite.connect('banco.db')

with con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS formulario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            dia_em DATE,
            estado TEXT,
            sobre TEXT)  -- Alterado de 'assunto' para 'sobre'
    """)

# Funções CRUD (Create, Read, Update, Delete)

# Inserir Informação:
def inserir_info(i):
    with lite.connect('banco.db') as con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, sobre) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Acessar Informação:
def mostrar_info():
    lista = []
    with lite.connect('banco.db') as con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        for i in informacao:
            lista.append(i)
    return lista

# Atualizar Informação:
def atualizar_info(i):
    with lite.connect('banco.db') as con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, sobre=? WHERE id=?"
        cur.execute(query, i)

# Deletar Informação:
def deletar_info(i):
    with lite.connect('banco.db') as con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
