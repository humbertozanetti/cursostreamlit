import streamlit as st

# Configuração da página
st.set_page_config(page_title='App com Menu Lateral')

# Menu lateral
pagina = st.sidebar.selectbox('Escolha uma página:', ['Home', 'Página 1', 'Página 2'])

# Caminhos dos arquivos
paginas = {
    'Home': 'aula03_06\home.py',
    'Página 1': 'aula03_06\pagina1.py',
    'Página 2': 'aula03_06\pagina2.py'
}

# Executa o conteúdo do arquivo correspondente
with open(paginas[pagina], 'r', encoding='utf-8') as arquivo:
    exec(arquivo.read())
