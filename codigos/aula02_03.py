import streamlit as st
import os

st.title('Cadastro de Aluno')

nome = st.text_input('Digite seu nome completo:')

periodo = st.selectbox(
    'Selecione o período em que estuda:',
    ['Manhã', 'Tarde', 'Noite']
)

curso = st.radio(
    'Selecione seu curso:',
    ['Desenvolvimento de Sistemas', 'Administração', 'Automação', 'Logística']
)

botao = st.button('Enviar')

if botao:
    if nome.strip() == '':
        st.warning('Por favor, preencha o nome do aluno.')
    else:
        sigla_periodo = periodo[:1]

        if curso == 'Desenvolvimento de Sistemas':
            sigla_curso = 'DS'
        elif curso == 'Administração':
            sigla_curso = 'Adm'
        elif curso == 'Automação':
            sigla_curso = 'Auto'
        else:
            sigla_curso = 'Log'

        with open('cadastro_alunos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome};{sigla_periodo};{sigla_curso}\n')

        st.success('Aluno cadastrado com sucesso!')

# mostrando o relatório sempre
st.markdown('---')
st.subheader('Relatório de Alunos')

# inicializando os contadores
m = t = n = 0
ds = adm = auto = log = 0
total_alunos = 0

if os.path.exists('cadastro_alunos.txt'):
    with open('cadastro_alunos.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(';')
            if len(partes) == 3:
                periodo = partes[1]
                curso = partes[2]

                if periodo == 'M':
                    m += 1
                elif periodo == 'T':
                    t += 1
                elif periodo == 'N':
                    n += 1

                if curso == 'DS':
                    ds += 1
                elif curso == 'Adm':
                    adm += 1
                elif curso == 'Auto':
                    auto += 1
                elif curso == 'Log':
                    log += 1

                total_alunos += 1

    st.markdown('**Quantidade de alunos por curso:**')
    st.write(f'Desenvol. de Sistemas: {ds}')
    st.write(f'Administração: {adm}')
    st.write(f'Automação: {auto}')
    st.write(f'Logística: {log}')

    st.markdown('**Quantidade de alunos por período:**')
    st.write(f'Manhã: {m}')
    st.write(f'Tarde: {t}')
    st.write(f'Noite: {n}')
    
    st.markdown('**TOTAL DE ALUNOS:**')
    st.write(f'{total_alunos}')
    
else:
    st.info('Nenhum dado cadastrado ainda.')
