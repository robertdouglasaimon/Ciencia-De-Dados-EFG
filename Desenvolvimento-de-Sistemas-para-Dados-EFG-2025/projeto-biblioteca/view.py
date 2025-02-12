import sqlite3

# Conexão com o banco de dados ou cria um novo banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função para inserir dados na tabela de livros
def inserir_livro(titulo, autor, editora, ano_publicacao, ISBN):
    conn = connect()
    conn.execute('INSERT INTO livros (titulo, autor, editora, ano_publicacao, ISBN) \
          VALUES (?, ?, ?, ?, ?)', 
          (titulo, autor, editora, ano_publicacao, ISBN))
    conn.commit()
    conn.close()

# Função para inserir usuários na tabela de usuários
def inserir_usuario(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute('INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone) \
          VALUES (?, ?, ?, ?, ?)', 
          (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para exibir os livros cadastrados na tabela de livros
def exibir_livros():
    conn = connect()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.close()
    
    # Exibindo os livros cadastrados
    if not livros:
        print("Nenhum livro encontrado na biblioteca.")
        return

    print("Livros cadastrados na biblioteca:")
    for livro in livros:
        print(f'ID: {livro[0]}')
        print(f'Titulo: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Editora: {livro[3]}')
        print(f'Ano de Publicacao: {livro[4]}')
        print(f'ISBN: {livro[5]}')
        print("\n")

# Inserir dados antes de exibi-los
# inserir_livro('A arte da guerra', 'Sun Tzu', 'Editora 1', 2000, '1234567890')
# inserir_usuario('Usuario 1', 'Sobrenome 1', 'Endereco 1', 'Email 1', 'Telefone 1')

inserir_usuario('Usuario 2', 'Sobrenome 2', 'Endereco 2', 'Email 2', 'Telefone 2')
inserir_livro('Imperio das tormentas', 'Jon Skovron', 'Editora Arqueiro', 2018, '1234567890')

# Chamando a função exibir_livros para mostrar os livros inseridos
exibir_livros()
