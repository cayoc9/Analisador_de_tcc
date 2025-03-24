# Prompts Estruturados para Comunicação entre Agentes

Este documento contém uma coleção de prompts estruturados para facilitar a comunicação eficiente entre o Curador de Knowledge Base e o Cartógrafo Conceitual, visando a construção sistemática do referencial teórico.

## Prompts para o Curador (Extração e Organização de Conhecimento)

### Prompt 1: Levantamento de Conceitos Fundamentais

```
Como Curador de Knowledge Base, analise a literatura sobre Self-Directed Learning (SDL) e extraia os conceitos fundamentais seguindo estas diretrizes:

1. OBJETIVO: Identificar e estruturar os conceitos centrais de SDL relevantes para o contexto de ensino de Computação.

2. INSTRUÇÕES:
   a) Identifique no mínimo 15-20 conceitos fundamentais de SDL
   b) Para cada conceito, forneça:
      - Definição concisa (1-2 frases)
      - Autores principais associados
      - Relevância para o contexto de Computação (alta/média/baixa + justificativa)
      - Relações primárias com outros conceitos (antecede, sucede, complementa, contradiz)
   c) Categorize os conceitos por:
      - Fundamentação teórica
      - Aplicação prática
      - Avaliação/mensuração
      - Desafios/limitações
   d) Identifique debates teóricos significativos onde existam perspectivas concorrentes

3. ESTRUTURA DE SAÍDA:
   - Utilize o template_conceitos_fundamentais.md
   - Organize os conceitos em ordem de relevância para a pesquisa
   - Destaque conceitos peculiares ao contexto de Computação

4. META-ANÁLISE:
   - Indique tendências na evolução conceitual de SDL
   - Sugira áreas conceituais que parecem subdesenvolvidas
   - Recomende abordagens para mapeamento conceitual integrado
```

### Prompt 2: Matriz de Competências e Perfil do Aluno

```
Como Curador de Knowledge Base, construa uma matriz estruturada de competências relacionadas a SDL e dados sobre o perfil do aluno no contexto de Computação:

1. OBJETIVO: Organizar sistematicamente as competências associadas a SDL e características do perfil do aluno para análise de interdependências.

2. INSTRUÇÕES:
   a) Para a matriz de competências:
      - Identifique 10-15 competências essenciais para SDL
      - Classifique cada competência por tipo (cognitiva, metacognitiva, socioafetiva, técnica)
      - Indique nível de desenvolvimento esperado (iniciante, intermediário, avançado)
      - Associe evidências de desenvolvimento na literatura
      - Relacione com resultados de aprendizagem mensuráveis

   b) Para o perfil do aluno:
      - Identifique 8-12 características relevantes do aluno
      - Categorize por aspectos (cognitivos, motivacionais, contextuais, experienciais)
      - Indique como cada aspecto influencia a capacidade de autodireção
      - Associe com desafios específicos no contexto de Computação
      - Relacione com intervenções pedagógicas recomendadas

3. ESTRUTURA DE SAÍDA:
   - Utilize o template_matriz_interdependencias.md
   - Organize as competências em ordem de complexidade
   - Apresente o perfil do aluno em ordem de impacto na autodireção

4. META-ANÁLISE:
   - Identifique padrões de interdependência sugeridos na literatura
   - Sugira relações que parecem insuficientemente estudadas
   - Destaque tensões potenciais entre expectativas de competências e realidades do perfil do aluno
```

### Prompt 3: Meta-análise Teórica para Diagnóstico de Completude

```
Como Curador de Knowledge Base, realize uma meta-análise teórica do corpo de literatura sobre SDL para auxiliar no diagnóstico de completude do referencial teórico:

1. OBJETIVO: Avaliar a abrangência, profundidade e diversidade do corpo teórico atual para identificar lacunas relevantes.

2. INSTRUÇÕES:
   a) Para avaliação de cobertura:
      - Analise a distribuição temporal das referências (clássicas vs. contemporâneas)
      - Verifique a representatividade das principais correntes teóricas
      - Avalie o equilíbrio entre fontes primárias e secundárias
      - Identifique subtemas com cobertura insuficiente

   b) Para alinhamento com objetivos:
      - Relacione cada objetivo de pesquisa com a base teórica correspondente
      - Avalie a suficiência da fundamentação para cada objetivo
      - Identifique áreas que necessitam aprofundamento

   c) Para diversidade teórico-metodológica:
      - Analise o equilíbrio entre estudos qualitativos e quantitativos
      - Identifique a representação de diferentes paradigmas de pesquisa
      - Avalie a presença de estudos empíricos vs. teóricos
      - Verifique a relevância contextual para o campo da Computação

3. ESTRUTURA DE SAÍDA:
   - Utilize o template_diagnostico_completude.md
   - Priorize lacunas por criticidade e relevância para os objetivos
   - Estruture recomendações em ordem de prioridade

4. META-REFLEXÃO:
   - Avalie limitações na própria análise
   - Sugira abordagens complementares para diagnóstico
   - Proponha estratégias específicas para preencher as lacunas mais críticas
```

## Prompts para o Cartógrafo (Análise e Mapeamento Conceitual)

### Prompt 4: Desenvolvimento do Mapa Conceitual Integrado

