# Biblioteca de Prompts para Revisão Sistemática de Literatura

Esta biblioteca apresenta uma coleção estruturada de prompts especializados para suporte à revisão sistemática de literatura científica, com ênfase em pesquisas sobre aprendizagem autodirigida e metodologias ativas.

## 1. Prompts para Planejamento da Revisão

### 1.1 Definição de Escopo e Questões de Pesquisa

```markdown
# PROMPT: Definição de Escopo para Revisão Sistemática

## CONTEXTO

Estou iniciando uma revisão sistemática da literatura sobre aprendizagem autodirigida no contexto do ensino superior em cursos de computação no Brasil.

## OBJETIVO

Definir com precisão o escopo da revisão, estabelecendo questões de pesquisa claras e critérios de inclusão/exclusão.

## REQUISITOS

- Utilize a técnica Zero-Shot + Role Prompting
- Assuma o papel de um pesquisador especialista em metodologia científica com experiência em revisões sistemáticas

## FORMATO DE SAÍDA

1. Escopo delimitado (tema, período, contexto geográfico e educacional)
2. 3-5 questões de pesquisa principais formuladas com precisão
3. Critérios de inclusão e exclusão operacionalizados
4. Justificativa metodológica para a delimitação proposta

## CONSIDERAÇÕES ADICIONAIS

- Considere a especificidade do contexto brasileiro
- Pondere sobre as particularidades da área de computação
- Identifique potenciais desafios de uma revisão neste campo
```

### 1.2 Definição de Protocolo de Revisão

```markdown
# PROMPT: Protocolo de Revisão Sistemática

## CONTEXTO

Estou conduzindo uma revisão sistemática sobre aprendizagem autodirigida (SDL) em cursos superiores de computação, com foco nas seguintes questões de pesquisa:
[INSERIR QUESTÕES DE PESQUISA]

## OBJETIVO

Desenvolver um protocolo detalhado para conduzir a revisão sistemática.

## REQUISITOS

- Utilize a técnica CoT + Role Prompting
- Raciocine passo a passo sobre cada elemento do protocolo
- Considere as especificidades da revisão em educação e tecnologia

## FORMATO DE SAÍDA

1. Estratégia de busca:

   - Bases de dados a serem consultadas
   - Strings de busca específicas para cada base
   - Operadores booleanos e wildcards recomendados

2. Processo de seleção:

   - Fluxo de triagem (títulos → resumos → textos completos)
   - Procedimento para resolução de discordâncias
   - Documentação do processo

3. Extração de dados:

   - Categorias específicas para extração
   - Template de fichamento padronizado
   - Método de codificação temática

4. Análise e síntese:
   - Abordagem para síntese (narrativa, meta-análise, etc.)
   - Método para avaliação de qualidade dos estudos
   - Estratégia para identificação de padrões

## CONSIDERAÇÕES ADICIONAIS

- [CONFIANÇA]: Indique seu nível de confiança em cada recomendação
- Justifique suas escolhas com referências a práticas estabelecidas em revisões sistemáticas
```

### 1.3 Planejamento Temporal da Revisão

```markdown
# PROMPT: Cronograma para Revisão Sistemática

## CONTEXTO

Estou planejando conduzir uma revisão sistemática sobre aprendizagem autodirigida em cursos de computação, seguindo o protocolo:
[INSERIR RESUMO DO PROTOCOLO]

## OBJETIVO

Criar um cronograma realista para a execução completa da revisão sistemática.

## REQUISITOS

- Utilize a técnica Zero-Shot + Directional Stimulus
- Considere desafios práticos comuns em revisões sistemáticas
- Oriente o cronograma para maximizar rigor e eficiência

## FORMATO DE SAÍDA

Apresente um cronograma detalhado com:

1. Fases principais e subfases
2. Duração estimada de cada fase
3. Dependências entre atividades
4. Marcos de controle de qualidade
5. Reservas de contingência para imprevistos

## CONSIDERAÇÕES ADICIONAIS

- Considere um pesquisador trabalhando em tempo parcial na revisão
- Inclua pontos de verificação para validar a qualidade
- Indique alternativas para acelerar o processo se necessário
```

## 2. Prompts para Busca e Seleção

