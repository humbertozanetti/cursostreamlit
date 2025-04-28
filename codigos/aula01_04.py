import streamlit as st
from datetime import date
import os

st.title('Formulário de Cadastro com Registro em TXT')

nome = st.text_input('Nome completo')
idade = st.number_input('Idade', min_value=0, max_value=120, step=1)
altura = st.number_input('Altura (em metros)', format='%.2f')
nascimento = st.date_input('Data de nascimento', min_value=date(1900, 1, 1), format='DD/MM/YYYY')
aceita_termos = st.checkbox('Aceito os termos de uso')

botao = st.button('Enviar')

# nome do arquivo base de dados
ARQUIVO_DADOS = 'dados.txt'

if st.button:
    if nome and aceita_termos:
        linha = f'{nome};{idade};{altura:.2f};{nascimento.strftime("%d/%m/%Y")}\n'
        
        # adiciona os dados ao final do arquivo
        with open(ARQUIVO_DADOS, 'a', encoding='utf-8') as f:
            f.write(linha)
        
        st.success('Dados salvos com sucesso!')

        # mostra os dados enviados
        st.markdown('### Último cadastro:')
        st.write(f'**Nome:** {nome}')
        st.write(f'**Idade:** {idade}')
        st.write(f'**Altura:** {altura:.2f} m')
        st.write(f'**Nascimento:** {nascimento.strftime("%d/%m/%Y")}')
    else:
        st.warning('Preencha o nome e aceite os termos!')

st.markdown('---')
st.markdown('### Registros Salvos:')

# verifica se o arquivo existe antes de ler
if os.path.exists(ARQUIVO_DADOS):
    with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        if linhas:
            for linha in linhas:
                nome, idade, altura, nascimento = linha.strip().split(';')
                st.write(f'👤 {nome}, {idade} anos, {altura} m, nascido em {nascimento}')
        else:
            st.info('Nenhum dado cadastrado ainda.')
else:
    st.info('Nenhum arquivo encontrado. Envie o primeiro registro!')
