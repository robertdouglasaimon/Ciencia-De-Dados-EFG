# importando SQLite
import sqlite3 as lite

# CRUD
# CREATE = Inserir
# READ = Ler
# READY = Editar/Acessar
# UPDATE = Atualizar
# DELETE = Deletar

# criando a conexão com o banco de dados
con = lite.connect('banco.db')

# Inserir informação
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, sobre) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Acessar informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista

# Atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=? , telefone=?, dia_em=?, estado=?, sobre=? WHERE id=?"
        cur.execute(query, i)

# Deletar informação
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