### 2.1 Refinamento de Strings de Busca

```markdown
# PROMPT: Refinamento de Strings de Busca

## CONTEXTO

Estou preparando strings de busca para uma revisão sistemática sobre aprendizagem autodirigida em cursos superiores de computação no Brasil.

## OBJETIVO

Desenvolver e refinar strings de busca otimizadas para diferentes bases de dados científicas.

## REQUISITOS

- Utilize a técnica Few-Shot + RAG
- Baseie-se nos exemplos de strings bem-sucedidas abaixo
- Adapte para capturar especificamente resultados relevantes sobre SDL em computação

## CONHECIMENTO CONTEXTUAL [RAG]

[Inclua aqui trechos de estudos sobre construção de strings de busca eficazes]

## EXEMPLOS (FEW-SHOT)

### Exemplo 1: String para Scopus

(("self-directed learning" OR "self directed learning" OR "SDL") AND ("higher education" OR "university" OR "college") AND ("computer science" OR "computing" OR "information technology"))

### Exemplo 2: String para SciELO

("aprendizagem autodirigida" OR "aprendizagem auto dirigida" OR "aprendizagem auto-dirigida") AND ("ensino superior" OR "universidade" OR "graduação") AND ("computação" OR "ciência da computação" OR "tecnologia da informação")

## FORMATO DE SAÍDA

Para cada base de dados a seguir, forneça:

1. String de busca otimizada
2. Justificativa para escolha dos termos e operadores
3. Estimativa de abrangência (cobertura vs. precisão)
4. Limitações potenciais da string

### Bases de Dados

- IEEE Xplore
- ACM Digital Library
- Periódicos CAPES
- Google Scholar
- BDTD (Biblioteca Digital Brasileira de Teses e Dissertações)

## CONSIDERAÇÕES ADICIONAIS

- Inclua variações em português e inglês quando relevante
- Considere peculiaridades de sintaxe de cada base de dados
- Sugira filtros adicionais (anos, tipos de documento, etc.)
```

### 2.2 Avaliação de Relevância de Estudos

```markdown
# PROMPT: Avaliação de Relevância de Artigos

## CONTEXTO

Estou conduzindo a fase de seleção de artigos para minha revisão sistemática sobre aprendizagem autodirigida em cursos de computação, com os seguintes critérios de inclusão:
[INSERIR CRITÉRIOS DE INCLUSÃO/EXCLUSÃO]

## OBJETIVO

Avaliar a relevância dos seguintes artigos com base nos títulos e resumos fornecidos.

## REQUISITOS

- Utilize a técnica CoT + Self-Consistency
- Analise cada artigo de forma independente
- Demonstre o raciocínio para inclusão ou exclusão

## FORMATO DE ENTRADA

Para cada artigo, fornecerei:

- Título
- Resumo
- Palavras-chave (quando disponíveis)
- Informações de publicação

## FORMATO DE SAÍDA

Para cada artigo, forneça:

1. **Decisão**: [INCLUIR/EXCLUIR]
2. **Raciocínio**: Análise passo a passo da adequação aos critérios
3. **Confiança**: [ALTA/MÉDIA/BAIXA]
4. **Observações**: Pontos específicos de potencial interesse

## CONJUNTO DE ARTIGOS

[LISTAR ARTIGOS COM TÍTULO E RESUMO]

## CONSIDERAÇÕES ADICIONAIS

- Em caso de dúvida, inclua o artigo para análise posterior
- Identifique padrões ou tendências nos artigos analisados
- Sugira ajustes nos critérios de inclusão/exclusão se necessário
```

### 2.3 Planejamento de Busca Manual Complementar

