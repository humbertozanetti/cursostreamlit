# CURSO STREAMLIT - **Aula 1**

**Prof. Dr. Humberto A. P. Zanetti**

---
## O que é o Streamlit?

O **Streamlit** é um framework de código aberto em Python criado para facilitar a construção rápida de aplicações web interativas, especialmente voltadas para Ciência de Dados, Machine Learning e Análise de Dados.  
A principal vantagem do Streamlit é permitir que, com poucas linhas de código Python, você crie interfaces web amigáveis para visualização de dados, coleta de informações e até interação em tempo real, sem precisar de conhecimentos em front-end (HTML, CSS ou JavaScript).
Ele transforma scripts Python comuns em aplicações web com apenas um comando (`streamlit run app.py`).

### **Áreas mais utilizadas**

+ **Ciência de Dados**: Para criar dashboards de análise de dados, explorando bases e mostrando gráficos interativos.
+ **Machine Learning**: Para construir interfaces para modelos treinados, permitindo testes rápidos e validação de resultados.
+ **Business Intelligence (BI)**: Empresas usam o Streamlit para criar ferramentas internas de visualização e relatórios.
+ **Educação e Pesquisa**: Professores e pesquisadores usam para apresentar projetos de forma interativa.
+ **Engenharia de Software**: Para criar protótipos de sistemas e ferramentas de back-office.

### **Links Oficiais**

+ Site Oficial: https://streamlit.io/
+ Documentação Oficial: https://docs.streamlit.io/
  
## Principais Elementos Gráficos do Streamlit

### 1. Textos e Títulos

- `st.title('Título')`  
  Exibe um título principal.

- `st.header('Cabeçalho')`  
  Exibe um cabeçalho secundário.

- `st.subheader('Subcabeçalho')`  
  Exibe um subcabeçalho menor.

- `st.text('Texto simples')`  
  Exibe um texto comum.

- `st.markdown('Texto com **Markdown**')`  
  Exibe texto com formatação em Markdown.

- `st.code('print("Olá mundo")', language='python')`  
  Exibe código com destaque de sintaxe.

---

### 2. Entradas de Dados (Inputs)

- `st.text_input('Digite algo')`  
  Campo de entrada para texto.

- `st.number_input('Digite um número')`  
  Campo de entrada para números.

- `st.date_input('Escolha uma data')`  
  Seletor de datas.

- `st.time_input('Escolha uma hora')`  
  Seletor de hora.

- `st.slider('Selecione um valor', 0, 100)`  
  Barra deslizante (slider) numérico.

- `st.selectbox('Escolha uma opção', ['Opção 1', 'Opção 2'])`  
  Caixa de seleção com opções únicas.

- `st.multiselect('Escolha múltiplas opções', ['Opção A', 'Opção B'])`  
  Caixa de seleção para múltiplas escolhas.

- `st.radio('Escolha uma opção', ['A', 'B', 'C'])`  
  Botões de rádio para uma escolha única.

- `st.checkbox('Aceito os termos')`  
  Caixa de seleção (checkbox).

---

## 3. Botões

- `st.button('Clique aqui')`  
  Botão de ação.

- `st.download_button('Baixar arquivo', data)`  
  Botão para download de arquivos.

---

## 4. Exibição de Dados

- `st.dataframe(df)`  
  Exibe um DataFrame interativo (Pandas).

- `st.table(df)`  
  Exibe uma tabela estática.

- `st.json(data)`  
  Exibe dados em formato JSON.

---

## 5. Gráficos e Imagens

- `st.line_chart(data)`  
  Gráfico de linha.

- `st.bar_chart(data)`  
  Gráfico de barras.

- `st.area_chart(data)`  
  Gráfico de área.

- `st.pyplot(fig)`  
  Exibe um gráfico do Matplotlib.

- `st.image('imagem.png')`  
  Exibe uma imagem.

- `st.video('video.mp4')`  
  Exibe um vídeo.

---

## 6. Layouts e Organização

- `st.sidebar`  
  Permite adicionar elementos à barra lateral.

- `st.columns(n)`  
  Divide a tela em colunas.

- `st.expander('Clique para expandir')`  
  Cria uma área expansível para agrupar conteúdo.

---

### Observações

- Todos os elementos podem ser combinados para criar interfaces ricas e interativas rapidamente.
- Componentes de entrada (`text_input`, `selectbox`, etc.) retornam valores que podem ser utilizados no fluxo do código.

---

## Exemplo 1 - Primeiro app em Streamlit

Nesse exemplo vamos simplismente importar a biblioteca e fazer o uso de elementos simples.

````python
import streamlit as st

st.title('Olá, mundo!')
st.header('Este é meu primeiro app com Streamlit')
st.write('Streamlit é uma biblioteca para criar apps web com Python de forma simples.')
````

## Exemplo 2 - Mais compoentes
Nesse exemplo vamos utilizar componentes que possuem opções e interação com botão

````python
import streamlit as st

st.title('Calculadora Simples')

num1 = st.number_input('Digite o primeiro número:')
num2 = st.number_input('Digite o segundo número:')

operacao = st.selectbox('Escolha a operação:', ['Soma', 'Subtração', 'Multiplicação', 'Divisão'])

botao = st.button('Calcular')

if botao : #quando pressionado, o botão gera True
    if operacao == 'Soma':
        resultado = num1 + num2
    elif operacao == 'Subtração':
        resultado = num1 - num2
    elif operacao == 'Multiplicação':
        resultado = num1 * num2
    elif operacao == 'Divisão':
        resultado = num1 / num2 if num2 != 0 else 'Erro: divisão por zero'

    st.success(f'Resultado: {resultado}')
````

## Exemplo 3 - Formatação de entrada de dados

Quando necessário, é sempre importante definir as entradas de dados com precisão. 
Lembrando que se não houver formatação, o parão de entrada será sempre **string**.

````python
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
````

## Exemplo 4 - Integrando com arquivos
Para que tenhamos uma aplicação "completa", vamos armazenar os dados que são inseridos, para uma manipulação posterior. Para isso, vamos integrar com manipulação de arquivos.

````python
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

if botao:
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
                st.write(f'{nome}, {idade} anos, {altura} m, nascido em {nascimento}')
        else:
            st.info('Nenhum dado cadastrado ainda.')
else:
    st.info('Nenhum arquivo encontrado. Envie o primeiro registro!')

````

## EXERCÍCIO

Crie uma aplicação Streamlit onde o usuário possa cadastrar livros informando:
+ Título do livro (campo de texto)
+ Autor (campo de texto)
+ Ano de publicação (campo numérico)    
+ Gênero literário (selectbox: Ex.: Romance, Ficção, História, Poesia)

Cada vez que um livro for cadastrado:
+ As informações devem ser salvas em um arquivo livros.txt, adicionando ao final.
+ Após o cadastro, todos os livros cadastrados até o momento devem ser lidos do arquivo e exibidos.
