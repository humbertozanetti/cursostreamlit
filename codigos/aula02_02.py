import streamlit as st

st.title('Cadastro de Aluno')

# Entrada do nome
nome = st.text_input('Digite seu nome completo:')

# Selectbox para período
periodo = st.selectbox(
    'Selecione o período em que estuda:',
    ['Manhã', 'Tarde', 'Noite']
)

# Radio para curso
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

        # conversão do período (pegamos a primeira letra)
        sigla_periodo = periodo[:1]
     
        # conversão do curso
        if curso == 'Desenvolvimento de Sistemas':
            sigla_curso = 'DS'
        elif curso == 'Administração':
            sigla_curso = 'Adm'
        elif curso == 'Automação':
            sigla_curso = 'Auto'
        else:
            sigla_curso = 'Log'

        # gravando os dados no arquivo
        with open('cadastro_alunos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome};{sigla_periodo};{sigla_curso}\n')

        st.success('Dados salvos com sucesso!')
