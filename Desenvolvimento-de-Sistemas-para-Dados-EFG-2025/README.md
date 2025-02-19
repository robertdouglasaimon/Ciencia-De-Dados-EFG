# Biblioteca de Livros

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![SQLite](https://img.shields.io/badge/SQLite-3-green)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![Pillow](https://img.shields.io/badge/Pillow-image%20processing-blueviolet)

Aplicação de gerenciamento de biblioteca de livros desenvolvida em Python e SQLite. Este projeto está em andamento e servirá como base para o meu TCC.

## Funcionalidades

- Inserir novos livros na biblioteca
- Inserir novos usuários
- Exibir livros cadastrados
- Realizar empréstimos de livros
- Exibir livros emprestados no momento
- Visualizar todos os usuários cadastrados
- Visualizar devoluções de empréstimos
- Exibir todos os livros disponíveis

## Requisitos

- Python 3.8 ou superior
- SQLite

## Tecnologias Utilizadas

- Python: Linguagem de programação.
- SQLite: Banco de dados relacional.
- Tkinter: Biblioteca para interface gráfica.
- Pillow: Biblioteca para manipulação de imagens.

## Status do Projeto

O projeto está atualmente em desenvolvimento, com as funcionalidades básicas de inserção e exibição de dados já implementadas. Recentemente, foram adicionadas funcionalidades para a realização de empréstimos de livros e a exibição dos livros emprestados no momento.

## Modificações Recentes
* Adicionado: Função para inserir um livro insert_book.
* Adicionado: Função para inserir um usuário insert_user.
* Adicionado: Função para exibir todos os livros exibir_livros.
* Adicionado: Função para realizar empréstimos insert_loan.
* Adicionado: Função para exibir todos os livros emprestados no momento get_books_on_loan.

## Código Adicionado:

``` import sqlite3

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

    if not livros:
        print("Nenhum livro encontrado na biblioteca.")
        return []
    
    print("Livros na biblioteca:")
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Editora: {livro[3]}")
        print(f"Ano de publicação: {livro[4]}")
        print(f"ISBN: {livro[5]}")
        print("\n")
    return livros
        
# Função para realizar empréstimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimo (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?,?,?,?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()
    
# Função para exibir todos os livros emprestados no momento
def get_books_on_loan():
    conn = connect()
    result = conn.execute("""SELECT livros.titulo AS livro_titulo, usuarios.nome AS usuario_nome, emprestimo.id, 
                                     usuarios.sobrenome AS usuario_sobrenome, emprestimo.data_emprestimo, emprestimo.data_devolucao 
                              FROM livros 
                              INNER JOIN emprestimo ON livros.id = emprestimo.id_livro
                              INNER JOIN usuarios ON usuarios.id = emprestimo.id_usuario
                              WHERE emprestimo.data_devolucao IS NULL""").fetchall()
    conn.close()
    return result

# Função para exibir devoluções
def exibir_devolucoes():
    conn = connect()
    print("Conexão aberta:", conn)
    cursor = conn.execute("""SELECT livros.titulo AS livro_titulo, usuarios.nome AS usuario_nome, emprestimo.id, 
                                     usuarios.sobrenome AS usuario_sobrenome, emprestimo.data_emprestimo, emprestimo.data_devolucao 
                              FROM livros 
                              INNER JOIN emprestimo ON livros.id = emprestimo.id_livro
                              INNER JOIN usuarios ON usuarios.id = emprestimo.id_usuario
                              WHERE emprestimo.data_devolucao IS NULL""")
    devolucoes = cursor.fetchall()
    conn.close()
    return devolucoes 
```
## Alteração 2: Mudanças no Controle do Menu e Formulário de Usuário
* Adicionado: Função control para controle do menu.
* Adicionado: Formulário de novo usuário e validação de campos.
* Adicionado: Função get_users para buscar todos os usuários.
* Adicionado: Função ver_usuarios para exibir todos os usuários no Treeview.
* Adicionado: Função exibir_todos_livros para mostrar todos os livros disponíveis.
* Adicionado: Função devolucao_emprestimos para mostrar devoluções de empréstimos.
* Adicionado: Função ver_livros_emprestados para exibir livros emprestados no momento.

```
# Função para controlar o menu
def control(i):
    
    # Novo usuário
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'novo_usuario'
        novo_usuario()
    
    # Exibir todos os usuários
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'ver_usuarios'
        ver_usuarios()
        
    # Exibir todos os livros
    if i == 'exibir_todos_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'exibir_todos_livros'
        exibir_todos_livros()
    
    # Devolução de empréstimos
    if i == 'devolucao_emprestimos':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'devolucao_empre
```



## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature (git checkout -b feature/AmazingFeature).
3. Faça commit das suas alterações (git commit -m 'Add some AmazingFeature').
4. Faça push para a branch (git push origin feature/AmazingFeature).
5. Abra um pull request.

## Como Rodar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/robertdouglasaimon/Ciencia-De-Dados-EFG.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Ciencia-De-Dados-EFG/Projeto-Profissional-de-Gestao-de-Dados
    ```

3. Certifique-se de que o SQLite está instalado.

4. Execute o script para criar as tabelas:
    ```bash
    python create_tables.py
    ```

5. Execute o script principal para inserir e exibir dados:
    ```bash
    python main.py
    ```

6. Execute o script da interface gráfica:
    ```bash
    python tela.py
    ```

## Estrutura do Projeto

```plaintext
Projeto-Profissional-de-Gestao-de-Dados/
│
├── create_tables.py         # Script para criação das tabelas no banco de dados
├── main.py                  # Script principal contendo as funções de inserir e exibir dados
├── view.py                  # Arquivo com funções CRUD do banco de dados, incluindo empréstimos
├── tela.py                  # Script para a interface gráfica
├── img/                     # Diretório com as imagens usadas na interface gráfica
│   ├── icons8-biblioteca-50.png
│   ├── icons8-usuário-100.png
│   ├── icons8-livro-100.png
│   ├── icons8-adicionar-100.png
│   ├── icons8-salvar-100.png
│   ├── icons8-emprestimo-100.png
│   ├── icons8-devolucao-100.png
│   └── ...                  # Outras imagens
└── README.md                # Documentação do projeto

