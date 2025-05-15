import streamlit as st

st.title('Exemplo com Colunas')

col1, col2 = st.columns(2)

with col1:
    st.header('Coluna 1')
    st.button('Botão 1')

with col2:
    st.header('Coluna 2')
    st.button('Botão 2')
