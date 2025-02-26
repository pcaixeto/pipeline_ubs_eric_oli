import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o arquivo atualizado
df = pd.read_csv("ubs_atualizado.csv", sep=";")

# Contar a frequência de UBS por estado
df_freq = df['Nome_UF'].value_counts().reset_index()
df_freq.columns = ['Estado', 'Frequência']

# Criar o dashboard
st.title("Dashboard de Unidades Básicas de Saúde (UBS)")

# Gráfico de barras
grafico = px.bar(df_freq, x='Estado', y='Frequência', 
                 title='Frequência de UBS por Estado', 
                 labels={'Estado': 'Estado', 'Frequência': 'Número de UBS'},
                 text_auto=True)

st.plotly_chart(grafico)

# Filtro para estados específicos
estados = st.multiselect("Selecione os estados", df_freq['Estado'].unique())
if estados:
    df_filtrado = df[df['Nome_UF'].isin(estados)]
    st.write(df_filtrado)

# Exercicio 3: Histograma da Quantidade de UBS por Município
# Contar a quantidade de UBS por município
df_municipios = df['Nome_Município'].value_counts().reset_index()
df_municipios.columns = ['Município', 'Quantidade_UBS']

# Controle deslizante para filtrar municípios com um número mínimo de UBS
min_ubs = st.slider("Selecione o número mínimo de UBS por município", 
                    min_value=int(df_municipios['Quantidade_UBS'].min()), 
                    max_value=int(df_municipios['Quantidade_UBS'].max()), 
                    value=int(df_municipios['Quantidade_UBS'].min()))

# Filtrar os municípios
df_filtrado = df_municipios[df_municipios['Quantidade_UBS'] >= min_ubs]

# Criar gráfico de barras para visualizar os municípios com o filtro aplicado
grafico_barras = px.bar(df_filtrado, x='Município', y='Quantidade_UBS', 
                        title="Número de UBS por Município",
                        labels={'Município': 'Município', 'Quantidade_UBS': 'Número de UBS'},
                        text_auto=True)

st.plotly_chart(grafico_barras)