```markdown
# PROMPT: Estratégia de Busca Manual Complementar

## CONTEXTO

Já realizei a busca sistemática nas principais bases de dados, mas desejo complementar com uma busca manual para identificar estudos relevantes que possam ter sido perdidos.

## OBJETIVO

Desenvolver uma estratégia sistemática de busca manual complementar para uma revisão sobre aprendizagem autodirigida em cursos de computação.

## REQUISITOS

- Utilize a técnica RAG + Few-Shot
- Considere fontes não indexadas nas principais bases de dados
- Priorize a sistematização e reprodutibilidade do processo

## CONHECIMENTO CONTEXTUAL [RAG]

[Inclua trechos de metodologias sobre busca manual em revisões sistemáticas]

## FORMATO DE SAÍDA

1. **Fontes Complementares**:

   - Periódicos relevantes não indexados
   - Anais de congressos específicos
   - Repositórios institucionais prioritários
   - Bases de literatura cinzenta

2. **Procedimento Sistemático**:

   - Protocolo passo a passo para cada fonte
   - Termos de busca a utilizar
   - Critérios de triagem adaptados

3. **Documentação**:

   - Template para registro da busca manual
   - Método para integração com resultados da busca principal
   - Estratégia para eliminação de duplicatas

4. **Cronograma Estimado**:
   - Tempo necessário para busca manual
   - Priorização de fontes se houver restrição de tempo

## CONSIDERAÇÕES ADICIONAIS

- Foque em fontes com alta probabilidade de conter estudos sobre o contexto brasileiro
- Sugira abordagens para verificação cruzada (ex.: snowballing)
- Indique métodos para avaliar a contribuição da busca manual
```

## 3. Prompts para Extração e Análise

### 3.1 Extração Estruturada de Dados

```markdown
# PROMPT: Extração Estruturada de Dados

## CONTEXTO

Tenho um conjunto de artigos selecionados para minha revisão sistemática sobre aprendizagem autodirigida em cursos de computação. Preciso extrair dados de forma estruturada e padronizada.

## OBJETIVO

Extrair informações estruturadas do seguinte artigo, seguindo um template padronizado.

## REQUISITOS

- Utilize a técnica Few-Shot + Chain-of-Thought
- Raciocine explicitamente sobre cada categoria de informação
- Mantenha consistência com o formato do template

## EXEMPLO (FEW-SHOT)

### Exemplo de Extração Estruturada:

**Referência**: Silva, J. P., & Oliveira, M. R. (2019). Self-directed learning in Computer Science education: A case study in Brazil. Journal of Educational Technology, 45(3), 123-145.

**Dados Bibliométricos**:

- Ano: 2019
- Periódico: Journal of Educational Technology
- Fator de Impacto: 2.3
- Citações: 17

**Características Metodológicas**:

- Tipo de Estudo: Estudo de caso
- Abordagem: Qualitativa
- Coleta de Dados: Entrevistas, observação, documentos
- Amostra: 28 estudantes de graduação em Ciência da Computação
- Duração: 1 semestre acadêmico

**Conceituação de SDL**:

- Definição Adotada: "Processo em que os indivíduos tomam a iniciativa para diagnosticar suas necessidades de aprendizagem, formular objetivos, identificar recursos, selecionar estratégias e avaliar os resultados" (baseado em Knowles, 1975)
- Dimensões Enfatizadas: Autonomia, motivação intrínseca, metacognição
- Perspectiva Teórica: Construtivista

**Contexto Educacional**:

- Nível: Graduação
- Curso: Bacharelado em Ciência da Computação
- Disciplina(s): Programação Orientada a Objetos
- Instituição: Universidade Federal do Sul do Brasil
- País: Brasil

**Intervenção/Abordagem**:

- Estratégia Principal: Projetos autodirigidos com mentoria
- Tecnologias Utilizadas: Ambiente virtual de aprendizagem, GitHub
- Duração da Intervenção: 16 semanas
- Papel do Professor: Facilitador, mentor

**Resultados Principais**:

- Descobertas Centrais: Aumento significativo na autonomia dos estudantes (p<0.05); Desenvolvimento de habilidades metacognitivas; Desafios na fase inicial de adaptação
- Avaliação de Eficácia: Positiva, com ressalvas para perfis de estudantes específicos
- Limitações Identificadas: Amostra de uma única instituição; Alta taxa de desistência inicial (17%)

**Conclusões e Recomendações**:

- Implicações Teóricas: Expandiu o modelo de Garrison para contextos técnicos
- Implicações Práticas: Recomenda implementação gradual com suporte intensivo nas fases iniciais
- Sugestões para Pesquisas Futuras: Investigar fatores culturais; Estudos longitudinais

**Observações Adicionais**:

- Conexão com outros conceitos: Forte relação com aprendizagem baseada em problemas
- Particularidades contextuais: Adaptado ao sistema educacional brasileiro

## FORMATO DE SAÍDA

Preencha o template acima com os dados do seguinte artigo:
[INSERIR REFERÊNCIA E/OU TEXTO DO ARTIGO]

## CONSIDERAÇÕES ADICIONAIS

- Mantenha-se fiel ao texto original para dados factuais
- Utilize [NÃO INFORMADO] quando a informação não estiver disponível
- Use [INTERPRETAÇÃO] para conteúdo inferido que não esteja explícito
- Adicione notas sobre qualidade ou clareza das informações quando relevante
```

