import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

# Criando uma pasta datasets
pastas_datasets = Path(__file__).parent / "datasets"

pastas_datasets.mkdir(parents=True, exist_ok=True)

LOJAS = [
    {"estado": "SP", "cidade": "Sao Paulo", "vendedores": ["Ana Oliveira", "Lucas Pereira"]},
    {"estado": "MG", "cidade": "Belo Horizonte", "vendedores": ["Maria Souza", "Pedro Alves"]},
    {"estado": "RJ", "cidade": "Rio de Janeiro", "vendedores": ["Joaquim Silva", "Claudia Lima"]},
    {"estado": "SC", "cidade": "Florianopolis", "vendedores": ["Pedro Alves", "Carla Mendes"]},
    {"estado": "RS", "cidade": "Porto Alegre", "vendedores": ["Pedro Alves", "Carla Mendes"]},
    {"estado": "BA", "cidade": "Salvador", "vendedores": ["João Silva", "Maria Oliveira"]},
    {"estado": "PR", "cidade": "Curitiba", "vendedores": ["Carlos Souza", "Luana Pereira"]},
    {"estado": "PE", "cidade": "Recife", "vendedores": ["Lucas Alves", "Ana Costa"]},
    {"estado": "CE", "cidade": "Fortaleza", "vendedores": ["Fernanda Silva", "Rodrigo Souza"]},
    {"estado": "GO", "cidade": "Goiânia", "vendedores": ["Juliana Mendes", "Carlos Almeida"]},
    {"estado": "MT", "cidade": "Cuiabá", "vendedores": ["Sofia Lima", "Fábio Costa"]},
    {"estado": "AM", "cidade": "Manaus", "vendedores": ["Henrique Alves", "Rafaela Costa"]},
    {"estado": "ES", "cidade": "Vitória", "vendedores": ["Mariana Santos", "Lucas Ferreira"]},
    {"estado": "AL", "cidade": "Maceió", "vendedores": ["Bruna Silva", "Paulo Oliveira"]},
    {"estado": "MS", "cidade": "Campo Grande", "vendedores": ["Ricardo Mendes", "Carla Alves"]},
    {"estado": "SE", "cidade": "Aracaju", "vendedores": ["Tatiane Pereira", "Gustavo Costa"]},
    {"estado": "MA", "cidade": "São Luís", "vendedores": ["Felipe Silva", "Amanda Pereira"]},
    {"estado": "PI", "cidade": "Teresina", "vendedores": ["Daniela Souza", "Ricardo Alves"]},
    {"estado": "RN", "cidade": "Natal", "vendedores": ["Nayara Costa", "Fábio Souza"]},
    {"estado": "PB", "cidade": "João Pessoa", "vendedores": ["Amanda Lima", "Bruno Almeida"]},
    {"estado": "DF", "cidade": "Brasília", "vendedores": ["Aline Souza", "Rafael Costa"]},
    {"estado": "RO", "cidade": "Porto Velho", "vendedores": ["Beatriz Mendes", "Felipe Ferreira"]},
    {"estado": "AC", "cidade": "Rio Branco", "vendedores": ["Marcelo Pereira", "Patrícia Alves"]},
    {"estado": "TO", "cidade": "Palmas", "vendedores": ["Simone Oliveira", "Caio Souza"]},
    {"estado": "SC", "cidade": "Joinville", "vendedores": ["Paula Costa", "Lucas Rocha"]},
    {"estado": "RS", "cidade": "Caxias do Sul", "vendedores": ["José Silva", "Laura Pereira"]},
    {"estado": "PR", "cidade": "Londrina", "vendedores": ["Gustavo Ferreira", "Michele Almeida"]},
    {"estado": "SP", "cidade": "Campinas", "vendedores": ["Ricardo Pereira", "Sabrina Souza"]},
    {"estado": "MG", "cidade": "Uberlândia", "vendedores": ["Eduardo Lima", "Cristiane Alves"]},
    {"estado": "RJ", "cidade": "Niterói", "vendedores": ["Eliane Costa", "Marcos Ferreira"]},
    {"estado": "BA", "cidade": "Feira de Santana", "vendedores": ["Carla Almeida", "José Ferreira"]},
    {"estado": "ES", "cidade": "Linhares", "vendedores": ["Felipe Mendes", "Mônica Alves"]},
    {"estado": "SC", "cidade": "Blumenau", "vendedores": ["Júlia Pereira", "Gustavo Lima"]},
    {"estado": "RS", "cidade": "Pelotas", "vendedores": ["Marina Alves", "Rodrigo Pereira"]},
    {"estado": "MT", "cidade": "Várzea Grande", "vendedores": ["Beatriz Rocha", "Vinícius Souza"]},
    {"estado": "PE", "cidade": "Olinda", "vendedores": ["Leonardo Almeida", "Renata Costa"]},
    {"estado": "CE", "cidade": "Juazeiro do Norte", "vendedores": ["Gabriela Lima", "Felipe Costa"]},
    {"estado": "GO", "cidade": "Anápolis", "vendedores": ["Carla Mendes", "Aline Ferreira"]},
    {"estado": "MG", "cidade": "Juiz de Fora", "vendedores": ["Renata Souza", "Carlos Lima"]},
    {"estado": "SP", "cidade": "São Bernardo do Campo", "vendedores": ["Igor Souza", "Raquel Oliveira"]},
    {"estado": "RJ", "cidade": "Campos dos Goytacazes", "vendedores": ["Eduarda Ferreira", "José Mendes"]},
    {"estado": "SC", "cidade": "Itajaí", "vendedores": ["Felipe Pereira", "Simone Souza"]},
    {"estado": "RS", "cidade": "Santa Maria", "vendedores": ["Aline Rocha", "Gustavo Almeida"]},
    {"estado": "PR", "cidade": "Foz do Iguaçu", "vendedores": ["Mário Ferreira", "Patrícia Mendes"]},
    {"estado": "SP", "cidade": "São José dos Campos", "vendedores": ["Lucas Rocha", "Júlia Mendes"]},
    {"estado": "MG", "cidade": "Uberaba", "vendedores": ["Amanda Souza", "Lucas Costa"]},
    {"estado": "BA", "cidade": "Vitória da Conquista", "vendedores": ["Roberta Pereira", "Tiago Rocha"]},
]

