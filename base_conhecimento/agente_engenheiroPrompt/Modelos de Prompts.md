# MODELOS DE PROMPTS PARA PESQUISA ACADÊMICA

## ÍNDICE

1. [Técnicas Fundamentais de Prompting](#técnicas-fundamentais)

   - Aprendizado com Exemplo (Few-Shot)
   - Cadeia de Pensamento (Chain of Thought)
   - Árvore de Pensamentos (Tree of Thoughts)
   - Justificação Estruturada

2. [Prompts para Definição de Pesquisa](#definição-de-pesquisa)

   - Definição de Questão de Pesquisa
   - Elaboração de Objetivos
   - Delimitação de Escopo

3. [Prompts para Análise de Literatura](#análise-de-literatura)
   - Extração e Crítica de Textos Científicos
   - Fichamento Estruturado por Tipo de Material
   - Síntese Integrativa para Revisão de Literatura
4. [Prompts para Avaliação e Refinamento](#avaliação-e-refinamento)

   - Avaliação de Textos e Remoção de Plágio
   - Avaliação de Prompts
   - Refinamento Iterativo de Análises

5. [Técnicas Avançadas por Contexto de Pesquisa](#técnicas-avançadas)
   - Pesquisa em Educação e Aprendizagem
   - Pesquisa em Ciências Sociais
   - Pesquisa em Tecnologia e Computação

## TÉCNICAS FUNDAMENTAIS

### APRENDIZADO COM EXEMPLO (FEW-SHOT)

[Manter o conteúdo existente sobre few-shot aqui]

### CADEIA DE PENSAMENTO (CHAIN OF THOUGHT)

[Manter o conteúdo existente sobre chain of thought aqui]

### ÁRVORE DE PENSAMENTOS (TREE OF THOUGHTS)

[Manter o conteúdo existente sobre tree of thoughts aqui]

### JUSTIFICAÇÃO ESTRUTURADA

[Manter o conteúdo existente sobre justificação estruturada aqui]

## DEFINIÇÃO DE PESQUISA

### PROMPT AVANÇADO: DEFINIR A QUESTÃO DE PESQUISA

[Manter o conteúdo existente sobre definição de questão de pesquisa]

## ANÁLISE DE LITERATURA

### PROMPT AVANÇADO: LEITOR E CRÍTICO DE TEXTOS CIENTÍFICOS

[Manter o conteúdo existente sobre leitor e crítico de textos]

### PROMPT AVANÇADO: FICHAMENTO ESTRUTURADO POR TIPO DE MATERIAL

#### Para Livros Teóricos (Material Extenso)

```markdown
Atue como um consórcio de especialistas em [ÁREA ESPECÍFICA]. Analise este livro [TÍTULO] seguindo estas etapas:

ETAPA 1: MAPEAMENTO CONCEITUAL

- Identifique os 5 conceitos principais sobre [TEMA] na obra
- Para cada conceito: forneça definição teórica, página da citação original, e autores citados

ETAPA 2: ANÁLISE CRÍTICA TRIDIMENSIONAL

1. Dimensão Teórica:

   - Fundamentos epistemológicos do conceito apresentado
   - Evolução histórica deste conceito na literatura
   - Relação com outras teorias relevantes

2. Dimensão Metodológica:

   - Aplicações práticas propostas pelo autor
   - Evidências empíricas apresentadas (se houver)
   - Limitações identificadas na implementação

3. Dimensão Contextual:
   - Adaptabilidade ao contexto de [SEU CONTEXTO ESPECÍFICO]
   - Relevância para [SEU OBJETIVO DE PESQUISA]
   - Desafios específicos para implementação

ETAPA 3: SÍNTESE INTEGRATIVA

- Apresente uma tabela de síntese relacionando os conceitos centrais com sua aplicabilidade na sua pesquisa

ETAPA 4: EXTRAÇÃO DE CITAÇÕES

- Selecione 3 citações diretas mais relevantes, priorizando definições operacionais que possam fundamentar seu referencial teórico
```

#### Para Artigos Científicos

```markdown
Atue como um metodologista especializado em análise de evidências científicas sobre [TEMA]. Analise este artigo científico seguindo rigorosamente estas etapas:

ETAPA 1: ANÁLISE ESTRUTURAL (MÉTODO PICO)

- População: Identifique precisamente o grupo estudado
- Intervenção: Detalhe a metodologia ou abordagem aplicada
- Comparação: Determine se houve grupo controle ou comparação com outra abordagem
- Outcomes (Resultados): Especifique as métricas utilizadas

ETAPA 2: AVALIAÇÃO DE QUALIDADE METODOLÓGICA
Classifique o artigo segundo os critérios abaixo, justificando cada pontuação (1-5):

1. Rigor metodológico (desenho de pesquisa, amostragem, controle de variáveis)
2. Validade das métricas utilizadas
3. Consistência dos resultados e análise estatística
4. Aplicabilidade ao seu contexto de pesquisa
5. Contribuição teórica para o campo

ETAPA 3: FICHAMENTO ESTRUTURADO
Forneça um fichamento completo contendo:

- Dados bibliográficos completos
- Objetivo do estudo (conciso)
- Metodologia detalhada
- Resultados principais (com dados quantitativos quando disponíveis)
- Citações relevantes (2-3 com página)
- Limitações citadas pelos autores
- Análise crítica da validade e contribuição
- Conexão com sua pesquisa

ETAPA 4: RECOMENDAÇÃO PARA INCLUSÃO
Recomende se o artigo deve ser incluído no referencial teórico, justificando sua decisão com base nos critérios de qualidade e relevância.
```

#### Para Documentos Institucionais e Normativos

```markdown
Atue como um especialista em análise de documentos institucionais na área de [SUA ÁREA]. Analise este documento usando uma abordagem exploratória e estruturada:

ETAPA 1: MAPEAMENTO ONTOLÓGICO DO DOCUMENTO

- Identifique explicitamente onde o documento aborda cada categoria relevante para sua pesquisa
- Para cada categoria, forneça:
  - Localização exata no documento (seção/página)
  - Citação textual do trecho relevante
  - Classificação da ênfase dada (Alta/Média/Baixa)

ETAPA 2: ANÁLISE POR MÚLTIPLAS PERSPECTIVAS
Explore o documento através de perspectivas relevantes para sua pesquisa, como:

- Perspectiva estrutural/organizacional
- Perspectiva metodológica/processual
- Perspectiva conceitual/teórica

ETAPA 3: COMPARAÇÃO COM OUTROS DOCUMENTOS RELEVANTES

- Compare o documento analisado com outros documentos similares ou relacionados
- Identifique alinhamentos e divergências nos pontos principais
- Avalie como este documento se relaciona com o contexto mais amplo

ETAPA 4: SÍNTESE CRÍTICA E RECOMENDAÇÕES

- Elabore uma síntese dos pontos fortes e fragilidades do documento
- Proponha recomendações específicas relevantes para sua pesquisa
- Classifique o documento quanto à sua relevância para seu objeto de estudo
```

### PROMPT AVANÇADO: SÍNTESE INTEGRATIVA PARA REVISÃO DE LITERATURA

```markdown
Atue como uma equipe multidisciplinar de pesquisadores especializada em síntese de conhecimento científico. Com base nos fichamentos que fornecerei sobre [TEMA DA PESQUISA], desenvolva:

ETAPA 1: MAPA DO ESTADO DA ARTE
Crie uma representação estruturada do conhecimento atual sobre [TEMA]:

1. Categorização Teórica:

   - Correntes teóricas identificadas (com principais autores)
   - Definições operacionais predominantes
   - Evolução cronológica dos conceitos (por períodos relevantes)

2. Mapeamento Metodológico:

   - Abordagens metodológicas mais utilizadas (categorizar e quantificar)
   - Métodos de avaliação (instrumentos validados, métricas)
   - Contextos de aplicação mais estudados

3. Síntese de Evidências:
   - Tabulação dos resultados empíricos por tipo de abordagem/intervenção
   - Níveis de evidência (forte, moderada, limitada) por metodologia
   - Fatores moderadores identificados

ETAPA 2: ANÁLISE DE LACUNAS E INCONSISTÊNCIAS
Aplique diferentes abordagens analíticas para identificar lacunas:

- Análise de Divergências Conceituais
- Análise de Vazios Metodológicos
- Análise de Gaps Contextuais

ETAPA 3: FRAMEWORK INTEGRATIVO
Desenvolva um modelo conceitual que integre as principais dimensões teóricas, metodológicas e contextuais identificadas.

ETAPA 4: AGENDA DE PESQUISA
Proponha 5-7 questões de pesquisa prioritárias que:

- Abordem as principais lacunas identificadas
- Sejam formuladas usando protocolo adequado (PICO, PEO, etc.)
- Incluam sugestões metodológicas específicas
- Considerem o impacto potencial para a área

ETAPA 5: VERIFICAÇÃO DE CONSISTÊNCIA
Revise criticamente a síntese produzida, verificando alinhamento com os dados originais e coerência interna.
```

## AVALIAÇÃO E REFINAMENTO

### PROMPT AVANÇADO: LEITURA, AVALIAÇÃO E MELHORIA DE TEXTOS (FOCO EM PLÁGIO DE IA)

[Manter o conteúdo existente sobre avaliação e melhoria de textos]

### PROMPT AVANÇADO: AVALIADOR DE PROMPTS

[Manter o conteúdo existente sobre avaliação de prompts]

### PROMPT AVANÇADO: LEITURA E CLASSIFICAÇÃO DE ARTIGOS EM RSL

[Manter o conteúdo existente sobre classificação de artigos em RSL]

## TÉCNICAS AVANÇADAS

### TÉCNICAS AVANÇADAS PARA PESQUISA EM EDUCAÇÃO E APRENDIZAGEM

#### Identificação de Modelos Teóricos

```markdown
Como pesquisador especializado em modelos teóricos de [ÁREA EDUCACIONAL], analise a literatura sobre [TEMA] e:

1. Identifique os 5-7 principais modelos teóricos relacionados
2. Para cada modelo, construa uma análise seguindo esta estrutura:
   - Autor(es) e ano de proposição
   - Pressupostos epistemológicos fundamentais
   - Componentes/dimensões do modelo
   - Processo de desenvolvimento segundo o modelo
   - Papel do educador/facilitador
   - Evidências empíricas de validação
3. Compare sistematicamente os modelos em uma matriz que destaque:
   - Convergências conceituais
   - Divergências teóricas
   - Complementaridades
   - Aplicabilidade ao contexto específico de [SEU CONTEXTO]
   - Limitações para o contexto em que você atua
4. Desenvolva um diagrama evolutivo que mostre:
   - Relações de influência entre os modelos
   - Ramificações teóricas
   - Tendências contemporâneas
```

#### Análise de Metodologias Educacionais

```markdown
Como especialista em metodologias de ensino-aprendizagem, analise:

1. Classifique as metodologias identificadas na literatura segundo:
   a) Princípio pedagógico predominante

   - [LISTAR PRINCIPAIS PRINCÍPIOS RELEVANTES PARA SUA ÁREA]

   b) Nível de autonomia demandado/promovido

   - Inicial (estruturado, com forte orientação)
   - Intermediário (semi-estruturado, com orientação moderada)
   - Avançado (pouco estruturado, com mínima orientação)

   c) Evidência de eficácia

   - Forte (múltiplos estudos convergentes)
   - Moderada (alguns estudos positivos)
   - Limitada (poucos estudos ou resultados mistos)
   - Inconclusiva (ausência de estudos ou resultados contraditórios)

2. Para cada metodologia, desenvolva uma matriz que relacione:
   - Competências específicas desenvolvidas
   - Desafios de implementação no seu contexto
   - Técnicas de avaliação recomendadas
3. Categorize as metodologias por adequação a:
   - Diferentes momentos da formação
   - Tipos de conteúdo
   - Modalidades de ensino
```

#### Análise de Perfis de Aprendizagem

```markdown
Como pesquisador especializado em perfis de aprendizagem, desenvolva:

1. Uma análise multifacetada do perfil do [TIPO DE APRENDIZ], considerando:

   - Dimensão cognitiva
   - Dimensão social/relacional
   - Dimensão tecnológica
   - Dimensão atitudinal

2. Crie 4-5 personas representativas de diferentes perfis de [TIPO DE APRENDIZ]:

   - Para cada persona, detalhe:
     - Background e experiências prévias
     - Motivações
     - Pontos fortes e desafios
     - Preferências de aprendizagem
     - Trajetória esperada de desenvolvimento

3. Para cada persona, projete:
   - Uma trajetória de desenvolvimento ao longo da formação
   - Abordagens pedagógicas mais adequadas para cada etapa
   - Estratégias de suporte recomendadas
   - Desafios específicos a serem superados
   - Indicadores de progresso a serem monitorados
```

### TÉCNICAS AVANÇADAS PARA PESQUISA EM CIÊNCIAS SOCIAIS

[Adicionar técnicas específicas para ciências sociais]

### TÉCNICAS AVANÇADAS PARA PESQUISA EM TECNOLOGIA E COMPUTAÇÃO

[Adicionar técnicas específicas para tecnologia e computação]
