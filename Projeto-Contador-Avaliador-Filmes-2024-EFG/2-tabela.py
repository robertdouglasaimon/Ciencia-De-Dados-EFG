import sqlite3

# 1 - Criando o BD
conexao = sqlite3.connect('Projeto-Contador-Avaliador-Filmes/banco.db')

# 2 - Criando o cursor
cursor = conexao.cursor()

#3 - Criando a tabela
cursor.execute(
    """
        CREATE TABLE filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

#4 - Fecha conexao
conexao.close()
print("Tabela foi criada")