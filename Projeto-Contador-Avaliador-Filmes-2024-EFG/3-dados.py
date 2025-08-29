import sqlite3

#1-Conectando no BD
conexao = sqlite3.connect('Projeto-Contador-Avaliador-Filmes/banco.db')
cursor = conexao.cursor()

#2-Inserindo dados
cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Sonic',2020,8)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Super Mario Bros. O Filme',2023,9)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Homem-Aranha: Através do Aranhaverso',2023,9.5)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Duna: Parte Dois',2024,9.2)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Oppenheimer',2023,9.0)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Barbie',2023,7.5)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Guardians of the Galaxy Vol. 3',2023,8.8)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Vingadores: Ultimato',2019,9.1)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Parasita',2019,9.3)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('Interestelar',2014,9.0)
"""
)

cursor.execute(
"""
INSERT INTO filmes(nome, ano,nota)
VALUES ('A Origem',2010,8.8)
"""
)


conexao.commit()
conexao.close()
print("Dados inseridos na tabela")