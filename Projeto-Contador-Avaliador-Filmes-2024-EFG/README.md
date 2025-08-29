# Projeto Contador Avaliador de Filmes 🎬⭐

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-0.92-orange?logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.39-blue?logo=sqlite&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white)

---

## Sobre o Projeto

Este projeto foi desenvolvido como exercício da disciplina **Storytelling de Dados - Aplicação WEB** ministrada pelo professor **Felipe** na instituição **EFG/UFG**.  

O objetivo é criar uma aplicação web simples para cadastrar, avaliar e listar filmes utilizando banco de dados SQLite e a biblioteca Streamlit para interface gráfica. A aplicação permite:

- Inserir filmes com nome, ano e nota;
- Visualizar a lista atualizada de filmes cadastrados;
- Manipular dados no banco SQLite com funções de inserção, atualização, exclusão e consulta.

---

## Como Funciona

O projeto é composto por dois principais módulos:

1. **Banco de Dados (SQLite)**
   - Criação da tabela `filmes` com colunas `id`, `nome`, `ano` e `nota`;
   - Inserção manual de dados via código e funções para manipulação do banco (`insere_dados()`, `obter_dados()`, etc.);
   - Comandos SQL para criação, atualização e exclusão de registros.
   - Abra o "bloco-de-notas.txt" para ver os comandos necessários para executar partes importantes do código.

2. **Aplicação Web (Streamlit)**
   - Interface simples para o usuário inserir novos filmes informando nome, ano e nota;
   - Exibição dos filmes cadastrados em formato de tabela;
   - Feedback visual quando um filme é adicionado com sucesso.

---

## Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [SQLite](https://www.sqlite.org/index.html) — banco de dados leve, embutido
- [Streamlit](https://streamlit.io/) — framework para criação de apps web interativos
- Git e GitHub para versionamento e hospedagem do código

---

## Como Rodar o Projeto Localmente

1. Clone o repositório:

```bash
git clone https://github.com/robertdouglasaimon/Ciencia-De-Dados-EFG.git
```

2. Navegue até a pasta do projeto:

```bash
cd Ciencia-De-Dados-EFG/Projeto-Contador-Avaliador-Filmes
```

3. Instale as dependências (recomendo criar um ambiente virtual):

```bash
pip install streamlit
```

4. Execute o app Streamlit:

```bash
streamlit run app.py
```

4. Execute o app Streamlit:

## Estrutura do Projeto
* ### banco.db — arquivo do banco de dados SQLite;

* ### dados.py — funções para conexão, inserção e leitura do banco;

* ### app.py — aplicação Streamlit para interação com o usuário;

* ### Código SQL para criação, atualização e exclusão de dados está embutido nos scripts.

## Agradecimentos
Este projeto é parte do trabalho acadêmico na disciplina Storytelling de Dados - Aplicação WEB, ministrada pelo professor Felipe na EFG/UFG. Agradeço a oportunidade de aprendizado e desenvolvimento prático.

```
Se tiver dúvidas ou quiser contribuir, fique à vontade para abrir issues ou pull requests.
```

##

Robert Douglas <br>
Projeto desenvolvido em 2025