### 3.2 Análise Comparativa de Metodologias

```markdown
# PROMPT: Análise Comparativa de Metodologias

## CONTEXTO

Estou analisando diferentes abordagens metodológicas utilizadas em estudos sobre aprendizagem autodirigida em computação.

## OBJETIVO

Desenvolver uma análise comparativa detalhada das metodologias utilizadas nos estudos selecionados.

## REQUISITOS

- Utilize a técnica ToT + RAG
- Explore diferentes perspectivas de análise metodológica
- Integre conhecimento contextual sobre métodos de pesquisa em educação

## CONHECIMENTO CONTEXTUAL [RAG]

[Inclua aqui trechos sobre metodologias de pesquisa em educação e tecnologia]

## FORMATO DE SAÍDA

1. **Mapeamento Comparativo**:

   - Tabela comparativa das metodologias por estudo
   - Classificação tipológica (experimental, quasi-experimental, etc.)
   - Análise de frequência de métodos e combinações

2. **Análise de Adequação**:

   - Avaliação da adequação metodológica às questões investigadas
   - Pontos fortes e limitações de cada abordagem
   - Vieses potenciais identificados

3. **Tendências Metodológicas**:

   - Evolução temporal das abordagens metodológicas
   - Particularidades metodológicas no contexto brasileiro
   - Lacunas metodológicas identificadas

4. **Recomendações**:
   - Sugestões para fortalecimento metodológico
   - Abordagens promissoras pouco exploradas
   - Combinações metodológicas potencialmente valiosas

## ESTUDOS PARA ANÁLISE

[LISTA DE REFERÊNCIAS DOS ESTUDOS]

## CONSIDERAÇÕES ADICIONAIS

- Considere as particularidades da pesquisa educacional na área de computação
- Analise criticamente a validade interna e externa dos estudos
- Identifique inovações metodológicas relevantes
```

### 3.3 Síntese de Evidências por Tema

