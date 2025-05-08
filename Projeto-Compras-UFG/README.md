# 📊 Análise de Dados de Compras com Streamlit

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Names](https://img.shields.io/badge/Names-Random%20Name%20Generator-green)

Este projeto permite a **geração, visualização, filtragem e análise de dados de compras** utilizando **Python** e **Streamlit**. Ele cria um dataset fictício de compras, lojas e produtos, permitindo interações dinâmicas para explorar os dados.

---

## 🚀 Funcionalidades

📌 **Geração de dados fictícios**  
📌 **Visualização interativa** dos dados  
📌 **Filtragem de colunas e registros**  
📌 **Adição de novas compras** ao dataset  
📌 **Análise de volumes de vendas**  
📌 **Criação de tabelas dinâmicas**  

---

## 📂 Estrutura do Projeto

```plaintext
📁 Projeto-Compras-UFG
│── 📁 datasets/               # Pasta onde os datasets são gerados
│── 📄 gere_datasets.py        # Gera os datasets fictícios
│── 📄 visualizando_tb.py      # Exibe os dados no Streamlit
│── 📄 selecionado_colunas.py  # Permite selecionar colunas e filtrar dados
│── 📄 adicionando_linhas.py   # Adiciona novas compras ao dataset
│── 📄 volumes_dados.py        # Analisa volumes de compras, lojas e vendedores
│── 📄 tb_dinâmicas.py         # Cria tabelas dinâmicas para análise personalizada
│── 📄 README.md               # Documentação do projeto
```

## 🛠️ Instalação e Uso

### 1️⃣ Instalar dependências
Antes de rodar o projeto, instale as bibliotecas necessárias:
```
pip install pandas streamlit names

```

### 2️⃣ Gerar os datasets
Execute o script para criar os arquivos de dados:
```
python gere_datasets.py

```

### 3️⃣ Visualizar os dados
Para abrir a interface do Streamlit e visualizar os dados:
```
streamlit run visualizando_tb.py

```

### 4️⃣ Filtrar colunas e registros
Para selecionar colunas e filtrar dados:
```
streamlit run selecionado_colunas.py
```

### 5️⃣ Adicionar novas compras
Para inserir novos registros no dataset:
```
streamlit run adicionando_linhas.py

```

### 6️⃣ Analisar volumes de vendas
Para visualizar estatísticas sobre compras, lojas e vendedores:
```
streamlit run volumes_dados.py

```

### 7️⃣ Criar tabelas dinâmicas
Para gerar tabelas dinâmicas e analisar os dados de forma personalizada:
```
streamlit run tb_dinâmicas.py

```

## 📊 Exemplo de Uso
<p>Após rodar <strong>volumes_dados.py</strong>, você verá métricas como:</p>

<ul>
    <li>✅ Valor total das compras no período: R$ 15.000,00</li>
    <li>✅ Quantidade de compras no período: 120</li>
    <li>✅ Principal loja: São Paulo</li>
    <li>✅ Principal vendedor: Ana Oliveira</li>
    <li>✅ Comissão total do vendedor: R$ 1.200,00</li>
</ul>

<p>Após rodar <strong>tb_dinâmicas.py</strong>, você poderá selecionar índices e colunas para criar tabelas dinâmicas, <br> 
analisando os dados de forma personalizada.</p>


## 📝 Contribuição
<p>Se quiser melhorar o projeto, sinta-se à vontade para abrir um <b>Pull Request</b> ou sugerir melhorias!</p>

## 📌 Licença
Este projeto é de uso livre para fins <b>educacionais</b> e <b>comerciais</b>.