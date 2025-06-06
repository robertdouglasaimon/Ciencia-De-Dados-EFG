import sqlite3

# Conexão com o banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função para inserir um livro
def insert_book(titulo, autor, editora, ano_publicacao, ISBN):
    conn = connect()
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES (?,?,?,?,?)", (titulo, autor, editora, ano_publicacao, ISBN))
    conn.commit()
    conn.close()

# Função para inserir um usuário
def insert_user(id, nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios (id, nome, sobrenome, endereco, email, telefone) VALUES (?,?,?,?,?,?)", (id, nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para exibir todos os livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()    
    return livros

# exibir_livros() 

# Função para exibir as data_devolucao e afins
def exibir_devolucoes():
    conn = connect()
    print("Conexão aberta:", conn)
    cursor = conn.execute("""SELECT emprestimo.id, livros.titulo AS livro_titulo, usuarios.nome AS usuario_nome,  
                                    emprestimo.data_emprestimo, emprestimo.data_devolucao 
                              FROM livros 
                              INNER JOIN emprestimo ON livros.id = emprestimo.id_livro
                              INNER JOIN usuarios ON usuarios.id = emprestimo.id_usuario
                              WHERE emprestimo.data_devolucao IS NULL""")
    devolucoes = cursor.fetchall()
    conn.close()
    return devolucoes
    
# Função para realizar empréstimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimo (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?,?,?,?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()
    
# Função para inserir um livro
def insert_book(titulo, autor, editora, ano_publicacao, ISBN):
    conn = connect()
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES (?,?,?,?,?)", (titulo, autor, editora, ano_publicacao, ISBN))
    conn.commit()
    print("Livro inserido com sucesso!")
    conn.close()
    
# Função para exibir todos os livros emprestados no momento
def get_books_on_loan():
    conn = connect()
    result = conn.execute("""SELECT livros.titulo AS livro_titulo, usuarios.nome AS usuario_nome,  
                              emprestimo.data_emprestimo, emprestimo.data_devolucao 
                              FROM livros 
                              INNER JOIN emprestimo ON livros.id = emprestimo.id_livro
                              INNER JOIN usuarios ON usuarios.id = emprestimo.id_usuario
                              WHERE emprestimo.data_devolucao IS NULL""").fetchall()
    conn.close()
    return result
print(get_books_on_loan())

def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    # print(users)
    conn.close()
    return users

# Exemplo de como inserir dados no banco de dados
# insert_user(1, "João", "Silva", "Rua A, 123", "GZ0jg@example.com", "123-456-7890")
# insert_book("Império das tormentas", "Jon Skrov", "Editora Arqueiro", 2018, "123456789")

# insert_user(2, "Erika", "Wanessa", "Rua B, 456", "erikawanessa@gmail.com", "987-654-3210")
# insert_book('A culpa é das estrelas', 'John Green', 'Intri', 2018, '123456789')

# Insere um empréstimo
# insert_loan(1, 1, "2023-01-01", None)
# insert_loan(2, 2, "2023-01-01", None)
livros_emprestados = get_books_on_loan()
# print(livros_emprestados)

exibir_livros()