```markdown
# PROMPT: Síntese Temática de Evidências

## CONTEXTO

Após a extração de dados dos artigos selecionados para minha revisão sobre aprendizagem autodirigida em computação, preciso sintetizar as evidências por temas emergentes.

## OBJETIVO

Realizar uma síntese temática das evidências encontradas nos estudos selecionados.

## REQUISITOS

- Utilize a técnica RAG + Few-Shot + Self-Consistency
- Identifique temas emergentes nos dados extraídos
- Sintetize evidências de forma estruturada para cada tema
- Avalie a consistência e qualidade das evidências

## CONHECIMENTO CONTEXTUAL [RAG]

[Inclua aqui trechos sobre síntese temática em revisões sistemáticas]

## EXEMPLO (FEW-SHOT)

### Exemplo de Síntese Temática:

**Tema: Estratégias de Scaffolding para SDL em Computação**

**Definição do Tema**:
Abordagens estruturadas que oferecem suporte gradual e temporário aos estudantes durante a transição para aprendizagem autodirigida em contextos de ensino de computação.

**Síntese das Evidências**:
Cinco estudos (S3, S7, S12, S15, S21) investigaram estratégias de scaffolding para SDL em cursos de computação. Os resultados convergem para a eficácia de uma abordagem gradual de retirada de suporte (S3, S15, S21), especialmente em disciplinas introdutórias de programação. Evidências moderadas sugerem que scaffolding digital personalizado (S7, S12) apresenta resultados superiores em comparação com abordagens padronizadas. Estudos qualitativos (S3, S12) destacam a importância de calibrar o suporte conforme perfis individuais dos alunos, identificando três padrões predominantes de necessidade de scaffolding: técnico, organizacional e motivacional.

Contudo, há inconsistências quanto à duração ideal do processo de transição, com resultados variando de 4 semanas (S7) a um semestre completo (S15, S21). Apenas um estudo (S21) realizou acompanhamento longitudinal, revelando que estudantes expostos a scaffolding estruturado mantiveram práticas de SDL após 18 meses da intervenção inicial.

**Qualidade das Evidências**:
A qualidade metodológica dos estudos neste tema é moderada. Dois estudos (S7, S21) empregaram grupos de controle, enquanto os demais utilizaram desenhos pré-pós sem grupo controle. Limitações incluem amostras relativamente pequenas (19-42 participantes) e contextos institucionais específicos, comprometendo a generalizabilidade. A operacionalização de "scaffolding" variou consideravelmente entre os estudos, dificultando comparações diretas.

**Lacunas Identificadas**:
Pesquisas futuras devem: (1) investigar a transferibilidade de estratégias de scaffolding entre diferentes disciplinas de computação; (2) desenvolver instrumentos validados para avaliar a eficácia de scaffolding específico para SDL; e (3) examinar como fatores socioculturais influenciam a eficácia de diferentes abordagens de scaffolding no contexto brasileiro.

## FORMATO DE SAÍDA

Para cada tema emergente, forneça:

1. **Definição do Tema**
2. **Síntese das Evidências**
3. **Qualidade das Evidências**
4. **Lacunas Identificadas**

## DADOS EXTRAÍDOS

[INSERIR DADOS EXTRAÍDOS DOS ESTUDOS]

## CONSIDERAÇÕES ADICIONAIS

- Identifique convergências e divergências nas evidências
- Avalie a força das evidências para cada tema
- Destaque particularidades do contexto brasileiro quando relevante
- Considere implicações teóricas e práticas
```

## 4. Prompts para Elaboração de Relatórios

### 4.1 Redação de Seção de Métodos

```markdown
# PROMPT: Redação da Seção de Métodos

## CONTEXTO

Estou elaborando o relatório da minha revisão sistemática sobre aprendizagem autodirigida em cursos de computação.

## OBJETIVO

Redigir uma seção de métodos detalhada e transparente que descreva todo o processo da revisão sistemática.

## REQUISITOS

- Utilize a técnica Few-Shot + Chain-of-Thought
- Siga as diretrizes PRISMA para relato de revisões sistemáticas
- Assegure transparência e reprodutibilidade

## EXEMPLO (FEW-SHOT)

[Inclua aqui um exemplo de seção de métodos bem estruturada]

## FORMATO DE SAÍDA

Produza uma seção de métodos estruturada em:

1. **Protocolo e Registro**:

   - Existência de protocolo prévio
   - Registro em plataformas específicas (se aplicável)

2. **Critérios de Elegibilidade**:

   - Critérios de inclusão detalhados
   - Critérios de exclusão detalhados
   - Justificativa para cada critério

3. **Fontes de Informação**:

   - Bases de dados eletrônicas consultadas
   - Fontes adicionais (busca manual, contato com autores)
   - Período de cobertura da busca

4. **Estratégia de Busca**:

   - Strings de busca completas para cada base
   - Filtros e limitadores utilizados
   - Data da última busca

5. **Seleção dos Estudos**:

   - Processo de triagem (individual/pareado)
   - Resolução de desacordos
   - Software utilizado (se aplicável)

6. **Processo de Extração de Dados**:

   - Dados extraídos e formulário utilizado
   - Processo de extração (individual/pareado)
   - Tratamento de informações ausentes

7. **Avaliação de Qualidade**:

   - Instrumento utilizado para avaliação de qualidade
   - Procedimento de aplicação
   - Incorporação na síntese

8. **Síntese dos Resultados**:
   - Método de síntese (narrativa, meta-análise)
   - Abordagem para análise de heterogeneidade
   - Análises adicionais realizadas

## INFORMAÇÕES DO PROTOCOLO

[INSERIR RESUMO DO PROTOCOLO UTILIZADO]

## CONSIDERAÇÕES ADICIONAIS

- Utilize tempo passado para relatar o que foi feito
- Inclua informações sobre desvios do protocolo original, se houver
- Referencie adequadamente instrumentos ou métodos adotados
- Mantenha linguagem científica, objetiva e precisa
```