PRODUTOS = [
    {"nome": "Smartphone Samsung Galaxy S20", "id": 0, "preco": 4000},
    {"nome": "Notbook Dell Inspiron", "id": 1, "preco": 3000},
    {"nome": "Tablet Apple iPad", "id": 2, "preco": 2000},
    {"nome": "Smartwatch Garmin Forerunner", "id": 3, "preco": 1000},
    {"nome": "Fone de Ouvido JBL", "id": 4, "preco": 500},
    {"nome": "Câmera Canon EOS 80D", "id": 5, "preco": 3500},
    {"nome": "Notebook Lenovo ThinkPad", "id": 6, "preco": 4500},
    {"nome": "TV Samsung 55 polegadas", "id": 7, "preco": 2500},
    {"nome": "Câmera GoPro Hero 8", "id": 8, "preco": 2000},
    {"nome": "Fone de Ouvido Sony WH-1000XM4", "id": 9, "preco": 1500},
    {"nome": "Xbox Series X", "id": 10, "preco": 4500},
    {"nome": "PlayStation 5", "id": 11, "preco": 5000},
    {"nome": "Smartphone Apple iPhone 12", "id": 12, "preco": 7000},
    {"nome": "Smartwatch Apple Watch Series 6", "id": 13, "preco": 2500},
    {"nome": "AirPods Pro", "id": 14, "preco": 1000},
    {"nome": "Geladeira Brastemp 400L", "id": 15, "preco": 3000},
    {"nome": "Micro-ondas Panasonic 32L", "id": 16, "preco": 800},
    {"nome": "Ventilador Mondial 40cm", "id": 17, "preco": 150},
    {"nome": "Notebook Acer Predator Helios", "id": 18, "preco": 7000},
    {"nome": "Máquina de Lavar LG 11kg", "id": 19, "preco": 2500},
    {"nome": "Ar-condicionado Samsung 12000 BTU", "id": 20, "preco": 2000},
    {"nome": "Smartphone Xiaomi Mi 11", "id": 21, "preco": 3500},
    {"nome": "Fritadeira Elétrica Philco", "id": 22, "preco": 500},
    {"nome": "Câmera de Segurança Intelbras", "id": 23, "preco": 600},
    {"nome": "Secador de Cabelos Taiff", "id": 24, "preco": 250},
    {"nome": "Aspirador de Pó Electrolux", "id": 25, "preco": 1000},
    {"nome": "TV LG OLED 55\"", "id": 26, "preco": 6000},
    {"nome": "Air Fryer Philips Walita", "id": 27, "preco": 600},
    {"nome": "Máquina de Café Expresso Nespresso", "id": 28, "preco": 2000},
    {"nome": "Drone DJI Mavic Air 2", "id": 29, "preco": 6000},
    {"nome": "Notebook Asus ROG Strix", "id": 30, "preco": 7500},
    {"nome": "Câmera de Ação Xiaomi Yi", "id": 31, "preco": 700},
    {"nome": "Teclado Mecânico Razer", "id": 32, "preco": 300}
]

FORMA_PG = ["cartão de crédito", "boleto", "pix", "dinheiro"]
GENERO_CLIENTES = ["male", "female"]

compras = []

for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja["vendedores"])
    produto = random.choice(PRODUTOS)
    hora_compra = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)
)
genero_cliente = random.choice(GENERO_CLIENTES)
nome_cliente = names.get_full_name(genero_cliente)
forma_pagamento = random.choice(FORMA_PG)

compras.append({
    "data": hora_compra,
    "id_compra": 0,
    "loja": loja["cidade"],
    "vendedor": vendedor,
    "produto": produto["nome"],
    "cliente_nome": nome_cliente,
    "cliente_genero": genero_cliente.replace("female", "feminino").replace("male", "masculino"),
    "forma_pagamento": forma_pagamento
})

df_compras = pd.DataFrame(compras).set_index("data").sort_index()
df_compras["id_compra"] = [i for i in range(len(df_compras))]

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)

df_compras.to_csv(pastas_datasets / "compras.csv", decimal=",", sep=";")
df_lojas.to_csv(pastas_datasets / "lojas.csv", decimal=",", sep=";")
df_produtos.to_csv(pastas_datasets / "produtos.csv", decimal=",", sep=";")

df_compras.to_excel(pastas_datasets / "compras.xlsx")
df_lojas.to_excel(pastas_datasets / "lojas.xlsx")
df_produtos.to_excel(pastas_datasets / "produtos.xlsx")

