# Nome dos integrantes


-   Caio Cesar Bueno

-   Hudson Cordeiro Pinto

-   Humberto Tiggemann

-   Junio Rodrigo Da Silva

-   Luiz Henrique Gomes Popoff

-   Melquisedeque Oliveira

-   Robson Souza

-   Ruan Ribeiro De Faria

# Nome do Projeto

Análise de dados da empresa Corp Solutions

# Proposta

### Introdução:

Nossa análise visa identificar padrões de diversidade e desequilíbrios nos dados da Corp Solutions, propondo soluções para promover a inclusão e equidade na empresa. Compreender a composição demográfica e as dinâmicas internas da força de trabalho é essencial para criar um ambiente de trabalho diversificado, inclusivo e equitativo. 

### Metodologia:

Nossa abordagem metodológica envolveu duas etapas principais.

-   *Análise Exploratória de Dados (EDA) em Jupyter Notebook:*

Utilizamos o ambiente interativo do Jupyter Notebook juntamente com bibliotecas de análise de dados como Pandas, Seaborn e Matplotlib para realizar uma análise exploratória detalhada dos dados da Corp Solutions.
Durante esta fase, examinamos a distribuição dos dados, identificamos valores ausentes ou inconsistentes, exploramos correlações entre variáveis e procuramos padrões e tendências significativas nos dados.
Essa etapa nos permitiu compreender melhor a estrutura e as características dos dados, além de identificar áreas de interesse para análises mais aprofundadas.

-   *Desenvolvimento de Dashboard no Power BI:*

Para uma visualização mais interativa e acessível dos resultados da análise, desenvolvemos um dashboard utilizando o Power BI.
O dashboard apresenta visualizações dinâmicas e intuitivas dos principais insights e tendências identificados durante a análise de dados.
Com o Power BI, conseguimos criar gráficos, tabelas e filtros interativos para permitir uma exploração mais detalhada dos dados pelos usuários finais.

### Análise Exploratória de Dados:

Durante a análise exploratória de dados, realizamos as seguintes etapas utilizando o arquivo 'ada_hack.ipynb':

-   Correção de Caracteres Não Codificados:

Implementamos uma função para corrigir caracteres não codificados corretamente nos dados. Isso garantiu a consistência e integridade dos dados para análise subsequente.

-   Identificação e Tratamento de Valores Incorretos e Faltantes:

Identificamos valores incorretos e faltantes no conjunto de dados. Para os valores faltantes, que estavam presentes nas colunas Idade (56), Formação (44) e Tempo de Casa (200), optamos por excluir essas entradas para evitar comprometer as métricas. Essas exclusões representam aproximadamente 3,5% dos dados.

-   Verificação de Dados Divergentes:

Durante a análise, observamos dados divergentes, como valores de idade de colaboradores menores ou iguais a 16 anos ocupando cargos de gerência e Analista Sênior. Esses casos foram destacados para investigação adicional e possível correção, se necessário.

Essas etapas nos permitiram limpar e preparar os dados para análises mais avançadas, garantindo a qualidade e confiabilidade dos resultados obtidos.


### Apresentação dos Resultados no Power BI

#### Link para o Dashboard Power BI:
[Corp Solutions Dashboard - Power BI](https://app.powerbi.com/view?r=eyJrIjoiMDllNmNjNzctOWQ3Zi00ODM0LTg3ZGUtZTM3MTlkYTJlZDExIiwidCI6IjJkMDBlYmMwLTJiYTctNGIxZC04ODE4LWRiZTZhYjE0ZmIzYiJ9)

![Power BI Dashboard](https://i.imgur.com/5hiETQC.png)

##### Principais Insights:
- A porcentagem em relação à raça ficou coerente com os dados do IBGE 2022 (fonte: Censo Demográfico 2022).
- Observamos uma disparidade de gênero significativa, com três vezes mais homens do que mulheres trabalhando na Corp Solutions. Essa diferença é ainda mais pronunciada nos cargos de diretoria, onde apenas 11 mulheres ocupam essas posições em comparação com 75 homens, representando apenas 13% do total.
- Nos cargos de diretoria, a representatividade de mulheres brancas é baixa, com apenas 11 mulheres brancas, enquanto no sexo masculino existem apenas 3 pretos e 1 indígena.
- Há uma predominância de contratados das regiões Sul e Sudeste, com uma quantidade mínima de contratados no Espírito Santo, representando apenas 1,02% do total.
- Notamos que o número de estagiários na faixa etária entre 40 e 50 anos está acima da proporção de outras faixas etárias em diferentes níveis de senioridade.

Esses insights fornecem uma compreensão detalhada da composição demográfica da força de trabalho da Corp Solutions e destacam áreas de desigualdade que podem exigir intervenções específicas para promover a inclusão e equidade na empresa.


### Propostas finais:

- *Igualdade de gênero:* Promover contratações de mulheres em todas as senioridades.
- *Promoção da igualdade de gênero e raça na senioridade de Diretor:* Implementar medidas específicas para garantir representatividade.
- *Homogeneidade nas contratações geográficas:* Ampliar recrutamento em áreas sub-representadas.
- *Continuação da política de recrutamento para pessoas com mais de 40 anos:* Fortalecer a inclusão de profissionais em transição de carreira.
- *Implementação de modelo de machine learning para auxiliar no processo de recrutamento e seleção:* Otimizar eficiência e reduzir viéses no processo de seleção.
- *Realização de pesquisa mais aprofundada em relação à comunidade LGBTQIA+ e PCD:* Entender melhor as necessidades e desafios para promover um ambiente mais inclusivo.
