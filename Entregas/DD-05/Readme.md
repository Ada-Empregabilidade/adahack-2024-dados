[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

![Banner](https://github.com/AdrielyZBoller/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Ada_hack.png)
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

# <span style="color:red">D</span><span style="color:orange">I</span><span style="color:yellow">V</span><span style="color:green">E</span><span style="color:blue">R</span><span style="color:purple">S</span><span style="color:pink">I</span><span style="color:brown">.</span>DATA

<p style="text-align: justify;">Nosso objetivo inicial foi dividir o projeto em quatro partes principais. Primeiramente, focamos na organização das ideias, atribuição de tarefas e monitoramento do progresso, utilizando o Trello. Em seguida, realizamos uma análise exploratória dos dados utilizando o Colab e a linguagem Python, juntamente com suas bibliotecas. Posteriormente, criamos visualizações através do Power BI. Por fim, realizamos a elaboração do pitch para a apresentação dos dados.</p>

## **Trello**
<p style="text-align: justify;">O Trello foi utilizado como uma plataforma para auxiliar na gestão do projeto, permitindo uma organização eficiente das tarefas e uma comunicação clara entre os membros da equipe.</p>
<details>
<summary>Desenvolvimento</summary>
<p style="text-align: justify;">A utilização do Trello auxiliou na criação de um fluxo de trabalho transparente, atribuindo tarefas, monitorando o progresso e garantindo a colaboração eficaz entre os membros. Isso facilitou o acompanhamento dos dados e garantiu que o projeto se mantivesse dentro do prazo estabelecido.</p>

Imagem da plataforma Trello

![Trello]()

</details>

## **Análise Exploratória** 
<p style="text-align: justify;">Para melhor entendimento dos padrões e tendências relacionados à diversidade dentro da Corp Solutions foi feita a análise exploratória do banco de dados da empresa.</p> 
<details>
<summary>Desenvolvimento</summary>

### **Entendendo os Dados**
<p style="text-align: justify;">Inicialmente, a base de dados foi importada para uma análise detalhada das informações, explorando a natureza dos dados disponíveis, sua estrutura, características e qualidade.</p>

Imagem geral do banco de dados

![Banco de dados]()


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

![Base_corrigida]()

### **Análise Univariável**

<p style="text-align: justify;">Para compreender os dados, é essencial examinar cada variável e compreender seu significado e relevância para o problema em questão. Como o tema do nosso desafio é diversidade algumas das colunas que devem destaque são as colunas Gênero e Raça.</p>

**Gênero**
<p style="text-align: justify;">A coluna Gênero indica o gênero de cada funcionário da empresa. Durante a análise, confirmamos que o tipo de dados é 'object' (texto), e não encontramos valores nulos. Uma observação relevante é que existem apenas dois valores distintos: "Fem" (Feminino) e "Masc" (Masculino). Adicionalmente, através do gráfico de barras, é visível a disparidade de registros classificados como masculino (7500) em comparação com os registros femininos (2500).</p>

Gráfico de barras quantidade de pessoas por Gênero

![Gênero]()

<p style="text-align: justify;">Essa disparidade pode ser valiosa para comparações futuras com dados fornecidos pelo IBGE ou outras fontes de dados, permitindo verificar se os padrões observados refletem a realidade da população do país.</p>

**Raça**
<p style="text-align: justify;">A coluna Raça indica a raça de cada funcionário na empresa. Durante a análise, verificamos que o tipo de dados é 'object' (texto), e não possui nenhum valor nulo. É importante ressaltar que esta coluna possui cinco valores distintos: Pardo, Branco, Preto, Indígena e Amarelo igual a classificação realizada pelo censo do IBGE. Com o auxílio do gráfico de barras, podemos observar como estão distribuidos esses valores e entender melhor a composição racial dos funcionários.</p>

Gráfico de barras quantidade de pessoas por Raça

![Raça]()

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

![Multivariavel_Raça_Senioridade]()

<p style="text-align: justify;">Outra análise relevante é a relação do gênero e da senioridade. Nessa análise fica evidente que a presença feminina é menor do que 27% em todos os cargos, sendo que no cargo de diretor, o mais elevado, as mulheres representam apenas 14% do quadro de funcionários. Esses números sugerem uma sub-representação significativa das mulheres em cada nível de senioridade dentro da organização. Esta constatação destaca a importância de uma análise mais aprofundada e de possíveis iniciativas para promover a igualdade de gênero, como o desenvolvimento de políticas e a implementação de ações corretivas para diminuir essa disparidade e promover um ambiente de trabalho mais inclusivo e equitativo.</p>

Relação entre a coluna Gênero e Senioridade

![Multivariavel_Gênero_Senioridade]()

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

![Tabela_power_bi]()

### **Comparação da Base de Dados da Corp Solutions com outras Bases de Dados**

<p style="text-align: justify;">Foram utilizados dados do IBGE e da State of Data para comparar com a base de dados da Corp Solutions com a finalidade de verificar se as se a equipe de funcionários da empresa estão condizentes com as estatísticas demográficas e os padrões observados em outras fontes confiáveis de dados.</p>

<p style="text-align: justify;">No gráfico abaixo, torna-se evidente a disparidade entre a distribuição da população brasileira e a composição dos funcionários dentro das empresas. Tanto nos dados da Corp Solutions quanto da State of Data, é notável uma predominância masculina, especialmente em cargos de liderança. Além disso, observa-se que a Corp Solutions apresenta uma maior quantidade de mulher quando comparado com o mercado na área de dados. Essas informações demonstram possíveis desafios relacionados à representatividade de gênero dentro da organização, destacando a importância de medidas afirmativas para melhorar a diversidade e inclusão no ambiente de trabalho.</p>

Gráfico de comparação da base de dados da Corp Solutions com outras Bases de Dados

![Comparacao_Corp_e_outras_bases]()

</details>

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

![Pitch]()


</details>


# Proposta 

📌**Calculadora**:

📌**Formulário de Diversidade**:

Acesso ao [Formulário](https://docs.google.com/forms/d/e/1FAIpQLSdoglp-c4JXYuu5TiSiKoYRZ_zdE3X7qBJeYQFudg4MWG5fMA/viewform)
<details>
<summary>Informações</summary>
<p style="text-align: justify;"> Com o objetivo de melhorar a base de dados da Corp Solutions em relação à diversidade de sua equipe, foi proposto um formulário com perguntas adicionais sobre o tema. Esse formulário procura obter maiores informações sobre a diversidade entre os membros da empresa, possibilitando a identificação de lacunas e áreas de melhoria.</p>

<p style="text-align: center;"> Imagem do Formulário de Diversidade</p>

![Form1](https://github.com/AdrielyZBoller/adahack-2024-dados/blob/main/Entregas/DD-05/Imagem/Form1.jpg)

</details>


# Referências
- Dados do IBGE - [Censo demográfico 2022](https://censo2022.ibge.gov.br/panorama/)
- Dados do State of Data - []()