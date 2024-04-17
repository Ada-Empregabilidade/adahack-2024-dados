from datetime import datetime

import streamlit as st


def idade_ano(idade: int) -> datetime:
    """Calcula o ano de nascimento conforme a idade informada."""
    data_atual = datetime.now()
    ano = data_atual.year - idade
    return ano


def calcula_idade(data_nascimento: datetime) -> int:
    """Calcula a idade a partir da data de nascimento fornecida."""
    data_atual = datetime.now()
    idade = (
        data_atual.year
        - data_nascimento.year
        - (
            (data_atual.month, data_atual.day)
            < (data_nascimento.month, data_nascimento.day)
        )
    )
    return idade


def main():
    st.set_page_config(page_title='Corp Solutions', page_icon='🟢')
    st.image(
        './Logo/logo-copr-solutions.png', use_column_width=False, width=100
    )

    st.markdown(
        "<h3 style='text-align: center; font-family: Verdana'>FORMULÁRIO DE INCLUSÃO E DIVERSIDADE</h3>",
        unsafe_allow_html=True,
    )
    st.header('', divider='rainbow')
    st.caption('Versão 1.0')

    cl1, cl2 = st.columns(2)

    nome = cl1.text_input('Informe o Nome Completo:', max_chars=40).upper()

    data_nascimento = cl2.date_input(
        'Data de Nascimento:',
        value=None,
        min_value=datetime(idade_ano(60), 12, 31),
        max_value=datetime(
            idade_ano(18), datetime.now().month, datetime.now().day
        ),
        format='DD/MM/YYYY',
    )

    if data_nascimento is not None:
        idade = calcula_idade(data_nascimento)
        st.write('Idade:', str(idade), 'anos')
    else:
        idade = 0

    nivel_escolaridade = st.selectbox(
        'Informe Seu Nível de Escolaridade:',
        [
            '',
            'Ensino Médio',
            'Graduação',
            'Pós-Graduação',
            'Mestrado',
            'Doutorado',
        ],
    )

    col1, col2, col3 = st.columns(3)
    rua = col1.text_input(
        'Informe Seu Endereço (Rua e N°):', max_chars=25
    ).upper()
    cidade = col2.text_input('Informe a Cidade:', max_chars=15)
    cep = col3.text_input('Informe o CEP (apenas números):', max_chars=8)

    estado = st.selectbox(
        'Selecione o Estado',
        [
            '',
            'Acre',
            'Alagoas',
            'Amapá',
            'Amazonas',
            'Bahia',
            'Ceará',
            'Distrito Federal',
            'Espírito Santo',
            'Goiás',
            'Maranhão',
            'Mato Grosso',
            'Mato Grosso do Sul',
            'Minas Gerais',
            'Pará',
            'Paraíba',
            'Paraná',
            'Pernambuco',
            'Piauí',
            'Rio de Janeiro',
            'Rio Grande do Norte',
            'Rio Grande do Sul',
            'Rondônia',
            'Roraima',
            'Santa Catarina',
            'São Paulo',
            'Sergipe',
            'Tocantins',
        ],
    )

    st.markdown(
        "<h4 style='text-align; font-family: Verdana'>Deficiência</h4>",
        unsafe_allow_html=True,
    )
    deficiencia = st.selectbox(
        'Você Possui Algum tipo de Deficiência:', ['Não', 'Sim']
    )

    c1, c2 = st.columns(2)
    if deficiencia == 'Sim':
        tipo_deficiencia = c1.selectbox(
            'Especifique Deficiencia:',
            [
                'Deficiência fisica',
                'Deficiência visual',
                'Deficiência auditiva',
                'Deficiência mental',
                'Deficiência intelectual',
                'Transtorno do espectro autista',
            ],
        )
        cid = c2.text_input('Informe o CID:', max_chars=5).upper()

    st.markdown(
        "<h4 style='text-align; font-family: Verdana'>Diversidade</h4>",
        unsafe_allow_html=True,
    )

    coluna1, coluna2 = st.columns(2)
    pronome = coluna1.radio(
        'Qual o pronome você prefere ser chamado:',
        ['Ele/Dele', 'Ela/Dela', 'Outros'],
    )
    orientacao = coluna1.radio(
        'Qual sua orientação sexual:',
        [
            'Assexual',
            'Bissexual',
            'Heterossexual',
            'Homossexual',
            'Pansexual',
            'Outros',
        ],
    )
    genero = coluna2.radio(
        'Qual sua identidade de gênero:',
        ['Cisgênero', 'Transgênero', 'Outros'],
    )
    cor = coluna2.radio(
        'Qual sua cor ou raça:',
        ['Amarela', 'Branca', 'Indígena', 'Parda', 'Preta'],
    )

    if st.button('ENVIAR CADASTRO'):
        try:
            if (
                not nome
                or not idade
                or not nivel_escolaridade
                or not rua
                or not cidade
                or not cep
                or not estado
            ):
                raise ValueError('Todos os campos devem ser preenchidos.')

            ficha = {
                'Nome Completo:': nome,
                'Idade:': f'{idade} anos',
                'Nivel de Escolaridade:': nivel_escolaridade,
                'Endereço:': rua,
                'CEP:': cep,
                'Cidade:': cidade,
                'Estado:': estado,
                'Deficiência:': deficiencia,
                'Tipo de deficiência:': '-'
                if deficiencia == 'Não'
                else tipo_deficiencia,
                'CID:': '-' if deficiencia == 'Não' else cid,
                'Pronome adequado:': pronome,
                'Gênero:': genero,
                'Orientação sexual:': orientacao,
                'Cor ou Raça:': cor,
            }
            st.write('Cadastro Enviado!')
            st.dataframe(ficha, width=500, height=525)
        except ValueError as e:
            st.error(e, icon='🚨')


if __name__ == '__main__':
    main()
