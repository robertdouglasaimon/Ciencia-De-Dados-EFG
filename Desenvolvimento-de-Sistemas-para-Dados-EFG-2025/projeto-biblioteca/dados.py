# Importando a biblioteca sqlite3
import sqlite3

# Conexão com o banco de dados
try:
    conn = sqlite3.connect('dados.db')
    # ... (resto do seu código)
    conn.commit()
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
# Criando tabela de emprestimo

    
# Criando a tabela de livros
conn.execute( 'CREATE TABLE livros ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        titulo TEXT, \
        autor TEXT, \
        editora TEXT, \
        ano_publicacao INTEGER, \
        isbn TEXT)'
    )

# Criando tabela de usuarios
conn.execute( 'CREATE TABLE usuarios ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        nome TEXT, \
        sobrenome TEXT, \
        endereco TEXT, \
        email TEXT, \
        telefone TEXT)'
    )

conn.execute('''
    CREATE TABLE emprestimo (
        id INTEGER PRIMARY KEY,
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

