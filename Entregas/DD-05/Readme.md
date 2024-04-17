[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

![Banner](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Ada_hack.png)
---
# Projeto Ada Hack 

<p style="text-align: justify;">Este repositório tem como objetivo mostrar o projeto desenvolvido durante o Hackathon promovido pela Ada Tech | Vem ser Tech - Ifood.</p>

**Contexto do Ada Hach**:
<p style="text-align: justify;">A Corp Solutions, é uma empresa líder no mercado de tecnologia para recursos humanos, recentemente recebeu um aporte milionário de uma grande corporação dos Estados Unidos. Com o compromisso de se tornar uma referência no mercado e promover um ambiente de trabalho diverso e inclusivo, identificou a necessidade de aumentar a diversidade em sua equipe. A empresa acredita que a diversidade impulsiona a inovação e o sucesso dos negócios, comprometendo-se a criar uma cultura inclusiva, onde todas as vozes são valorizadas e respeitadas.</p>

**Desafio**:

<p style="text-align: justify;">Diante do contexto da Corp Solutions o objetivo do Ada Hack é identificar padrões de diversidade e desequilíbrios nos dados e propor soluções para promover a inclusão e equidade na empresa.</p>
 

**Integrantes**:

- [Adriely Boller](https://www.linkedin.com/in/adrielyzambiasiboller/)
- [Caio Miazzi Vieira](https://br.linkedin.com/in/caio-miazzi)
- [Camila Stavola](https://br.linkedin.com/in/camila-stavola-954a60190)
- [Jadeson Bruno Albuquerque da Silva](https://br.linkedin.com/in/jadeson-silva)
- [José Diniz Madruga Neto](https://br.linkedin.com/in/jose-diniz-madruga-neto)
- [Matheus Muniz](https://br.linkedin.com/in/math-muniz?challengeId=AQE0ZJagcErswgAAAY7dNYgNEUaX7RN32uYRSQSTj8DGn2KK7d6GtyoiPfh_IfSAzwQe_w9Obv4njgOYLqKVAJjKq4f2_vIhNA&submissionId=c2b0c1f4-e12e-c617-c5a0-e62175ad9566&challengeSource=AgFUNIpjewJ_aQAAAY7dNi79khiHSZ6qZkX0iMptJDx80fzNjbZLB1adSwA4z8I&challegeType=AgHoV4SzCm1PoAAAAY7dNi8AgIAqDU98mqn6vxPIFl_--zbwkm9MaAw&memberId=AgHFoAiYzn8IggAAAY7dNi8DwjuWeC22QkZmW_DHhwmfIMc&recognizeDevice=AgESEDUl853DAwAAAY7dNi8G45FGNk48_4iFyt3Fph7UOUgf_2Hd)
- [Pedro Henrique Sena Lima](https://www.linkedin.com/in/pedro-sena-994a63116/)
- [Rodrigo Freitas Bispo](https://br.linkedin.com/in/rodrigo-freitas-bispo)

**Professor**:
- [Flávio Crispin](https://www.linkedin.com/in/flaviocrispin/)

# DIVERSI.DATA

<p style="text-align: justify;">Nosso objetivo inicial foi dividir o projeto em quatro partes principais. Primeiramente, focamos na organização das ideias, atribuição de tarefas e monitoramento do progresso, utilizando o Trello. Em seguida, realizamos uma análise exploratória dos dados utilizando o Colab e a linguagem Python, juntamente com suas bibliotecas.</p> 

<p style="text-align: justify;">Posteriormente, criamos visualizações através do Power BI. Por fim, realizamos a elaboração do pitch para a apresentação dos dados.</p>

## **Trello**
<p style="text-align: justify;">O Trello foi utilizado como uma plataforma para auxiliar na gestão do projeto, permitindo uma organização eficiente das tarefas e uma comunicação clara entre os membros da equipe.</p>
<details>
<summary>Desenvolvimento</summary>
<p style="text-align: justify;">A utilização do Trello auxiliou na criação de um fluxo de trabalho transparente, atribuindo tarefas, monitorando o progresso e garantindo a colaboração eficaz entre os membros. Isso facilitou o acompanhamento dos dados e garantiu que o projeto se mantivesse dentro do prazo estabelecido.</p>

Imagem da plataforma Trello

![Trello](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Trello.jpeg)

</details>

## **Análise Exploratória** 
<p style="text-align: justify;">Para melhor entendimento dos padrões e tendências relacionados à diversidade dentro da Corp Solutions foi feita a análise exploratória do banco de dados da empresa.</p> 
<details>
<summary>Desenvolvimento</summary>

### **Entendendo os Dados**
<p style="text-align: justify;">Inicialmente, a base de dados foi importada para uma análise detalhada das informações, explorando a natureza dos dados disponíveis, sua estrutura, características e qualidade.</p>

Imagem geral do banco de dados

![Banco de dados](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Banco_de_dados.jpeg)


<p style="text-align: justify;">Durante essa análise, observamos que a base de dados continha erros de digitação. Tentamos resolver esse problema utilizando diferentes formatos de codificação, como 'utf-8', 'latin-1' e 'iso-8859-15', porém sem sucesso. Para corrigir esses erros, foi necessário realizar uma correção manual, implementando uma função específica para essa finalidade.</p>

``` 
def substituir_padroes(texto):

    if isinstance(texto, str):
        correcoes = {
            'Ã§': 'ç',
            'Ã¡': 'á',
            'Ã£': 'ã',
            'Ã©': 'é',
            'Ã³': 'ó',
            'Ã´': 'ô',
            'Ãº': 'ú',
            'Ãª': 'ê',
            'Ã‚': 'Â',
            'Ã¢': 'â',
            'Ã': 'í',
            'íµ': 'õ',
            'í': 'Á',
            'í´': 'ô'
        }
        for errado, correto in correcoes.items():
            texto = texto.replace(errado, correto)
    return texto

df.columns = df.columns.map(substituir_padroes)

df = df.applymap(substituir_padroes)
``` 
<p style="text-align: justify;">Após executar o código de correção de erros de digitação, podemos agora visualizar como a base de dados ficou após a correção.</p>

Base de dados corrigida

![Base_corrigida](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Banco_corrigido.jpeg)

### **Análise Univariável**

<p style="text-align: justify;">Para compreender os dados, é essencial examinar cada variável e compreender seu significado e relevância para o problema em questão. Como o tema do nosso desafio é diversidade algumas das colunas que devem destaque são as colunas Gênero e Raça.</p>

**Gênero**
<p style="text-align: justify;">A coluna Gênero indica o gênero de cada funcionário da empresa. Durante a análise, confirmamos que o tipo de dados é 'object' (texto), e não encontramos valores nulos. Uma observação relevante é que existem apenas dois valores distintos: "Fem" (Feminino) e "Masc" (Masculino). Adicionalmente, através do gráfico de barras, é visível a disparidade de registros classificados como masculino (7500) em comparação com os registros femininos (2500).</p>

Gráfico de barras quantidade de pessoas por Gênero

![Gênero](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Grafico_genero.jpeg)

<p style="text-align: justify;">Essa disparidade pode ser valiosa para comparações futuras com dados fornecidos pelo IBGE ou outras fontes de dados, permitindo verificar se os padrões observados refletem a realidade da população do país.</p>

**Raça**
<p style="text-align: justify;">A coluna Raça indica a raça de cada funcionário na empresa. Durante a análise, verificamos que o tipo de dados é 'object' (texto), e não possui nenhum valor nulo. É importante ressaltar que esta coluna possui cinco valores distintos: Pardo, Branco, Preto, Indígena e Amarelo igual a classificação realizada pelo censo do IBGE. Com o auxílio do gráfico de barras, podemos observar como estão distribuidos esses valores e entender melhor a composição racial dos funcionários.</p>

Gráfico de barras quantidade de pessoas por Raça

![Raça](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Grafico_raca.jpeg)

<p style="text-align: justify;">A distribuição da quantidade de pessoas por raça é outra informação que poderemos utilizar para comparações com outras bases de dados, oferecendo insights valiosos e relevantes para a discussão do projeto.<p>

### **Tratamento dos Dados**

<p style="text-align: justify;">Durante a análise dos dados, identificamos que algumas colunas apresentavam valores nulos e/ou dados inconsistentes, exigindo tratamentos específicos para cada situação.</p>

**Formação**
<p style="text-align: justify;">Na coluna de Formação, encontramos 44 valores nulos. Dado o baixo número de valores faltantes e o caráter categórico da variável, optamos por substituir os valores nulos pela string 'Não Informado', criando assim uma nova categoria para esses dados ausentes.</p>

*Código utilizado na substituição*:
```
               df["formacao"] = ["Não informado" if pd.isnull(a) else a for a in df["formacao"]]
```


**Idade**

<p style="text-align: justify;">Observamos que na coluna Idade havia 56 valores nulos e também registros com idade inferior a 18 anos. E de acordo com as leis trabalhistas do Brasil, a contratação geral para estágios e contratação no regime CLT é de 18 anos.Para resolver esses problemas, realizamos uma análise da distribuição dos valores da coluna por meio de um gráfico, observando que a distribuição é aproximadamente simétrica (com skewness próxima de 0) e ligeiramente achatada (com kurtosis negativa). Portanto, decidimos substituir os valores nulos e aqueles inferiores a 18 anos pela mediana da idade de cada nível de senioridade.</p>

*Código utilizado na substituição*:
```
mediana_por_senioridade = df.groupby('senioridade')['idade'].median()
for senioridade, mediana in mediana_por_senioridade.items():
    mascara = (df['senioridade'] == senioridade) & ((df['idade'].isnull()) | (df['idade'] < 18))
    df.loc[mascara, 'idade'] = mediana
```
**Tempo de casa**

<p style="text-align: justify;">A coluna 'Tempo de Casa' apresentava tanto valores negativos quanto ausentes, totalizando 298 registros problemáticos. Para resolver esses problemas, realizamos uma análise da distribuição dos valores da coluna por meio de um gráfico, observando que a distribuição é aproximadamente simétrica (com skewness próxima de 0) e ligeiramente achatada (com kurtosis negativa). Com base nessa análise, optamos por substituir os valores negativos e ausentes pela mediana da coluna 'Tempo de Casa', considerando-a uma medida adequada para representar o tempo de serviço dos funcionários.</p>

*Código utilizado na substituição*:
```
mascara = (df['tempo_de_casa'] < 0) | ((df['tempo_de_casa'].isnull()))
df.loc[mascara, 'tempo_de_casa'] = df["tempo_de_casa"].median()
```


### **Análise Multivariável**

<p style="text-align: justify;">A análise multivariável é uma técnica estatística utilizada para examinar simultaneamente a relação entre múltiplas variáveis ​​em um conjunto de dados. Sendo assim, nessa etapa foi realizada uma análise dos dados com o objetivo de obter insights que nos ajudarão a responder às questões levantadas no início deste trabalho, além de verificar a natureza e a extensão das relações entre as variáveis.</p>

**Alguns Insights Obtidos**

<p style="text-align: justify;">Analisando a relação entre raça e senioridade, podemos observar disparidades na distribuição de pessoas em diferentes níveis organizacionais entre os diversos grupos raciais.Essa discrepância entre grupos raciais levanta questionamentos sobre a equidade das oportunidades de progressão na carreira. Para aprofundar a compreensão, posteriormente será realizada uma análise comparativa entre os dados internos da empresa e estatísticas populacionais.</p>

Relação entre a coluna Raça e Senioridade

![Multivariavel_Raça_Senioridade](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Grafico_raca_senioridade.jpeg)

<p style="text-align: justify;">Outra análise relevante é a relação do gênero e da senioridade. Nessa análise fica evidente que a presença feminina é menor do que 27% em todos os cargos, sendo que no cargo de diretor, o mais elevado, as mulheres representam apenas 14% do quadro de funcionários. Esses números sugerem uma sub-representação significativa das mulheres em cada nível de senioridade dentro da organização. Esta constatação destaca a importância de uma análise mais aprofundada e de possíveis iniciativas para promover a igualdade de gênero, como o desenvolvimento de políticas e a implementação de ações corretivas para diminuir essa disparidade e promover um ambiente de trabalho mais inclusivo e equitativo.</p>

Relação entre a coluna Gênero e Senioridade

![Multivariavel_Gênero_Senioridade](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Grafico_genero_senioridade.jpeg)

### **Criação da tabela para uso no Power BI**
<p style="text-align: justify;">Nessa etapa, foi criado uma tabela essencial para a elaboração do dashboard no Power BI. Essa tabela teve os valores substituídos por IDs para identificar cada categoria. Para a substituição foi utilizado um dicionário, garantindo a consistência e a precisão das informações em ambas as tabelas. Essa abordagem facilitará a integração dos dados coletados com o ambiente de análise no Power BI, permitindo uma visualização eficiente e interativa dos resultados.</p>

*Parte do dicionário utilizado na substituição*
```
id_formacao = {'Ensino Médio': 1,
'Ensino Superior': 2,
'Pós Graduação': 3,
'Mestrado':4,
'Doutorado':5,
'Não informado':6}

```
Base de dados após a substituição

![Tabela_power_bi](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/base_dados_bi.jpeg)

### **Comparação da Base de Dados da Corp Solutions com outras Bases de Dados**

<p style="text-align: justify;">Foram utilizados dados do IBGE e da State of Data para comparar com a base de dados da Corp Solutions com a finalidade de verificar se as se a equipe de funcionários da empresa estão condizentes com as estatísticas demográficas e os padrões observados em outras fontes confiáveis de dados.</p>

<p style="text-align: justify;">No gráfico abaixo, torna-se evidente a disparidade entre a distribuição da população brasileira e a composição dos funcionários dentro das empresas. Tanto nos dados da Corp Solutions quanto da State of Data, é notável uma predominância masculina, especialmente em cargos de liderança. Além disso, observa-se que a Corp Solutions apresenta uma maior quantidade de mulher quando comparado com o mercado na área de dados. Essas informações demonstram possíveis desafios relacionados à representatividade de gênero dentro da organização, destacando a importância de medidas afirmativas para melhorar a diversidade e inclusão no ambiente de trabalho.</p>

Gráfico de comparação da base de dados da Corp Solutions com outras Bases de Dados

![Comparacao_Corp_e_outras_bases](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Grafico_com_Bases_comparativas.jpeg)

</details>

**OBS:** Vários colaboradores contribuíram para a versão final deste projeto por meio de arquivos colaborativos individuais, que foram posteriormente integrados para criar uma narrativa coesa e abrangente.

## **Power BI**
<p style="text-align: justify;">O Power BI foi utilizado para criar visualizações dinâmicas e interativas que destacam os dados relacionados à diversidade e à inclusão presentes na base de dados da Corp Solutions.</p>

<details>
<summary>Desenvolvimento</summary>
<p style="text-align: justify;"> </p>



</details>


## **Pitch**
<p style="text-align: justify;">O pitch foi desenvolvido para apresentar os pontos mais importantes durante as análises e destacar a importância da diversidade e inclusão para o sucesso da organização.</p> 
<details>
<summary>Desenvolvimento</summary>
<p style="text-align: justify;">O pitch foi elaborado para transmitir o desafio enfrentado pela Corp Solutions e a proposta para aprimorar a inclusão e a diversidade dentro da organização. Para isso, utilizou-se o Canva como nossa ferramenta principal para criar uma apresentação atraente e interativa.</p>
<p style="text-align: justify;">A apresentação começa com uma contextualização do problema em questão e destacando sua importância. Em seguida, é apresentada uma visão geral da base de dados da Corp Solutions e identificado os principais problemas existentes. E logo após é apresentado a proposta para enfrentar esses desafios de maneira eficaz.</p>
<p style="text-align: justify;">Por fim, são apresentados links importantes para informações adicionais e recursos relevantes para complementar a proposta.</p>

Imagem do Pitch

![Pitch](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Pitch.jpeg)

</details>


# Proposta 

Após uma análise detalhada das informações, comparando os dados com referências do IBGE e do State of Data, ficou evidente uma discrepância na composição demográfica da empresa em relação à população em geral. Diante desse cenário, propomos uma abordagem inovadora que não apenas fomenta a inclusão e a diversidade, mas também impulsiona o crescimento e o sucesso organizacional.
### O que é a nossa proposta?
Nossa proposta consiste em implementar um processo eficaz e sólido para a coleta e tratamento de dados diversos sobre os diferentes grupos dentro das empresas. Realizaremos um diagnóstico detalhado do nível de diversidade de cada estabelecimento e ofereceremos consultorias personalizadas de acordo com as necessidades de cada ambiente de trabalho, além de um acompanhamento contínuo duradouro.

Para executar esse ciclo, contamos com uma equipe especializada que se encarregará desde a coleta e tratamento dos dados até a implementação de planos de desenvolvimento personalizados, adaptados à realidade identitária de cada empresa. Além disso, desenvolvemos um dashboard eficiente o qual funcionará como uma calculadora de diversidade, que será nossa principal ferramenta para receber e analisar os dados de cada local, fornecendo métricas e índices para avaliar o nível de diversidade da empresa e como isso pode impactar positivamente na produtividade laboratórial.

Com essa abordagem abrangente e focada em resultados, estamos preparados para ajudar as empresas a promover um ambiente mais inclusivo e diversificado, o que não apenas fortalece a cultura organizacional, mas também impulsiona o sucesso a longo prazo.

### Por que optar por nossa proposta?

O diferencial de nossa abordagem reside na implementação de toda uma arquitetura de dados, incorporação de uma Calculadora de Diversidade,a implementação de um formulário para coleta e administração de dados e na realização de consultorias personalizadas,criando, assim, um ciclo eficiente , cujas fases citadas anteriormente estão descritas abaixo:

📌**Coleta de dados**: Nessa fase será utilizada um formulário desenvolvido pela nossa equipe, o qual será divulgado na empresa com o intuito de coletar as informações relacionadas com as caracteristicas de diversidade de cada funcionário. Assim, temos de maneira eficiente e rápida dados relacionados com as caracteristicas de raça, genero e faixa etária de cada colaborador da empresa. Vale destacar que todos as informações serão armazenados com muito cuidado pela nossa equipe seguindo todas as diretrizes da LGPD(Lei Geral de Proteção aos Dados). Ademais, o formulário poderá ser usado para manutenção e atualização dos dados a longo prazo.

Acesso ao [Formulário](https://docs.google.com/forms/d/e/1FAIpQLSdoglp-c4JXYuu5TiSiKoYRZ_zdE3X7qBJeYQFudg4MWG5fMA/viewform)

Imagem do Formulário de Diversidade

![Form1](https://github.com/mxthunder123/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Form1.jpg)

📌**Tratamento e Arquitetura dos dados**: Com os dados coletados, nossa equipe irá realizar todo o tratamento, geração de tabelas, administração de data lake, organização de acessos e manutenção de toda essa infraestrutura.

📌**Calculadora de Diversidade**: Introduzimos um dashboard inovador que evidencia a diferença entre a composição de raça, genero e faixa etária da empresa com a composição implementada por fontes confiaveis, como o IBGE. Essa ferramenta permitirá uma avaliação precisa do progresso da empresa em direção à diversidade, trazendo indices que demonstram o quanto a inclusão presente hoje no local analisado influencia na produtividade.

📌**Serviço de Consultoria**: Após a avaliação da diversidade dentro da empresa contratante,será ofertado um serviço de consultoria personalizado conforme os resultados da análise resultante do dashboard. Assim, serão implementadas ações afirmativas com o objetivo de reduzir disparidades dentro da equipe. Algumas dessas ações incluem:

- **Vagas Afirmativas e Grupos de Afinidade:** As vagas afirmativas garantem igualdade de oportunidades de emprego para todos, enquanto os grupos de afinidade promovem um ambiente de trabalho inclusivo e acolhedor.

- **Formação de Novos Profissionais:** Investir na formação e capacitação de novos profissionais assegura que todos tenham acesso às mesmas oportunidades de desenvolvimento e crescimento na carreira, além de fornecer orientação e suporte para a progressão profissional.

- **Letramento Racial:** Além de identificar o racismo nas relações sociais e institucionais, é essencial implementar práticas que conscientizem sobre a luta antirracista na sociedade, por meio do reconhecimento de eventos históricos relevantes.

- **Comitê de Diversidade:** A criação de comitês dedicados à diversidade auxilia na promoção de políticas e práticas que impactam igualmente todos os membros das equipes da organização.

### Quais serão os benefícios para a empresa após a implementação da proposta?

- Aumento de 4% na produtividade dos colaboradores a cada 10% de aumento na diversidade étnico-racial;
- Maior capacidade de atrair profissionais com habilidades e competências diversas;
- Melhoria do bem-estar geral dos colaboradores;
- Ampliação da diversidade de talentos e habilidades dentro da organização;
- Aquisição de um serviço de acompanhamento personalizado;


# Referências
- Dados do IBGE - [Censo demográfico 2022](https://censo2022.ibge.gov.br/panorama/)
- Dados do State of Data - [Dados de 2023](https://e99c657b-32c7-4c8b-aed5-f9d1d1155ccb.usrfiles.com/ugd/e99c65_5ffb2f84b01a401d8738481f56d570f9.pdf?utm_source=www.datahackers.news&utm_medium=referral&utm_campaign=download-do-relatorio-state-of-data-brazil-2023-o-panorama-do-mercado-brasileiro-de-trabalho-em-dados)
- Veja 6 passos para promover igualdade racial dentro das empresas - [Exame](https://exame.com/carreira/veja-6-passos-para-promover-igualdade-racial-dentro-das-empresas/)
- O que é letramento racial e qual a sua importância? - [Estado de Minas](https://www.em.com.br/diversidade/2024/02/6796399-o-que-e-letramento-racial-e-qual-a-sua-importancia.html)
- Mulheres na tecnologia: cenário, desafios e nomes que marcaram a história - [CNN Brasil](https://www.cnnbrasil.com.br/tecnologia/mulheres-na-tecnologia/)
- Números não mentem: diversidade nas empresas aumenta a produtividade - [Exame](https://exame.com/bussola/numeros-nao-mentem-diversidade-nas-empresas-aumenta-a-produtividade/)
- Marcadores sociais: o conceito na construção de políticas pública - [Centro de Liderança Pública](https://www.clp.org.br/marcadores-sociais-o-conceito-na-construcao-de-politicas-publicas/#:~:text=Os%20Marcadores%20Sociais%20s%C3%A3o%20definidos,%2C%20etnia%2C%20entre%20muitas%20outras.)
- Pluraridade nas instituições traz benefícios - [CNN Brasil](https://www.cnnbrasil.com.br/economia/pluralidade-nas-instituicoes-traz-beneficios/)
- A gente promove a igualdade racial em todos os espaços possíveis - [Instituto Entidades do Brasil ](https://www.simaigualdaderacial.com.br/)
