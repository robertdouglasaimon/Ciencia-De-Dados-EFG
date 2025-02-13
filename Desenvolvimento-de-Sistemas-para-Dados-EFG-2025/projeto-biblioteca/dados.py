# Importando a biblioteca sqlite3
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('dados.db')

# Criando a tabela de livros
conn.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        editora TEXT,
        ano_publicacao INTEGER,
        ISBN TEXT
    )
''')

# Criando a tabela de usuários
conn.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        sobrenome TEXT,
        endereco TEXT,
        email TEXT,
        telefone TEXT
    )
''')

# Criando tabela de emprestimo de livrosDD
conn.execute('''
    CREATE TABLE IF NOT EXISTS emprestimos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_livro INTEGER,
        id_usuario INTEGER,
        data_emprestimo TEXT,
        data_devolucao TEXT,
        FOREIGN KEY (id_livro) REFERENCES livros(id),
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
    )
''')

conn.commit()
conn.close()
