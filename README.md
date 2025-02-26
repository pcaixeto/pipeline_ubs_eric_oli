# Dashboard de Unidades Básicas de Saúde (UBS)

Este projeto é um **dashboard interativo** desenvolvido com **Streamlit** para visualizar a frequência das **Unidades Básicas de Saúde (UBS)** por estado no Brasil.

## 🏗️ Funcionalidades
- **Gráfico de barras** interativo mostrando a frequência de UBS por estado.
- **Filtro** para visualizar dados de estados específicos.
- **Visualização de dados** filtrados diretamente na interface.

## 📂 Estrutura do Projeto
```
├── ubs_dashboard.py  # Código do dashboard em Streamlit
├── ubs_atualizado.csv # Arquivo de dados atualizado
├── requirements.txt  # Dependências necessárias
└── README.md  # Documentação do projeto
```

## 🚀 Como Executar
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/ubs-dashboard.git
cd ubs-dashboard
```

### 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv env
source env/bin/activate  # Para Linux/Mac
env\Scripts\activate  # Para Windows
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar a aplicação
```bash
streamlit run ubs_dashboard.py
```

## 📦 Dependências
As principais bibliotecas utilizadas no projeto são:
- `streamlit` → Interface do dashboard
- `pandas` → Manipulação de dados
- `plotly` → Visualização de gráficos interativos



# 📌 Exercício de Refatoração do BI - Dashboard de UBS

## 🎯 Objetivo
Refatorar e aprimorar o **Dashboard de Unidades Básicas de Saúde (UBS)**, implementando **três novas visualizações** e garantindo que a entrega seja feita corretamente no **GitHub**.

---

## 🚀 Tarefas

### 1️⃣ Mapa Interativo das UBS por Estado
- Criar um **mapa de dispersão** usando `latitude` e `longitude` para plotar a localização das UBS.
- Adicionar um **filtro por estado** para exibir apenas UBS da região desejada.

### 2️⃣ Gráfico de Pizza da Distribuição de UBS por Estado
- Criar um **gráfico de pizza** mostrando opercentual de UBS por estado.
- Utilizar `plotly.express.pie()` para exibir os dados.

### 3️⃣ Histograma da Quantidade de UBS por Município
- Criar um **histograma** que exiba a **quantidade de UBS por município**.
- Utilizar `plotly.express.histogram()` agrupando os municípios por contagem de UBS.
- Adicionar um controle deslizante (`st.slider()`) para filtrar municípios com um número mínimo de UBS.

---
## Alunos
- Eric Akio Uchiyamada RA: 10395287
- Oliver Kieran Galvão McCormack RA: 10395672
- Pedro Machado Gomes Caixeta RA: 10314309
