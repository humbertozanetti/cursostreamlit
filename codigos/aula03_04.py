import streamlit as st

st.title('Exemplo com Expander')

# Área expansível
with st.expander('Clique para ver mais'):
    st.write('Aqui dentro do expander pode ter qualquer conteúdo')
    st.link_button('ETEC Rosa Perrone Scavone', 'http://rosaperrone.com.br/')