### 4.2 Elaboração de Diagrama PRISMA

```markdown
# PROMPT: Elaboração de Diagrama PRISMA

## CONTEXTO

Preciso elaborar um diagrama PRISMA para documentar o processo de seleção de estudos na minha revisão sistemática sobre aprendizagem autodirigida em computação.

## OBJETIVO

Criar uma descrição textual detalhada para um diagrama PRISMA, incluindo todos os números e justificativas para exclusões.

## REQUISITOS

- Utilize a técnica Chain-of-Thought
- Raciocine passo a passo sobre cada estágio do processo
- Siga as diretrizes PRISMA mais recentes

## FORMATO DE SAÍDA

Forneça uma descrição textual detalhada para cada elemento do diagrama PRISMA:

1. **Identificação**:

   - Número de registros identificados através de busca em bases de dados
   - Número de registros identificados por outras fontes
   - Total de registros antes da remoção de duplicatas

2. **Triagem**:

   - Número de registros após remoção de duplicatas
   - Número de registros triados
   - Número de registros excluídos na triagem

3. **Elegibilidade**:

   - Número de artigos em texto completo avaliados para elegibilidade
   - Número de artigos em texto completo excluídos, com justificativas
   - Categorização das razões de exclusão com respectivos números

4. **Inclusão**:
   - Número de estudos incluídos na síntese qualitativa
   - Número de estudos incluídos na síntese quantitativa (se aplicável)

## DADOS DO PROCESSO

[INSERIR DADOS NUMÉRICOS DO PROCESSO DE SELEÇÃO]

## CONSIDERAÇÕES ADICIONAIS

- Assegure que os números sejam consistentes entre as etapas
- Categorize as razões de exclusão de forma clara e informativa
- Mencione qualquer processo de verificação da qualidade da triagem
- Indique se houve mudanças nos critérios durante o processo
```

### 4.3 Discussão de Limitações e Implicações

```markdown
# PROMPT: Discussão de Limitações e Implicações

## CONTEXTO

Concluí a síntese dos resultados da minha revisão sistemática sobre aprendizagem autodirigida em cursos de computação e preciso elaborar uma discussão crítica.

## OBJETIVO

Desenvolver uma discussão abrangente sobre limitações da revisão e implicações dos resultados.

## REQUISITOS

- Utilize a técnica Role + CoT + Self-Consistency
- Assuma os papéis de diferentes stakeholders acadêmicos
- Desenvolva um raciocínio crítico e balanceado
- Valide a consistência das conclusões por múltiplas perspectivas

## FORMATO DE SAÍDA

Produza uma discussão estruturada em:

1. **Limitações da Revisão**:

   - Limitações metodológicas da própria revisão
   - Restrições das evidências primárias
   - Desafios de síntese e interpretação
   - Lacunas na cobertura da literatura

2. **Implicações Teóricas**:

   - Contribuições para o entendimento conceitual de SDL
   - Refinamentos teóricos sugeridos pelos achados
   - Conexões com teorias adjacentes
   - Desafios aos pressupostos teóricos existentes

3. **Implicações Práticas**:

   - Recomendações para docentes e instituições
   - Considerações para design instrucional
   - Sugestões para políticas educacionais
   - Orientações para implementação contextualizada

4. **Direções para Pesquisas Futuras**:
   - Lacunas críticas de conhecimento
   - Questões emergentes dos resultados
   - Abordagens metodológicas recomendadas
   - Oportunidades específicas no contexto brasileiro

## RESULTADOS SINTETIZADOS

[INSERIR RESUMO DOS PRINCIPAIS RESULTADOS]

## CONSIDERAÇÕES ADICIONAIS

- Equilibre limitações com contribuições positivas
- Contextualize as implicações para a realidade educacional brasileira
- Diferencie entre conclusões robustas e tentativas
- Discuta aplicabilidade em diferentes contextos institucionais
- Considere fatores socioculturais na transferência de conhecimento
```

## 5. Prompts para Aplicações Específicas

### 5.1 Identificação de Gaps de Pesquisa

