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


# Função para realizar o empréstimo
def inserir_emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) \
          VALUES (?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()
    
# Função para exibir todos os livros emprestados no momento
def livros_emprestados_no_momento():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, emprestimos.id, usuarios.sobrenome, \
        emprestimos.data_emprestimo, emprestimos.data_devolucao \
        FROM livros \
        INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
        INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
        WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# Inserir dados antes de exibi-los
# inserir_livro('A arte da guerra', 'Sun Tzu', 'Editora 1', 2000, '1234567890')
# inserir_usuario('Usuario 1', 'Sobrenome 1', 'Endereco 1', 'Email 1', 'Telefone 1')

# inserir_livro('A culpa é das estrelas', 'John Green', 'Editora 1', 2000, '1234567890')
# inserir_usuario('Usuario 2', 'Sobrenome 2', 'Endereco 2', 'Email 2', 'Telefone 2')

# Exemplo de uso das funções
inserir_emprestimo(1, 1, "2023-01-01", "NULL")
livros_emprestados = livros_emprestados_no_momento()
print(livros_emprestados)

# update_loan_return_date(1, "2023-02-01")
    
# # Chamando a função exibir_livros para mostrar os livros inseridos
exibir_livros()

# Função para exibir o usuário
def exibir_usuarios():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    conn.close()
    return usuarios