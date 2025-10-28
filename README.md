# 📊 Dashboard Musical - Análise Spotify & YouTube

## 🎯 Contexto do Projeto

**Você foi contratado pela Mateus Music** como Desenvolvedor de Dashboards para criar uma plataforma visual interativa que permita analisar o catálogo musical da empresa. 

Sua missão é desenvolver um dashboard em Streamlit que transforme dados complexos em insights visuais simples e acessíveis, facilitando a tomada de decisão estratégica.

## 📁 Sobre a Base de Dados

A Mateus Music possui um catálogo com **mais de 20.000 músicas** e dados de performance em múltiplas plataformas:

### Estrutura Principal:
- **+20.000 registros** de músicas
- Dados de **Streams no Spotify**
- Dados de **Views no YouTube**
- **Metadados completos** de artistas e álbuns
- **Audio features** (danceability, energy, valence, etc.)

### Colunas Principais:
```csv
Artist, Track, Stream, Views, Danceability, Energy, Album_type, ...
```

## 🎵 Funcionalidades do Dashboard

### **1. Filtro Interativo por Artista**
- Seletor dropdown com todos os artistas disponíveis
- Opção "TODOS" para análise geral do catálogo
- Atualização em tempo real de todos os componentes

### **2. Métricas Principais em Destaque**
- **Total de Músicas** no catálogo/filtro
- **Soma Total de Views** no YouTube
- **Soma Total de Streams** no Spotify

### **3. Visualizações Gráficas Lado a Lado**

#### **Gráfico da Esquerda:**
- **Modo "TODOS"**: `🎤 Top 5 Artistas com Mais Músicas`
- **Modo Artista Específico**: `🎵 Músicas do [Artista] no YouTube`

#### **Gráfico da Direita:**
- **`📊 Comparação: Views vs Streams`** - Análise correlacional entre plataformas

### **4. Ranking das Músicas Mais Populares**
- **`🎧 Top 10 Músicas no Spotify`** - Ordenadas por número de streams
- Tabela interativa com scroll
- Dados em formato amigável

## 💻 Tecnologias Utilizadas

- **Streamlit** - Framework para criação do dashboard
- **Pandas** - Manipulação e análise de dados
- **Python** - Lógica de programação

## 🚀 Como Executar o Projeto

### **Pré-requisitos:**
```bash
pip install streamlit pandas
```

### **Execução:**
```bash
streamlit run dashboard_musical.py
```

### **Estrutura de Arquivos:**
```
projeto/
├── dashboard_musical.py
├── Dados_Artistas.csv
└── README.md
```

## 📊 Métodos do Pandas Utilizados

- `pd.read_csv()` - Carregamento dos dados
- `df['coluna'].unique()` - Listagem de artistas
- `df[df['coluna'] == valor]` - Filtragem de dados
- `df.groupby().sum()` - Agregação de métricas
- `df.nlargest()` - Ordenação para rankings
- `df.value_counts().head()` - Contagem para gráficos

## 🎨 Layout e Design

### **Estrutura Visual:**
```
┌─────────────────────────────────┐
│          TÍTULO PRINCIPAL       │
├─────────────────────────────────┤
│    [M1]      [M2]      [M3]     │
├─────────────────────────────────┤
│   GRÁFICO    │    GRÁFICO       │
│   ESQUERDA   │    DIREITA       │
├─────────────────────────────────┤
│        TABELA TOP 10            │
│   (Ranking Spotify Streams)     │
└─────────────────────────────────┘
```

### **Características de UX:**
- ✅ **Layout responsivo** com `layout="wide"`
- ✅ **Filtro intuitivo** na parte superior
- ✅ **Gráficos lado a lado** para comparação visual
- ✅ **Tabela interativa** com dados detalhados
- ✅ **Atualização em tempo real** ao alterar filtros

## 🎯 Objetivos de Negócio Atendidos

### **Para a Mateus Music:**
1. **Identificar artistas mais produtivos** (quantidade de músicas)
2. **Analisar performance cross-platform** (Spotify vs YouTube)
3. **Ranking de músicas mais populares** por streams
4. **Tomada de decisão baseada em dados** visuais

### **Para os Usuários:**
1. **Interface simples e intuitiva**
2. **Navegação por artista favorito**
3. **Visualização clara de métricas**
4. **Comparação rápida entre plataformas**

## 💡 Dicas de Customização

### **Para Adicionar Novos Gráficos:**
```python
# Exemplo: Gráfico de dispersão
st.scatter_chart(dados[['Danceability', 'Energy']])
```

### **Para Adicionar Novos Filtros:**
```python
# Exemplo: Filtro por tipo de álbum
album_type = st.selectbox("Tipo de Álbum:", dados['Album_type'].unique())
```

## 📈 Próximos Passos Sugeridos

1. **Adicionar mais visualizações** (histogramas, scatter plots)
2. **Implementar download de relatórios**
3. **Adicionar análise temporal** (se houver dados de data)
4. **Criar modo comparativo entre artistas**

---

**🚀 Dashboard Desenvolvido com Sucesso!** 

A Mateus Music agora possui uma ferramenta visual poderosa para análise estratégica do catálogo musical! 🎧✨

**Desenvolvido por:** MTech  
**Contratante:** Mateus Music  
**Tecnologias:** Streamlit + Pandas + Python