```
Como Cartógrafo Conceitual, desenvolva um mapa conceitual integrado sobre SDL com base nos conceitos fundamentais fornecidos pelo Curador:

1. OBJETIVO: Criar uma representação visual integrada das relações entre conceitos fundamentais de SDL relevantes para o contexto de Computação.

2. INSTRUÇÕES:
   a) Análise preliminar:
      - Identifique conceitos-âncora que estruturam o campo
      - Determine agrupamentos naturais e categorias emergentes
      - Identifique conceitos-ponte que conectam diferentes áreas

   b) Desenvolvimento do mapa:
      - Estabeleça hierarquias conceituais claras
      - Represente visualmente diferentes tipos de relações (causal, compositiva, temporal, etc.)
      - Destaque zonas de convergência e divergência teórica
      - Indique a força relativa das conexões conceituais

   c) Contextualização para Computação:
      - Destaque conceitos com aplicação direta no ensino de Computação
      - Indique adaptações necessárias para o contexto específico
      - Identifique conceitos que requerem elaboração adicional

3. FORMATO DE SAÍDA:
   - Mapa conceitual principal (formato digital)
   - Submapas detalhados para áreas complexas
   - Legenda explicativa do sistema de notação
   - Narrativa explicativa das principais relações (1-2 páginas)

4. META-REFLEXÃO:
   - Avalie limitações do mapeamento atual
   - Identifique áreas que se beneficiariam de aprofundamento
   - Proponha perspectivas alternativas de visualização
```

### Prompt 5: Análise de Interdependências

```
Como Cartógrafo Conceitual, analise as interdependências entre competências de SDL e o perfil do aluno com base nos dados fornecidos pelo Curador:

1. OBJETIVO: Desenvolver uma análise sistemática das relações entre competências necessárias para SDL e características do perfil do aluno em Computação.

2. INSTRUÇÕES:
   a) Análise de alinhamento:
      - Identifique correspondências naturais entre competências e características do perfil
      - Avalie o grau de alinhamento (forte, moderado, fraco, conflitante)
      - Destaque áreas de potencial sinergia e tensão

   b) Análise de lacunas:
      - Identifique competências esperadas que podem ser desafiadoras para o perfil típico
      - Avalie a criticidade dessas lacunas para o sucesso em SDL
      - Sugira intervenções pedagógicas para abordar as lacunas

   c) Análise de oportunidades:
      - Identifique características do perfil que podem ser aproveitadas como vantagens
      - Sugira como as oportunidades podem ser maximizadas
      - Indique condições contextuais necessárias para aproveitamento

3. FORMATO DE SAÍDA:
   - Matriz de interdependências (formato tabular)
   - Mapa visual de influências (formato diagrama)
   - Análise narrativa das relações mais significativas (2-3 páginas)

4. META-REFLEXÃO:
   - Avalie como as interdependências podem variar em diferentes contextos
   - Identifique pressupostos subjacentes à análise
   - Sugira como a análise pode informar o design instrucional
```

### Prompt 6: Diagnóstico de Completude Teórica

```
Como Cartógrafo Conceitual, desenvolva um diagnóstico abrangente da completude teórica do referencial com base na meta-análise fornecida pelo Curador:

1. OBJETIVO: Avaliar criticamente a suficiência, coerência e relevância do corpo teórico atual para fundamentar a pesquisa sobre SDL em Computação.

2. INSTRUÇÕES:
   a) Análise de suficiência:
      - Avalie a cobertura dos conceitos fundamentais identificados
      - Identifique subtemas subrepresentados na literatura atual
      - Determine a adequação da base empírica para as afirmações teóricas

   b) Análise de coerência:
      - Avalie a consistência interna entre diferentes componentes teóricos
      - Identifique contradições ou tensões não resolvidas
      - Avalie a integração entre diferentes perspectivas teóricas

   c) Análise de relevância:
      - Avalie a adequação do referencial para responder às perguntas de pesquisa
      - Determine a aplicabilidade ao contexto específico de Computação
      - Identifique necessidades de adaptação ou recontextualização

3. FORMATO DE SAÍDA:
   - Relatório estruturado de diagnóstico
   - Mapa visual de lacunas teóricas
   - Recomendações priorizadas para complementação

4. META-REFLEXÃO:
   - Avalie as limitações do próprio diagnóstico
   - Identifique áreas onde julgamentos subjetivos foram necessários
   - Sugira abordagens complementares para validação do diagnóstico
```

## Prompts para Verificação Cruzada

### Prompt 7: Alinhamento com Perguntas de Pesquisa

```
Como Cartógrafo Conceitual, realize uma verificação cruzada entre o referencial teórico desenvolvido e as perguntas de pesquisa:

1. OBJETIVO: Avaliar sistematicamente se o referencial teórico construído fornece base adequada para responder às perguntas de pesquisa.

2. INSTRUÇÕES:
   a) Para cada pergunta de pesquisa:
      - Identifique conceitos-chave necessários para respondê-la
      - Avalie a presença e profundidade desses conceitos no referencial
      - Determine se existem relações conceituais necessárias estabelecidas
      - Identifique lacunas específicas que comprometem a resposta

   b) Análise de coerência global:
      - Avalie se o referencial apresenta uma narrativa teórica coerente
      - Identifique incongruências entre diferentes seções do referencial
      - Determine se a estrutura lógica suporta a progressão das perguntas

   c) Recomendações específicas:
      - Para cada lacuna identificada, sugira adições ou modificações específicas
      - Priorize recomendações por impacto nas perguntas de pesquisa
      - Indique fontes potenciais para preencher as lacunas

3. FORMATO DE SAÍDA:
   - Utilize o documento_verificacao_cruzada.md
   - Apresente uma tabela de alinhamento entre perguntas e conceitos
   - Forneça uma síntese das principais fortalezas e limitações

4. META-REFLEXÃO:
   - Avalie o grau de confiança nas conclusões do diagnóstico
   - Identifique áreas que se beneficiariam de revisão por especialistas
   - Sugira como o processo de verificação pode ser aprimorado
```

## Metadados do Documento

**Versão:** 1.0  
**Autor:** Engenheiro de Prompts  
**Data de criação:** [data]  
**Última atualização:** [data]  
**Status:** Ativo
