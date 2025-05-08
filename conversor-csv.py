import pandas as pd

# Criando os dados com 34 itens variados
dados = [
    ["2024-10-15 14:22:30", 1, "São Paulo", "Ana Oliveira", "Notebook Dell Inspiron", "Lucas Mendes", "masculino", "cartão de crédito"],
    ["2024-09-05 18:45:12", 2, "Recife", "Carlos Souza", "Smartwatch Garmin Forerunner", "Mariana Souza", "feminino", "pix"],
    ["2024-08-20 09:10:55", 3, "Porto Alegre", "Carla Mendes", "TV Samsung 55 polegadas", "João Pereira", "masculino", "boleto"],
    ["2024-07-30 16:35:20", 4, "Fortaleza", "Rodrigo Souza", "PlayStation 5", "Fernanda Lima", "feminino", "dinheiro"],
    ["2024-06-12 11:50:40", 5, "Goiânia", "Carlos Almeida", "AirPods Pro", "Juliana Rocha", "feminino", "cartão de crédito"],
    ["2024-05-25 08:15:30", 6, "Belo Horizonte", "Maria Souza", "Smartphone Xiaomi Mi 11", "Pedro Lima", "masculino", "pix"],
    ["2024-04-18 19:30:10", 7, "Rio de Janeiro", "Joaquim Silva", "Fone de Ouvido Sony WH-1000XM4", "Claudia Mendes", "feminino", "boleto"],
    ["2024-03-10 13:45:50", 8, "Curitiba", "Lucas Alves", "Drone DJI Mavic Air 2", "Luana Pereira", "feminino", "dinheiro"],
    ["2024-02-22 17:20:25", 9, "Salvador", "João Silva", "Teclado Mecânico Razer", "Maria Oliveira", "feminino", "cartão de crédito"],
    ["2024-01-15 10:05:40", 10, "Cuiabá", "Fábio Costa", "Notebook Asus ROG Strix", "Sofia Lima", "feminino", "pix"],
    ["2023-12-30 15:55:10", 11, "Manaus", "Henrique Alves", "Câmera Canon EOS 80D", "Rafaela Costa", "feminino", "boleto"],
    ["2023-11-18 09:40:30", 12, "Vitória", "Mariana Santos", "Smartphone Apple iPhone 12", "Lucas Ferreira", "masculino", "dinheiro"],
    ["2023-10-05 18:25:45", 13, "Maceió", "Bruna Silva", "TV LG OLED 55\"", "Paulo Oliveira", "masculino", "cartão de crédito"],
    ["2023-09-12 12:10:20", 14, "Campo Grande", "Ricardo Mendes", "Air Fryer Philips Walita", "Carla Alves", "feminino", "pix"],
    ["2023-08-27 16:45:55", 15, "Aracaju", "Tatiane Pereira", "Notebook Lenovo ThinkPad", "Gustavo Costa", "masculino", "boleto"],
    ["2023-07-14 11:30:40", 16, "São Luís", "Felipe Silva", "Smartwatch Apple Watch Series 6", "Amanda Pereira", "feminino", "dinheiro"],
    ["2023-06-01 14:55:30", 17, "Teresina", "Daniela Souza", "PlayStation 5", "Ricardo Alves", "masculino", "cartão de crédito"],
    ["2023-05-20 08:40:15", 18, "Natal", "Nayara Costa", "Smartphone Samsung Galaxy S20", "Fábio Souza", "masculino", "pix"],
    ["2023-04-05 19:15:50", 19, "João Pessoa", "Amanda Lima", "Notebook Acer Predator Helios", "Bruno Almeida", "masculino", "boleto"],
    ["2023-03-12 13:30:25", 20, "Brasília", "Aline Souza", "Câmera GoPro Hero 8", "Rafael Costa", "masculino", "dinheiro"],
    ["2023-02-28 17:05:40", 21, "Porto Velho", "Beatriz Mendes", "Smartphone Xiaomi Mi 11", "Felipe Ferreira", "masculino", "cartão de crédito"],
    ["2023-01-15 10:50:30", 22, "Rio Branco", "Marcelo Pereira", "AirPods Pro", "Patrícia Alves", "feminino", "pix"],
    ["2022-12-30 15:35:10", 23, "Palmas", "Simone Oliveira", "Drone DJI Mavic Air 2", "Caio Souza", "masculino", "boleto"],
    ["2022-11-18 09:20:30", 24, "Joinville", "Paula Costa", "Teclado Mecânico Razer", "Lucas Rocha", "masculino", "dinheiro"],
    ["2022-10-05 18:05:45", 25, "Caxias do Sul", "José Silva", "Notebook Asus ROG Strix", "Laura Pereira", "feminino", "cartão de crédito"],
    ["2022-09-12 11:50:20", 26, "Londrina", "Gustavo Ferreira", "Câmera Canon EOS 80D", "Michele Almeida", "feminino", "pix"],
    ["2022-08-27 16:25:55", 27, "Campinas", "Ricardo Pereira", "Smartphone Apple iPhone 12", "Sabrina Souza", "feminino", "boleto"],
    ["2022-07-14 11:10:40", 28, "Uberlândia", "Eduardo Lima", "TV LG OLED 55\"", "Cristiane Alves", "feminino", "dinheiro"],
    ["2022-06-01 14:35:30", 29, "Niterói", "Eliane Costa", "Air Fryer Philips Walita", "Marcos Ferreira", "masculino", "cartão de crédito"],
    ["2022-05-20 08:20:15", 30, "Feira de Santana", "Carla Almeida", "Notebook Lenovo ThinkPad", "José Ferreira", "masculino", "pix"],
    ["2022-04-05 19:05:50", 31, "Linhares", "Felipe Mendes", "Smartwatch Apple Watch Series 6", "Mônica Alves", "feminino", "boleto"],
    ["2022-03-12 13:20:25", 32, "Blumenau", "Júlia Pereira", "PlayStation 5", "Gustavo Lima", "masculino", "dinheiro"],
    ["2022-02-28 16:55:40", 33, "Pelotas", "Marina Alves", "Smartphone Samsung Galaxy S20", "Rodrigo Pereira", "masculino", "cartão de crédito"],
    ["2022-01-15 10:40:30", 34, "Várzea Grande", "Beatriz Rocha", "Notebook Acer Predator Helios", "Vinícius Souza", "masculino", "pix"],
]

# Criando o DataFrame
colunas = ["data", "id_compra", "loja", "vendedor", "produto", "cliente_nome", "cliente_genero", "forma_pagamento"]
df = pd.DataFrame(dados, columns=colunas)

# Salvando em um arquivo CSV
df.to_csv("compras.csv", index=False, sep=";", encoding="utf-8")

print("Arquivo CSV 'compras.csv' gerado com sucesso!")
