import streamlit as st

st.title('Cadastro de Aluno')

nome = st.text_input('Digite seu nome completo:')

# selectbox
periodo = st.selectbox(
    'Selecione o período em que estuda:',
    ['Manhã', 'Tarde', 'Noite']
)

# radio
curso = st.radio(
    'Selecione seu curso:',
    ['Desenvolvimento de Sistemas', 'Administração', 'Automação', 'Logística']
)

botao = st.button('Enviar')
if botao: 
    st.markdown('---')
    st.subheader('Dados Informados:')
    
    if nome.strip() == '':
        st.warning('Por favor, preencha o nome do aluno.')
    else:
        st.write(f'Nome: {nome}')
        st.write(f'Período: {periodo}')
        st.write(f'Curso: {curso}')