```markdown
# PROMPT: Identificação Sistemática de Gaps de Pesquisa

## CONTEXTO

Completei a revisão sistemática sobre aprendizagem autodirigida em cursos de computação e desejo identificar de forma sistemática as lacunas de pesquisa.

## OBJETIVO

Identificar, categorizar e priorizar gaps de pesquisa identificados na literatura revisada.

## REQUISITOS

- Utilize a técnica ToT + RAG + Self-Consistency
- Explore múltiplas perspectivas para identificação de lacunas
- Integre conhecimento contextual sobre tendências de pesquisa
- Valide a consistência e relevância das lacunas identificadas

## CONHECIMENTO CONTEXTUAL [RAG]

[Inclua aqui trechos sobre tendências de pesquisa em educação em computação]

## FORMATO DE SAÍDA

1. **Mapa de Lacunas de Conhecimento**:

   - Lacunas metodológicas identificadas
   - Lacunas teóricas/conceituais
   - Lacunas contextuais (populações, cenários)
   - Lacunas de implementação prática

2. **Categorização por Tipo**:

   - Lacunas por contradição (evidências conflitantes)
   - Lacunas por omissão (tópicos não investigados)
   - Lacunas por superficialidade (investigações limitadas)
   - Lacunas por obsolescência (conhecimento desatualizado)

3. **Análise de Relevância**:

   - Priorização baseada em critérios explícitos
   - Implicações para avanço teórico
   - Relevância para prática educacional
   - Viabilidade de investigação

4. **Proposições de Pesquisa**:
   - Questões de pesquisa bem formuladas para cada gap
   - Abordagens metodológicas sugeridas
   - Considerações para design de estudos
   - Potenciais contribuições esperadas

## SÍNTESE DOS RESULTADOS

[INSERIR SÍNTESE DOS PRINCIPAIS RESULTADOS DA REVISÃO]

## CONSIDERAÇÕES ADICIONAIS

- Considere o contexto específico da educação em computação no Brasil
- Analise tendências emergentes na literatura internacional
- Avalie a maturidade das diferentes linhas de pesquisa
- Identifique oportunidades para inovação metodológica
```

### 5.2 Análise de Evolução Conceitual

```markdown
# PROMPT: Análise de Evolução Conceitual

## CONTEXTO

A revisão sistemática sobre aprendizagem autodirigida em computação revelou diferentes conceituações e entendimentos do termo ao longo do tempo e entre diferentes autores.

## OBJETIVO

Analisar a evolução conceitual da aprendizagem autodirigida no contexto do ensino de computação.

## REQUISITOS

- Utilize a técnica RAG + CoT + Role
- Incorpore conhecimento histórico sobre o desenvolvimento do conceito
- Demonstre raciocínio sobre as transformações conceituais
- Assuma papel de historiador de conceitos educacionais

## CONHECIMENTO CONTEXTUAL [RAG]

[Inclua aqui trechos sobre a evolução histórica do conceito de SDL]

## FORMATO DE SAÍDA

1. **Mapeamento Cronológico**:

   - Linha do tempo das definições principais
   - Marcos conceituais importantes
   - Transições paradigmáticas identificadas

2. **Análise Comparativa**:

   - Dimensões conceituais permanentes vs. transitórias
   - Diferenças terminológicas e semânticas
   - Influências disciplinares na conceituação

3. **Escolas de Pensamento**:

   - Identificação de perspectivas teóricas distintas
   - Pressupostos epistemológicos subjacentes
   - Tensões e complementaridades entre abordagens

4. **Contextualização em Computação**:

   - Adaptações específicas para o ensino de computação
   - Reinterpretações baseadas em particularidades da área
   - Integrações com conceitos específicos de computação

5. **Tendências Atuais e Futuras**:
   - Direções conceituais emergentes
   - Convergências interdisciplinares
   - Projeções para evolução futura do conceito

## DADOS CONCEITUAIS

[INSERIR DEFINIÇÕES E CONCEITUAÇÕES EXTRAÍDAS DOS ESTUDOS]

## CONSIDERAÇÕES ADICIONAIS

- Considere influências socioculturais nas conceituações
- Analise como a tecnologia moldou a compreensão do conceito
- Identifique terminologias adjacentes que se sobrepõem
- Avalie a adequação das conceituações para o contexto brasileiro
```

