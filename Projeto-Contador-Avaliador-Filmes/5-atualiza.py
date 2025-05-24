import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('Projeto-Contador-Avaliador-Filmes/banco.db')
cursor = conexao.cursor()

# 2 - Atualizando dados
id = 1
cursor.execute(
    """
        UPDATE filmes SET nome = ?
        WHERE id = ?
""",
    ("Homem Aranha", id)
)

conexao.commit()
conexao.close()
print("Dados atualizados")