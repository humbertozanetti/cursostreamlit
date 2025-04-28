import streamlit as st

st.title('Calculadora Simples')

num1 = st.number_input('Digite o primeiro número:')
num2 = st.number_input('Digite o segundo número:')

operacao = st.selectbox('Escolha a operação:', ['Soma', 'Subtração', 'Multiplicação', 'Divisão'])

botao = st.button('Calcular')

if botao :
    if operacao == 'Soma':
        resultado = num1 + num2
    elif operacao == 'Subtração':
        resultado = num1 - num2
    elif operacao == 'Multiplicação':
        resultado = num1 * num2
    elif operacao == 'Divisão':
        resultado = num1 / num2 if num2 != 0 else 'Erro: divisão por zero'

    st.success(f'Resultado: {resultado}')
