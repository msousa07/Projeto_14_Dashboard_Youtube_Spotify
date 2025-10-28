import streamlit as st
import pandas as pd

# Configuração com layout wide
st.set_page_config(page_title="Dashboard Musical", page_icon="🎵", layout="wide")

st.title("📊 Dashboard Musical")

# Carregar dados
df = pd.read_csv('Dados_Artistas.csv')

# Único filtro, adicionando opção 'TODOS'
artista = st.selectbox("Escolha um Artista:", ['TODOS'] + list(df['Artist'].unique()))

if artista == 'TODOS':
    dados = df
else:
    dados = df[df['Artist'] == artista]

# Apenas 3 métricas
st.write("### 📈 Métricas")
col1, col2, col3 = st.columns(3)
col1.metric("Músicas", len(dados))
col2.metric("Views Totais", f"{dados['Views'].sum():,.0f}")
col3.metric("Streams Totais", f"{dados['Stream'].sum():,.0f}")

# GRÁFICOS LADO A LADO COM CONTAINER
container = st.container()

with container:
    # Criar duas colunas com mais espaço
    graf_esq, graf_dir = st.columns(2)
    
    with graf_esq:
        
        if artista == 'TODOS':
            st.write("#### Artistas Mais Populares no YouTube")
            top_5 = df['Artist'].value_counts().head(5)
            st.bar_chart(top_5)
        else:
            st.write("#### Músicas Mais Populares no YouTube")
            musicas = dados[['Track', 'Views']].set_index('Track').head(8)
            st.bar_chart(musicas)
    
    with graf_dir:
        st.write("#### Comparação: Views vs Streams")
        comparacao = dados[['Views', 'Stream']].head(20)
        st.line_chart(comparacao)

# TABELA ABAIXO
st.write("### 🎵 Músicas com Mais Streams no Spotify")

# Apenas ordenar por Stream e pegar os top 10
top_10_spotify = dados.sort_values('Stream', ascending=False).head(10)[['Track', 'Artist', 'Stream']]

# Mostrar a tabela diretamente
st.dataframe(top_10_spotify, use_container_width=True)