import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('Projeto-Contador-Avaliador-Filmes/banco.db')
cursor = conexao.cursor()

# 2 - Leitura de dados
dados = cursor.execute('SELECT * FROM filmes')

print(dados.fetchall())