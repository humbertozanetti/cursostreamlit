import streamlit as st
from datetime import date

st.title('Formulário com Tipos de Dados Definidos')

nome = st.text_input('Nome completo')  # string
idade = st.number_input('Idade', min_value=0, max_value=120, step=1)  # inteiro
altura = st.number_input('Altura em metros', format='%.2f')  # float
nascimento = st.date_input('Data de nascimento', min_value=date(1900, 1, 1), format='DD/MM/YYYY')  # data
aceita_termos = st.checkbox('Aceito os termos de uso')  # booleano

botao = st.button('Enviar')

if botao:
    if nome and aceita_termos:
        st.success('Dados enviados com sucesso!')
        st.write(f'Nome: {nome}')
        st.write(f'Idade: {idade}')
        st.write(f'Altura: {altura} m')
        st.write(f'Data de nascimento: {nascimento}')
    else:
        st.warning('Preencha o nome e aceite os termos.')