### 5.3 Desenvolvimento de Framework Integrativo

```markdown
# PROMPT: Desenvolvimento de Framework Integrativo

## CONTEXTO

Após concluir a revisão sistemática sobre aprendizagem autodirigida em computação, desejo desenvolver um framework integrativo que sintetize os principais elementos encontrados.

## OBJETIVO

Criar um framework conceitual integrativo que organize e relacione os principais componentes da aprendizagem autodirigida no contexto do ensino de computação.

## REQUISITOS

- Utilize a técnica Few-Shot + Directional Stimulus + Self-Consistency
- Direcione o desenvolvimento para um framework visual e conceitual
- Valide a consistência lógica e teórica do framework proposto

## EXEMPLO (FEW-SHOT)

[Inclua aqui exemplos de frameworks conceituais bem estruturados]

## DIRECIONAMENTO

Desenvolva um framework que:

- Integre dimensões individuais e contextuais da SDL
- Considere aspectos específicos do ensino-aprendizagem de computação
- Incorpore fatores sociotécnicos relevantes
- Seja aplicável ao contexto educacional brasileiro
- Permita avaliar maturidade e progressão em SDL

## FORMATO DE SAÍDA

1. **Descrição Conceitual do Framework**:

   - Fundamentação teórica
   - Componentes principais e suas definições
   - Relações entre componentes
   - Níveis ou dimensões organizacionais

2. **Descrição Visual**:

   - Detalhamento textual da representação visual
   - Elementos visuais propostos
   - Legenda explicativa
   - Fluxos e interconexões

3. **Aplicações do Framework**:

   - Utilização para análise de contextos educacionais
   - Aplicação no design instrucional
   - Uso para avaliação de intervenções
   - Orientação para pesquisas futuras

4. **Validação Conceitual**:
   - Correspondência com evidências da literatura
   - Consistência lógica interna
   - Limitações e considerações
   - Propostas para validação empírica

## SÍNTESE DOS RESULTADOS

[INSERIR SÍNTESE DOS PRINCIPAIS RESULTADOS DA REVISÃO]

## CONSIDERAÇÕES ADICIONAIS

- Equilibre complexidade teórica com aplicabilidade prática
- Considere a transferibilidade para diferentes contextos institucionais
- Integre perspectivas de diversos stakeholders educacionais
- Preveja mecanismos de adaptação e evolução do framework
```

## 6. Metadados e Integração com o Sistema

### 6.1 Informações Técnicas

**Versão**: 1.0  
**Data de Criação**: Março/2024  
**Última Atualização**: Março/2024  
**Compatibilidade**: Aplicável a Claude 3 Sonnet/Opus, GPT-4 e outros LLMs avançados  
**Domínio Primário**: Metodologia Científica > Revisão Sistemática de Literatura  
**Subdomínio**: Educação > Aprendizagem Autodirigida > Computação

### 6.2 Integração com o Framework

Esta biblioteca de prompts se integra ao framework mais amplo de engenharia de prompts para pesquisa científica:

- **Taxonomia de Técnicas**: Implementa múltiplas técnicas catalogadas na taxonomia
- **Princípios de Estruturação**: Segue os princípios de clareza, rigor científico e estruturação formal
- **Framework de Validação**: Incorpora elementos de validação científica em todos os prompts
- **Sistema de Metadados**: Compatível com o esquema de metadados estabelecido

### 6.3 Diretrizes de Uso e Adaptação

1. **Personalização Contextual**:

   - Substitua os elementos em [COLCHETES] pelas informações específicas do seu estudo
   - Ajuste o escopo para outras áreas além da computação quando necessário
   - Adapte referências a bases de dados conforme disponibilidade e relevância

2. **Seleção de Técnicas**:

   - Considere o índice mestre de técnicas para selecionar combinações alternativas
   - Ajuste o nível de complexidade conforme sua familiaridade com as técnicas
   - Consulte recomendações de fluxos de trabalho no manual técnico

3. **Avaliação de Eficácia**:
   - Documente os resultados obtidos com cada prompt
   - Refine iterativamente conforme necessário
   - Compartilhe adaptações bem-sucedidas para enriquecer a biblioteca

```

```
