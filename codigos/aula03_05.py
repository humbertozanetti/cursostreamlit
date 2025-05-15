import streamlit as st

st.title('Layout combinando Container e Colunas')

# Container agrupando colunas
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('Coluna 1')
    with col2:
        st.write('Coluna 2')
    with col3:
        st.write('Coluna 3')

st.write('Conteúdo depois do container')
