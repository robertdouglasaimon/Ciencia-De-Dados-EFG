import streamlit as st
import pandas as pd

caminho_compras = pd.read_csv("datasets\compras.csv", sep=";", decimal=",")
lojas = pd.read_csv("datasets\lojas.csv", sep=";", decimal=",")
produtos = pd.read_csv("datasets\produtos.csv", sep=";", decimal=",")


df_compras = pd.DataFrame(caminho_compras)


st.dataframe(df_compras)

# Usar esse comando aqui: streamlit run 1-visualizando_tb.py
# no terminal para abrir o Streamlit e ver o dataset.
# CTRL + C no terminal para parar o Streamlit