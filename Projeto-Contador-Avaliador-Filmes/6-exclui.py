import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('Projeto-Contador-Avaliador-Filmes/banco.db')
cursor = conexao.cursor()

# 2 - Atualizando dados
id = (1,2)
cursor.execute(
    """
        DELETE FROM filmes
        WHERE ID in (?,?)
    """,
    id
)

conexao.commit()
print("Dados excluidos")