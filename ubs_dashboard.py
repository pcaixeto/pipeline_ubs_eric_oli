import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o arquivo atualizado
df = pd.read_csv("ubs_atualizado.csv", sep=";")

# Converter latitude e longitude para float
df['LATITUDE'] = pd.to_numeric(df['LATITUDE'].str.replace(',', '.'), errors='coerce')
df['LONGITUDE'] = pd.to_numeric(df['LONGITUDE'].str.replace(',', '.'), errors='coerce')

# Remover linhas com valores inválidos após a conversão
df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])


# Verifica se as colunas de latitude e longitude existem
if 'LATITUDE' in df.columns and 'LONGITUDE' in df.columns:
    # Criar o dashboard
    st.title("Dashboard de Unidades Básicas de Saúde (UBS)")

    # Contar a frequência de UBS por estado
    df_freq = df['Nome_UF'].value_counts().reset_index()
    df_freq.columns = ['Estado', 'Frequência']

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

        # Criar um mapa com os pontos das UBS filtradas
        df_mapa = df_filtrado[['LATITUDE', 'LONGITUDE']]
        st.map(df_mapa)
    else:
        # Se nenhum estado for selecionado, mostrar todas as UBS no mapa
        df_mapa = df[['LATITUDE', 'LONGITUDE']]
        st.map(df_mapa)
else:
    st.error("As colunas 'latitude' e 'longitude' não foram encontradas no dataset.")
