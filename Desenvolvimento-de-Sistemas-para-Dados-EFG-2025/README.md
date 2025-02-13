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

## Requisitos

- Python 3.8 ou superior
- SQLite

## Tecnologias Ultilizadas
- Python: Linguagem de programação.
- SQLite: Banco de dados relacional.
- Tkinter: Biblioteca para interface gráfica.
- Pillow: Biblioteca para manipulação de imagens.

## Status do Projeto
O projeto está atualmente em desenvolvimento, com as funcionalidades básicas de inserção e exibição de dados já implementadas. Recentemente, foram adicionadas funcionalidades para a realização de empréstimos de livros e a exibição dos livros emprestados no momento.

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
│   └── ...                  # Outras imagens
└── README.md                # Documentação do projeto

