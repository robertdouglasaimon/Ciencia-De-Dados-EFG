# Biblioteca de Livros

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![SQLite](https://img.shields.io/badge/SQLite-3-green)

Aplicação de gerenciamento de biblioteca de livros desenvolvida em Python e SQLite. Este projeto está em andamento e servirá como base para o meu TCC.

## Funcionalidades

- Inserir novos livros na biblioteca
- Inserir novos usuários
- Exibir livros cadastrados

## Requisitos

- Python 3.8 ou superior
- SQLite

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

## Estrutura do Projeto

```markdown
Projeto-Profissional-de-Gestao-de-Dados/
│
├── create_tables.py         # Script para criação das tabelas no banco de dados
├── main.py                  # Script principal contendo as funções de inserir e exibir dados (a ser desenvolvida)
├── README.md                # Documentação do projeto
├── banco.py                 # Arquivo com funções CRUD do banco de dados
└── view.py                  # Interface do usuário (a ser desenvolvida)
